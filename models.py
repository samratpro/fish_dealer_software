from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

# Seller Model
class SellerProfileModel(Base):
    __tablename__ = "seller_profile_model"
    id = Column(Integer, primary_key=True)
    seller_name = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    seller_rank = Column(Integer, default=0)
    total_payable = Column(Integer, default=0)
    total_get_paid_amount = Column(Integer, default=0)
    total_commission = Column(Float, default=0.0)
    date = Column(Date)
    entry_by = Column(String, nullable=True)

    sellers = relationship("SellingModel", back_populates="seller_profile")

class SellingModel(Base):
    __tablename__ = "selling_model"
    id = Column(Integer, primary_key=True)
    vouchar_no = Column(String, nullable=False)
    seller_name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    sell_amount = Column(Integer)
    commission_amount = Column(Float, default=0.0)
    total_cost_amount = Column(Integer, default=0.0)
    entry_by = Column(String, nullable=True)

    category_id = Column(Integer, ForeignKey("seller_profile_model.id"))
    seller_profile = relationship("SellerProfileModel", back_populates="sellers")

# Buyer Model
class BuyerProfileModel(Base):
    __tablename__ = "buyer_profile_model"
    id = Column(Integer, primary_key=True)
    buyer_name = Column(String, unique=True, nullable=False)
    buyer_rank = Column(Integer, default=0)
    total_receivable = Column(Integer, default=0)
    total_paid = Column(Integer, default=0)
    date = Column(Date)
    entry_by = Column(String, nullable=True)

    buyers = relationship("BuyingModel", back_populates="buyer_profile")

class BuyingModel(Base):
    __tablename__ = 'buying_model'
    id = Column(Integer, primary_key=True)
    vouchar_no = Column(String, nullable=False)
    buyer_name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    fish_name = Column(String, nullable=True)
    fish_rate = Column(String)
    raw_weight = Column(String)
    final_weight = Column(String)
    buying_amount = Column(Integer)
    seller_name = Column(String, nullable=True)
    entry_by = Column(String, nullable=True)

    category_id = Column(Integer, ForeignKey("buyer_profile_model.id"))
    buyer_profile = relationship("BuyerProfileModel", back_populates="buyers")

# Dealer Model
class DealerModel(Base):
    __tablename__ = 'dealer_model'
    id = Column(Integer, primary_key=True)
    entry_name = Column(String, nullable=False)  # all_accounting, paid_to_seller, get_paid_from_buyer,
    # capital_withdrawal, capital_deposit, borrowing, loan_repayment, others
    payer_name = Column(String, nullable=True)
    receiver_name = Column(String, nullable=True)
    date = Column(Date, nullable=False)
    paying_amount = Column(Float, default=0.0)
    receiving_amount = Column(Float, default=0.0)
    entry_by = Column(String, nullable=True)


# Final Accounting Model
class FinalAccounting(Base):
    __tablename__ = "final_accounting"
    id = Column(Integer, primary_key=True, default=1)
    total_capital = Column(Float, default=0.0)
    total_loan = Column(Float, default=0.0)
    total_receivable = Column(Float, default=0.0)
    total_payable = Column(Float, default=0.0)
    total_commission = Column(Float, default=0.0)
    total_cost = Column(Float, default=0.0)

    @staticmethod
    def update_final_accounting(session):
        # Compute and update final accounting based on other tables
        total_receivable = session.query(func.sum(SellingModel.remaining_receivable_amount)).scalar() or 0.0
        total_payable = session.query(func.sum(BuyingModel.remaining_amount)).scalar() or 0.0
        total_commission = session.query(func.sum(SellerProfileModel.commission_amount)).scalar() or 0.0
        total_cost = session.query(func.sum(SellingModel.total_cost_amount)).scalar() or 0.0

        # Ensure only one record exists
        accounting = session.query(FinalAccounting).first()
        if not accounting:
            accounting = FinalAccounting()
            session.add(accounting)

        accounting.total_receivable = total_receivable
        accounting.total_payable = total_payable
        accounting.total_commission = total_commission
        accounting.total_cost = total_cost
        session.commit()

# Create a new SQLite database and session
engine = create_engine('sqlite:///business.db')  # Use your preferred database URL
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()