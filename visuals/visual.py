from operationmap import operationMap

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

        self.snd = snd
        self.loader = loader
        self.render = render

        self.path = self.loader.loadModel("monitor")
        self.path.reparentTo(self.render)
        self.path.setPos(0,0,0)
#        self.path.setRenderModeWireframe()

        self.attached = True
        self.op = operationMap

        self.specialStatusString = """
This is a visual Template which has no special status.
Just a placeholder for the case. blablabla
bla bla blab la... . 
"""


        self.setup() # also apply custom stuff

    def getBeat(self):
        self.sndX, self.sndY, self.sndZ = self.snd.getBeat()
        self.performBeat()

    def setup(self): # custom stuff
        pass

    def performBeat(self):
        self.scaleToBeat()
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

    def updateOperationMap(self, op):
        self.op = dict(op)

    def getOperationMap(self):
        return self.op

    def getSpecialStatus(self):
        return self.specialStatusString

    def setMovementSpeed(self, value):
        self.visualMovementSpeed = value
