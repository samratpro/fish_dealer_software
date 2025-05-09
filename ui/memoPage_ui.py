from PyQt6 import QtCore
from PyQt6 import QtWidgets, QtGui

class Ui_memoPageMain(object):
    def setupUi(self, memoPageMain):
        memoPageMain.setObjectName("memoPageMain")
        memoPageMain.resize(814, 647)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        memoPageMain.setFont(font)
        memoPageMain.setStyleSheet("""*{text-align: left;}
                                   QLineEdit, QDateEdit{border-radius:10px;
                                                        border:1px solid #B8B8B8;
                                                        padding:2px;}
                                   QPushButton{background-color:#2D221B;color:white;
                                                padding:5px 8px;
                                                border-radius:9px;}
                                   QDateEdit::drop-down {
                                            image: url('./images/down-arrow.png');
                                            margin:3px 4px 0 0;
                                            border:1px solid #DEDEDE;
                                           }
                                   """)
        self.memoPageMain_Layout = QtWidgets.QVBoxLayout(memoPageMain)
        self.memoPageMain_Layout.setContentsMargins(15, 15, 15, 15)
        self.memoPageMain_Layout.setSpacing(6)
        self.memoPageMain_Layout.setObjectName("memoPageMain_Layout")
        self.memoHeader = QtWidgets.QWidget(parent=memoPageMain)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.memoHeader.setFont(font)
        self.memoHeader.setStyleSheet("")
        self.memoHeader.setObjectName("memoHeader")
        self.memoHeader_Layout = QtWidgets.QHBoxLayout(self.memoHeader)
        self.memoHeader_Layout.setContentsMargins(0, 0, 0, 0)
        self.memoHeader_Layout.setSpacing(0)
        self.memoHeader_Layout.setObjectName("memoHeader_Layout")
        self.memoHeaderLeft = QtWidgets.QWidget(parent=self.memoHeader)
        self.memoHeaderLeft.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.memoHeaderLeft.setFont(font)
        self.memoHeaderLeft.setObjectName("memoHeaderLeft")
        self.memoHeaderLeft_lLayout = QtWidgets.QVBoxLayout(self.memoHeaderLeft)
        self.memoHeaderLeft_lLayout.setObjectName("memoHeaderLeft_lLayout")
        self.memoVoucharFrame = QtWidgets.QFrame(parent=self.memoHeaderLeft)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.memoVoucharFrame.setFont(font)
        self.memoVoucharFrame.setObjectName("memoVoucharFrame")
        self.memoVoucharFrame_Layout = QtWidgets.QHBoxLayout(self.memoVoucharFrame)
        self.memoVoucharFrame_Layout.setContentsMargins(0, 0, 0, 0)
        self.memoVoucharFrame_Layout.setSpacing(0)
        self.memoVoucharFrame_Layout.setObjectName("memoVoucharFrame_Layout")
        self.voucharLabel = QtWidgets.QLabel(parent=self.memoVoucharFrame)
        self.voucharLabel.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.voucharLabel.setFont(font)
        self.voucharLabel.setObjectName("voucharLabel")
        self.memoVoucharFrame_Layout.addWidget(self.voucharLabel)
        self.voucharInput = QtWidgets.QLineEdit(parent=self.memoVoucharFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.voucharInput.setFont(font)
        self.voucharInput.setObjectName("voucharInput")
        self.memoVoucharFrame_Layout.addWidget(self.voucharInput)
        self.memoHeaderLeft_lLayout.addWidget(self.memoVoucharFrame)
        self.memoSellerFrame = QtWidgets.QFrame(parent=self.memoHeaderLeft)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.memoSellerFrame.setFont(font)
        self.memoSellerFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.memoSellerFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.memoSellerFrame.setObjectName("memoSellerFrame")
        self.memoSellerFrame_Layout = QtWidgets.QHBoxLayout(self.memoSellerFrame)
        self.memoSellerFrame_Layout.setContentsMargins(0, 0, 0, 0)
        self.memoSellerFrame_Layout.setSpacing(0)
        self.memoSellerFrame_Layout.setObjectName("memoSellerFrame_Layout")
        self.sellerNameLabel = QtWidgets.QLabel(parent=self.memoSellerFrame)
        self.sellerNameLabel.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sellerNameLabel.setFont(font)
        self.sellerNameLabel.setObjectName("sellerNameLabel")
        self.memoSellerFrame_Layout.addWidget(self.sellerNameLabel)
        self.sellerNameInput = QtWidgets.QLineEdit(parent=self.memoSellerFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sellerNameInput.setFont(font)
        self.sellerNameInput.setObjectName("sellerNameInput")
        self.memoSellerFrame_Layout.addWidget(self.sellerNameInput)
        self.memoHeaderLeft_lLayout.addWidget(self.memoSellerFrame)
        self.memoAddressFrame = QtWidgets.QFrame(parent=self.memoHeaderLeft)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.memoAddressFrame.setFont(font)
        self.memoAddressFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.memoAddressFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.memoAddressFrame.setObjectName("memoAddressFrame")
        self.memoAddressFrame_Layout = QtWidgets.QHBoxLayout(self.memoAddressFrame)
        self.memoAddressFrame_Layout.setContentsMargins(0, 0, 0, 0)
        self.memoAddressFrame_Layout.setSpacing(0)
        self.memoAddressFrame_Layout.setObjectName("memoAddressFrame_Layout")
        self.sellerAddresslabel = QtWidgets.QLabel(parent=self.memoAddressFrame)
        self.sellerAddresslabel.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sellerAddresslabel.setFont(font)
        self.sellerAddresslabel.setObjectName("sellerAddresslabel")
        self.memoAddressFrame_Layout.addWidget(self.sellerAddresslabel)
        self.sellerAddressInput = QtWidgets.QLineEdit(parent=self.memoAddressFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sellerAddressInput.setFont(font)
        self.sellerAddressInput.setObjectName("sellerAddressInput")
        self.memoAddressFrame_Layout.addWidget(self.sellerAddressInput)
        self.memoHeaderLeft_lLayout.addWidget(self.memoAddressFrame)
        self.memoHeader_Layout.addWidget(self.memoHeaderLeft)
        self.memoHeaderRight = QtWidgets.QWidget(parent=self.memoHeader)
        self.memoHeaderRight.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.memoHeaderRight.setFont(font)
        self.memoHeaderRight.setObjectName("memoHeaderRight")
        self.memoHeaderRight_Layout = QtWidgets.QVBoxLayout(self.memoHeaderRight)
        self.memoHeaderRight_Layout.setObjectName("memoHeaderRight_Layout")
        self.memoDateFrame = QtWidgets.QFrame(parent=self.memoHeaderRight)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.memoDateFrame.setFont(font)
        self.memoDateFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.memoDateFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.memoDateFrame.setObjectName("memoDateFrame")
        self.memoDateFrame_Layout = QtWidgets.QHBoxLayout(self.memoDateFrame)
        self.memoDateFrame_Layout.setObjectName("memoDateFrame_Layout")
        self.sellingDatelabel = QtWidgets.QLabel(parent=self.memoDateFrame)
        self.sellingDatelabel.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sellingDatelabel.setFont(font)
        self.sellingDatelabel.setObjectName("sellingDatelabel")
        self.memoDateFrame_Layout.addWidget(self.sellingDatelabel)
        self.sellingDateInput = QtWidgets.QDateEdit(parent=self.memoDateFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sellingDateInput.setFont(font)
        self.sellingDateInput.setCalendarPopup(True)
        self.sellingDateInput.setObjectName("sellingDateInput")
        self.memoDateFrame_Layout.addWidget(self.sellingDateInput)
        self.memoHeaderRight_Layout.addWidget(self.memoDateFrame)
        self.mobileFrame = QtWidgets.QFrame(parent=self.memoHeaderRight)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.mobileFrame.setFont(font)
        self.mobileFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mobileFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.mobileFrame.setObjectName("mobileFrame")
        self.mobileFrame_Layout = QtWidgets.QHBoxLayout(self.mobileFrame)
        self.mobileFrame_Layout.setObjectName("mobileFrame_Layout")
        self.sellerMobilelabel = QtWidgets.QLabel(parent=self.mobileFrame)
        self.sellerMobilelabel.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sellerMobilelabel.setFont(font)
        self.sellerMobilelabel.setObjectName("sellerMobilelabel")
        self.mobileFrame_Layout.addWidget(self.sellerMobilelabel)
        self.sellerMobileInput = QtWidgets.QLineEdit(parent=self.mobileFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sellerMobileInput.setFont(font)
        self.sellerMobileInput.setObjectName("sellerMobileInput")
        self.mobileFrame_Layout.addWidget(self.sellerMobileInput)
        self.memoHeaderRight_Layout.addWidget(self.mobileFrame)
        self.buyerAddFrame = QtWidgets.QFrame(parent=self.memoHeaderRight)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.buyerAddFrame.setFont(font)
        self.buyerAddFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.buyerAddFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.buyerAddFrame.setObjectName("buyerAddFrame")
        self.buyerAddFrame_Layout = QtWidgets.QHBoxLayout(self.buyerAddFrame)
        self.buyerAddFrame_Layout.setContentsMargins(8, 0, 0, 0)
        self.buyerAddFrame_Layout.setSpacing(0)
        self.buyerAddFrame_Layout.setObjectName("buyerAddFrame_Layout")
        self.addBuyerBtn = QtWidgets.QPushButton(parent=self.buyerAddFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.addBuyerBtn.setFont(font)
        self.addBuyerBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/user-plus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.addBuyerBtn.setIcon(icon)
        self.addBuyerBtn.setIconSize(QtCore.QSize(22, 22))
        self.addBuyerBtn.setObjectName("addBuyerBtn")
        self.buyerAddFrame_Layout.addWidget(self.addBuyerBtn, 0, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.memoHeaderRight_Layout.addWidget(self.buyerAddFrame)
        self.memoHeader_Layout.addWidget(self.memoHeaderRight)
        self.memoPageMain_Layout.addWidget(self.memoHeader)
        self.memoBody = QtWidgets.QWidget(parent=memoPageMain)
        self.memoBody.setMinimumSize(QtCore.QSize(0, 250))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.memoBody.setFont(font)
        self.memoBody.setObjectName("memoBody")
        self.memoBody_Layout = QtWidgets.QHBoxLayout(self.memoBody)
        self.memoBody_Layout.setContentsMargins(0, 0, 0, 0)
        self.memoBody_Layout.setSpacing(0)
        self.memoBody_Layout.setObjectName("memoBody_Layout")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.memoBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tableWidget.setFont(font)
        font.setPointSize(12)  # Set the font size to 12 points
        self.tableWidget.setFont(font)
        # Apply the stylesheet for row headers
        self.tableWidget.setStyleSheet("""QHeaderView::section, QHeaderView{
                                                        background-color: #2D221B;
                                                        color: white;
                                                        font-size: 12pt;
                                                        text-align: center;
                                                        }
                                                """)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragDrop)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(180)

        self.memoBody_Layout.addWidget(self.tableWidget)
        self.memoPageMain_Layout.addWidget(self.memoBody)
        self.memoBottom = QtWidgets.QWidget(parent=memoPageMain)
        self.memoBottom.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.memoBottom.setFont(font)
        self.memoBottom.setStyleSheet("QLabel{text-aligen:center;}")
        self.memoBottom.setObjectName("memoBottom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.memoBottom)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.commisionFrame = QtWidgets.QFrame(parent=self.memoBottom)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.commisionFrame.setFont(font)
        self.commisionFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.commisionFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.commisionFrame.setObjectName("commisionFrame")
        self.commisionFrame_Layout = QtWidgets.QVBoxLayout(self.commisionFrame)
        self.commisionFrame_Layout.setContentsMargins(0, 0, 0, 0)
        self.commisionFrame_Layout.setSpacing(0)
        self.commisionFrame_Layout.setObjectName("commisionFrame_Layout")
        self.commissionLabel = QtWidgets.QLabel(parent=self.commisionFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.commissionLabel.setFont(font)
        self.commissionLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.commissionLabel.setObjectName("commissionLabel")
        self.commisionFrame_Layout.addWidget(self.commissionLabel)
        self.commissionInput = QtWidgets.QLineEdit(parent=self.commisionFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.commissionInput.setFont(font)
        self.commissionInput.setObjectName("commissionInput")
        self.commisionFrame_Layout.addWidget(self.commissionInput)
        self.horizontalLayout_2.addWidget(self.commisionFrame)
        self.mosqueFrame = QtWidgets.QFrame(parent=self.memoBottom)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.mosqueFrame.setFont(font)
        self.mosqueFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mosqueFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.mosqueFrame.setObjectName("mosqueFrame")
        self.mosqueFrame_Layout = QtWidgets.QVBoxLayout(self.mosqueFrame)
        self.mosqueFrame_Layout.setContentsMargins(0, 0, 0, 0)
        self.mosqueFrame_Layout.setSpacing(0)
        self.mosqueFrame_Layout.setObjectName("mosqueFrame_Layout")
        self.mosqueLabel = QtWidgets.QLabel(parent=self.mosqueFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.mosqueLabel.setFont(font)
        self.mosqueLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mosqueLabel.setObjectName("mosqueLabel")
        self.mosqueFrame_Layout.addWidget(self.mosqueLabel)
        self.mosqueInput = QtWidgets.QLineEdit(parent=self.mosqueFrame)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.mosqueInput.setFont(font)
        self.mosqueInput.setObjectName("mosqueInput")
        self.mosqueFrame_Layout.addWidget(self.mosqueInput)
        self.horizontalLayout_2.addWidget(self.mosqueFrame)
        self.somitiFrame = QtWidgets.QFrame(parent=self.memoBottom)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.somitiFrame.setFont(font)
        self.somitiFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.somitiFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.somitiFrame.setObjectName("somitiFrame")
        self.somitiFrame_Layout = QtWidgets.QVBoxLayout(self.somitiFrame)
        self.somitiFrame_Layout.setContentsMargins(0, 0, 0, 0)
        self.somitiFrame_Layout.setSpacing(0)
        self.somitiFrame_Layout.setObjectName("somitiFrame_Layout")
        self.somitiLabel = QtWidgets.QLabel(parent=self.somitiFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.somitiLabel.setFont(font)
        self.somitiLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.somitiLabel.setObjectName("somitiLabel")
        self.somitiFrame_Layout.addWidget(self.somitiLabel)
        self.somitiInput = QtWidgets.QLineEdit(parent=self.somitiFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.somitiInput.setFont(font)
        self.somitiInput.setObjectName("somitiInput")

        self.somitiFrame_Layout.addWidget(self.somitiInput)
        self.horizontalLayout_2.addWidget(self.somitiFrame)
        self.otherCostFrame = QtWidgets.QFrame(parent=self.memoBottom)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.otherCostFrame.setFont(font)
        self.otherCostFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.otherCostFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.otherCostFrame.setObjectName("otherCostFrame")
        self.otherCostFrame_Layout = QtWidgets.QVBoxLayout(self.otherCostFrame)
        self.otherCostFrame_Layout.setContentsMargins(0, 0, 0, 0)
        self.otherCostFrame_Layout.setSpacing(0)
        self.otherCostFrame_Layout.setObjectName("otherCostFrame_Layout")
        self.otherLabel = QtWidgets.QLabel(parent=self.otherCostFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.otherLabel.setFont(font)
        self.otherLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.otherLabel.setObjectName("otherLabel")
        self.otherCostFrame_Layout.addWidget(self.otherLabel)
        self.otherInput = QtWidgets.QLineEdit(parent=self.otherCostFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.otherInput.setFont(font)
        self.otherInput.setObjectName("otherInput")

        self.otherCostFrame_Layout.addWidget(self.otherInput)
        self.horizontalLayout_2.addWidget(self.otherCostFrame)
        self.totalTakaFrame = QtWidgets.QFrame(parent=self.memoBottom)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.totalTakaFrame.setFont(font)
        self.totalTakaFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.totalTakaFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.totalTakaFrame.setObjectName("totalTakaFrame")
        self.totalTakaFrame_Layout = QtWidgets.QVBoxLayout(self.totalTakaFrame)
        self.totalTakaFrame_Layout.setContentsMargins(0, 0, 0, 0)
        self.totalTakaFrame_Layout.setSpacing(0)
        self.totalTakaFrame_Layout.setObjectName("totalTakaFrame_Layout")
        self.totalTakaLabel = QtWidgets.QLabel(parent=self.totalTakaFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.totalTakaLabel.setFont(font)
        self.totalTakaLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.totalTakaLabel.setObjectName("totalTakaLabel")
        self.totalTakaFrame_Layout.addWidget(self.totalTakaLabel)
        self.totalTakaInput = QtWidgets.QLineEdit(parent=self.totalTakaFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.totalTakaInput.setFont(font)
        self.totalTakaInput.setObjectName("totalTakaInput")
        self.totalTakaFrame_Layout.addWidget(self.totalTakaInput)
        self.horizontalLayout_2.addWidget(self.totalTakaFrame)
        self.totalCostFrame = QtWidgets.QFrame(parent=self.memoBottom)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.totalCostFrame.setFont(font)
        self.totalCostFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.totalCostFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.totalCostFrame.setObjectName("totalCostFrame")
        self.totalCostFrame_Layout = QtWidgets.QVBoxLayout(self.totalCostFrame)
        self.totalCostFrame_Layout.setContentsMargins(0, 0, 0, 0)
        self.totalCostFrame_Layout.setSpacing(0)
        self.totalCostFrame_Layout.setObjectName("totalCostFrame_Layout")
        self.totalCostLabel = QtWidgets.QLabel(parent=self.totalCostFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.totalCostLabel.setFont(font)
        self.totalCostLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.totalCostLabel.setObjectName("totalCostLabel")
        self.totalCostFrame_Layout.addWidget(self.totalCostLabel)
        self.totalCostInput = QtWidgets.QLineEdit(parent=self.totalCostFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.totalCostInput.setFont(font)
        self.totalCostInput.setObjectName("totalCostInput")
        self.totalCostFrame_Layout.addWidget(self.totalCostInput)
        self.horizontalLayout_2.addWidget(self.totalCostFrame)
        self.finalTakaFrame = QtWidgets.QFrame(parent=self.memoBottom)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.finalTakaFrame.setFont(font)
        self.finalTakaFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.finalTakaFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.finalTakaFrame.setObjectName("finalTakaFrame")
        self.finalTakaFrame_Layout = QtWidgets.QVBoxLayout(self.finalTakaFrame)
        self.finalTakaFrame_Layout.setContentsMargins(0, 0, 0, 0)
        self.finalTakaFrame_Layout.setSpacing(0)
        self.finalTakaFrame_Layout.setObjectName("finalTakaFrame_Layout")
        self.finalTakaLabel = QtWidgets.QLabel(parent=self.finalTakaFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.finalTakaLabel.setFont(font)
        self.finalTakaLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.finalTakaLabel.setObjectName("finalTakaLabel")
        self.finalTakaFrame_Layout.addWidget(self.finalTakaLabel)
        self.finalTakaInput = QtWidgets.QLineEdit(parent=self.finalTakaFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.finalTakaInput.setFont(font)
        self.finalTakaInput.setObjectName("finalTakaInput")
        self.finalTakaFrame_Layout.addWidget(self.finalTakaInput)
        self.horizontalLayout_2.addWidget(self.finalTakaFrame)
        self.sellerPaidFrame = QtWidgets.QFrame(parent=self.memoBottom)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.sellerPaidFrame.setFont(font)
        self.sellerPaidFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.sellerPaidFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sellerPaidFrame.setObjectName("sellerPaidFrame")
        self.sellerPaidFrame_Layout = QtWidgets.QVBoxLayout(self.sellerPaidFrame)
        self.sellerPaidFrame_Layout.setContentsMargins(0, 0, 0, 0)
        self.sellerPaidFrame_Layout.setSpacing(0)
        self.sellerPaidFrame_Layout.setObjectName("sellerPaidFrame_Layout")
        self.sellerPaidTakaLabel = QtWidgets.QLabel(parent=self.sellerPaidFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sellerPaidTakaLabel.setFont(font)
        self.sellerPaidTakaLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sellerPaidTakaLabel.setObjectName("sellerPaidTakaLabel")
        self.sellerPaidFrame_Layout.addWidget(self.sellerPaidTakaLabel)
        self.sellerPaidTakaInput = QtWidgets.QLineEdit(parent=self.sellerPaidFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.sellerPaidTakaInput.setFont(font)
        self.sellerPaidTakaInput.setObjectName("sellerPaidTakaInput")
        self.sellerPaidTakaInput.setText('0')

        self.sellerPaidFrame_Layout.addWidget(self.sellerPaidTakaInput)
        self.horizontalLayout_2.addWidget(self.sellerPaidFrame)
        self.remainFrame = QtWidgets.QFrame(parent=self.memoBottom)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.remainFrame.setFont(font)
        self.remainFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.remainFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.remainFrame.setObjectName("remainFrame")
        self.remainFrame_Layout = QtWidgets.QVBoxLayout(self.remainFrame)
        self.remainFrame_Layout.setContentsMargins(0, 0, 0, 0)
        self.remainFrame_Layout.setSpacing(0)
        self.remainFrame_Layout.setObjectName("remainFrame_Layout")
        self.remainTakaLabel = QtWidgets.QLabel(parent=self.remainFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.remainTakaLabel.setFont(font)
        self.remainTakaLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.remainTakaLabel.setObjectName("remainTakaLabel")
        self.remainFrame_Layout.addWidget(self.remainTakaLabel)
        self.remainTakaInput = QtWidgets.QLineEdit(parent=self.remainFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.remainTakaInput.setFont(font)
        self.remainTakaInput.setObjectName("remainTakaInput")
        self.remainTakaInput.setText('0')

        self.remainFrame_Layout.addWidget(self.remainTakaInput)
        self.horizontalLayout_2.addWidget(self.remainFrame)
        self.memoPageMain_Layout.addWidget(self.memoBottom)
        self.memoFooter = QtWidgets.QWidget(parent=memoPageMain)
        self.memoFooter.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.memoFooter.setFont(font)
        self.memoFooter.setStyleSheet("")
        self.memoFooter.setObjectName("memoFooter")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.memoFooter)
        self.horizontalLayout.setContentsMargins(20, -1, 20, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_db_Btn = QtWidgets.QPushButton(parent=self.memoFooter)
        self.save_db_Btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.save_db_Btn.setFont(font)
        self.save_db_Btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/database.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.save_db_Btn.setIcon(icon1)
        self.save_db_Btn.setIconSize(QtCore.QSize(22, 22))
        self.save_db_Btn.setCheckable(True)
        self.save_db_Btn.setAutoExclusive(True)
        self.save_db_Btn.setObjectName("save_db_Btn")
        self.horizontalLayout.addWidget(self.save_db_Btn, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.saveExcelBtn = QtWidgets.QPushButton(parent=self.memoFooter)
        self.saveExcelBtn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.saveExcelBtn.setFont(font)
        self.saveExcelBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/save.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.saveExcelBtn.setIcon(icon2)
        self.saveExcelBtn.setIconSize(QtCore.QSize(22, 22))
        self.saveExcelBtn.setCheckable(True)
        self.saveExcelBtn.setAutoExclusive(True)
        self.saveExcelBtn.setObjectName("saveExcelBtn")
        self.horizontalLayout.addWidget(self.saveExcelBtn, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.printBtn = QtWidgets.QPushButton(parent=self.memoFooter)
        self.printBtn.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.printBtn.setFont(font)
        self.printBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./icons/printer.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.printBtn.setIcon(icon3)
        self.printBtn.setIconSize(QtCore.QSize(22, 22))
        self.printBtn.setCheckable(True)
        self.printBtn.setAutoExclusive(True)
        self.printBtn.setObjectName("printBtn")
        self.horizontalLayout.addWidget(self.printBtn, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.memoPageMain_Layout.addWidget(self.memoFooter)

        self.retranslateUi(memoPageMain)
        QtCore.QMetaObject.connectSlotsByName(memoPageMain)

    def retranslateUi(self, memoPageMain):
        _translate = QtCore.QCoreApplication.translate
        memoPageMain.setWindowTitle(_translate("memoPageMain", "Form"))
        self.voucharLabel.setText(_translate("memoPageMain", "*ভাউচার নং:"))
        self.sellerNameLabel.setText(_translate("memoPageMain", "*বিক্রেতার নাম:"))
        self.sellerAddresslabel.setText(_translate("memoPageMain", "ঠিকানা:"))
        self.sellingDatelabel.setText(_translate("memoPageMain", "*তারিখ :"))
        self.sellerMobilelabel.setText(_translate("memoPageMain", "মোবাইল নং:"))
        self.addBuyerBtn.setText(_translate("memoPageMain", "ক্রেতা যোগ করুন "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("memoPageMain", "ক্রেতার নাম"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("memoPageMain", "মাছের নাম"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("memoPageMain", "মাছের দর"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("memoPageMain", "কাঁচা"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("memoPageMain", "পাকা"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("memoPageMain", "মোট দাম"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("memoPageMain", "অ্যাকশন"))
        self.commissionLabel.setText(_translate("memoPageMain", "*কমিশন"))
        self.mosqueLabel.setText(_translate("memoPageMain", "*মসজিদ/মাদ্রাসা"))
        self.somitiLabel.setText(_translate("memoPageMain", "*সমিতি"))
        self.otherLabel.setText(_translate("memoPageMain", "অন্যান্য"))
        self.totalTakaLabel.setText(_translate("memoPageMain", "*মোট টাকা"))
        self.totalCostLabel.setText(_translate("memoPageMain", "*মোট খরচ"))
        self.finalTakaLabel.setText(_translate("memoPageMain", "*সর্বমোট টাকা"))
        self.sellerPaidTakaLabel.setText(_translate("memoPageMain", "প্রদান"))
        self.remainTakaLabel.setText(_translate("memoPageMain", "বাকি"))
        self.save_db_Btn.setText(_translate("memoPageMain", "সেভ ইন ডাটাবেস"))
        self.saveExcelBtn.setText(_translate("memoPageMain", "সেভ এক্সেল ফাইল"))
        self.printBtn.setText(_translate("memoPageMain", "প্রিন্ট মেমো"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    memoPageMain = QtWidgets.QWidget()
    ui = Ui_memoPageMain()
    ui.setupUi(memoPageMain)
    memoPageMain.show()
    sys.exit(app.exec())
