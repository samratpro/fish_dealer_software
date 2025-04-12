from PyQt6.QtWidgets import QDialog
from models import SellerProfileModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from ui.profile_edit_ui import Ui_ProfileEdit

class Profile_Edit_Form(QDialog):
    def __init__(self, id):
        super().__init__()
        self.ui = Ui_ProfileEdit()
        self.ui.setupUi(self)  # Call setupUi to apply the design to this dialog
        self.id = id
        self.setup_database()
        self.setup_ui()
    def setup_database(self):
        self.Base = declarative_base()
        self.engine = create_engine('sqlite:///business.db')
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def setup_ui(self):
        session = self.Session()
        profile = session.query(SellerProfileModel).filter_by(id=self.id).all().first()
        self.ui.name.setText(profile.seller_name)
        self.ui.address.setText(profile.address)
        self.ui.phone.setText(profile.phone)





