#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, initial_total=0.0):
      self.discount = discount
      self.total = initial_total
      self.items = []

  def add_item(self, title, price, quantity=1):
      self.total += price * quantity
      self.items.extend([(title, price)] * quantity)

  def apply_discount(self):
      if self.discount == 0:
          print("There is no discount to apply.")
      else:
          discount_amount = self.total * (self.discount / 100)
          discounted_total = self.total - discount_amount
          self.total = discounted_total
          print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
      if self.items:
          last_item = self.items.pop()
          last_price = last_item[1]
          self.total -= last_price
      else:
          print("No items to void.")