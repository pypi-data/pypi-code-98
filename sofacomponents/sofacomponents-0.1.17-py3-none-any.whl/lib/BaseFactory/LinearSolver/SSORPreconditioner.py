# -*- coding: utf-8 -*-

from sofacomponents.lib.base_component import sofa_component


"""
Component SSORPreconditioner

.. autofunction:: SSORPreconditioner

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""


@sofa_component
def SSORPreconditioner(self, name=None, printLog=None, tags=None, bbox=None, componentState=None, listening=None, verbose=None, omega=None, **kwargs):
    """
    Linear system solver / preconditioner based on Symmetric Successive Over-Relaxation (SSOR). If the matrix is decomposed as $A = D + L + L^T$, this solver computes $(1/(2-w))(D/w+L)(D/w)^{-1}(D/w+L)^T x = b, or $(D+L)D^{-1}(D+L)^T x = b$ if $w=1$.


    :param name: object name  Default value: SSORPreconditioner

    :param printLog: if true, emits extra messages at runtime.  Default value: 0

    :param tags: list of the subsets the objet belongs to  Default value: []

    :param bbox: this object bounding box  Default value: [[1.7976931348623157e+308, 1.7976931348623157e+308, 1.7976931348623157e+308], [-1.7976931348623157e+308, -1.7976931348623157e+308, -1.7976931348623157e+308]]

    :param componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).  Default value: Undefined

    :param listening: if true, handle the events, otherwise ignore the events  Default value: 0

    :param verbose: Dump system state at each iteration  Default value: 0

    :param omega: Omega coefficient  Default value: 1.0


    """
    params = dict(name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, verbose=verbose, omega=omega)
    return "SSORPreconditioner", params
