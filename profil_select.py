import sys
import os
import json

import bpy

# So we can find the bgui module
sys.path.append('../..')

import bgui
import bgui.bge_utils
import bge

userspth = bpy.path.abspath("//") + 'scripts' + os.sep + 'users.json'
with open(userspth) as data_source:
    bge.logic.globalDict['users'] = json.load(data_source)


class MenuMain(bgui.bge_utils.Layout):

    def __init__(self, sys, data):
        super().__init__(sys, data)

        posy = 0.700
        button = None
        strbut = ''
        lblist = []

        for item in bge.logic.globalDict['users']:
            strbut = item
            lblist.append(strbut)
            button = bgui.FrameButton(self, text=strbut, size=[.14, .09], pos=[.03, posy], options = bgui.BGUI_DEFAULT)
            button.on_click = self.onBut
            posy -= 0.100

        #self.lb = bgui.ListBox(self, "lb", items=lblist, padding=0.05, size=[0.9, 0.9], pos=[0.05, 0.05])

        self.buttonAddProfil = bgui.FrameButton(self, text="Nouveau", size=[.14, .09], pos=[0.2200, 0.3], options = bgui.BGUI_DEFAULT)
        self.buttonAddProfil.on_click = self.onAdd

        self.buttonexit = bgui.FrameButton(self, text="Quitter", size=[.14, .09], pos=[.0500, 0.3], options = bgui.BGUI_DEFAULT)
        self.buttonexit.on_click = self.onExit

    def onBut(self, widget):
        tmp = bge.logic.globalDict['users'][widget.text]
        bge.logic.globalDict['users'] = tmp
        blendfile = bpy.path.abspath("//") + os.sep + 'main_menu.blend'
        bge.logic.startGame(blendfile)

    def onAdd(self, widget):
        #blendfile = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]))) + os.sep + 'add_user.blend'
        #bge.logic.startGame(blendfile)
        print('Pas encore implémentée...')

    def onExit(self, widget):
        #sys.exit() Ferme blender...
        bge.logic.endGame()


def main(cont):
    own = cont.owner
    mouse = bge.logic.mouse

    if 'sys' not in own:
        # Create our system and show the mouse
        own['sys'] = bgui.bge_utils.System('../../themes/default')
        own['sys'].load_layout(MenuMain, None)
        mouse.visible = True
    else:
        own['sys'].run()
