class RATSError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'RATSError: {self.message}'
        else:
            return 'RATSError: Something went wrong, sorry about the lack of info...'
