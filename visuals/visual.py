class visual:
    def __init__(self, loader, render, snd):
        self.snd = snd
        self.loader = loader
        self.render = render
        self.path = self.loader.loadModel("voyager")
        self.path.reparentTo(self.render)
        self.visualMovementSpeed = 1.0
        self.scaleValue = 10.0
        self.path.setPos(0,-self.scaleValue/2,0)
        self.path.setRenderModeWireframe()

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
        bass, mid, hi = self.snd.getBeat()
        self.path.setScale(self.scaleValue + ( 1*(bass/100)))
