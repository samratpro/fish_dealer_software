from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSignal
from login import Ui_LoginForm
from dashboard import Ui_MainWindow
import sys

class Dashboard(QMainWindow):
    logout_signal = pyqtSignal()

    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.setMinimumSize(1000, 600)

        # Initialize the dashboard UI
        self.dashboard_ui = Ui_MainWindow()
        self.dashboard_ui.setupUi(self, username)

        print("user name from app.py : ", username)

        # Assuming you have a logout button defined in your UI
        self.dashboard_ui.logoutBtn.clicked.connect(self.handle_logout)

    def handle_logout(self):
        """Handle the logout button click."""
        self.logout_signal.emit()

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ওসমান ফিশ")
        self.setMinimumSize(1200, 700)
        self.setWindowIcon(QIcon("images/logo.png"))
        # Initialize login form and dashboard attributes
        self.login_widget = None
        self.dashboard = None

        # Set the initial widget to login form
        self.show_login()

    def show_login(self):
        try:
            """Switches back to the login page."""
            # Recreate the login form and widget
            self.login_form = Ui_LoginForm()
            self.login_widget = QWidget()
            self.login_form.setupUi(self.login_widget)
            self.login_form.login_success_signal.connect(self.show_dashboard)
            print("Showing login form")
            self.setCentralWidget(self.login_widget)
        except Exception as e:
            print(f"Error in show_login: {e}")

    def show_dashboard(self, username):
        try:
            """Switches to the dashboard after a successful login."""
            # Recreate the dashboard
            self.dashboard = Dashboard(username)
            self.dashboard.logout_signal.connect(self.show_login)
            print("Showing dashboard")
            self.setCentralWidget(self.dashboard)
        except Exception as e:
            print(f"Error in show_dashboard: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()
    sys.exit(app.exec())