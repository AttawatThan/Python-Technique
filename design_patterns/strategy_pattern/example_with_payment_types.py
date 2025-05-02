#--------------------------------------
# Before
#--------------------------------------
from enum import Enum, auto

class PaymentType(Enum):
    CREDIT_CARD = auto()
    DEBIT_CARD = auto()
    PAYPAL = auto()

class PaymentProcessor:
    def __init__(self):
        self._payment_type = None
    
    def set_payment_type(self, payment_type: PaymentType):
        self._payment_type = payment_type
    
    def process_payment(self, amount: float):
        if self._payment_type == PaymentType.CREDIT_CARD:
            print(f"Processing credit card payment of amount {amount}")
        elif self._payment_type == PaymentType.DEBIT_CARD:
            print(f"Processing debit card payment of amount {amount}")
        elif self._payment_type == PaymentType.PAYPAL:
            print(f"Processing PayPal payment of amount {amount}")
        else:
            raise ValueError("Invalid payment type")

## Example Payment type with Credit card
# my_processor = PaymentProcessor()
# my_processor.set_payment_type(PaymentType.CREDIT_CARD)
# payment_amount_1 = 125.50
# my_processor.process_payment(payment_amount_1)



#--------------------------------------
# After used Strategy Pattern
#--------------------------------------
from abc import ABC, abstractmethod

# Payment Strategy
class PaymentStrategy(ABC):
    
    @abstractmethod
    def process_payment(self, amount: float):
        pass

class CreditCardPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount: float):
        print(f"Processing credit card payment of amount {xx}")

class DebitCardPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount: float):
        print(f"Processing debit card payment of amount {amount}")

class PaypalPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount: float):
        print(f"Processing PayPal payment of amount {amount}")

# Payment Processor
class PaymentProcessor:
    def __init__(self, payment_strategy: PaymentStrategy):
        self._payment_strategy = payment_strategy

    def process_payment(self, amount: float):
        self._payment_strategy.process_payment(amount)

## Example Payment type with Credit card
credit_card = CreditCardPaymentStrategy()
processor = PaymentProcessor(credit_card)
processor.process_payment(100.5)

