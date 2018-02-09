from operationmap import operationMap

class CameraOperations:
    def __init__(self, vrc):
        self.vrc = vrc
        self.op = operationMap
        self.cam = self.vrc.cam
        self.otherCam = self.vrc.otherCam
        self.camSpeed = 1
        self.heading = 180
        self.pitch = 0
        self.win = self.vrc.win

    def setOperationMap(self, key, value):
        self.op[key] = value

    def setCamOperation(self, key):
        if key == 'a' : self.setOperationMap('cam-left', 1)
        if key == 'a-up' : self.setOperationMap('cam-left', 0)
        if key == 'd' : self.setOperationMap('cam-right', 1)
        if key == 'd-up' : self.setOperationMap('cam-right', 0)
        if key == 'w' : self.setOperationMap('cam-forward', 1)
        if key == 'w-up' : self.setOperationMap('cam-forward', 0)
        if key == 's' : self.setOperationMap('cam-backward', 1)
        if key == 's-up' : self.setOperationMap('cam-backward', 0)
        if key == 'h' : self.setOperationMap('cam-rotate-left', 1)
        if key == 'h-up' : self.setOperationMap('cam-rotate-left', 0)
        if key == 'l' : self.setOperationMap('cam-rotate-right', 1)
        if key == 'l-up' : self.setOperationMap('cam-rotate-right', 0)
        if key == 'j' : self.setOperationMap('cam-rotate-down', 1)
        if key == 'j-up' : self.setOperationMap('cam-rotate-down', 0)
        if key == 'k' : self.setOperationMap('cam-rotate-up', 1)
        if key == 'k-up' : self.setOperationMap('cam-rotate-up', 0)
        if key == 'i' : self.setOperationMap('cam-roll-right', 1)
        if key == 'i-up' : self.setOperationMap('cam-roll-right', 0)
        if key == 'u' : self.setOperationMap('cam-roll-left', 1)
        if key == 'u-up' : self.setOperationMap('cam-roll-left', 0)
        if key == 'space' : self.setOperationMap('cam-up', 1)
        if key == 'space-up' : self.setOperationMap('cam-up', 0)
        if key == 'shift' : self.setOperationMap('cam-down', 1)
        if key == 'shift-up' : self.setOperationMap('cam-down', 0)
        if key == 'r' : self.setOperationMap('cam-reset', 1)
        if key == 'r-up': self.setOperationMap('cam-reset', 0)
        if key == 'f':
            self.setOperationMap('cam-sync-toggle', -self.op['cam-sync-toggle'])
            self.camAfterMath()
        if key == 'g':
            self.setOperationMap('cam-fix-toggle', -self.op['cam-fix-toggle'])
            self.camAfterMath()
        if key == 't':
            self.setOperationMap('cam-sync-to', -self.op['cam-sync-to'])
            self.camAfterMath()
        if key == "wheel-up" : self.increaseCamSpeed()
        if key == "wheel-down" : self.decreaseCamSpeed()
        if key == 'mouse1' :
            self.setOperationMap('cam-mouse-control', 1)
            self.win.movePointer(0, 100, 100)
        if key == 'mouse1-up' : self.setOperationMap('cam-mouse-control', 0)

    def executeOperations(self, task):
        # camera operations
        if self.op['cam-left'] == 1: self.moveCamLeft()
        if self.op['cam-right'] == 1: self.moveCamRight()
        if self.op['cam-up'] == 1: self.moveCamUp()
        if self.op['cam-down'] == 1: self.moveCamDown()
        if self.op['cam-forward'] == 1: self.moveCamForward()
        if self.op['cam-backward'] == 1: self.moveCamBackward()
        if self.op['cam-rotate-left'] == 1: self.rotateCamLeft()
        if self.op['cam-rotate-right'] == 1: self.rotateCamRight()
        if self.op['cam-rotate-up'] == 1: self.rotateCamUp()
        if self.op['cam-rotate-down'] == 1: self.rotateCamDown()
        if self.op['cam-roll-left'] == 1: self.rollCamLeft()
        if self.op['cam-roll-right'] == 1: self.rollCamRight()
        if self.op['cam-reset'] == 1: self.resetCam()

        return task.cont

    def moveCamLeft(self):
        self.cam.setX(self.cam, -self.camSpeed)
        self.camAfterMath()

    def moveCamRight(self):
        self.cam.setX(self.cam, +self.camSpeed)
        self.camAfterMath()

    def moveCamUp(self):
        self.cam.setZ(self.cam, +self.camSpeed)
        self.camAfterMath()

    def moveCamDown(self):
        self.cam.setZ(self.cam, -self.camSpeed)
        self.camAfterMath()

    def moveCamForward(self):
        self.cam.setY(self.cam, +self.camSpeed)
        self.camAfterMath()

    def moveCamBackward(self):
        self.cam.setY(self.cam, -self.camSpeed)
        self.camAfterMath()

    def rotateCamLeft(self):
        self.cam.setH(self.cam, +self.camSpeed)
        self.camAfterMath()

    def rotateCamRight(self):
        self.cam.setH(self.cam, -self.camSpeed)
        self.camAfterMath()

    def rotateCamUp(self):
        self.cam.setP(self.cam, +self.camSpeed)
        self.camAfterMath()

    def rotateCamDown(self):
        self.cam.setP(self.cam, -self.camSpeed)
        self.camAfterMath()

    def rollCamLeft(self):
        self.cam.setR(self.cam, -self.camSpeed)
        self.camAfterMath()

    def rollCamRight(self):
        self.cam.setR(self.cam, +self.camSpeed)
        self.camAfterMath()

    def resetCam(self):
        self.cam.setPos(0,-100,0)

    def increaseCamSpeed(self):
        self.camSpeed = self.camSpeed + 0.1

    def decreaseCamSpeed(self):
        self.camSpeed = self.camSpeed - 0.1

    def camAfterMath(self):
        if self.op['cam-fix-toggle'] > 0:
            #self.cam.lookAt(self.activeVisual.path.getBounds().getCenter())
            if self.vrc.activeVisual != None:
                self.cam.lookAt(self.vrc.activeVisual.path)
        if self.op['cam-sync-toggle'] > 0:
            if self.op['cam-sync-to'] > 0:
                self.otherCam.setPos(self.cam.getPos())
                self.otherCam.setHpr(self.cam.getHpr())
            else:
                self.cam.setPos(self.otherCam.getPos())
                self.cam.setHpr(self.otherCam.getHpr())

    # camera mouse control
    def controlCamera(self, task):
        # figure out how much the mouse has moved (in pixels)
        if self.op['cam-mouse-control'] == 1:
            md = self.win.getPointer(0)
            x = md.getX()
            y = md.getY()
            self.heading = self.cam.getH()
            self.pitch = self.cam.getP()
            if self.win.movePointer(0, 100, 100):
                self.heading = self.heading - (x - 100) * 0.1
                self.pitch = self.pitch - (y - 100) * 0.1
            self.cam.setHpr(self.heading,self.pitch, self.cam.getR())
            self.camAfterMath()
        return task.cont

    def setCamSpeed(self, value):
        self.camSpeed = value
