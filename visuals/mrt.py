from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval, LerpPosInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class MRT(visual):

    def setup(self):
        card = CardMaker("plane")

        card.setFrame(-10,10,-10,10)

        self.path.setTwoSided(1)
        self.card = self.path.attachNewNode("card")
        self.card.attachNewNode(card.generate())

        self.mrt = MovieTexture("textures/mrt.avi")
        assert self.mrt.read('textures/mrt.avi')

    def effect1up(self):
        self.card.clearTexture()
        self.card.setTexture(self.mrt, 1)
        self.mrt.play()

    def effect0up(self):
        self.card.clearTexture()
