from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import Vec3, FrameBufferProperties, GraphicsPipe, WindowProperties, NodePath, loadPrcFile, CardMaker
from operationMap import operationMap
from visuals.monitor.Monitor import Monitor
from visuals.enterprise.Enterprise import Enterprise
from visuals.videobackground.VideoBackground import VideoBackground

loadPrcFile('Config.prc')

class VRC(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # set up another camera to view stuff in other window
        self.otherWin = self openWindow(makeCamera = 0)
        self.otherCam = self.makeCamera(self.otherWin)

        # allocate visuals
        self.visuals = []

        self.op = operationMap
        self.mode = self.op['mode']

        # movement keys
        self.accept('a', self.setOperation, ['a'])
        self.accept('a-up', self.setOperation, ['a-up'])
        self.accept('d', self.setOperation, ['d'])
        self.accept('d-up', self.setOperation, ['d-up'])
        self.accept('w', self.setOperation, ['w'])
        self.accept('w-up', self.setOperation, ['w-up'])
        self.accept('d', self.setOperation, ['d'])
        self.accept('d-up', self.setOperation, ['d-up'])
        self.accept('h', self.setOperation, ['h'])
        self.accept('h-up', self.setOperation, ['h'])
        self.accept('j', self.setOperation, ['j'])
        self.accept('j-up', self.setOperation, ['j-up'])
        self.accept('k', self.setOperation, ['k'])
        self.accept('k-up', self.setOperation, ['k-up'])
        self.accept('l', self.setOperation, ['l'])
        self.accept('l-up', self.setOperation, ['l-up'])
        self.accept('arrow_up', self.setOperation, ['arrow_up'])
        self.accept('arrow_up-up', self.setOperation, ['arrow_up-up'])
        self.accept('arrow_down', self.setOperation, ['arrow_down'])
        self.accept('arrow_down-up', self.setOperation, ['arrow_down-up'])
        self.accept('arrow_left', self.setOperation, ['arrow_left'])
        self.accept('arrow_left-up', self.setOperation, ['arrow_left-up'])
        self.accept('arrow_right', self.setOperation, ['arrow_right'])
        self.accept('arrow_right-up', self.setOperation, ['arrow_right-up'])
        self.accept('page_up', self.setOperation, ['page_up'])
        self.accept('page_up-up', self.setOperation, ['page_up-up'])
        self.accept('page_down', self.setOperation, ['page_down'])
        self.accept('page_down-up', self.setOperation, ['page_down-up'])
        self.accept('1', self.setOperation, ['1'])
        self.accept('1-up', self.setOperation, ['1-up'])
        self.accept('2', self.setOperation, ['2'])
        self.accept('2-up', self.setOperation, ['2-up'])
        self.accept('3', self.setOperation, ['3'])
        self.accept('3-up', self.setOperation, ['3-up'])
        self.accept('4', self.setOperation, ['4'])
        self.accept('4-up', self.setOperation, ['4-up'])
        self.accept('5', self.setOperation, ['5'])
        self.accept('5-up', self.setOperation, ['5-up'])
        self.accept('6', self.setOperation, ['6'])
        self.accept('6-up', self.setOperation, ['6-up'])
        self.accept('7', self.setOperation, ['7'])
        self.accept('7-up', self.setOperation, ['7-up'])
        self.accept('8', self.setOperation, ['8'])
        self.accept('8-up', self.setOperation, ['8-up'])
        self.accept('9', self.setOperation, ['9'])
        self.accept('9-up', self.setOperation, ['9-up'])
        self.accept('0', self.setOperation, ['0'])
        self.accept('0-up', self.setOperation, ['0-up'])

        # mode keys
        self.accept('escape', self.setOperation, ['escape'])
        self.accept('v', self.setOperation, ['v'])
        self.accept('c', self.setOperation, ['c'])
        self.accept('b', self.setOperation, ['b'])
        self.accept('n', self.setOperation, ['n'])
        self.accept('i', self.setOperation, ['i'])

        # misc
        self.accept('r', self.setOperation, ['r'])
        self.accept('r-up', self.setOperation, ['r-up'])
        self.accept('f-up', self.setOperation, ['f-up'])
        self.accept('g-up', self.setOperation, ['g-up'])
        self.accept('t-up', self.setOperation, ['t-up'])

        # effect keys
        self.accept('1', self.setOperation, ['1'])
        self.accept('1-up', self.setOperation, ['1-up'])
        self.accept('2', self.setOperation, ['2'])
        self.accept('2-up', self.setOperation, ['2-up'])
        self.accept('3', self.setOperation, ['3'])
        self.accept('3-up', self.setOperation, ['3-up'])
        self.accept('4', self.setOperation, ['4'])
        self.accept('4-up', self.setOperation, ['4-up'])
        self.accept('5', self.setOperation, ['5'])
        self.accept('5-up', self.setOperation, ['5-up'])
        self.accept('6', self.setOperation, ['6'])
        self.accept('6-up', self.setOperation, ['6-up'])
        self.accept('7', self.setOperation, ['7'])
        self.accept('7-up', self.setOperation, ['7-up'])
        self.accept('8', self.setOperation, ['8'])
        self.accept('8-up', self.setOperation, ['8-up'])
        self.accept('9', self.setOperation, ['9'])
        self.accept('9-up', self.setOperation, ['9-up'])
        self.accept('0', self.setOperation, ['0'])
        self.accept('0-up', self.setOperation, ['0-up'])

        self.taskMgr.add(self.keyboardAction, 'keyboardAction')

    def setOperation(self, key):
        if self.mode == "escaped" : self.setMode(key)
        if self.mode == "visual" : self.setVisualOperation(key)
        if self.mode == "cam" : self.setCamOperation(key)
        if self.mode == "insert" : self.setInsertOperation(key)
        if self.mode == "light" : self.setLightOperation(key)
        if key == 'escape' : self.mode = 'escaped'

    def setMode(self, key):
        if key == "v" : self.mode = 'visual'
        if key == "c" : self.mode = 'cam'
        if key == "b" : self.mode = 'music'
        if key == "n" : self.mode = 'light'
        if key == "i" : self.mode = 'insert'

    def setCamOperation(key):
        if key == 'a' : self.setOperationMap('cam-left', 1)
        if key == 'a-up' : self.setOperationMap('cam-left', 0)
        if key == 'd' : self.setOperationMap('cam-right', 1)
        if key == 'd-up' : self.setOperationMap('cam-rigt', 0)
        if key == 'w' : self.setOperationMap('cam-up', 1)
        if key == 'w-up' : self.setOperationMap('cam-up', 0)
        if key == 's' : self.setOperationMap('cam-down', 1)
        if key == 's-up' : self.setOperationMap('cam-down', 0)
        if key == 'h' : self.setOperationMap('cam-rotate-left', 1)
        if key == 'h-up' : self.setOperationMap('cam-rotate-left', 0)
        if key == 'l' : self.setOperationMap('cam-rotate-right', 1)
        if key == 'l-up' : self.setOperationMap('cam-rotate-right', 0)
        if key == 'j' : self.setOperationMap('cam-rotate-down', 1)
        if key == 'j-up' : self.setOperationMap('cam-rotate-down', 0)
        if key == 'k' : self.setOperationMap('cam-rotate-up', 1)
        if key == 'k-up' : self.setOperationMap('cam-rotate-up', 0)
        if key == 'r' : self.setOperationMap('cam-reset', 1)
        if key == 'r-up': self.setOperationMap('cam-reset', 0)
        if key == 'f-up': self.setOperation('cam-fix-toggle', -self.op['cam-fix-toggle'])
        if key == 'g-up': self.setOperation('cam-sync-toggle', -self.op['cam-sync-toggle'])
        if key == 't-up': self.setOperation('cam-sync-to', -self.op['cam-sync-to'])

    def setVisualOperation(key):
        if key == 'a' : self.setOperationMap('visual-left', 1)
        if key == 'a-up' : self.setOperationMap('visual-left', 0)
        if key == 'd' : self.setOperationMap('visual-right', 1)
        if key == 'd-up' : self.setOperationMap('visual-rigt', 0)
        if key == 'w' : self.setOperationMap('visual-up', 1)
        if key == 'w-up' : self.setOperationMap('visual-up', 0)
        if key == 's' : self.setOperationMap('visual-down', 1)
        if key == 's-up' : self.setOperationMap('visual-down', 0)
        if key == 'h' : self.setOperationMap('visual-rotate-left', 1)
        if key == 'h-up' : self.setOperationMap('visual-rotate-left', 0)
        if key == 'l' : self.setOperationMap('visual-rotate-right', 1)
        if key == 'l-up' : self.setOperationMap('visual-rotate-right', 0)
        if key == 'j' : self.setOperationMap('visual-rotate-down', 1)
        if key == 'j-up' : self.setOperationMap('visual-rotate-down', 0)
        if key == 'k' : self.setOperationMap('visual-rotate-up', 1)
        if key == 'k-up' : self.setOperationMap('visual-rotate-up', 0)
        if key == '1' : self.setOperationMap('visual-effect1', 1)
        if key == '1-up' : self.setOperationMap('visual-effect1', 0)
        if key == '2' : self.setOperationMap('visual-effect2', 1)
        if key == '2-up' : self.setOperationMap('visual-effect2', 0)
        if key == '3' : self.setOperationMap('visual-effect3', 1)
        if key == '3-up' : self.setOperationMap('visual-effect3', 0)
        if key == '4' : self.setOperationMap('visual-effect4', 1)
        if key == '4-up' : self.setOperationMap('visual-effect4', 0)
        if key == '5' : self.setOperationMap('visual-effect5', 1)
        if key == '5-up' : self.setOperationMap('visual-effect5', 0)
        if key == '6' : self.setOperationMap('visual-effect6', 1)
        if key == '6-up' : self.setOperationMap('visual-effect6', 0)
        if key == '7' : self.setOperationMap('visual-effect7', 1)
        if key == '7-up' : self.setOperationMap('visual-effect7', 0)
        if key == '8' : self.setOperationMap('visual-effect8', 1)
        if key == '8-up' : self.setOperationMap('visual-effect8', 0)
        if key == '9' : self.setOperationMap('visual-effect9', 1)
        if key == '9-up' : self.setOperationMap('visual-effect9', 0)
        if key == '0' : self.setOperationMap('visual-effect0', 1)
        if key == '0-up' : self.setOperationMap('visual-effect0', 0)

