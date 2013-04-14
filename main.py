from vrc import VRC
from gui import GUI

Gui = None

def updateGui(task):
    Gui.update()
    return task.again

if __name__ == "__main__":
    App = VRC()
    Gui = GUI(App)
    App.taskMgr.doMethodLater(0.5, updateGui, 'gui')
    print "done"
    App.run()
