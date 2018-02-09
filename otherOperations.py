from panda3d.core import VBase4
class OtherOperations:

    def __init__(self, vrc):
        self.vrc = vrc

        # booleans representing states
        self.clearColor = True
        self.alpha = 1.0
        self.red = 1.0
        self.green = 1.0
        self.blue = 1.0

    def setOperation(self, key):
        print key
        if key == "f" : self.toggleClearColor()
        if key == "2": self.plusAlpha()
        if key == "1": self.minusAlpha()
        if key == "3": self.minusRed()
        if key == "4": self.plusRed()
        if key == "5": self.minusGreen()
        if key == "6": self.plusGreen()
        if key == "7": self.minusBlue()
        if key == "8": self.plusBlue()

    def toggleClearColor(self):
        if self.clearColor:
            self.vrc.win.setClearColorActive(False)
            self.vrc.otherWin.setClearColorActive(False)
            self.clearColor = False
        else:
            self.vrc.win.setClearColorActive(True)
            self.vrc.otherWin.setClearColorActive(True)
            self.clearColor = True

    def updateClearColor(self):
        self.vrc.win.setClearColorActive(True)
        self.vrc.otherWin.setClearColorActive(True)
        self.vrc.win.setClearColor(VBase4(self.red, self.green, self.blue, self.alpha))
        self.vrc.otherWin.setClearColor(VBase4(self.red, self.green, self.blue, self.alpha))
        print "updateClearColor (red:"+str(self.red)+" green:"+str(self.green)+" blue:"+str(self.blue)+")"
            
    def plusAlpha(self):
        if self.alpha < 1: self.alpha = self.alpha + 0.1
        self.updateClearColor()

    def minusAlpha(self):
        if self.alpha > 0: self.alpha = self.alpha - 0.1
        self.updateClearColor()

    def plusRed(self):
        if self.red < 1: self.red = self.red + 0.1
        self.updateClearColor()

    def minusRed(self):
        if self.red > 0: self.red = self.red - 0.1
        self.updateClearColor()

    def plusGreen(self):
        if self.green < 1: self.green = self.green + 0.1
        self.updateClearColor()

    def minusGreen(self):
        if self.green > 0: self.green = self.green - 0.1
        self.updateClearColor()
        
    def plusBlue(self):
        if self.blue < 1: self.blue = self.blue + 0.1
        self.updateClearColor()

    def minusBlue(self):
        if self.blue > 0: self.blue= self.blue - 0.1
        self.updateClearColor()
