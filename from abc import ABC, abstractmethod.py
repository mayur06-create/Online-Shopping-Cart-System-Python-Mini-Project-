from abc import ABC, abstractmethod

# Product Class
class Product:
    def __init__(self, product_id, name, price):
        self.__product_id = product_id   # Encapsulation
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def display_product(self):
        print(f"{self.__name} - ₹{self.__price}")
        
# Cart Class
class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("Product added to cart")

    def get_total(self):
        total = 0
        for product in self.products:
            total += product.get_price()
        return total
        
# Order Class
class Order:
    def __init__(self, order_id, cart):
        self.order_id = order_id
        self.cart = cart

    def get_order_amount(self):
        return self.cart.get_total()
        
# User (Abstract Class)
class User(ABC):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    @abstractmethod
    def display_role(self):
        pass

# Customer Class
class Customer(User):
    def display_role(self):
        print("Role: Customer")

# Payment Interface
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Credit Card Payment
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Payment of ₹{amount} done using Credit Card")

# UPI Payment
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Payment of ₹{amount} done using UPI")

# Main Program (Execution)
def main():
    print("---- Online Shopping Cart System ----\n")

    # Create Customer
    customer = Customer("C101", "Mayur")
    customer.display_role()

    # Create Products
    product1 = Product("P1", "Laptop", 50000)
    product2 = Product("P2", "Mouse", 500)

    # Create Cart and add products
    cart = Cart()
    cart.add_product(product1)
    cart.add_product(product2)

    # Create Order
    order = Order("ORD001", cart)
    amount = order.get_order_amount()

    print(f"\nTotal Order Amount: ₹{amount}")

    # Payment (Polymorphism)
    payment = CreditCardPayment()   # Change to UPIPayment()
    payment.pay(amount)

    print("\nOrder placed successfully!")


# Program Entry Point
if __name__ == "__main__":
    main()

