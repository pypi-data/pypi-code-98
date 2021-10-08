# -*- coding: utf-8 -*-

from sofacomponents.lib.base_component import sofa_component


"""
Component TriangleSetTopologyModifier

.. autofunction:: TriangleSetTopologyModifier

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""


@sofa_component
def TriangleSetTopologyModifier(self, name=None, printLog=None, tags=None, bbox=None, componentState=None, listening=None, propagateToDOF=None, list_Out=None, **kwargs):
    """
    Triangle set topology modifier


    :param name: object name  Default value: TriangleSetTopologyModifier

    :param printLog: if true, emits extra messages at runtime.  Default value: 0

    :param tags: list of the subsets the objet belongs to  Default value: []

    :param bbox: this object bounding box  Default value: [[1.7976931348623157e+308, 1.7976931348623157e+308, 1.7976931348623157e+308], [-1.7976931348623157e+308, -1.7976931348623157e+308, -1.7976931348623157e+308]]

    :param componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).  Default value: Undefined

    :param listening: if true, handle the events, otherwise ignore the events  Default value: 0

    :param propagateToDOF:  propagate changes to MEchanical object DOFs if true  Default value: 1

    :param list_Out: triangles with at least one null values.  Default value: []


    """
    params = dict(name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, propagateToDOF=propagateToDOF, list_Out=list_Out)
    return "TriangleSetTopologyModifier", params
