from PyQt6.QtWidgets import QDialog
from models import SellerProfileModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from ui.profile_edit_ui import Ui_ProfileEdit

class Profile_Edit_Form(QDialog):
    def __init__(self, name):
        super().__init__()
        self.ui = Ui_ProfileEdit()
        self.ui.setupUi(self)  # Call setupUi to apply the design to this dialog
        self.name = name
        self.setup_database()
        self.setup_ui()
    def setup_database(self):
        self.Base = declarative_base()
        self.engine = create_engine('sqlite:///business.db')
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def setup_ui(self):
        session = self.Session()
        profile = session.query(SellerProfileModel).filter(SellerProfileModel.seller_name == self.name).first()
        self.ui.name.setText(profile.seller_name)
        self.ui.address.setText(profile.address)
        self.ui.phone.setText(profile.phone)

    def handle_entry(self):
        name = self.ui.name.text().strip()  # Change input field
        phone = self.ui.phone.text().strip()
        address = self.ui.address.text().strip()
        if not name:
            return False, "নাম ফাঁকা থাকা যাবেনা .."
        if not phone:
            return False, "ফোন নম্বর ফাঁকা থাকা যাবেনা .."
        if not address:
            return False, "এড্রেস ফাঁকা থাকা যাবেনা.."
        return True, None





