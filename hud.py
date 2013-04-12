from operationmap import operationMap
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *

class HUD:

    def __init__(self):
        self.op = operationMap
        self.oplength = len(self.op)
        self.opText = []
        self.opText.append(
            OnscreenText(
                align = TextNode.ALeft,
                pos = (0.9, 0.9),
                scale = 0.06,
                fg = (0,0,0,1),
                bg = (1,0,0,0.5),
                mayChange = True
            )
        )
        i = 0.0
        x = -1.2
        for o in self.op:
            self.opText.append(
                OnscreenText(
                    align = TextNode.ALeft,
                    pos = (x ,0.9-i),
                    scale = 0.05,
                    fg = (0,0,0,1),
                    bg = (1,1,1,0.5),
                    mayChange = True
                )
            )
            i = i+0.06
        self.activeOps = {}
        self.visualOps = {}
        for v in self.op:
            if v.startswith("visual-"): self.visualOps[v] = self.op[v]
        self.camOps = {}
        for c in self.op:
            if c.startswith("cam-"): self.camOps[c] = self.op[c]
        self.updateOperationMap(self.op)

    def updateOperationMap(self, operationMap):
        self.op = operationMap

        # set active ops
        self.mode = self.op['mode']
        self.opText[0].setText("MODE: " +self.mode) 
        
        # visual hud
        for v in self.visualOps:
            self.visualOps[v] = self.op[v]

        # cam hud
        for c in self.camOps:
            self.camOps[c] = self.op[c]

        # display active values on 
        if self.mode is "visual" : self.activeOps = self.visualOps
        if self.mode is "cam" : self.activeOps = self.camOps
        j = 1
        for o in self.activeOps:
            self.opText[j].setText(o +":\t"+ str(self.activeOps[o]))
            self.opText[j].setBg((1,1,1,0.5))
            j = j+1
        k = range(len(self.activeOps)+1, self.oplength)
        for j in k:
            self.opText[j].setText("")
            self.opText[j].setBg((1,1,1,0))

    def clear(self):
        for o in self.opText:
            o.setText('')

