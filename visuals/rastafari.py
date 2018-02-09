from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval, LerpPosInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class Rastafari(visual):

    def setup(self):
        card = CardMaker("plane")
        card.setFrame(-10,10,-10,10)

        self.boxes = []
        self.whitetex = self.loader.loadTexture("white.png")
        for x in range(0,3):
            self.boxes.append(self.path.attachNewNode("box"+str(x)))

        for x in range(0,3):
            box = self.loader.loadModel("box.egg")
            box.setScale(20)
            box.setSx(box, 50)
            box.setPos(-10,-10,-10)
            box.reparentTo(self.boxes[x])
        
        self.path.setTexture(self.whitetex, 1)
        self.red = Vec4(1,0,0,1)
        self.yellow = Vec4(1,1,0,1)
        self.green = Vec4(0,1,0,1)
        self.colors = [self.red, self.yellow, self.green]

        self.boxes[0].setColor(self.red)
        self.boxes[1].setColor(self.yellow)
        self.boxes[2].setColor(self.green)

        self.boxes[0].setY(self.boxes[0], -15)
        self.boxes[0].setZ(self.boxes[0], -15)
        self.boxes[1].setY(self.boxes[1], 15)
        self.boxes[1].setZ(self.boxes[1], -15)
        self.boxes[2].setY(self.boxes[2], 0)
        self.boxes[2].setZ(self.boxes[2], 15)

        for x in range(0,3):
            self.boxes[x].setX(-25)

        self.rotations = [
            self.rotateInterval(self.boxes[0], 5, True),
            self.rotateInterval(self.boxes[1], 5, True),
            self.rotateInterval(self.boxes[2], 5, True),
            self.rotateInterval(self.boxes[0], 5, False),
            self.rotateInterval(self.boxes[1], 5, False),
            self.rotateInterval(self.boxes[2], 5, False),
        ]

        self.soundfunctions = {
            'count': self.count
        }
        self.beatcount = 0
        self.lowbeatcount = 0
        self.midbeatcount = 0
        self.hibeatcount = 0

    def rotateInterval(self, path, t, positive = True):
        degree = 360
        if not positive: degree = -360
        return LerpHprInterval(path, t, Vec3(0,0,0), Vec3(0,degree,0)) 


    def performBeat(self):
        map(lambda x: x(), self.soundfunctions.values())

    def effect1up(self):
        if 'rotate1' in self.soundfunctions:
            self.soundfunctions.pop('rotate1')
            print "rotate1 off"
        else:
            self.soundfunctions['rotate1'] = self.randomrotate
            print "rotate1 on"

    def playrotation(self, rotation):
        if rotation.isPlaying():
            rotation.finish()
        else:
            rotation.loop()

    def randomrotate(self):
        r = random.randint(0,1)
        if self.sndX > self.snd.xThreshold:
            if self.lowbeatcount % 10 == 0:
                self.lowbeatcount = self.lowbeatcount + 1
                rotations = random.sample(self.rotations, 3)
                map(lambda x: self.playrotation(x), rotations) 

    def effect2up(self):
        if 'negativemovementspeed' in self.soundfunctions:
            self.soundfunctions.pop('negativemovementspeed')
            print "negativemovementspeed off"
        else:
            self.soundfunctions['negativemovementspeed'] = self.negativemovementspeed
            print "negativemovementspeed on"

    def negativemovementspeed(self):
        if self.lowbeatcount % 99 == 0:
            self.visualMovementSpeed = self.visualMovementSpeed * -1
            self.lowbeatcount = self.lowbeatcount + 1

    def nothing(self):
        pass

    def count(self):
        if self.sndX > self.snd.xThreshold: self.lowbeatcount = self.lowbeatcount + 1
        if self.sndY > self.snd.yThreshold: self.midbeatcount = self.midbeatcount + 1
        if self.sndZ > self.snd.zThreshold: self.hibeatcount = self.hibeatcount + 1

