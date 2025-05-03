from PyQt6 import QtWidgets
from pages.homePage import homepage
from pages.memoPage import memoPage
from pages.costExpenseEntryPage import costExpensePage
from pages.buyerProfiles import buyerProfiles
from pages.sellerProfiles import sellerProfiles
from pages.receivableReportPage import receivableReport
from pages.payableableReportPage import payableableReport
from pages.settingsPage import settingsPage
from pages.loanPage import Ui_LoanPage
from pages.commissionReportPage import commissionReportPage
from pages.costReportPage import CostReport
from pages.usersPage import userPage
from pages.loanPayingPage import Ui_LoanPayingPage
from ui.dashboard_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow


class DashboardPage(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_ui()

    def setup_ui(self):
        # ************  Home Page
        print("debug HomePage")
        self.homePage = homepage()
        self.ui.stackedWidget.addWidget(self.homePage)

        # ***********  Cash Memo page
        print("debug CashMemoPage")
        self.memoPage = memoPage(self.username)
        self.ui.stackedWidget.addWidget(self.memoPage)

        # ************ debit credit page
        print("debug CostExpensePage")
        self.costExpensePage = costExpensePage(self.username)
        self.ui.stackedWidget.addWidget(self.costExpensePage)

        # ************ buyers profiles
        print("debug BuyerProfilePage")
        self.buyerProfilePage = buyerProfiles(self.username)  # Create the buyer profile page instance
        self.ui.stackedWidget.addWidget(self.buyerProfilePage)  # Add it to the stacked widget

        # ************ seller profiles
        print("debug SellerProfilePage")
        self.sellerProfilePage = sellerProfiles(self.username)  # Create the buyer profile page instance
        self.ui.stackedWidget.addWidget(self.sellerProfilePage)

        # ************ receiveable report page
        print("debug receivableReportPage")
        self.receivableReportStack = QtWidgets.QWidget()
        self.receivableReportStack.setObjectName("Receivable Report Page")
        self.ui.stackedWidget.addWidget(self.receivableReportStack)
        self.receivableReportPage = receivableReport()
        self.receivableReportPage.setupUi(self.receivableReportStack)

        # ************ rpayable report page
        print("debug payableReportPage")
        self.payableReportStack = QtWidgets.QWidget()
        self.payableReportStack.setObjectName("Payable Report Page")
        self.ui.stackedWidget.addWidget(self.payableReportStack)
        self.payableReportPage = payableableReport()
        self.payableReportPage.setupUi(self.payableReportStack)

        # ************ loan page
        print("debug loanPage")
        self.loanStack = QtWidgets.QWidget()
        self.loanStack.setObjectName("Loan Report Page")
        self.ui.stackedWidget.addWidget(self.loanStack)
        self.loanPage = Ui_LoanPage()
        self.loanPage.setupUi(self.loanStack, self.username)

        # ************ loan page
        print("debug loanPage")
        self.loanPayingStack = QtWidgets.QWidget()
        self.loanPayingStack.setObjectName("Loan Report Page")
        self.ui.stackedWidget.addWidget(self.loanPayingStack)
        self.loanPayingPage = Ui_LoanPayingPage()
        self.loanPayingPage.setupUi(self.loanPayingStack)

        # ************ commission page
        print("debug commissionReportPage")
        self.commissionReportPage = commissionReportPage()
        self.ui.stackedWidget.addWidget(self.commissionReportPage)

        # ************ cost report
        print("debug costreportPage")
        self.costreportPage = CostReport(self.username)
        self.ui.stackedWidget.addWidget(self.costreportPage)

        # ************ Users Pages
        print("debug userPage")
        self.userPage = userPage(self.username)
        self.ui.stackedWidget.addWidget(self.userPage)

        # ************ settings page
        print("debug settingsPage")
        self.settingsPage = settingsPage(self.username)
        self.ui.stackedWidget.addWidget(self.settingsPage)
        print("debug after settingsPage")
        # End pages ***********************
        # Page switching
        try:
            self.ui.homeIconBtn.clicked.connect(lambda: self.switch_page("home"))
            self.ui.homeBtn.clicked.connect(lambda: self.switch_page("home"))

            self.ui.memoIconBtn.clicked.connect(lambda: self.switch_page("cash_memo"))
            self.ui.memoBtn.clicked.connect(lambda: self.switch_page("cash_memo"))

            self.ui.costEntryIconBtn.clicked.connect(lambda: self.switch_page("earn_expense"))
            self.ui.costEntryBtn.clicked.connect(lambda: self.switch_page("earn_expense"))

            self.ui.buyerProfileIconBtn.clicked.connect(lambda: self.switch_page("buyer_profile"))
            self.ui.buyerProfileBtn.clicked.connect(lambda: self.switch_page("buyer_profile"))

            self.ui.sellerProfileIconBtn.clicked.connect(lambda: self.switch_page("seller_profile"))
            self.ui.sellerProfileBtn.clicked.connect(lambda: self.switch_page("seller_profile"))

            self.ui.receivableIconBtn.clicked.connect(lambda: self.switch_page("receivable_report"))
            self.ui.receivableBtn.clicked.connect(lambda: self.switch_page("receivable_report"))

            self.ui.payableIconBtn.clicked.connect(lambda: self.switch_page("payable_report"))
            self.ui.payableBtn.clicked.connect(lambda: self.switch_page("payable_report"))

            self.ui.loanBtn.clicked.connect(lambda: self.switch_page("loan_page"))
            self.ui.loanIconBtn.clicked.connect(lambda: self.switch_page("loan_page"))

            self.ui.loanPayingBtn.clicked.connect(lambda: self.switch_page("loan_paying_page"))
            self.ui.loanPayingIconBtn.clicked.connect(lambda: self.switch_page("loan_paying_page"))

            self.ui.commissionIconBtn.clicked.connect(lambda: self.switch_page("commission_report"))
            self.ui.commissionBtn.clicked.connect(lambda: self.switch_page("commission_report"))

            self.ui.costIconBtn.clicked.connect(lambda: self.switch_page("cost_report"))
            self.ui.costBtn.clicked.connect(lambda: self.switch_page("cost_report"))

            self.ui.settingsBtn.clicked.connect(lambda: self.switch_page("settings_page"))
            self.ui.settingsIconBtn.clicked.connect(lambda: self.switch_page("settings_page"))
            self.ui.userBtn.clicked.connect(lambda: self.switch_page("user_page"))

        except AttributeError as e:
            print(f"Error connecting button: {e}")

    def switch_page(self, page_name):
        try:
            if page_name == "home":
                self.ui.stackedWidget.setCurrentWidget(self.homePage)
            elif page_name == "cash_memo":
                self.ui.stackedWidget.setCurrentWidget(self.memoPage)
            elif page_name == "earn_expense":
                self.ui.stackedWidget.setCurrentWidget(self.costExpensePage)
            elif page_name == "buyer_profile":
                self.ui.stackedWidget.setCurrentWidget(self.buyerProfilePage)
            elif page_name == "seller_profile":
                self.ui.stackedWidget.setCurrentWidget(self.sellerProfilePage)
            elif page_name == "receivable_report":
                self.ui.stackedWidget.setCurrentWidget(self.receivableReportStack)
            elif page_name == "payable_report":
                self.ui.stackedWidget.setCurrentWidget(self.payableReportStack)
            elif page_name == "loan_page":
                self.ui.stackedWidget.setCurrentWidget(self.loanStack)
            elif page_name == "loan_paying_page":
                self.ui.stackedWidget.setCurrentWidget(self.loanPayingStack)
            elif page_name == "commission_report":
                self.ui.stackedWidget.setCurrentWidget(self.commissionReportPage)
            elif page_name == "cost_report":
                self.ui.stackedWidget.setCurrentWidget(self.costreportPage)
            elif page_name == "settings_page":
                self.ui.stackedWidget.setCurrentWidget(self.settingsPage)
            elif page_name == "user_page":
                self.ui.stackedWidget.setCurrentWidget(self.userPage)
            else:
                print(f"Invalid page name: {page_name}")
        except Exception as e:
            print(f"Error switching page: {e}")
