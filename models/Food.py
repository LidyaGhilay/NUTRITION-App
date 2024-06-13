from models.Nutritionist import Nutritionist
from models.User import User

class Food:
    def __init__(self,id,name,category,calories,description,Nutri_id):
        self.id = None
        self.name=name
        self.category=category
        self.description=description
        self.calories=calories
        self.Nutri_id =Nutri_id