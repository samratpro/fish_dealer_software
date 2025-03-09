from PyQt6 import QtWidgets
from ui.printmemo_ui import Ui_Form
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import QHeaderView
from PyQt6 import QtCore
import os

class Print_Form(QtWidgets.QWidget):  # ✅ Inherit QWidget
    def __init__(self, min_section_size=135):
        super().__init__()  # ✅ Properly initialize QWidget
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # ✅ Set up UI on self (which is now a QWidget)
        self.min_section_size = min_section_size
        self.setup_ui()

    def setup_ui(self):
        self.apply_bangla_font()
        self.ui.tableWidget.horizontalHeader().setMinimumSectionSize(self.min_section_size)

    def apply_bangla_font(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        bangla_font_path = os.path.join(base_dir, "font", "nato.ttf")
        print("bangla_font_path : ", bangla_font_path)
        font_id = QFontDatabase.addApplicationFont(bangla_font_path)
        if font_id == -1:
            print(f"❌ Failed to load font: {bangla_font_path}")
            return
        custom_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        print(f"✅ Font loaded successfully: {custom_font_family}")
        custom_font_low = QFont(custom_font_family, 11)  # Font size 11
        custom_font_high = QFont(custom_font_family, 22)  # Font size 22
        custom_font = QFont(custom_font_family, 11)  # Font size 11
        self.ui.tableWidget.horizontalHeader().setFont(custom_font)
        self.ui.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.tableWidget.setFont(custom_font)
        self.ui.tableWidget.verticalHeader().setFont(custom_font)
        self.ui.label.setFont(custom_font_low)
        self.ui.memoLabel.setFont(custom_font)
        self.ui.label_9.setFont(custom_font_high)
        self.ui.label_10.setFont(custom_font_low)
        self.ui.label_11.setFont(custom_font)
        self.ui.label_13.setFont(custom_font)
        self.ui.label_12.setFont(custom_font)
        self.ui.label_14.setFont(custom_font)
        self.ui.label_2.setFont(custom_font_low)
        self.ui.label_3.setFont(custom_font_low)
        self.ui.label_4.setFont(custom_font_low)
        self.ui.label_5.setFont(custom_font_low)
        self.ui.label_6.setFont(custom_font_low)
        self.ui.label_7.setFont(custom_font_low)
        self.ui.label_19.setFont(custom_font)
        self.ui.label_20.setFont(custom_font)
        self.ui.label_21.setFont(custom_font)
        self.ui.label_22.setFont(custom_font)
        self.ui.label_23.setFont(custom_font)
        self.ui.label_24.setFont(custom_font)
        self.ui.label_25.setFont(custom_font)
        self.ui.label_26.setFont(custom_font)
        self.ui.label_16.setFont(custom_font)
        self.ui.label_15.setFont(custom_font)
        self.ui.label_17.setFont(custom_font_low)
        self.ui.label_18.setFont(custom_font)
        self.ui.date.setFont(custom_font)
