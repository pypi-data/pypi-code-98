# -*- coding: utf-8 -*-

from sofacomponents.lib.base_component import sofa_component


"""
Component Spiral

.. autofunction:: Spiral

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""


@sofa_component
def Spiral(self, name=None, printLog=None, tags=None, bbox=None, componentState=None, listening=None, rest_position=None, position=None, curvature=None, **kwargs):
    """
    This class truns on spiral any topological model


    :param name: object name  Default value: Spiral

    :param printLog: if true, emits extra messages at runtime.  Default value: 0

    :param tags: list of the subsets the objet belongs to  Default value: []

    :param bbox: this object bounding box  Default value: [[1.7976931348623157e+308, 1.7976931348623157e+308, 1.7976931348623157e+308], [-1.7976931348623157e+308, -1.7976931348623157e+308, -1.7976931348623157e+308]]

    :param componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).  Default value: Undefined

    :param listening: if true, handle the events, otherwise ignore the events  Default value: 0

    :param rest_position: Rest position coordinates of the degrees of freedom  Default value: []

    :param position: Position coordinates of the degrees of freedom  Default value: []

    :param curvature: Spiral curvature factor  Default value: 0.2


    """
    params = dict(name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, rest_position=rest_position, position=position, curvature=curvature)
    return "Spiral", params
