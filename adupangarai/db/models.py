from sqlalchemy import (
    String,
    ForeignKey,
    DateTime,
    Column,
    Boolean,
    Integer,
    Enum
)
from datetime import datetime, timezone
from adupangarai.db.common_enum import Category, Unit
from adupangarai.db.session import Base, engine
from sqlalchemy.orm import relationship

class AccountModel(Base):
    __tablename__ = "account"
    
    id = Column(String(256), primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    users = relationship("User", back_populates="account")
    inventory = relationship("InventoryModel", back_populates="account_inventory")


class User(Base):
    __tablename__ = "user_account"
    
    id = Column(String(256), primary_key=True, index=True)
    account_id = Column(String(256), ForeignKey("account.id"), nullable=False)
    name = Column(String(256), nullable=False)
    email = Column(String(256), index=True, nullable=False)
    phone_number = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    notification_enabled = Column(Boolean, default=False)
    avatar_url = Column(String(512), nullable=True)

    account = relationship("AccountModel", back_populates="users")
    user_inventory = relationship("InventoryModel", back_populates="created_by_user")


class InventoryModel(Base):
    __tablename__ = "inventory"
    
    id = Column(String(256), primary_key=True, index=True)
    account_id = Column(String(256), ForeignKey("account.id"), nullable=False)
    name = Column(String(256), nullable=False)
    image_url = Column(String(512), nullable=True)
    category = Column(Enum(Category), nullable=False)
    unit = Column(Enum(Unit), nullable=False)
    quantity = Column(Integer, default=0)
    threshold = Column(Integer, default=0)
    expiry_date = Column(DateTime, nullable=True)
    alert_enabled = Column(Boolean, default=False)
    created_by = Column(String(256), ForeignKey("user_account.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    account_inventory = relationship("AccountModel", back_populates="inventory")
    created_by_user = relationship("User", back_populates="user_inventory")

Base.metadata.create_all(bind=engine)