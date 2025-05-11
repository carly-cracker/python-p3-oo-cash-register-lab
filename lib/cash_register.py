#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0,):
        self.discount= discount
        self.total= 0
        self.items = []
        self.previous_transaction = 0

    def add_item(self,title,price,quantity=1):
        self.total += price * quantity
        self.previous_transaction = price*quantity
        self.title = title
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
          self.total = self.total * (1 - self.discount /100)
          print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.previous_transaction