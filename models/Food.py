from models.Nutritionist import Nutritionist
from models.User import User

class Food:
    def __init__(self,id,name,category,calories,description):
        self.id = None
        self.name=name
        self.category=category
        self.description=description
        self.calories=calories