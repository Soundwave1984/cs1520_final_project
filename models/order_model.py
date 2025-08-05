from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    orders = Column(Text, nullable=False)  # Comma-separated order items
    table_number = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"<Order(id={self.id}, customer='{self.customer_name}', table={self.table_number})>"