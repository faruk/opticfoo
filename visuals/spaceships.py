from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval, LerpPosInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class SpaceShips(visual):

    def setup(self):
        
        self.stardestroyer = self.loader.loadModel("stardestroyer")
        self.sts = self.loader.loadModel("sts")
        self.enterprise = self.loader.loadModel("enterprise")
        self.saturnv = self.loader.loadModel("saturn")

        self.ship = self.path.attachNewNode("ship")

        self.ships = [
            self.stardestroyer,
            self.sts,
            self.enterprise,
            self.saturnv,
        ]

    def effect1up(self):
        ship = self.ships.pop(0)
        ship.reparentTo(self.ship)
        self.ships.append(ship)
