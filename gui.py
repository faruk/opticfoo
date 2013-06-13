import Tkinter as tk
import tkFont
import ttk
from operationmap import operationMap

class GUI():
    def __init__(self, vrc
        ):
        self.op = operationMap
        self.bigfont = tkFont.Font(family = 'Courier New', size = 16)

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
        self.generalTab = tk.Frame()
        self.debugFrame = tk.Frame()
        self.overviewTab = tk.Frame()
        self.tabs.pack(anchor="nw")

        self.tabs.add(self.generalTab)
        self.tabs.tab(0, text="General")
        self.tabs.add(self.cameraTab)
        self.tabs.tab(1 , text="Camera")
        self.tabs.add(self.visualTab)
        self.tabs.tab(2, text="Active Visual")
        self.tabs.add(self.insertTab)
        self.tabs.tab(3, text="Insert Visual")
        self.tabs.add(self.visualsTab)
        self.tabs.tab(4, text="Visuals")
        self.tabs.add(self.overviewTab)
        self.tabs.tab(5, text="Overview")


        #self.activeVisual = vrc.activeVisual
        #self.visuals = vrc.visuals
        #self.cam = vrc.cam
        #self.otherCam = vrc.otherCam

        #self.vrc = vrc
        #self.initCameraFrame()

        self.initVisualsFrame()

        #self.initVisualFrame()

        self.initGeneralFrame()

        self.initOverviewTab()

        self.vrc.spawnTkLoop()


        # general labels

    def initOverviewTab(self):
        self.activeVisualName = self.visuals.keys()[0]
        self.activeVisualsListbox = tk.Listbox(self.overviewTab)
        self.activeVisualsListbox.bind('<<ListboxSelect>>', self.updateActiveVisual)
        active = []
        for k in self.visuals.keys():
            if self.visuals[k]['button'].config()['text'][4] == "attach":
                active.append(k)
        for k in active:
            self.activeVisualsListbox.insert(tk.END, k)
        self.activeVisualsListbox.grid(column = 0, row = 2, rowspan=30, sticky = tk.NE)
        x,y,z = self.vrc.activeVisual.path.getPos()
        h,p,r = self.vrc.activeVisual.path.getHpr()
        self.visualLabel = tk.Label(self.overviewTab, text = "Visual", font = self.bigfont)
        self.visualLabel.grid(column = 0, row = 0, sticky = tk.W)
        self.visualLabelInfo = tk.Label(self.overviewTab, text = "position rotation: ")
        self.visualLabelInfo.grid(column = 0, row = 1, sticky = tk.E)
        self.visualPos = tk.Label(self.overviewTab, text = "x: "+str(int(x))+", y: "+str(int(y))+", z: "+str(int(z)))
        self.visualPos.grid(column = 1, row = 1, sticky = tk.W)
        self.visualHpr = tk.Label(self.overviewTab, text = "h: "+str(int(h))+", p: "+str(int(p))+", r: "+str(int(r)))
        self.visualHpr.grid(column = 1, row = 1, sticky = tk.E)
        self.visualSpeed = tk.Scale(
            self.overviewTab,
            from_ = -10.0,
            to = 10.0,
            orient=tk.HORIZONTAL,
            resolution = 0.01,
            length=250,
            command=self.updateActiveVisualSpeed,
            label="Visual movement speed"
        )
        self.visualSpeed.set(1)
        self.visualSpeed.grid(column = 1, row = 12, sticky = tk.E)
        self.visualScale= tk.Scale(
            self.overviewTab,
            from_ = 0.0,
            to = 10.0,
            orient=tk.HORIZONTAL,
            resolution = 0.01,
            length=250,
            command=self.updateActiveVisualScale,
            label="Visual scale"
        )
        self.visualScale.set(1)
        self.visualScale.grid(column = 1, row = 13, sticky = tk.E)
        self.visualTransparency= tk.Scale(
            self.overviewTab,
            from_ = 0.0,
            to = 1.0,
            orient=tk.HORIZONTAL,
            resolution = 0.01,
            length=250,
            command=self.updateActiveVisualTransparency,
            label="Visual transparency"
        )
        self.visualTransparency.set(1)
        self.visualTransparency.grid(column = 1, row = 14, sticky = tk.E)

        self.separator = ttk.Separator(self.overviewTab, orient = tk.HORIZONTAL)
        self.separator.grid(column = 0, row = 15, columnspan = 2, sticky = tk.EW)

        # camera labels
        self.camLabel = tk.Label(self.overviewTab, text = "Camera", font = self.bigfont)
        self.camLabel.grid(column = 0, row = 16, sticky = tk.W)
        self.camLabelInfo = tk.Label(self.overviewTab, text = "position / rotation: ")
        self.camLabelInfo.grid(column = 0, row = 17, sticky = tk.E)
        self.camPos = tk.Label(self.overviewTab, text = "")
        self.camPos.grid(column = 1, row = 17, sticky = tk.W)
        self.camHpr = tk.Label(self.overviewTab, text = "")
        self.camHpr.grid(column = 1, row = 17, sticky = tk.E)
        self.camSpeed = tk.Scale(
            self.overviewTab,
            from_ = -10.0,
            to = 10.0,
            orient=tk.HORIZONTAL,
            resolution = 0.1,
            length=250,
            command=self.updateCamSpeed,
            label="Camera speed"
        )
        self.camSpeed.grid(column = 1, row = 18, sticky = tk.E)

        self.separator2 = ttk.Separator(self.overviewTab, orient = tk.HORIZONTAL)
        self.separator2.grid(column = 0, row = 19, columnspan = 2, sticky = tk.EW)

        # sound labels
        self.soundLabel = tk.Label(self.overviewTab, text = "Sound", font = self.bigfont)
        self.soundLabel.grid(column = 0, row = 20, sticky = tk.NW)
        self.soundLabelInfo = tk.Label(self.overviewTab, text = "Threshold settings: ")
        self.soundLabelInfo.grid(column = 0, row = 21, sticky = tk.E)
        self.soundXThreshold = tk.Scale(
            self.overviewTab,
            from_ = 0.0,
            to = 100.0,
            orient=tk.HORIZONTAL,
            resolution = 0.25,
            length=250,
            command=self.updateSoundXThreshold,
            label="Lo Threshold"
        )
        self.soundXThreshold.set(30)
        self.soundXThreshold.grid(column = 1, row = 21, sticky = tk.E)
        self.soundYThreshold = tk.Scale(
            self.overviewTab,
            from_ = 0.0,
            to = 100.0,
            orient=tk.HORIZONTAL,
            resolution = 0.25,
            length=250,
            command=self.updateSoundYThreshold,
            label="Mid Threshold"
        )
        self.soundYThreshold.set(1)
        self.soundYThreshold.grid(column = 1, row = 22, sticky = tk.E)
        self.soundZThreshold = tk.Scale(
            self.overviewTab,
            from_ = 0.0,
            to = 100.0,
            orient=tk.HORIZONTAL,
            resolution = 0.25,
            length=250,
            command=self.updateSoundZThreshold,
            label="Hi Threshold"
        )
        self.soundZThreshold.set(1)
        self.soundZThreshold.grid(column = 1, row = 23, sticky = tk.E)

    def initVisualsFrame(self):
        self.visuals = {}
        i = 0
        for v in self.vrc.factory.visuals.keys():
            label = tk.Label(self.visualsTab, text = v)
            button = tk.Button(self.visualsTab, text = "attach", command = lambda t = v: self.toggleAttach(t))
            x = tk.Entry(self.visualsTab, width=3)
            y = tk.Entry(self.visualsTab, width=3)
            z = tk.Entry(self.visualsTab, width=3)
            x.insert(0, "0")
            y.insert(0, "0")
            z.insert(0, "0")
            label.grid(row = i)
            button.grid(row = i, column=1)
            x.grid(row = i, column=2)
            y.grid(row = i, column=3)
            z.grid(row = i, column=4)
            self.visuals[v] = {'label': label, 'button': button, 'x': x, 'y': y, 'z': z}
            #self.visuals[v]['button'].config(command = self.toggleAttach(v))
            i = i + 1

    def toggleAttach(self, v):
        print v
        if self.vrc.factory.visuals[v].attached:
           self.vrc.factory.visuals[v].detach()
           self.vrc.activeVisual = None
           self.visuals[v]['button'].config(text = "attach")
        else:
            x = int(self.visuals[v]['x'].get())
            y = int(self.visuals[v]['y'].get())
            z = int(self.visuals[v]['z'].get())
            self.vrc.factory.visuals[v].setPos(x,y,z)
            self.vrc.factory.visuals[v].attach()
            self.visuals[v]['button'].config(text = "detach")
            self.vrc.activeVisual = self.vrc.factory.visuals[v]
        self.updateActiveVisualListbox()

    def initVisualFrame(self):
        self.activeVisualName = self.visuals.keys()[0]
        self.activeVisualsListbox = tk.Listbox(self.visualTab)
        self.activeVisualsListbox.bind('<<ListboxSelect>>', self.updateActiveVisual)
        active = []
        for k in self.visuals.keys():
            if self.visuals[k]['button'].config()['text'][4] == "attach":
                active.append(k)
        for k in active:
            self.activeVisualsListbox.insert(tk.END, k)
        self.activeVisualsListbox.grid(column = 0, rowspan=30)
        x,y,z = self.vrc.activeVisual.path.getPos()
        h,p,r = self.vrc.activeVisual.path.getHpr()
        self.visualPos = tk.Label(self.visualTab, text = "x: "+str(int(x))+", y: "+str(int(y))+", z: "+str(int(z)))
        self.visualPos.grid(column = 1, row = 0, sticky = tk.E)
        self.visualHpr = tk.Label(self.visualTab, text = "h: "+str(int(h))+", p: "+str(int(p))+", r: "+str(int(r)))
        self.visualHpr.grid(column = 1, row = 1, sticky = tk.E)
        self.visualLeft = tk.Label(self.visualTab, text = "visual-left: "+str(self.op['visual-left']))
        self.visualLeft.grid(column = 1, row = 2, sticky = tk.E)
        self.visualRight= tk.Label(self.visualTab, text = "visual-right: "+str(self.op['visual-right']))
        self.visualRight.grid(column = 1, row = 3, sticky = tk.E)
        self.visualUp = tk.Label(self.visualTab, text = "visual-up: "+str(self.op['visual-up']))
        self.visualUp.grid(column=1, row=4, sticky = tk.E)
        self.visualDown = tk.Label(self.visualTab, text = "visual-down: "+str(self.op['visual-down']))
        self.visualDown.grid(column=1, row=5, sticky = tk.E)
        self.visualForward = tk.Label(self.visualTab, text = "visual-forward: "+str(self.op['visual-forward']))
        self.visualForward.grid(column = 1, row = 6, sticky = tk.E)
        self.visualBackward = tk.Label(self.visualTab, text = "visual-backward: "+str(self.op['visual-backward']))
        self.visualBackward.grid(column = 1, row = 7, sticky = tk.E)
        self.visualRotateLeft = tk.Label(self.visualTab, text = "visual-rotate-left: "+str(self.op['visual-rotate-left']))
        self.visualRotateLeft.grid(column = 1, row = 8, sticky = tk.E)
        self.visualRotateRight = tk.Label(self.visualTab, text = "visual-rotate-right: "+str(self.op['visual-rotate-right']))
        self.visualRotateRight.grid(column = 1, row = 9, sticky = tk.E)
        self.visualRotateUp = tk.Label(self.visualTab, text = "visual-rotate-up: "+str(self.op['visual-rotate-up']))
        self.visualRotateUp.grid(column = 1, row = 10, sticky = tk.E)
        self.visualRotateDown = tk.Label(self.visualTab, text = "visual-rotate-down: "+str(self.op['visual-rotate-down']))
        self.visualRotateDown.grid(column = 1, row = 11, sticky = tk.E)
        self.visualSpeed = tk.Scale(
            self.visualTab,
            from_ = 0.0,
            to = 10.0,
            orient=tk.HORIZONTAL,
            resolution = 0.01,
            length=200,
            command=self.updateActiveVisualSpeed,
            label="Visual movement speed"
        )
        self.visualSpeed.set(1)
        self.visualSpeed.grid(column = 1, row = 12, sticky = tk.E)
        self.visualScale= tk.Scale(
            self.visualTab,
            from_ = 0.0,
            to = 10.0,
            orient=tk.HORIZONTAL,
            resolution = 0.01,
            length=200,
            command=self.updateActiveVisualScale,
            label="Visual scale"
        )
        self.visualScale.set(1)
        self.visualScale.grid(column = 1, row = 13, sticky = tk.E)
        self.visualTransparency= tk.Scale(
            self.visualTab,
            from_ = 0.0,
            to = 1.0,
            orient=tk.HORIZONTAL,
            resolution = 0.01,
            length=200,
            command=self.updateActiveVisualTransparency,
            label="Visual transparency"
        )
        self.visualTransparency.set(1)
        self.visualTransparency.grid(column = 1, row = 14, sticky = tk.E)
        self.visualSpecialStatus = tk.Label(self.visualTab, text = self.vrc.activeVisual.getSpecialStatus(), width=50, justify = tk.LEFT)
        self.visualSpecialStatus.grid(column = 2, row =0, sticky = tk.NE, rowspan=30)

    def updateActiveVisualListbox(self):
        self.activeVisualsListbox.delete(0, self.activeVisualsListbox.size()-1)
        active = []
        for k in self.visuals.keys():
            if self.visuals[k]['button'].config()['text'][4] == "detach":
                active.append(k)
        self.vrc.visuals.clear()
        for k in active:
            self.activeVisualsListbox.insert(tk.END, k)
            self.vrc.visuals[k] = self.vrc.factory.visuals[k]
        self.activeVisualsListbox.grid(column=0)

    def updateActiveVisual(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.vrc.activeVisual = self.vrc.visuals[value]
        print value
        self.visualScale.set(self.vrc.activeVisual.getScale())
        self.visualSpeed.set(self.vrc.activeVisual.getSpeed())
        self.visualTransparency.set(self.vrc.activeVisual.getAlpha())
        #self.updateActiveVisualOperationMap()
        self.activeVisualName = value

    def updateActiveVisualOperationMap(self):
        #self.visualLeft.config(text = "visual-left: "+str(self.op['visual-left']))
        #self.visualRight.config(text = "visual-right: "+str(self.op['visual-right']))
        #self.visualUp.config(text = "visual-up: "+str(self.op['visual-up']))
        #self.visualDown.config(text = "visual-down: "+str(self.op['visual-down']))
        #self.visualForward.config(text = "visual-forward: "+str(self.op['visual-forward']))
        #self.visualBackward.config(text = "visual-backward: "+str(self.op['visual-backward']))
        #self.visualRotateLeft.config(text = "visual-rotate-left: "+str(self.op['visual-rotate-left']))
        #self.visualRotateRight.config(text = "visual-rotate-right: "+str(self.op['visual-rotate-right']))
        #self.visualRotateUp.config(text = "visual-rotate-up: "+str(self.op['visual-rotate-up']))
        #self.visualRotateDown.config(text = "visual-rotate-down: "+str(self.op['visual-rotate-down']))
        pass

    def updateActiveVisualSpeed(self, event):
        self.vrc.activeVisual.setMovementSpeed(self.visualSpeed.get())

    def updateActiveVisualScale(self, event):
        self.vrc.activeVisual.setScale(self.visualScale.get())

    def updateActiveVisualTransparency(self, event):
        self.vrc.activeVisual.setAlpha(self.visualTransparency.get())

    def getActiveVisualStatus(self):
        if self.vrc.activeVisual != None:
            x, y, z = map(lambda i: str(int(i)), self.vrc.activeVisual.getPos())
            self.visualPos.config(text="x: "+x+", y: "+y+", z: "+z)
            h,p,r = map(lambda i: str(int(i)), self.vrc.activeVisual.getHpr())
            self.visualHpr.config(text="h: "+h+", p: "+p+", r: "+r)
            self.visuals[self.activeVisualName]['x'].delete(0,10)
            self.visuals[self.activeVisualName]['y'].delete(0,10)
            self.visuals[self.activeVisualName]['z'].delete(0,10)
            self.visuals[self.activeVisualName]['x'].insert(0,x)
            self.visuals[self.activeVisualName]['y'].insert(0,y)
            self.visuals[self.activeVisualName]['z'].insert(0,z)
            #self.updateActiveVisualOperationMap()

    def initCameraFrame(self):
        # camera labels
        self.camPos = tk.Label(self.cameraTab, text = "")
        self.camPos.pack(anchor="w")
        self.camHpr = tk.Label(self.cameraTab, text = "")
        self.camHpr.pack(anchor="w")
        self.camSpeed = tk.Scale(
            self.cameraTab,
            from_ = 0.0,
            to = 10.0,
            orient=tk.VERTICAL,
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

    def update(self):
        self.getCameraStatus()
        self.getGeneralStatus()
        self.getActiveVisualStatus()
        self.visualScale.set(self.vrc.activeVisual.getScale())
        self.visualSpeed.set(self.vrc.activeVisual.getSpeed())
        self.visualTransparency.set(self.vrc.activeVisual.getAlpha())


    def setCameraValues(self, values):
        pass

    def getCameraStatus(self):
        x, y, z = map(lambda i: int(i), self.vrc.cam.getPos())
        self.camPos.config(text = "x: "+str(x)+", y: "+str(y)+", z: "+str(z))
        h, p, r = map(lambda i: int(i), self.vrc.cam.getHpr())
        self.camHpr.config(text = "h: "+str(h)+", p: "+str(p)+", r: "+str(r))
        #self.camLeft.config(text="cam-left: "+str(self.vrc.op['cam-left']))
        #self.camRight.config(text="cam-right: "+str(self.vrc.op['cam-right']))
        #self.camUp.config(text="cam-up: "+str(self.vrc.op['cam-up']))
        #self.camDown.config(text="cam-down: "+str(self.vrc.op['cam-down']))
        #self.camForward.config(text="cam-forward: "+str(self.vrc.op['cam-forward']))
        #self.camBackward.config(text="cam-backward: "+str(self.vrc.op['cam-backward']))
        #self.camRotateLeft.config(text="cam-rotate-left: "+str(self.vrc.op['cam-rotate-left']))
        #self.camRotateRight.config(text="cam-rotate-right: "+str(self.vrc.op['cam-rotate-right']))
        #self.camRotateUp.config(text="cam-rotate-up: "+str(self.vrc.op['cam-rotate-up']))
        #self.camRotateDown.config(text="cam-rotate-down: "+str(self.vrc.op['cam-rotate-down']))
        #self.camReset.config(text="cam-reset: "+str(self.vrc.op['cam-reset']))
        #self.camSyncToggle.config(text="cam-sync-toggle: "+str(self.vrc.op['cam-sync-toggle']))
        #self.camSyncTo.config(text="cam-sync-to: "+str(self.vrc.op['cam-sync-to']))
        #self.camFixToggle.config(text="cam-fix-toggle: "+str(self.vrc.op['cam-fix-toggle']))

    def getGeneralStatus(self):
        self.mode.config(text=self.vrc.mode+" mode")

    def updateCamSpeed(self, event):
        print self.camSpeed.get(), event
        self.vrc.setCamSpeed(self.camSpeed.get())

    def initGeneralFrame(self):
        self.soundXThreshold = tk.Scale(
            self.generalTab,
            from_ = 0.0,
            to = 100.0,
            orient=tk.HORIZONTAL,
            resolution = 0.25,
            length=400,
            command=self.updateSoundXThreshold,
            label="Lo Threshold"
        )
        self.soundXThreshold.set(30)
        self.soundXThreshold.grid(column = 0, row = 1, sticky = tk.E)
        self.soundYThreshold = tk.Scale(
            self.generalTab,
            from_ = 0.0,
            to = 100.0,
            orient=tk.HORIZONTAL,
            resolution = 0.25,
            length=400,
            command=self.updateSoundYThreshold,
            label="Mid Threshold"
        )
        self.soundYThreshold.set(1)
        self.soundYThreshold.grid(column = 0, row = 2, sticky = tk.E)
        self.soundZThreshold = tk.Scale(
            self.generalTab,
            from_ = 0.0,
            to = 100.0,
            orient=tk.HORIZONTAL,
            resolution = 0.25,
            length=400,
            command=self.updateSoundZThreshold,
            label="Hi Threshold"
        )
        self.soundZThreshold.set(1)
        self.soundZThreshold.grid(column = 0, row = 3, sticky = tk.E)

    def updateSoundXThreshold(self, event):
        self.vrc.snd.setXThreshold(self.soundXThreshold.get())

    def updateSoundYThreshold(self, event):
        self.vrc.snd.setYThreshold(self.soundYThreshold.get())

    def updateSoundZThreshold(self, event):
        self.vrc.snd.setZThreshold(self.soundZThreshold.get())
