# -*- coding: utf-8 -*-

from sofacomponents.lib.base_component import sofa_component


"""
Component ROIValueMapper

.. autofunction:: ROIValueMapper

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""


@sofa_component
def ROIValueMapper(self, name=None, printLog=None, tags=None, bbox=None, componentState=None, listening=None, nbROIs=None, outputValues=None, defaultValue=None, **kwargs):
    """
    Generate a list of values from value-indices pairs


    :param name: object name  Default value: ROIValueMapper

    :param printLog: if true, emits extra messages at runtime.  Default value: 0

    :param tags: list of the subsets the objet belongs to  Default value: []

    :param bbox: this object bounding box  Default value: [[1.7976931348623157e+308, 1.7976931348623157e+308, 1.7976931348623157e+308], [-1.7976931348623157e+308, -1.7976931348623157e+308, -1.7976931348623157e+308]]

    :param componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).  Default value: Undefined

    :param listening: if true, handle the events, otherwise ignore the events  Default value: 0

    :param nbROIs: size of indices/value vector  Default value: 0

    :param outputValues: New vector of values  Default value: []

    :param defaultValue: Default value for indices out of ROIs  Default value: 0.0


    """
    params = dict(name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, nbROIs=nbROIs, outputValues=outputValues, defaultValue=defaultValue)
    return "ROIValueMapper", params
