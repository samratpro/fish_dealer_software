from PyQt6.QtWidgets import QDialog
from sqlalchemy.orm import declarative_base
from ui.profile_edit_ui import Ui_ProfileEdit
from models import *
from sqlalchemy import and_
from PyQt6.QtGui import QFont, QFontDatabase
from features.data_save_signals import data_save_signals
from PyQt6 import QtWidgets

class Profile_Edit_Form(QDialog):
    def __init__(self, name, cost_type):
        super().__init__()
        self.ui = Ui_ProfileEdit()
        self.ui.setupUi(self)  # Call setupUi to apply the design to this dialog
        self.name = name
        self.cost_type = cost_type
        self.setup_database()
        self.setup_ui()
    def setup_database(self):
        self.Base = declarative_base()
        self.engine = create_engine('sqlite:///business.db')
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def setup_ui(self):
        session = self.Session()
        print("Cost Profile edit, cost_type : ", self.cost_type)
        profile = session.query(CostProfileModel).filter(
            and_(
                CostProfileModel.name == self.name,
                CostProfileModel.cost_type == self.cost_type
            )
        ).first()

        if not profile:
            print(f"No profile found for name: {self.name}, cost_type: {self.cost_type}")
            QtWidgets.QMessageBox.warning(
                self, "Error", f"No profile found for name '{self.name}' and cost_type '{self.cost_type}'."
            )
            self.close()  # Close the form if no profile is found
            return

        print("profile.name ", profile.name)
        self.ui.name.setText(profile.name)
        self.ui.phone.setDisabled(True)
        self.ui.phone.setStyleSheet("background-color: #F0F0F0;")
        self.ui.address.setDisabled(True)
        self.ui.address.setStyleSheet("background-color: #F0F0F0;")
        self.update_setting_font()
        data_save_signals.data_saved.connect(self.update_setting_font)

    def handle_entry(self):
        name = self.ui.name.text().strip()
        if not name:
            return False, "নাম ফাঁকা থাকা যাবেনা .."
        return True, None

    def update_setting_font(self):
        session = self.Session()
        setting = session.query(SettingModel).first()
        bangla_font_path = "font/nato.ttf"
        english_font_path = "font/arial.ttf"
        font_id = QFontDatabase.addApplicationFont(bangla_font_path)
        if font_id == -1:
            print(f"❌ Failed to load font: {bangla_font_path}")
            return
        # Load the appropriate font
        if setting.font == "Bangla":
            font_id = QFontDatabase.addApplicationFont(bangla_font_path)
            custom_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            custom_font = QFont(custom_font_family, 12)  # Font size 12
        else:
            font_id = QFontDatabase.addApplicationFont(english_font_path)
            custom_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            custom_font = QFont(custom_font_family, 12)  # Font size 12

        from bangla_typing import enable_bangla_typing
        self.ui.name.setFont(custom_font)
        enable_bangla_typing(self.ui.name, setting.font)





