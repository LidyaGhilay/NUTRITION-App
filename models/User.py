from models.Food import Food
from models.Nutritionist import Nutritionist

class User:
    tableName="userDetails"
    def __init__(self, id, name, phone_number, age):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.age = age
    
    def save(self):
        sql="f"
           INSERT INTO {self.tableName} (name,phone)
           VALUES (?,?)
        """
        curso.execute(sql,(self.name,self.phone))
        conn.commit

