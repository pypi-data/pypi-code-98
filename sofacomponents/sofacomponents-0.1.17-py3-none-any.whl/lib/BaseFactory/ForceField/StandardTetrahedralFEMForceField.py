# -*- coding: utf-8 -*-

from sofacomponents.lib.base_component import sofa_component


"""
Component StandardTetrahedralFEMForceField

.. autofunction:: StandardTetrahedralFEMForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""


@sofa_component
def StandardTetrahedralFEMForceField(self, name=None, printLog=None, tags=None, bbox=None, componentState=None, listening=None, isCompliance=None, rayleighStiffness=None, materialName=None, ParameterSet=None, AnisotropyDirections=None, ParameterFile=None, tetrahedronInfo=None, edgeInfo=None, **kwargs):
    """
    Generic Tetrahedral finite elements


    :param name: object name  Default value: StandardTetrahedralFEMForceField

    :param printLog: if true, emits extra messages at runtime.  Default value: 0

    :param tags: list of the subsets the objet belongs to  Default value: []

    :param bbox: this object bounding box  Default value: [[1.7976931348623157e+308, 1.7976931348623157e+308, 1.7976931348623157e+308], [-1.7976931348623157e+308, -1.7976931348623157e+308, -1.7976931348623157e+308]]

    :param componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).  Default value: Undefined

    :param listening: if true, handle the events, otherwise ignore the events  Default value: 0

    :param isCompliance: Consider the component as a compliance, else as a stiffness  Default value: 0

    :param rayleighStiffness: Rayleigh damping - stiffness matrix coefficient  Default value: 0.0

    :param materialName: the name of the material to be used  Default value: ArrudaBoyce

    :param ParameterSet: The global parameters specifying the material  Default value: []

    :param AnisotropyDirections: The global directions of anisotropy of the material  Default value: []

    :param ParameterFile: the name of the file describing the material parameters for all tetrahedra  Default value: myFile.param

    :param tetrahedronInfo: Internal tetrahedron data  Default value: 

    :param edgeInfo: Internal edge data  Default value: 


    """
    params = dict(name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, materialName=materialName, ParameterSet=ParameterSet, AnisotropyDirections=AnisotropyDirections, ParameterFile=ParameterFile, tetrahedronInfo=tetrahedronInfo, edgeInfo=edgeInfo)
    return "StandardTetrahedralFEMForceField", params
