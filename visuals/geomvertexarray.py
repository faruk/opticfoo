from panda3d.core import GeomVertexArrayFormat
from panda3d.core import Geom
from panda3d.core import InternalName
from panda3d.core import GeoVertexData
from panda3d.core import GeomVertexFormat
from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval, LerpPosInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class GeomVertexArray(visual):
    
    def setup(self):
        array = GeomVertexArrayFormat()
        array.addColumn(InternalName.make('vertex'), 3, Geom NTFloat32, Geom.CPoint)
        array.addColumn(InternalName.make('texcoord'), 2, Geom.NTFloat32, Geom.CTexcoord)

        format = GeomVertexFormat()
        format.addArray(array)

        format = GeomVertexFormat.registerFormat(format)

        vdata = GeomVertexData('name', formate, Geom.UHStatic)

        vdata.setNumRows(4)
        vertex = GeomVertexWriter(vdata, 'vertex')
        normal = GeomVertexWriter(vdata, 'normal')
        color = GeomVertexWriter(vdata, 'color')
        texcoord = GeomVertexWriter(vdata, 'texcoord')

        vertex.addData3f(1, 0, 0)
        normal.addData3f(0, 0, 1)
        color.addData4f(0, 0, 1, 1)
        texcoord.addData2f(1, 0)

        vertex.addData3f(1, 1, 0)
        normal.addData3f(0, 0, 1)
        color.addData4f(0, 0, 1, 1)
        texcoort.addData2f(1, 1)
