import torch
from torch import nn
import numpy as np

class fastText(nn.Module):
    def __init__(self, config, vocab_size, word_embeddings, evaluate_model):
        super(fastText, self).__init__()
        self.evaluate_model = evaluate_model
        self.config = config

        # Embedding Layer
        self.embeddings = nn.Embedding(vocab_size, self.config.embed_size)
        self.embeddings.weight = nn.Parameter(word_embeddings, requires_grad=False)

        # Hidden Layer
        self.fc1 = nn.Linear(self.config.embed_size, self.config.hidden_size)

        # Output Layer
        self.fc2 = nn.Linear(self.config.hidden_size, self.config.output_size)

        # Softmax non-linearity
        self.softmax = nn.LogSoftmax()

    def forward(self, x):
        embedded_sent = self.embeddings(x).permute(1,0,2)
        h = self.fc1(embedded_sent.mean(1))
        z = self.fc2(h)
        return self.softmax(z)

    def add_optimizer(self, optimizer):
        self.optimizer = optimizer

    def add_loss_op(self, loss_op):
        self.loss_op = loss_op

    def reduce_lr(self):
        for g in self.optimizer.param_groups:
            g['lr'] = g['lr'] / 2

    def run_epoch(self, train_iterator, val_iterator, epoch, classes, pos_label):
        train_losses = []
        val_accuracies = []
        losses = []

        # Reduce learning rate as number of epochs increase
        if (epoch == int(self.config.max_epochs/3)) or (epoch == int(2*self.config.max_epochs/3)):
            self.reduce_lr()

        for i, batch in enumerate(train_iterator):
            self.optimizer.zero_grad()
            if torch.cuda.is_available():
                x = batch.text.cuda()
                y = (batch.label).type(torch.cuda.LongTensor)
            else:
                x = batch.text
                y = (batch.label).type(torch.LongTensor)
            y_pred = self.__call__(x)
            loss = self.loss_op(y_pred, y)
            loss.backward()
            losses.append(loss.data.cpu().numpy())
            self.optimizer.step()

            if i % 100 == 0:
                avg_train_loss = np.mean(losses)
                train_losses.append(avg_train_loss)
                losses = []
                # Evalute Accuracy on validation set
                report = self.evaluate_model(self, val_iterator, classes, pos_label)
                report.training_loss = avg_train_loss
                val_accuracies.append(report.accuracy)
                self.train()
        # return report about current epoch
        return report
