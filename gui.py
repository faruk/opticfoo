import Tkinter as tk
import ttk
from operationmap import operationMap

class GUI():
    def __init__(self, vrc
        ):
        self.op = operationMap

        # operationmap preparation for presentation
        self.activeOps = {}
        self.visualOps = {}
        for v in self.op:
            if v.startswith("visual-"): self.visualOps[v] = self.op[v]
        self.camOps = {}
        for c in self.op:
            if c.startswith("cam-"): self.camOps[c] = self.op[c]

        self.vrc = vrc

        self.root = self.vrc.tkRoot

        self.mode = tk.Label(self.root, text = self.vrc.mode+" mode")
        self.mode.pack(anchor="w")

        self.tabs = ttk.Notebook()
        self.lightTab = tk.Frame()
        self.visualTab = tk.Frame()
        self.visualsTab = tk.Frame()
        self.insertTab = tk.Frame()
        self.cameraTab = tk.Frame()
        self.escapeTab = tk.Frame()
        self.debugFrame = tk.Frame()
        self.tabs.pack(anchor="nw")

        self.tabs.add(self.escapeTab)
        self.tabs.tab(0, text="General")
        self.tabs.add(self.cameraTab)
        self.tabs.tab(1 , text="Camera")
        self.tabs.add(self.visualTab)
        self.tabs.tab(2, text="Active Visual")
        self.tabs.add(self.insertTab)
        self.tabs.tab(3, text="Insert Visual")
        self.tabs.add(self.visualsTab)
        self.tabs.tab(4, text="Visuals")


        #self.activeVisual = vrc.activeVisual
        #self.visuals = vrc.visuals
        #self.cam = vrc.cam
        #self.otherCam = vrc.otherCam

        #self.vrc = vrc

        # camera labels
        self.camPos = tk.Label(self.cameraTab, text = "")
        self.camPos.pack(anchor="w")
        self.camHpr = tk.Label(self.cameraTab, text = "")
        self.camHpr.pack(anchor="w")
        self.camSpeed = tk.Scale(
            self.cameraTab, 
            from_ = 0.0, 
            to = 10.0, 
            orient=tk.HORIZONTAL, 
            resolution = 0.1, 
            length=200,
            command=self.updateCamSpeed,
            label="Camera speed"
        )
        self.camSpeed.pack(anchor="w")
        
        self.camLeft = tk.Label(self.cameraTab, text = "")
        self.camLeft.pack(anchor="w")
        self.camRight = tk.Label(self.cameraTab, text = "")
        self.camRight.pack(anchor="w")
        self.camUp = tk.Label(self.cameraTab, text = "")
        self.camUp.pack(anchor="w")
        self.camDown = tk.Label(self.cameraTab, text = "")
        self.camDown.pack(anchor="w")
        self.camForward = tk.Label(self.cameraTab, text = "")
        self.camForward.pack(anchor="w")
        self.camBackward = tk.Label(self.cameraTab, text = "")
        self.camBackward.pack(anchor="w")
        self.camRotateLeft = tk.Label(self.cameraTab, text = "")
        self.camRotateLeft.pack(anchor="w")
        self.camRotateRight = tk.Label(self.cameraTab, text = "")
        self.camRotateRight.pack(anchor="w")
        self.camRotateUp = tk.Label(self.cameraTab, text = "")
        self.camRotateUp.pack(anchor="w")
        self.camRotateDown = tk.Label(self.cameraTab, text = "")
        self.camRotateDown.pack(anchor="w")
        self.camReset = tk.Label(self.cameraTab, text = "")
        self.camReset.pack(anchor="w")
        self.camSyncToggle = tk.Label(self.cameraTab, text = "")
        self.camSyncToggle.pack(anchor="w")
        self.camSyncTo = tk.Label(self.cameraTab, text = "")
        self.camSyncTo.pack(anchor="w")
        self.camFixToggle = tk.Label(self.cameraTab, text = "")
        self.camFixToggle.pack(anchor="w")

        self.vrc.spawnTkLoop()


        # general labels

    def initVisualFrame(self):
        pass

    def update(self):
        self.getCameraStatus()
        self.getGeneralStatus()

    def setCameraValues(self, values):
        pass

    def getCameraStatus(self):
        x, y, z = self.vrc.cam.getPos()
        self.camPos.config(text = "x: "+str(x)+", y: "+str(y)+", z: "+str(z))
        h, p, r = self.vrc.cam.getHpr()
        self.camHpr.config(text = "h: "+str(h)+", p: "+str(p)+", r: "+str(r))
        self.camLeft.config(text="cam-left: "+str(self.vrc.op['cam-left']))
        self.camRight.config(text="cam-right: "+str(self.vrc.op['cam-right']))
        self.camUp.config(text="cam-up: "+str(self.vrc.op['cam-up']))
        self.camDown.config(text="cam-down: "+str(self.vrc.op['cam-down']))
        self.camForward.config(text="cam-forward: "+str(self.vrc.op['cam-forward']))
        self.camBackward.config(text="cam-backward: "+str(self.vrc.op['cam-backward']))
        self.camRotateLeft.config(text="cam-rotate-left: "+str(self.vrc.op['cam-rotate-left']))
        self.camRotateRight.config(text="cam-rotate-right: "+str(self.vrc.op['cam-rotate-right']))
        self.camRotateUp.config(text="cam-rotate-up: "+str(self.vrc.op['cam-rotate-up']))
        self.camRotateDown.config(text="cam-rotate-down: "+str(self.vrc.op['cam-rotate-down']))
        self.camReset.config(text="cam-reset: "+str(self.vrc.op['cam-reset']))
        self.camSyncToggle.config(text="cam-sync-toggle: "+str(self.vrc.op['cam-sync-toggle']))
        self.camSyncTo.config(text="cam-sync-to: "+str(self.vrc.op['cam-sync-to']))
        self.camFixToggle.config(text="cam-fix-toggle: "+str(self.vrc.op['cam-fix-toggle']))

    def getVisualStatus(self):
        pass

    def getGeneralStatus(self):
        self.mode.config(text=self.vrc.mode+" mode")

    def updateCamSpeed(self, event):
        print self.camSpeed.get(), event
        self.vrc.setCamSpeed(self.camSpeed.get())