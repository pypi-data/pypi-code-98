# -*- coding: utf-8 -*-

from sofacomponents.lib.base_component import sofa_component


"""
Component TriangleSetTopologyContainer

.. autofunction:: TriangleSetTopologyContainer

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""


@sofa_component
def TriangleSetTopologyContainer(self, name=None, printLog=None, tags=None, bbox=None, componentState=None, listening=None, filename=None, position=None, checkTopology=None, nbPoints=None, points=None, edges=None, checkConnexity=None, triangles=None, **kwargs):
    """
    Triangle set topology container


    :param name: object name  Default value: TriangleSetTopologyContainer

    :param printLog: if true, emits extra messages at runtime.  Default value: 0

    :param tags: list of the subsets the objet belongs to  Default value: []

    :param bbox: this object bounding box  Default value: [[1.7976931348623157e+308, 1.7976931348623157e+308, 1.7976931348623157e+308], [-1.7976931348623157e+308, -1.7976931348623157e+308, -1.7976931348623157e+308]]

    :param componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).  Default value: Undefined

    :param listening: if true, handle the events, otherwise ignore the events  Default value: 0

    :param filename: Filename of the mesh  Default value: 

    :param position: Initial position of points  Default value: []

    :param checkTopology: Parameter to activate internal topology checks (might slow down the simulation)  Default value: 0

    :param nbPoints: Number of points  Default value: 0

    :param points: List of point indices  Default value: []

    :param edges: List of edge indices  Default value: []

    :param checkConnexity: It true, will check the connexity of the mesh.  Default value: 0

    :param triangles: List of triangle indices  Default value: []


    """
    params = dict(name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, filename=filename, position=position, checkTopology=checkTopology, nbPoints=nbPoints, points=points, edges=edges, checkConnexity=checkConnexity, triangles=triangles)
    return "TriangleSetTopologyContainer", params
