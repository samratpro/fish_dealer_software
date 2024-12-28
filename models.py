from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# Association table for many-to-many relationship between Seller and Buyer via Dealer
association_table = Table('association', Base.metadata,
    Column('seller_id', Integer, ForeignKey('seller.id')),
    Column('buyer_id', Integer, ForeignKey('buyer.id')),
    Column('dealer_id', Integer, ForeignKey('dealer.id')),
)

# Seller Model
class Seller(Base):
    __tablename__ = 'seller'

    id = Column(Integer, primary_key=True, autoincrement=True)
    voucher_no = Column(String)
    seller_name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    address = Column(String)
    phone = Column(String)
    sell_amount = Column(Integer)
    commission_amount = Column(Float)
    total_cost_amount = Column(Integer)
    get_paid_amount = Column(Integer)
    remaining_get_paid_amount = Column(Integer)

    # Many-to-many relationship with Buyer through Dealer
    buyers = relationship('Buyer', secondary=association_table, back_populates='sellers')
    dealers = relationship('Dealer', back_populates='seller')
    entry_by = Column(String)

    def __repr__(self):
        return f"<Seller(name={self.seller_name}, voucher_no={self.voucher_no})>"

# Buyer Model
class Buyer(Base):
    __tablename__ = 'buyer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    voucher_no = Column(String)
    date = Column(Date, nullable=False)
    buyer_name = Column(String, nullable=False)
    fish_name = Column(String)
    fish_rate = Column(String)
    raw_rate = Column(String)
    final_rate = Column(String)
    buying_amount = Column(Integer)
    paid_amount = Column(Integer)
    remaining_amount = Column(Integer)

    # Many-to-many relationship with Seller through Dealer
    sellers = relationship('Seller', secondary=association_table, back_populates='buyers')
    dealers = relationship('Dealer', back_populates='buyer')
    entry_by = Column(String)

    def __repr__(self):
        return f"<Buyer(name={self.buyer_name}, voucher_no={self.voucher_no})>"

# Dealer Model
class Dealer(Base):
    __tablename__ = 'dealer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    entry_name = Column(String)
    date = Column(Date, nullable=False)
    paying_amount = Column(Integer)
    receiving_amount = Column(Integer)
    commission_amount = Column(Float)

    # Foreign key references to Seller and Buyer
    seller_id = Column(Integer, ForeignKey('seller.id'))
    buyer_id = Column(Integer, ForeignKey('buyer.id'))

    # Define relationships to Seller and Buyer
    seller = relationship('Seller', back_populates='dealers')
    buyer = relationship('Buyer', back_populates='dealers')

    # Additional fields
    seller_name = Column(String)
    buyer_name = Column(String)
    entry_by = Column(String)
    def __repr__(self):
        return f"<Dealer(entry_name={self.entry_name}, seller_name={self.seller.seller_name}, buyer_name={self.buyer.buyer_name})>"

# Create a new SQLite database and session
engine = create_engine('sqlite:///business.db')  # Use your preferred database URL
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()