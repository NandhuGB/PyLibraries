'''
Scenario: Processing an Order in an E-commerce System
Problem:

In an e-commerce application, you want to process an order, apply discounts, send an email notification to the customer, and log the order details.
'''

class OrderLogger:
    def order(self, order):
        pass

        
class DiscountManager:
    def apply_discount(self, order):
        pass


class EmailManager:
    def send_email(self, order):
        pass


class OrderProcessor:
    def __init__(self, order_logger: OrderLogger, discount_manager :DiscountManager, email_manager :EmailManager):
        self.order_logger = order_logger
        self.discount_manager = discount_manager
        self.email_manager = email_manager

    def process_order(self, order):
        self.discount_manager.apply_discount(order)
        self.email_manager.send_email(order)
        self.order_logger.order(order)

