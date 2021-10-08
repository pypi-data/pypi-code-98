# -*- coding: utf-8 -*-

from sofacomponents.lib.base_component import sofa_component


"""
Component DefaultAnimationLoop

.. autofunction:: DefaultAnimationLoop

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""


@sofa_component
def DefaultAnimationLoop(self, name=None, printLog=None, tags=None, bbox=None, componentState=None, listening=None, **kwargs):
    """
    Simulation loop to use in scene without constraints nor contact.

This loop do the following steps:
- build and solve all linear systems in the scene : collision and time integration to compute the new values of the dofs
- update the context (dt++)
- update the mappings
- update the bounding box (volume covering all objects of the scene)


    :param name: object name  Default value: DefaultAnimationLoop

    :param printLog: if true, emits extra messages at runtime.  Default value: 0

    :param tags: list of the subsets the objet belongs to  Default value: []

    :param bbox: this object bounding box  Default value: [[1.7976931348623157e+308, 1.7976931348623157e+308, 1.7976931348623157e+308], [-1.7976931348623157e+308, -1.7976931348623157e+308, -1.7976931348623157e+308]]

    :param componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).  Default value: Undefined

    :param listening: if true, handle the events, otherwise ignore the events  Default value: 0


    """
    params = dict(name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening)
    return "DefaultAnimationLoop", params
