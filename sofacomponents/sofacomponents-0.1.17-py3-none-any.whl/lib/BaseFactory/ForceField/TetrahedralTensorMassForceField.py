# -*- coding: utf-8 -*-

from sofacomponents.lib.base_component import sofa_component


"""
Component TetrahedralTensorMassForceField

.. autofunction:: TetrahedralTensorMassForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""


@sofa_component
def TetrahedralTensorMassForceField(self, name=None, printLog=None, tags=None, bbox=None, componentState=None, listening=None, isCompliance=None, rayleighStiffness=None, poissonRatio=None, youngModulus=None, edgeInfo=None, **kwargs):
    """
    Linear Elastic Tetrahedral Mesh


    :param name: object name  Default value: TetrahedralTensorMassForceField

    :param printLog: if true, emits extra messages at runtime.  Default value: 0

    :param tags: list of the subsets the objet belongs to  Default value: []

    :param bbox: this object bounding box  Default value: [[1.7976931348623157e+308, 1.7976931348623157e+308, 1.7976931348623157e+308], [-1.7976931348623157e+308, -1.7976931348623157e+308, -1.7976931348623157e+308]]

    :param componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).  Default value: Undefined

    :param listening: if true, handle the events, otherwise ignore the events  Default value: 0

    :param isCompliance: Consider the component as a compliance, else as a stiffness  Default value: 0

    :param rayleighStiffness: Rayleigh damping - stiffness matrix coefficient  Default value: 0.0

    :param poissonRatio: Poisson ratio in Hooke's law  Default value: 0.3

    :param youngModulus: Young modulus in Hooke's law  Default value: 1000.0

    :param edgeInfo: Internal edge data  Default value: 


    """
    params = dict(name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, poissonRatio=poissonRatio, youngModulus=youngModulus, edgeInfo=edgeInfo)
    return "TetrahedralTensorMassForceField", params
