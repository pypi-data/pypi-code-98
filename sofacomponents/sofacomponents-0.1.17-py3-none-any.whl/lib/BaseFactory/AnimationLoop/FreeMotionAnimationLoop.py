# -*- coding: utf-8 -*-

from sofacomponents.lib.base_component import sofa_component


"""
Component FreeMotionAnimationLoop

.. autofunction:: FreeMotionAnimationLoop

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""


@sofa_component
def FreeMotionAnimationLoop(self, name=None, printLog=None, tags=None, bbox=None, componentState=None, listening=None, solveVelocityConstraintFirst=None, threadSafeVisitor=None, **kwargs):
    """
    
The animation loop to use with constraints.
You must add this loop at the beginning of the scene if you are using constraints."


    :param name: object name  Default value: FreeMotionAnimationLoop

    :param printLog: if true, emits extra messages at runtime.  Default value: 0

    :param tags: list of the subsets the objet belongs to  Default value: []

    :param bbox: this object bounding box  Default value: [[1.7976931348623157e+308, 1.7976931348623157e+308, 1.7976931348623157e+308], [-1.7976931348623157e+308, -1.7976931348623157e+308, -1.7976931348623157e+308]]

    :param componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).  Default value: Undefined

    :param listening: if true, handle the events, otherwise ignore the events  Default value: 0

    :param solveVelocityConstraintFirst: solve separately velocity constraint violations before position constraint violations  Default value: 0

    :param threadSafeVisitor: If true, do not use realloc and free visitors in fwdInteractionForceField.  Default value: 0


    """
    params = dict(name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, solveVelocityConstraintFirst=solveVelocityConstraintFirst, threadSafeVisitor=threadSafeVisitor)
    return "FreeMotionAnimationLoop", params
