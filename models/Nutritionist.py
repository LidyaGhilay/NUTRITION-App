from models.Food import Food
from models.User import User

class Nutritionist:
    def __init__(self,id,name,phone_number,email):
        self.id = None
        self.name=name
        self.phone_number=phone_number
        self.email= email