import Tkinter as tk
import tkMessageBox
import tkFont
import ttk
import json
from operationmap import operationMap
import os

class GUI():
    def __init__(self, vrc
        ):
        self.bigfont = tkFont.Font(family = 'Courier New', size = 16)

        # operationmap preparation for presentation
        # obsolete since not interesting with reduced gui in v2
        self.op = operationMap
        self.activeOps = {}
        self.visualOps = {}
        for v in self.op:
            if v.startswith("visual-"): self.visualOps[v] = self.op[v]
        self.camOps = {}
        for c in self.op:
            if c.startswith("cam-"): self.camOps[c] = self.op[c]

        # reference to vrc object
        self.vrc = vrc

        # get tk root from vrc
        self.root = self.vrc.tkRoot
        self.root.protocol('WM_DELETE_WINDOW', self.quitCallback)

        # initialize mode label
        self.mode = tk.Label(self.root, text = self.vrc.mode+" mode", font = self.bigfont)
        self.mode.grid(row = 0, column =0, sticky = tk.W, columnspan = 2)

        # setup tabs
        self.tabs = ttk.Notebook()
        self.visualsTab = tk.Frame()
        self.overviewTab = tk.Frame()
        self.tabs.grid(row = 2, column = 0, columnspan = 2)
        self.tabs.add(self.visualsTab)
        self.tabs.tab(0, text="Visuals")
        self.tabs.add(self.overviewTab)
        self.tabs.tab(1, text="Overview")

        # init gui elements inside tabs
        self.initVisualsFrame()
        self.initOverviewTab()

        # start gui
        self.vrc.spawnTkLoop()

    def initOverviewTab(self):
        # active visuals list
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
        self.camSpeed.set(1)

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
        self.visualsLabel = tk.Label(self.visualsTab, text = "Visuals", font = self.bigfont)
        self.visualsLabel.grid(column = 0, row = 0, sticky = tk.NW)
        self.visuals = {}
        i = 1
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

        self.separator3 = ttk.Separator(self.visualsTab, orient = tk.VERTICAL)
        self.separator3.grid(column = 5, row = 0, rowspan = 100, sticky = tk.NS)

        self.saveLabel = tk.Label(self.visualsTab, text = "Scenery", font = self.bigfont)
        self.saveLabel.grid(column = 6, row = 0, sticky = tk.NW)

        self.saveName = tk.Entry(self.visualsTab, width = 20)
        self.saveName.grid(row = 1, column = 6, sticky = tk.W)
        self.saveButton = tk.Button(self.visualsTab, text = "save scenery", command = self.saveScene)
        self.saveButton.grid(row = 2, column = 6, sticky = tk.W)
        self.loadButton = tk.Button(self.visualsTab, text = "load scenery", command = self.loadScene)
        self.loadButton.grid(row = 3, column = 6, sticky = tk.W)

        saved=os.listdir('save')
        saved.sort()
        self.saves = tk.Listbox(self.visualsTab)
        self.saves.bind('<<ListboxSelec>>', self.markScene)
        self.saves.grid(row = 4, column = 6, rowspan=100)
        for save in saved:
            self.saves.insert(tk.END, save)

        self.deleteButton = tk.Button(self.visualsTab, text = "delete scenery", command = self.deleteScene)
        self.deleteButton.grid(row = 104, column = 6, sticky = tk.W)

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
        self.activeVisualName = value

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

    def update(self):
        self.getCameraStatus()
        self.getGeneralStatus()
        self.getActiveVisualStatus()
        if self.vrc.activeVisual != None:
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

    def getGeneralStatus(self):
        self.mode.config(text=self.vrc.mode+" mode")

    def updateCamSpeed(self, event):
        print self.camSpeed.get(), event
        self.vrc.setCamSpeed(self.camSpeed.get())

    def updateSoundXThreshold(self, event):
        self.vrc.snd.setXThreshold(self.soundXThreshold.get())

    def updateSoundYThreshold(self, event):
        self.vrc.snd.setYThreshold(self.soundYThreshold.get())

    def updateSoundZThreshold(self, event):
        self.vrc.snd.setZThreshold(self.soundZThreshold.get())

    # save scene in json file
    def saveScene(self):
        vrc = self.vrc
        name = self.saveName.get()
        visuals = vrc.visuals
        if len(name) > 0:
            file = open('save/' + name, 'w')
            scene = []

            # gather info
            for v in visuals:
                visual = visuals[v]
                x, y, z = visual.getPos()
                pos = (x, y, z)
                h, p, r = visual.getHpr()
                hpr = (h, p, r)
                info = {
                    'type': 'visual',
                    'name': v,
                    'pos': pos,
                    'hpr': hpr,
                    'scale': visual.getScale(),
                    'alpha': visual.getAlpha(),
                    'speed' : visual.getSpeed()
                }
                scene.append(info)

            x, y, z = self.vrc.cam.getPos()
            h, p, r = self.vrc.cam.getHpr()
            pos = (x, y, z)
            hpr = (h, p, r)
            cam = {
                'type': 'cam',
                'pos': pos,
                'hpr': hpr
            }
            scene.append(cam)
            # write scene as json string in order to read/load again
            string = json.dumps(scene)
            file.write(string)
            file.close()
            self.saves.insert(tk.END, name)

    def markScene(self, event):
        print event

    def filterVisuals(self, x):
        return x['type'] == 'visual'

    def filterCam(self, x):
        return x['type'] == 'cam'

    # load scene from json files in saves directory
    def loadScene(self):
        scene = self.saves.curselection()[0]
        scene = self.saves.get(scene)
        scene = open('save/'+scene, 'r').read()
        scene = json.loads(scene)
        visuals = filter(self.filterVisuals, scene)
        cam = filter(self.filterCam, scene)[0]
        for visual in visuals:
            x, y, z = visual['pos']
            h, p, r = visual['hpr']
            self.vrc.visuals[visual['name']] = self.vrc.factory.visuals[visual['name']]
            self.vrc.visuals[visual['name']].setPos(x,y,z)
            self.vrc.visuals[visual['name']].setHpr(h,p,r)
            self.vrc.visuals[visual['name']].setScale(visual['scale'])
            self.vrc.visuals[visual['name']].setAlpha(visual['alpha'])
            self.vrc.visuals[visual['name']].setSpeed(visual['speed'])
            self.vrc.visuals[visual['name']].attach()
        x,y,z = cam['pos']
        h,p,r = cam['hpr']
        self.vrc.cam.setPos((x,y,z))
        self.vrc.cam.setHpr((h,p,r))
        #self.vrc.camAfterMath()

    def deleteScene(self):
        sceneID = self.saves.curselection()[0]
        scene = self.saves.get(sceneID)
        self.saves.delete(sceneID)
        os.remove('save/'+scene)

    def quitCallback(self):
        if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()
            self.vrc.exit()
