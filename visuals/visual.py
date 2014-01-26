'''
Author: Jan Swoboda
Date: April - July 2013

Copyright 2013

LEGAL INFO:

This file is part of opticfoo (virtual room VJ concept - VRC in short).

Opticfoo is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Opticfoo is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
'''

from operationmap import operationMap
from panda3d.core import TransparencyAttrib

class visual:
    def __init__(self, loader, render, snd):
        # hold state of visual
        self.beatdetect = True
        self.active = True
        self.sndX = 0.0 # bass
        self.sndY = 0.0 # mid
        self.sndZ = 0.0 # high
        self.visualMovementSpeed = 1.0
        self.scale = 1.0
        self.transparency = 1.0
        self.transparencyToggle = False
        self.visualMovementSpeedToggle = False
        self.scaleToggle = False

        self.snd = snd
        self.loader = loader
        self.render = render

        self.path = self.render.attachNewNode('dummy')
        self.path.setPos(0,0,0)
        self.path.setTransparency(TransparencyAttrib.MAlpha)
#        self.path.setRenderModeWireframe()

        self.attached = True
        self.op = operationMap.copy()

        self.specialStatusString = """
This is a visual Template which has no special status.
Just a placeholder for the case. blablabla
bla bla blab la... . 
"""


        self.setup() # also apply custom stuff
        self.detach()
        self.path.setTransparency(TransparencyAttrib.MAlpha)

    def getBeat(self):
        self.sndX, self.sndY, self.sndZ = self.snd.getBeat()
        self.performBeat()

    def setup(self): # custom stuff
        pass

    def performBeat(self):
        pass

    def moveLeft(self):
        self.path.setX(self.path, -self.visualMovementSpeed)

    def moveRight(self):
        self.path.setX(self.path, +self.visualMovementSpeed)

    def moveUp(self):
        self.path.setY(self.path, +self.visualMovementSpeed)

    def moveDown(self):
        self.path.setY(self.path, -self.visualMovementSpeed)

    def moveForward(self):
        self.path.setZ(self.path, +self.visualMovementSpeed)

    def moveBackward(self):
        self.path.setZ(self.path, -self.visualMovementSpeed)

    def rotateLeft(self):
        self.path.setH(self.path, +self.visualMovementSpeed)

    def rotateRight(self):
        self.path.setH(self.path, -self.visualMovementSpeed)

    def rotateUp(self):
        self.path.setP(self.path, +self.visualMovementSpeed)

    def rotateDown(self):
        self.path.setP(self.path, -self.visualMovementSpeed)

    def rollLeft(self):
        self.path.setR(self.path, +self.visualMovementSpeed)

    def rollRight(self):
        self.path.setR(self.path, -self.visualMovementSpeed)

    def effect0(self):
        pass

    def effect1(self):
        pass

    def effect2(self):
        pass

    def effect3(self):
        pass

    def effect4(self):
        pass

    def effect5(self):
        pass

    def effect6(self):
        pass

    def effect7(self):
        pass

    def effect8(self):
        pass

    def effect9(self):
        pass

    def effect0up(self):
        pass

    def effect1up(self):
        pass

    def effect2up(self):
        pass

    def effect3up(self):
        pass

    def effect4up(self):
        pass

    def effect5up(self):
        pass

    def effect6up(self):
        pass

    def effect7up(self):
        pass

    def effect8up(self):
        pass

    def effect9up(self):
        pass

    def scaleToBeat(self):
        self.path.setScale(self.scale + ( 1*(self.sndX/100)))

    def detach(self):
        self.path.detachNode()
        self.attached = False

    def attach(self):
        self.path.reparentTo(self.render)
        self.attached = True

    def getPos(self):
        return self.path.getPos()

    def setPos(self, x,y,z):
        self.path.setPos((x,y,z))

    def getHpr(self):
        return self.path.getHpr()

    def setHpr(self, h, p, r):
        self.path.setHpr((h, p, r))

    def setScale(self, value):
        self.scale = value
        print "set scale: ", value
        self.path.setScale(value)

    def getScale(self):
        return self.scale

    def getSpeed(self):
        return self.visualMovementSpeed

    def setSpeed(self, value):
        self.visualMovementSpeed = value

    def setAlpha(self, value):
        self.transparency = value
        print "transparency", value
        self.path.setAlphaScale(self.transparency)

    def getAlpha(self):
        return self.transparency

    def setOp(self, key, value):
        self.op[key] = value

    def update(self):
        if self.op['visual-left'] == 1: self.moveLeft()
        if self.op['visual-right'] == 1: self.moveRight()
        if self.op['visual-up'] == 1: self.moveUp()
        if self.op['visual-down'] == 1: self.moveDown()
        if self.op['visual-forward'] == 1: self.moveForward()
        if self.op['visual-backward'] == 1: self.moveBackward()
        if self.op['visual-rotate-left'] == 1: self.rotateLeft()
        if self.op['visual-rotate-right'] == 1: self.rotateRight()
        if self.op['visual-rotate-up'] == 1: self.rotateUp()
        if self.op['visual-rotate-down'] == 1: self.rotateDown()
        if self.op['visual-roll-left'] == 1: self.rollLeft()
        if self.op['visual-roll-right'] == 1: self.rollRight()
        if self.op['visual-effect0'] == 1: self.effect0()
        if self.op['visual-effect1'] == 1: self.effect1()
        if self.op['visual-effect2'] == 1: self.effect2()
        if self.op['visual-effect3'] == 1: self.effect3()
        if self.op['visual-effect4'] == 1: self.effect4()
        if self.op['visual-effect5'] == 1: self.effect5()
        if self.op['visual-effect6'] == 1: self.effect6()
        if self.op['visual-effect7'] == 1: self.effect7()
        if self.op['visual-effect8'] == 1: self.effect8()
        if self.op['visual-effect9'] == 1: self.effect9()

    def keyUpEvent(self, key):
        if key == 'visual-effect0': self.effect0up()
        if key == 'visual-effect1': self.effect1up()
        if key == 'visual-effect2': self.effect2up()
        if key == 'visual-effect3': self.effect3up()
        if key == 'visual-effect4': self.effect4up()
        if key == 'visual-effect5': self.effect5up()
        if key == 'visual-effect6': self.effect6up()
        if key == 'visual-effect7': self.effect7up()
        if key == 'visual-effect8': self.effect8up()
        if key == 'visual-effect9': self.effect9up()

    def getSpecialStatus(self):
        return self.specialStatusString

    def setMovementSpeed(self, value):
        self.visualMovementSpeed = value

    def setMovementSpeedToggle(self):
        self.scaleToggle = False
        self.transparencyToggle = False;
        self.visualMovementSpeedToggle = True;

    def setScaleToggle(self):
        self.transparencyToggle = False
        self.visualMovementSpeedToggle = False
        self.scaleToggle = True

    def setTransparencyToggle(self):
        self.scaleToggle = False
        self.visualMovementSpeedToggle = False
        self.transparencyToggle = True

    def increaseValue(self):
        if self.scaleToggle : 
            self.setScale(self.scale + 0.01)
        if self.transparencyToggle : 
            if self.transparency < 1: 
                self.setAlpha(self.transparency + 0.01)
        if self.visualMovementSpeedToggle : 
            self.setMovementSpeed(self.visualMovementSpeed + 0.01)

    def decreaseValue(self):
        if self.scaleToggle : 
            if self.scale > 0 : self.setScale(self.scale - 0.01)
        if self.transparencyToggle : 
            if self.transparency > 0: self.setAlpha(self.transparency - 0.01)
        if self.visualMovementSpeedToggle : 
            self.setMovementSpeed(self.visualMovementSpeed - 0.01)

    def resetOperationMap(self):
        for x in self.op:
            self.op[x] = 0
        self.visualMovementSpeed = 1

    def getVisualToggleInfo(self):
        if self.transparencyToggle : return "transparency"
        if self.visualMovementSpeedToggle : return "speed"
        if self.scaleToggle : return "scale"
        else: return "nothing"
