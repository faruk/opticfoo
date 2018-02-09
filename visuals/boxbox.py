from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval, LerpPosInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class BoxBox(visual):
    
    def setup(self):

        self.cubes = []
        self.cubespath = self.path.attachNewNode("cubes") 
        
        i = 0
        for x in range(0,5):
            for y in range(0,5):
                for z in range(0,5):
                    c = self.loader.loadModel("box.egg")
                    self.cubes.append(c)
                    c.setPos(x,y,z)
                    c.reparentTo(self.cubespath)

                    i = i + 1
                    
        map(lambda x: x.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, 1), self.cubes)
