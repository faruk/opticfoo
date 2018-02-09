from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval, LerpPosInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class Trotzdem(visual):

    def setup(self):

        card = CardMaker("plane")

        card.setFrame(-10,10,-10,10)

        self.trotzdempath = self.path.attachNewNode(card.generate())

        self.background = self.path.attachNewNode(card.generate())

        self.trotzdemtex = self.loader.loadTexture("trotzdem.png")

        self.trotzdempath.setTexture(self.trotzdemtex, 1)

        self.background.setPos(0,0,1)

        self.background.setColor(1,1,0,1)

    def performBeat(self):
        pass
