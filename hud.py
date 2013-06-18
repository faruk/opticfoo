from operationmap import operationMap
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *

class HUD:

    def __init__(self, vrc):
        self.vrc = vrc
        self.mode = OnscreenText(
            align = TextNode.ALeft,
            pos = (-0.99, 0.9),
            scale = 0.06,
            fg = (0,0,0,1),
            bg = (1,1,1,1),
            mayChange = True
        )
        self.visual = OnscreenText(
            align = TextNode.ALeft,
            pos = (-0.99, 0.8),
            scale = 0.06,
            fg = (0,0,0,1),
            bg = (1,1,1,1),
            mayChange = True
        )
        self.cam = OnscreenText(
            align = TextNode.ALeft,
            pos = (-0.99, 0.7),
            scale = 0.06,
            fg = (0,0,0,1),
            bg = (1,1,1,1),
            mayChange = True
        )

        self.mode.setText("mode: " + self.vrc.mode)
        self.visual.setText("visual: " + self.vrc.activeVisual.__class__.__name__)
        pos = self.vrc.cam.getPos()
        self.cam.setText("cam: " + str(pos[0]) + "/" + str(pos[1]) + "/" + str(pos[2]))

    def updateHUD(self):
        self.mode.setText("mode: " + self.vrc.mode)
        x = y = z = 0
        h = p = r = 0
        visualToggle = ""
        if self.vrc.activeVisual != None:
            visualToggle = self.vrc.activeVisual.getVisualToggleInfo()
            x, y, z= self.vrc.activeVisual.getPos()
            h, p, r= self.vrc.activeVisual.getHpr()
        self.visual.setText(
            "visual: " + self.vrc.activeVisual.__class__.__name__+ " " +
            str(int(x)) + "/" + str(int(y)) + "/" + str(int(z)) + " " +
            str(int(h)) +"/"+ str(int(p))+"/"+str(int(r)) + 
            " toggle: " + visualToggle

        )
        x, y, z = self.vrc.cam.getPos()
        h, p, r = self.vrc.cam.getHpr()
        self.cam.setText(
            "cam: " + str(int(x)) + "/" + str(int(y)) + "/" + str(int(z)) + " " +
            str(int(h)) +"/"+ str(int(p))+"/"+str(int(r))
        )

    def clear(self):
        self.mode.setText('')
        self.visual.setText('')
        self.cam.setText('')
