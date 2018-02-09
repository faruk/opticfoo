from panda3d.core import Triangulator,GeomVertexFormat,GeomVertexData,Geom,GeomVertexWriter,GeomTriangles,GeomNode

class Polygon(object):
    def __init__(self,vertices=[]):
        self.vertices=list(tuple(v) for v in vertices)
    def addVertex(self,x,y):
        self.vertices.append((x,y))
    def makeNode(self,pointmap=(lambda x,y: (x,y,0))):
        vt=tuple(self.vertices)
        t=Triangulator()
        fmt=GeomVertexFormat.getV3()
        vdata = GeomVertexData('name', fmt, Geom.UHStatic)
        vertex = GeomVertexWriter(vdata, 'vertex')
        for x,y in vt:
            t.addPolygonVertex(t.addVertex(x,y))
            vertex.addData3f(pointmap(x,y))
        t.triangulate()
        prim = GeomTriangles(Geom.UHStatic)
        for n in xrange(t.getNumTriangles()):
            prim.addVertices(t.getTriangleV0(n),t.getTriangleV1(n),t.getTriangleV2(n))
        prim.closePrimitive()
        geom = Geom(vdata)
        geom.addPrimitive(prim) 
        node = GeomNode('gnode')
        node.addGeom(geom)
        return node

#simple demonstration

poly=Polygon([(0,0),(0,1),(1,1),(1,0)])

import direct.directbase.DirectStart

nodePath = render.attachNewNode(poly.makeNode())

run()
