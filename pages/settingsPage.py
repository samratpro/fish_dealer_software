from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from sqlalchemy.exc import SQLAlchemyError
from features.data_save_signals import data_save_signals
from sqlalchemy import create_engine, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from ui.settings_ui import Ui_settingsPage
from models import *


class settingsPage(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setup_database()  # First setup database
        self.ui = Ui_settingsPage()
        self.ui.setupUi(self)
        self.setup_ui()


    def setup_database(self):
        self.Base = declarative_base()
        self.engine = create_engine('sqlite:///business.db') 
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)


    def setup_ui(self):
        session = self.Session()
        setting = session.query(SettingModel).first()

        user = session.query(UserModel).filter(UserModel.username==self.username).one()
        self.ui.username.setText(user.username)
        self.ui.username.setDisabled(True)

        self.passEcho = True
        self.ui.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.ui.password.setText(user.password)
        self.ui.viewPassword.clicked.connect(self.passEchoBool)

        self.ui.commission.setText(str(setting.commission))
        self.ui.dhol.setText(str(setting.dhol))
        session.close()
        session = self.Session()
        try:
            setting = session.query(SettingModel).first()
            if setting:
                self.ui.username.setText(user.username)
                self.ui.password.setText(user.password)
                self.ui.commission.setText(str(setting.commission))
                self.ui.dhol.setText(str(setting.dhol))
            else:
                QtWidgets.QMessageBox.warning(None, "Error", f"সেটিংস পাওয়া যায়নি")
        except SQLAlchemyError as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"ডেটাবেস ত্রুটি: {e}")
        finally:
            session.close()
        self.ui.updateBtn.clicked.connect(self.update_setting)

    def passEchoBool(self):
        if self.passEcho == True:
            self.ui.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.passEcho = False
        else:
            self.ui.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            self.passEcho = True


    def update_setting(self):
        username = self.ui.username.text().strip()
        password = self.ui.password.text().strip()
        commision = self.ui.commission.text().strip()
        dhol = self.ui.dhol.text().strip()

        # Check if any field is empty
        if not username or not commision or not dhol or not password:
            QtWidgets.QMessageBox.warning(None, "Error", f"কোন ফিল্ড ফাঁকা থাকা যাবেনা")
            return

        # Validate commission
        try:
            commission_value = float(commision)
        except ValueError:
            QtWidgets.QMessageBox.warning(None, "Error", f"কমিশন (শতাংশ) একটি সঠিক সংখ্যা প্রদান করুন")
            return

        # Validate dhol
        try:
            dhol_value = int(dhol)
        except ValueError:
            QtWidgets.QMessageBox.warning(None, "Error", f"ঢল (গ্রাম) একটি সঠিক সংখ্যা প্রদান করুন")
            return

        # Update the setting
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            setting = session.query(SettingModel).first()
            user = session.query(UserModel).filter(UserModel.username==username).one_or_none()
            if setting is None:
                QtWidgets.QMessageBox.warning(None, "Error", f"কোনো সেটিংস পাওয়া যায়নি")
                return
            if user is None:
                QtWidgets.QMessageBox.warning(None, "Error", f"ইউজারনেম পাওয়া যায়নি")
                return

            setting.commission = commission_value
            setting.dhol = dhol_value
            user.username = username
            user.password = password
            session.commit()
        except SQLAlchemyError as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"সেটিংস আপডেট করতে সমস্যা হয়েছে: {e}")
            session.rollback()
        finally:
            session.close()
        QtWidgets.QMessageBox.information(None, "Success", f"সেটিংস আপডেট হয়েছে")
        data_save_signals.data_saved.emit()
