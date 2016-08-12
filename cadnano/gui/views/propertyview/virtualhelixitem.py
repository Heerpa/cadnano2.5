"""VirtualHelixItem for the PropertyView.

Attributes:
    KEY_COL (int): QTreeWidgetItem column that will display property keys
    VAL_COL (int): QTreeWidgetItem column that will display property values
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox
from cadnano.enum import ItemType
from cadnano.gui.views.abstractitems.abstractvirtualhelixitem import AbstractVirtualHelixItem
from cadnano.gui.controllers.itemcontrollers.virtualhelixitemcontroller import VirtualHelixItemController
from .cnpropertyitem import CNPropertyItem

KEY_COL = 0
VAL_COL = 1


class VirtualHelixItem(QTreeWidgetItem):
    """VirtualHelixItem class for the PropertyView.
    """
    def __init__(self, model_part, parent, id_num_list, key=None):
        """Summary

        Args:
            model_part (Part): The model part
            parent (TYPE): Description
            id_num (int): VirtualHelix ID number. See `NucleicAcidPart` for description and related methods.
            key (None, optional): Description
        """
        self._cn_model = model_part
        self._cn_model_list = [model_part]
        self._model_part = model_part
        self._id_num_list = id_num_list
        self._controller = None
        self.is_enum = False  # for use of CNPropertyItem class methods
        super(VirtualHelixItem, self).__init__(parent, QTreeWidgetItem.UserType)
        self.setFlags(self.flags() | Qt.ItemIsEditable)

        if key is None:
            self._controller = VirtualHelixItemController(self, model_part, True, False)
            root = parent.invisibleRootItem()  # add propertyitems as siblings

            # Properties
            self._prop_items = {}
            id_num_props = {}
            combined_props = {}
            for id_num in self._id_num_list:
                id_num_props[id_num] = AbstractVirtualHelixItem.getAllPropertiesForIdNum(self, id_num)
                for cn_key, cn_val in id_num_props[id_num].items():
                    if cn_key in combined_props:
                        if cn_val != combined_props[cn_key]:
                            combined_props[cn_key] = '~~multiple~~'
                    else:
                        combined_props[cn_key] = cn_val

            # model_props = AbstractVirtualHelixItem.getAllProperties(self)
            # print(combined_props)

            # add properties alphabetically, but with 'name' on top
            if len(self._id_num_list) == 1:
                name = id_num_props[self._id_num_list[0]]['name']
                if name is None:
                    name = "generic"
            else:
                name = "%d helices..." % len(self._id_num_list)
            self._key = key = "name"
            self._prop_items[key] = self
            self.setData(KEY_COL, Qt.EditRole, key)
            self.setData(VAL_COL, Qt.EditRole, name)

            for key in sorted(combined_props):
                if key == 'name':
                    continue
                p_i = VirtualHelixItem(model_part, root, id_num_list, key=key)
                self._prop_items[key] = p_i
                p_i.setData(KEY_COL, Qt.EditRole, key)
                model_value = combined_props[key]
                # print(key, model_value, type(model_value))
                if isinstance(model_value, float):
                    model_value = "%0.3f" % model_value
                # elif not isinstance(model_value, str):
                #     model_value = str(model_value)
                p_i.setData(VAL_COL, Qt.EditRole, model_value)
        else:
            self._key = key
    # end def

    def key(self):
        """Summary

        Returns:
            TYPE: Description
        """
        return self._key

    ### PUBLIC SUPPORT METHODS ###
    def cnModel(self):
        """Summary

        Returns:
            TYPE: Description
        """
        return self._cn_model
    # end def

    def itemType(self):
        """Overrides AbstractPropertyPartItem.itemType

        Returns:
            ItemType: VIRTUALHELIX
        """
        return ItemType.VIRTUALHELIX
    # end def

    def disconnectSignals(self):
        """Summary

        Returns:
            TYPE: Description
        """
        if self._controller is not None:
            self._controller.disconnectSignals()
            self._controller = None
    # end def

    # SLOTS
    def partVirtualHelixPropertyChangedSlot(self, sender, id_num, keys, values):
        """Summary

        Args:
            sender (obj): Model object that emitted the signal.
            id_num (int): VirtualHelix ID number. See `NucleicAcidPart` for description and related methods.
            keys (TYPE): Description
            values (TYPE): Description

        Returns:
            TYPE: Description
        """
        if self._cn_model == sender and id_num in self._id_num_list:
            for key, val in zip(keys, values):
                # print("change slot", key, val)
                self.setValue(key, val)

    def partVirtualHelixRemovingSlot(self, sender, id_num, neighbors):
        """Summary

        Args:
            sender (obj): Model object that emitted the signal.
            id_num (int): VirtualHelix ID number. See `NucleicAcidPart` for description and related methods.
            neighbors (list):
        """
        if self._cn_model == sender and id_num in self._id_num_list:
            self._cn_model = None
            self._controller = None
            self.parent().removeChild(self)
    # end def

    def partVirtualHelixRemovedSlot(self, sender, id_num):
        """Summary

        Args:
            sender (obj): Model object that emitted the signal.
            id_num (int): VirtualHelix ID number. See `NucleicAcidPart` for description and related methods.
        """
        pass
    # end def

    def configureEditor(self, parent_QWidget, option, model_index):
        """Summary

        Args:
            parent_QWidget (TYPE): Description
            option (TYPE): Description
            model_index (TYPE): Description

        Returns:
            TYPE: Description
        """
        key = self.key()
        if key == 'eulerZ':
            editor = QDoubleSpinBox(parent_QWidget)
            tpb, _ = AbstractVirtualHelixItem.getTwistPerBase()
            editor.setSingleStep(tpb)
            editor.setDecimals(1)
            editor.setRange(0, 359)
        elif key == 'scamZ':
            editor = QDoubleSpinBox(parent_QWidget)
            tpb, _ = AbstractVirtualHelixItem.getTwistPerBase()
            editor.setSingleStep(tpb)
            editor.setDecimals(1)
            editor.setRange(0, 359)
        elif key == 'length':
            editor = QSpinBox(parent_QWidget)
            bpr, length = AbstractVirtualHelixItem.getProperty(self,
                                                               ['bases_per_repeat',
                                                                'length'])
            editor.setRange(length, 4*length)
            editor.setSingleStep(bpr)
        elif key == 'z' and self._model_part.isZEditable():
            editor = QDoubleSpinBox(parent_QWidget)
            bw = self._model_part.baseWidth()
            editor.setSingleStep(bw)
            editor.setRange(-bw*21, bw*21)
        else:
            editor = CNPropertyItem.configureEditor(self, parent_QWidget, option, model_index)
        return editor
    # end def

    def updateCNModel(self):
        """Notify the cadnano model that a property may need updating.
        This method should be called by the item model dataChangedSlot.
        """
        value = self.data(1, Qt.DisplayRole)
        key = self._key
        if key == 'length':
            print("Property view 'length' updating", key, value, self._id_num_list)
            AbstractVirtualHelixItem.setSize(self, value, id_nums=self._id_num_list)
        elif key == 'z':
            print("Property view 'z' updating", key, value)
            AbstractVirtualHelixItem.setZ(self, value, id_nums=self._id_num_list)
        else:
            AbstractVirtualHelixItem.setProperty(self, self._key, value, id_nums=self._id_num_list)
    # end def

    def setValue(self, property_key, new_value):
        """Summary

        Args:
            property_key (TYPE): Description
            new_value (TYPE): Description

        Returns:
            TYPE: Description
        """
        p_i = self._prop_items[property_key]
        current_value = p_i.data(VAL_COL, Qt.DisplayRole)
        if current_value != new_value:
            p_i.setData(VAL_COL, Qt.EditRole, new_value)
    # end def

    def getItemValue(self, property_key):
        """Summary

        Args:
            property_key (TYPE): Description

        Returns:
            TYPE: Description
        """
        return self._prop_items[property_key].data(VAL_COL, Qt.DisplayRole)
    # end def
# end class
