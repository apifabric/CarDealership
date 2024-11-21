# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class Car(Base):
    """description: Represents a car available for sale in the dealership."""
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, autoincrement=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    price = Column(Integer)


class Customer(Base):
    """description: Represents a customer who buys cars."""
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    phone_number = Column(String)


class Salesperson(Base):
    """description: Represents a salesperson working for the dealership."""
    __tablename__ = 'salespersons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    hire_date = Column(Date)
    phone_number = Column(String)


class Sale(Base):
    """description: Represents a transaction of selling a car to a customer."""
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    salesperson_id = Column(Integer, ForeignKey('salespersons.id'))
    sale_date = Column(Date)


class Service(Base):
    """description: Represents a service record for a car."""
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    service_date = Column(Date)
    description = Column(String)
    cost = Column(Integer)


class Warranty(Base):
    """description: Represents a warranty purchased for a car."""
    __tablename__ = 'warranties'

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    warranty_start_date = Column(Date)
    warranty_end_date = Column(Date)
    warranty_provider = Column(String)
    coverage_details = Column(String)


class Repair(Base):
    """description: Represents a repair performed on a car."""
    __tablename__ = 'repairs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    service_id = Column(Integer, ForeignKey('services.id'))
    repair_date = Column(Date)
    description = Column(String)
    repair_cost = Column(Integer)


class Accessory(Base):
    """description: Represents a car accessory available for sale."""
    __tablename__ = 'accessories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)


class Order(Base):
    """description: Represents an order made by a customer for accessories."""
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_date = Column(Date)


class OrderItem(Base):
    """description: Represents an item within an order, linking accessories to orders."""
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    accessory_id = Column(Integer, ForeignKey('accessories.id'))
    quantity = Column(Integer)


class Inventory(Base):
    """description: Represents inventory levels for cars and accessories at a dealership."""
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=True)
    accessory_id = Column(Integer, ForeignKey('accessories.id'), nullable=True)
    quantity_in_stock = Column(Integer)


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

from datetime import date

car1 = Car(make='Toyota', model='Corolla', year=2020, price=20000)
car2 = Car(make='Honda', model='Civic', year=2019, price=18000)
car3 = Car(make='Ford', model='Mustang', year=2021, price=30000)
car4 = Car(make='Tesla', model='Model 3', year=2021, price=35000)

customer1 = Customer(first_name='John', last_name='Doe', date_of_birth=date(1985, 5, 17), phone_number='1234567890')
customer2 = Customer(first_name='Jane', last_name='Smith', date_of_birth=date(1990, 8, 24), phone_number='0987654321')
customer3 = Customer(first_name='Jim', last_name='Beam', date_of_birth=date(1975, 3, 20), phone_number='1122334455')
customer4 = Customer(first_name='Jack', last_name='Daniels', date_of_birth=date(1980, 7, 13), phone_number='2233445566')

salesperson1 = Salesperson(first_name='Alice', last_name='Johnson', hire_date=date(2010, 6, 15), phone_number='3344556677')
salesperson2 = Salesperson(first_name='Bob', last_name='Brown', hire_date=date(2015, 2, 20), phone_number='4455667788')
salesperson3 = Salesperson(first_name='Charlie', last_name='Davis', hire_date=date(2018, 11, 5), phone_number='5566778899')
salesperson4 = Salesperson(first_name='Dana', last_name='White', hire_date=date(2020, 8, 20), phone_number='6677889900')

sale1 = Sale(car_id=1, customer_id=1, salesperson_id=1, sale_date=date(2022, 1, 10))
sale2 = Sale(car_id=2, customer_id=2, salesperson_id=2, sale_date=date(2022, 2, 15))
sale3 = Sale(car_id=3, customer_id=3, salesperson_id=3, sale_date=date(2022, 3, 20))
sale4 = Sale(car_id=4, customer_id=4, salesperson_id=4, sale_date=date(2022, 4, 25))

service1 = Service(car_id=1, service_date=date(2022, 5, 1), description='Oil Change', cost=100)
service2 = Service(car_id=2, service_date=date(2022, 6, 3), description='Tire Rotation', cost=150)
service3 = Service(car_id=3, service_date=date(2022, 7, 5), description='Brake Inspection', cost=200)
service4 = Service(car_id=4, service_date=date(2022, 8, 7), description='Battery Replacement', cost=250)

warranty1 = Warranty(car_id=1, warranty_start_date=date(2022, 1, 5), warranty_end_date=date(2024, 1, 5), warranty_provider='Provider A', coverage_details='Full Coverage')
warranty2 = Warranty(car_id=2, warranty_start_date=date(2022, 2, 10), warranty_end_date=date(2024, 2, 10), warranty_provider='Provider B', coverage_details='Basic Coverage')
warranty3 = Warranty(car_id=3, warranty_start_date=date(2022, 3, 15), warranty_end_date=date(2024, 3, 15), warranty_provider='Provider C', coverage_details='Extended Coverage')
warranty4 = Warranty(car_id=4, warranty_start_date=date(2022, 4, 20), warranty_end_date=date(2024, 4, 20), warranty_provider='Provider D', coverage_details='Limited Coverage')

repair1 = Repair(service_id=1, repair_date=date(2022, 5, 2), description='Engine Repair', repair_cost=300)
repair2 = Repair(service_id=2, repair_date=date(2022, 6, 4), description='Transmission Fix', repair_cost=400)
repair3 = Repair(service_id=3, repair_date=date(2022, 7, 6), description='Air Conditioning Repair', repair_cost=500)
repair4 = Repair(service_id=4, repair_date=date(2022, 8, 8), description='Windshield Repair', repair_cost=600)

accessory1 = Accessory(name='GPS Navigation System', price=250)
accessory2 = Accessory(name='Roof Rack', price=120)
accessory3 = Accessory(name='Car Cover', price=80)
accessory4 = Accessory(name='Sunshade', price=40)

order1 = Order(customer_id=1, order_date=date(2022, 9, 1))
order2 = Order(customer_id=2, order_date=date(2022, 10, 15))
order3 = Order(customer_id=3, order_date=date(2022, 11, 20))
order4 = Order(customer_id=4, order_date=date(2022, 12, 25))

order_item1 = OrderItem(order_id=1, accessory_id=1, quantity=2)
order_item2 = OrderItem(order_id=2, accessory_id=2, quantity=1)
order_item3 = OrderItem(order_id=3, accessory_id=3, quantity=3)
order_item4 = OrderItem(order_id=4, accessory_id=4, quantity=4)

inventory1 = Inventory(car_id=1, quantity_in_stock=5)
inventory2 = Inventory(accessory_id=1, quantity_in_stock=10)
inventory3 = Inventory(car_id=2, quantity_in_stock=3)
inventory4 = Inventory(accessory_id=2, quantity_in_stock=8)



session.add_all([car1, car2, car3, car4, customer1, customer2, customer3, customer4, salesperson1, salesperson2, salesperson3, salesperson4, sale1, sale2, sale3, sale4, service1, service2, service3, service4, warranty1, warranty2, warranty3, warranty4, repair1, repair2, repair3, repair4, accessory1, accessory2, accessory3, accessory4, order1, order2, order3, order4, order_item1, order_item2, order_item3, order_item4, inventory1, inventory2, inventory3, inventory4])
session.commit()
