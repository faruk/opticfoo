from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval, LerpPosInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class Hackers(visual):

    def setTextures(self, t):
        self.textures = t.textures
        self.codetex = self.textures['vrc'].values()

        for x in self.towers:
            x.setTexture(random.sample(self.codetex, 1)[0], 1)

        self.pinkpixels = self.textures['pinkpixels'].values()
        self.top.setTexture(random.sample(self.pinkpixels, 1)[0], 1)
        self.top.setColor(1,1,1,0)
        self.bottom.setTexture(self.textures['grid'])
        self.bottom.setColor(1,1,1,0.5)

    def genTower(self, point):
        tower = self.towerpaths.attachNewNode("tower")
        card = CardMaker("plane")
        card.setFrame(-2.5,2.5,-5,5)
        
        c1 = tower.attachNewNode(card.generate())
        c2 = tower.attachNewNode(card.generate())
        c3 = tower.attachNewNode(card.generate())
        c4 = tower.attachNewNode(card.generate())

        c1.setX(2.5)
        c1.setH(90)

        c2.setX(-2.5)
        c2.setH(-90)

        c3.setY(2.5)
        c3.setH(180)

        c4.setY(-2.5)
        
        self.cards.append(c1)
        self.cards.append(c2)
        self.cards.append(c3)
        self.cards.append(c4)

        tower.setPos(point)
        return tower

    def genElectron(self, point):
        electron = self.electronpaths.attachNewNode("electron")
        sphere = self.loader.loadModel("smiley.egg")
        sphere.setTexture(self.textures['white'], 1)
        sphere.reparentTo(electron)
        sphere.setColor(1,1,1,0.2)
        sphere.setScale(0.5)
        """
        box = self.loader.loadModel("box")
        box.setTexture(self.textures['white'], 1)
        box.setColor(1,1,1,0.4)
        box.setPos(-0.5,-0.5,-0.5)
        box.reparentTo(electron)
        """
        electron.setPos(point)
        x, y, z = point
        target = None
        if not abs(x) == abs(y):
            z = z + random.randint(-4,4)
            if abs(x) > abs(y):
                y = y + random.randint(-4,4)
                target = Vec3(-x,y,z)
            else:
                x = x + random.randint(-4,4)
                target = Vec3(x,-y,z)
        else:
            z = z + random.randint(-4,4)
            target = Vec3(y, x, z)
        t = random.randint(2,10)    
        motion = LerpPosInterval(electron, t, target, Vec3(x,y,z), 'easeInOut')
        fadein = LerpColorInterval(electron, t/2.0, Vec4(1,1,1,1), (1,1,1,0), 'easeIn')
        fadeout = LerpColorInterval(electron, t/2.0, Vec4(1,1,1,0), (1,1,1,1), 'easeOut')
        animation = Parallel(motion, Sequence(fadein, fadeout)).start()

    def setup(self):
        self.path.setTwoSided(1)
        self.towerpaths = self.path.attachNewNode("towers")
        self.cards = []

        self.towers = [
            self.genTower(Vec3(0,0,0)),
            self.genTower(Vec3(20,0,0)),
            self.genTower(Vec3(-20,0,0)),
            self.genTower(Vec3(0,20,0)),
            self.genTower(Vec3(0,-20,0)),
        ]
        self.cardscount = 1
        
        card = CardMaker("plane")
        card.setFrame(-50,50,-50,50)
        self.top = self.path.attachNewNode(card.generate())
        self.top.setPos(0,0,-25)
        self.top.setP(-90)
        self.top.setZ(10)

        self.bottom = self.path.attachNewNode(card.generate())
        self.bottom.setPos(0,0,-25)
        self.bottom.setP(90)
        self.bottom.setZ(-5)

        self.electronpaths = self.path.attachNewNode("electrons")
        self.electrons = []
        self.electron_start_positions = [
            Vec3(-50,10,0),
            Vec3(-50,-10,0),
            Vec3(-50,30,0),
            Vec3(-50,-30,0),
            Vec3(-50,50,0),
            Vec3(-50,-50,0),
            Vec3(50,10,0),
            Vec3(50,-10,0),
            Vec3(50,30,0),
            Vec3(50,-30,0),
            Vec3(50,50,0),
            Vec3(50,-50,0),
            Vec3(10,-50,0),
            Vec3(-10,-50,0),
            Vec3(30,-50,0),
            Vec3(-30,-50,0),
            Vec3(10,50,0),
            Vec3(-10,50,0),
            Vec3(30,50,0),
            Vec3(-30,50,0),
        ]
        self.electron_animations = []

        self.functions = {
            'nothing': self.nothing
        }

    def performBeat(self):
        map(lambda x: x(), self.functions.values())

    def nothing(self):
        pass

    def effect1(self):
        c = random.sample(self.cards, self.cardscount)
        for x in c:
            x.setTexture(random.sample(self.codetex, 1)[0], 1)

    def effect2up(self):
        if self.cardscount > 1:
            self.cardscount = self.cardscount - 1

    def effect3up(self):
        if self.cardscount < 4:
            self.cardscount = self.cardscount + 1

    def pixelize_top(self):
        texture = random.sample(self.pinkpixels,1)[0]
        self.top.setTexture(texture, 1)

    def pixelize(self):
        if self.sndX > self.snd.xThreshold:
            self.pixelize_top()

    def effect4(self):
        self.pixelize_top()

    def effect4up(self):
        if "pixelize" in self.functions:
            self.functions.pop("pixelize")
        else:
            self.functions['pixelize'] = self.pixelize
        
    def effect5(self):
        self.bottom.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, 0.5)

    def colorize_bottom(self):
        if self.sndY > self.snd.yThreshold:
            self.effect5()

    def effect5up(self):
        if "colorize" in self.functions:
            self.functions.pop("colorize")
        else:
            self.functions['colorize'] = self.colorize_bottom

    def plain_tower(self):
        tower = random.sample(self.towers,1)[0]
        for child in tower.getChildren():
            child.clearTexture()
            child.setTexture(self.textures['white'], 1)
        tower.setColor(0,1,1,1)

    def code_tower(self):
        tower = random.sample(self.towers,1)[0]
        for child in tower.getChildren():
            child.setTexture(random.sample(self.codetex, 1)[0], 1)
        tower.setColor(1,1,1,1)

    def tower_madness(self):
        if self.sndY > self.snd.yThreshold:
            self.plain_tower()
            self.code_tower()
        self.plain_tower()

    def effect6up(self):
        if 'towermadness' in self.functions:
            self.functions.pop("towermadness")
        else:
            self.functions['towermadness'] = self.tower_madness

    def effect7up(self):
        self.genElectron(random.sample(self.electron_start_positions, 1)[0])

    def effect0up(self):
        for c in self.cards:
            c.setTexture(random.sample(self.codetex, 1)[0], 1)
        for tower in self.towers:
            tower.setColor(1,1,1,1)
