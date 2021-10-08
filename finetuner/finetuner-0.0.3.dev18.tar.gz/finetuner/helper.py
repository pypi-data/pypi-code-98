from typing import TypeVar, Sequence, Iterator, Union, Callable, List, Dict, Any

from jina import Document, DocumentArray, DocumentArrayMemmap

AnyDNN = TypeVar(
    'AnyDNN'
)  #: The type of any implementation of a Deep Neural Network object
AnyDataLoader = TypeVar(
    'AnyDataLoader'
)  #: The type of any implementation of a data loader
DocumentSequence = TypeVar(
    'DocumentSequence',
    Sequence[Document],
    DocumentArray,
    DocumentArrayMemmap,
    Iterator[Document],
)  #: The type of any sequence of Document
DocumentArrayLike = Union[
    DocumentSequence,
    Callable[..., DocumentSequence],
]  #: The type :py:data:`DocumentSequence` or a function that gives :py:data:`DocumentSequence`

EmbeddingLayerInfoType = List[
    Dict[str, Any]
]  #: The type of embedding layer information used in Tailor
TunerReturnType = Dict[
    str, Dict[str, Any]
]  #: The type of loss, metric information Tuner returns


def get_framework(dnn_model: AnyDNN) -> str:
    """Return the framework that enpowers a DNN model

    :param dnn_model: a DNN model
    :return: `keras`, `torch`, `paddle` or ValueError

    """
    if 'keras' in dnn_model.__module__:
        return 'keras'
    elif 'torch' in dnn_model.__module__:  # note: cover torch and torchvision
        return 'torch'
    elif 'paddle' in dnn_model.__module__:
        return 'paddle'
    else:
        raise ValueError(
            f'can not determine the backend from embed_model from {dnn_model.__module__}'
        )


def is_list_int(tp) -> bool:
    """Return True if the input is a list of integers."""
    return tp and isinstance(tp, Sequence) and all(isinstance(p, int) for p in tp)
