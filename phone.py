from item import Item

class Phone(Item):

    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):
        # calling super function to access attributes/methods of parent class
        super().__init__(
            name,price,quantity
        )

        # Run validation on recieved arguments 
        assert broken_phones>=0, f"Quantity {broken_phones} is not positive"
        
        # Assing to self objects
        self.broken_phones=broken_phones
    
    def __repr__(self):
        return f"{__class__.__name__}('{self.name}',{self.price},{self.quantity},{self.broken_phones})"