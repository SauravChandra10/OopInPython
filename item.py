import csv

class Item:
    # class level attributes 
    pay_rate = 0.8

    all = []

    def __init__(self,name:str,price:float,quantity=0):
        # Run validation on recieved arguments 
        assert price>=0, f"Price {price} is not positive"
        assert quantity>=0, f"Quantity {quantity} is not positive"
        
        # Assing to self objects
        # __ makes attributes private
        self.__name=name
        self.price=price
        self.quantity=quantity
        
        # actions to execute
        Item.all.append(self)
    
    @property
    # Property decorator = Read-Only Attribute 
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,newName):
        if len(newName) > 10:
            raise Exception("This name is too long!")
        else:
            self.__name = newName

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # This method is called upon the class itself, not on any instance of a class
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items  = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def check_integer(num):
        # count out the float which are point zero
        if isinstance(num,float):
            # count out floats which are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}',{self.price},{self.quantity})"