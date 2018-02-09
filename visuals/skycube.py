from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
from helper.colors import Colors
import random
from visual import visual

class SkyCube(visual):
    def setTextures(self, t):
        self.textures = t.textures
        self.texList = self.textures['technics'].values()
        self.stripetex = self.textures['stripes']
        self.box1.setTexture(self.stripetex, 1)
        self.codetex = self.textures['vrc']['0']

    def setup(self):
        self.Colors = Colors()

        self.box1 = self.loader.loadModel("box.egg")
        self.box2 = self.loader.loadModel("box.egg")

        self.apollotex = MovieTexture("textures/apollo_big.avi")
        self.facetex = MovieTexture("textures/astronaut_big.avi")
        self.trackboy1 = MovieTexture("textures/4trackboy_explosions.mpeg")
        self.trackboy2 = MovieTexture("textures/4trackboy_explosions3.avi")
        self.trackboy3 = MovieTexture("textures/4trackboy_atomic.avi")
        assert self.apollotex.read("textures/apollo_big.avi")
        assert self.facetex.read("textures/astronaut_big.avi")
        assert self.trackboy1.read("textures/4trackboy_explosions.mpeg")
        assert self.trackboy2.read("textures/4trackboy_explosions3.avi")
        assert self.trackboy3.read("textures/4trackboy_atomic.avi")

        self.box1.setTwoSided(1)
        self.box1.reparentTo(self.path)
        self.box1.setPos(Vec3(-50,-50, -50))
        self.box1.setScale(100)

        """
        self.amplifiertex = self.loader.loadTexture("1210amplifier.png")
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
        self.texList = [
            self.amplifiertex,
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
        """
        self.func = {}

    def performBeat(self):
        map(lambda x: x(), self.func.values())
    
    def effect1up(self):
        self.box1.clearTexture()
        self.box1.setTexture(self.apollotex, 1)
        self.apollotex.play()

    def effect2up(self):
        self.box1.clearTexture()
        self.box1.setTexture(self.facetex, 1)
        self.facetex.play()

    def effect3up(self):
        self.box1.clearTexture()
        #ts = TextureStage('ts')
        #ts.setMode(TextureStage.MGlow)
        self.box1.setColor(1,1,1,1)
        self.box1.setTexture(self.stripetex, 1)

    def effect4up(self):
        if 'schemas' in self.func:
            self.func.pop('schemas')
        else:
            self.func['schemas'] = self.schemas

    def effect5up(self):
        self.box1.setColor(1,1,1,1)

    def effect6up(self):
        self.box1.clearTexture()
        self.box1.setTexture(self.trackboy3, 1)
        self.trackboy3.play()

    def effect7up(self):
        self.box1.clearTexture()
        self.box1.setTexture(self.trackboy2, 1)
        self.trackboy3.play()

    def effect8(self):
        #self.box1.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, 1)
        v =  random.sample(self.Colors.colors['sunset cloud colors'], 1)[0]
        r, g, b, a = v
        self.box1.setColor(r, g, b, a)

    def colors(self):
        if self.sndY > self.snd.yThreshold:
            self.effect8()

    def effect9up(self):
        if 'colors' in self.func:
            self.func.pop('colors')
            self.box1.setColor(1,1,1,1)
        else:
            self.func['colors'] = self.colors

    def effect0up(self):
        self.apollotex.stop()
        self.facetex.stop()
    
    def schemas(self):
        if self.sndX > self.snd.xThreshold:
            x = random.randint(0, len(self.texList)-1)
            self.box1.setTexture(self.texList[x],1)
