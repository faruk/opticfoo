from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class Sphere(visual):
    def setup(self):
        self.texture_list = [
            self.loader.loadTexture("spherical_stars_hi.png"),
        ]

        self.sphere = self.loader.loadModel("smiley.egg")
        self.sphere.setTexture(self.texture_list[0], 1)
        self.sphere.setTwoSided(1)

        self.sphere.reparentTo(self.path)
        self.sphere.setScale(200)


