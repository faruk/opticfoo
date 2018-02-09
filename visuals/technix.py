from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class Technix(visual):
    def setup(self):
        self.path.removeNode()
        self.path = self.render.attachNewNode("1210mk3")

        self.plane = CardMaker("plane")

        self.plane.setFrame(-10,10,-10,10)
        
        self.card = self.path.attachNewNode(self.plane.generate())

        self.amplifiertex = self.loader.loadTexture("1210amplifier.png")
        #self.comictex = self.loader.loadTexture("1210comic.png")
        self.drivecoiltex = self.loader.loadTexture("1210drivecoil.png")
        self.drivecontroltex = self.loader.loadTexture("1210drivecontrol_pcb.png")
        self.outputtex = self.loader.loadTexture("1210output_pcb.png")
        self.parts1tex = self.loader.loadTexture("1210parts1.png")
        self.parts2tex = self.loader.loadTexture("1210parts2.png")
        self.tonearmtex = self.loader.loadTexture("1210pickup.png")
        self.pitchledtex = self.loader.loadTexture("1210pitchled.png")
        self.schemetex = self.loader.loadTexture("1210scheme.png")
        self.setuptex = self.loader.loadTexture("1210setup.png")
        self.strobeilluminatortex = self.loader.loadTexture("1210strobeilluminator_pcb.png")
        self.stylustex = self.loader.loadTexture("1210stylus.png")
        self.toptex = self.loader.loadTexture("1210top.png")
        self.tonearmbalancetex = self.loader.loadTexture("1210tonearmbalance.png")

        self.path.setTransparency(TransparencyAttrib.MAlpha, 1)
        self.path.setTwoSided(1)

        self.texList = [
            self.amplifiertex,
            #self.comictex,
            self.drivecoiltex,
            self.drivecontroltex,
            self.outputtex,
            self.parts1tex,
            self.parts2tex,
            self.tonearmtex,
            self.pitchledtex,
            self.schemetex,
            self.setuptex,
            self.strobeilluminatortex,
            self.stylustex,
            self.toptex,
            self.tonearmbalancetex
        ]

        self.func = {}

    def performBeat(self):
        map(lambda x: x(), self.func.values())
    
    def effect1(self):
        if 'schemas' in self.func:
            self.func.pop('schemas')
        else:
            self.func['schemas'] = self.schemas
    
    def schemas(self):
        if self.sndX > self.snd.xThreshold:
            x = random.randint(0, len(self.texList)-1)
            self.card.setTexture(self.texList[x],1)
