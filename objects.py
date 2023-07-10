import csv

class Item:
    pay_rate = 0.8 # price after 20% discount
    all = []

    def __init__(self, name: str, quantity: int, price: float):
        
        # run validation
        assert price >=1, f"price should not be less than 1"
        assert quantity >=0, f"quantity should not be less than 0"

        self.name = name
        self.quantity = quantity
        self.price = price

        # Add all the instances into 'all' list
        Item.all.append(self)

    # calculate the price of item
    def calculate_price(self) ->int:
        return self.quantity * self.price


    # Class method to instanciate objects from a csv file
    @classmethod
    def instanciate(cls):

        # Open csv file and read items
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        # For every item in list instanciate objects 
        for item in items:
            Item(
                name = item['name'],
                price = float(item['price']),
                quantity = int(item['quantity'])
            )
        

    # Apply discount to item's price
    def apply_discount(self):
        self.price = self.price * self.pay_rate


    def __repr__(self):
        return f"Item({self.name}, {self.quantity}, {self.price})"


class Phone(Item):

    def __init__(self, name: str, quantity: int, price: float, broken_phones = 0):
        super().__init__(
            name,quantity,price
        )
        assert broken_phones >= 0, f"Broken phones should be greater than or equl to zero"

        self.broken_phones = broken_phones

    def good_phones(self):
        return self.quantity - self.broken_phones

    def broken_phones(self):
        return None
