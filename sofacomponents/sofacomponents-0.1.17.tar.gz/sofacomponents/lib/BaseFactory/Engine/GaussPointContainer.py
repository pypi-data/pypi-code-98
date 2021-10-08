# -*- coding: utf-8 -*-

from sofacomponents.lib.base_component import sofa_component


"""
Component GaussPointContainer

.. autofunction:: GaussPointContainer

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""


@sofa_component
def GaussPointContainer(self, name=None, printLog=None, tags=None, bbox=None, componentState=None, listening=None, method=None, position=None, transforms=None, order=None, volume=None, showSamplesScale=None, drawMode=None, showIndicesScale=None, volumeDim=None, inputVolume=None, **kwargs):
    """
    Container for user defined Gauss points (position and volume)


    :param name: object name  Default value: GaussPointContainer

    :param printLog: if true, emits extra messages at runtime.  Default value: 0

    :param tags: list of the subsets the objet belongs to  Default value: []

    :param bbox: this object bounding box  Default value: [[1.7976931348623157e+308, 1.7976931348623157e+308, 1.7976931348623157e+308], [-1.7976931348623157e+308, -1.7976931348623157e+308, -1.7976931348623157e+308]]

    :param componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).  Default value: Undefined

    :param listening: if true, handle the events, otherwise ignore the events  Default value: 0

    :param method: quadrature method  Default value: 0 - Gauss-Legendre

    :param position: output sample positions  Default value: []

    :param transforms: output sample orientations  Default value: []

    :param order: order of quadrature method  Default value: 1

    :param volume: output weighted volume  Default value: []

    :param showSamplesScale: show samples scale  Default value: 0.0

    :param drawMode: 0: Green points; 1: Green spheres  Default value: 0

    :param showIndicesScale: show indices scale  Default value: 0.0

    :param volumeDim: dimension of quadrature weight vectors  Default value: 1

    :param inputVolume: weighted volumes (=quadrature weights)  Default value: []


    """
    params = dict(name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, method=method, position=position, transforms=transforms, order=order, volume=volume, showSamplesScale=showSamplesScale, drawMode=drawMode, showIndicesScale=showIndicesScale, volumeDim=volumeDim, inputVolume=inputVolume)
    return "GaussPointContainer", params
