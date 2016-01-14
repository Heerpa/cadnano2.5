from PyQt5.QtCore import Qt

from cadnano.enum import ItemType

from .cnoutlineritem import CNOutlinerItem
from cadnano.gui.views.abstractitems.abstractvirtualhelixitem import AbstractVirtualHelixItem
from cadnano.gui.controllers.itemcontrollers.virtualhelixitemcontroller import VirtualHelixItemController


class VirtualHelixItem(AbstractVirtualHelixItem, CNOutlinerItem):
    def __init__(self, id_num, part_item):
        AbstractVirtualHelixItem.__init__(self, id_num, part_item)
        model_part = self._model_part
        CNOutlinerItem.__init__(self, model_part, parent=part_item)
        vhg = model_part.virtualHelixGroup()
        name = vhg.getName(id_num)
        self.setData(0, Qt.EditRole, name)
        self._controller = VirtualHelixItemController(self, model_part, False, False)
    # end def

    ### PRIVATE SUPPORT METHODS ###

    ### PUBLIC SUPPORT METHODS ###
    def itemType(self):
        return ItemType.VIRTUALHELIX
    # end def

    def updateCNModel(self):
        # this works only for color. uncomment below to generalize to properties
        # print("outliner %s - updateCNModel" % (str(type(self))))
        cn_model = self._cn_model
        color = self.data(COLOR_COL, Qt.DisplayRole)
        if color != cn_model.getColor():
            cn_model.setProperty('color', color)
    # end def

    ### SLOTS ###
# end class
