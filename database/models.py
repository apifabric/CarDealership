# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 21, 2024 10:47:54
# Database: sqlite:////tmp/tmp.FjQCHN3eKc-01JD75AH1200Z2G7BQW27VC4HW/CarDealership/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Accessory(SAFRSBaseX, Base):
    """
    description: Represents a car accessory available for sale.
    """
    __tablename__ = 'accessories'
    _s_collection_name = 'Accessory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="accessory")
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="accessory")



class Car(SAFRSBaseX, Base):
    """
    description: Represents a car available for sale in the dealership.
    """
    __tablename__ = 'cars'
    _s_collection_name = 'Car'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    price = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="car")
    SaleList : Mapped[List["Sale"]] = relationship(back_populates="car")
    ServiceList : Mapped[List["Service"]] = relationship(back_populates="car")
    WarrantyList : Mapped[List["Warranty"]] = relationship(back_populates="car")



class Customer(SAFRSBaseX, Base):
    """
    description: Represents a customer who buys cars.
    """
    __tablename__ = 'customers'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    phone_number = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    SaleList : Mapped[List["Sale"]] = relationship(back_populates="customer")



class Salesperson(SAFRSBaseX, Base):
    """
    description: Represents a salesperson working for the dealership.
    """
    __tablename__ = 'salespersons'
    _s_collection_name = 'Salesperson'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    hire_date = Column(Date)
    phone_number = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    SaleList : Mapped[List["Sale"]] = relationship(back_populates="salesperson")



class Inventory(SAFRSBaseX, Base):
    """
    description: Represents inventory levels for cars and accessories at a dealership.
    """
    __tablename__ = 'inventory'
    _s_collection_name = 'Inventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    car_id = Column(ForeignKey('cars.id'))
    accessory_id = Column(ForeignKey('accessories.id'))
    quantity_in_stock = Column(Integer)

    # parent relationships (access parent)
    accessory : Mapped["Accessory"] = relationship(back_populates=("InventoryList"))
    car : Mapped["Car"] = relationship(back_populates=("InventoryList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: Represents an order made by a customer for accessories.
    """
    __tablename__ = 'orders'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'))
    order_date = Column(Date)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="order")



class Sale(SAFRSBaseX, Base):
    """
    description: Represents a transaction of selling a car to a customer.
    """
    __tablename__ = 'sales'
    _s_collection_name = 'Sale'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    car_id = Column(ForeignKey('cars.id'))
    customer_id = Column(ForeignKey('customers.id'))
    salesperson_id = Column(ForeignKey('salespersons.id'))
    sale_date = Column(Date)

    # parent relationships (access parent)
    car : Mapped["Car"] = relationship(back_populates=("SaleList"))
    customer : Mapped["Customer"] = relationship(back_populates=("SaleList"))
    salesperson : Mapped["Salesperson"] = relationship(back_populates=("SaleList"))

    # child relationships (access children)



class Service(SAFRSBaseX, Base):
    """
    description: Represents a service record for a car.
    """
    __tablename__ = 'services'
    _s_collection_name = 'Service'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    car_id = Column(ForeignKey('cars.id'))
    service_date = Column(Date)
    description = Column(String)
    cost = Column(Integer)

    # parent relationships (access parent)
    car : Mapped["Car"] = relationship(back_populates=("ServiceList"))

    # child relationships (access children)
    RepairList : Mapped[List["Repair"]] = relationship(back_populates="service")



class Warranty(SAFRSBaseX, Base):
    """
    description: Represents a warranty purchased for a car.
    """
    __tablename__ = 'warranties'
    _s_collection_name = 'Warranty'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    car_id = Column(ForeignKey('cars.id'))
    warranty_start_date = Column(Date)
    warranty_end_date = Column(Date)
    warranty_provider = Column(String)
    coverage_details = Column(String)

    # parent relationships (access parent)
    car : Mapped["Car"] = relationship(back_populates=("WarrantyList"))

    # child relationships (access children)



class OrderItem(SAFRSBaseX, Base):
    """
    description: Represents an item within an order, linking accessories to orders.
    """
    __tablename__ = 'order_items'
    _s_collection_name = 'OrderItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'))
    accessory_id = Column(ForeignKey('accessories.id'))
    quantity = Column(Integer)

    # parent relationships (access parent)
    accessory : Mapped["Accessory"] = relationship(back_populates=("OrderItemList"))
    order : Mapped["Order"] = relationship(back_populates=("OrderItemList"))

    # child relationships (access children)



class Repair(SAFRSBaseX, Base):
    """
    description: Represents a repair performed on a car.
    """
    __tablename__ = 'repairs'
    _s_collection_name = 'Repair'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    service_id = Column(ForeignKey('services.id'))
    repair_date = Column(Date)
    description = Column(String)
    repair_cost = Column(Integer)

    # parent relationships (access parent)
    service : Mapped["Service"] = relationship(back_populates=("RepairList"))

    # child relationships (access children)
