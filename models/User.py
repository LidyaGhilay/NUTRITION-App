from models.Food import Food
from models.Nutritionist import Nutritionist
import sqlite3

def get_db_connection():
    return sqlite3.connect('database.db')

class User:
    tableName="userDetails"
    def __init__(self, id, name, phone_number, age):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.age = age
    
    def save(self):
        sql=f"""
I           INSERT INTO {self.tableName} (id, name, phone_number, age)
           
        """
        cursor.execute(sql,(self.name,self.phone))
        conn.commit()
        self.id = cursor.lastrowid
        
        return self
    
    def dictionary(self):
        return{
            "id": self.id,
            "name":self.name,
            "phone_number":self.age,
            "age":self.age
        }
    


    @classmethod
    def using_the_phone(cls, phone):
        sql = f"""
            SELECT * FROM {cls.TABLE_NAME}
            WHERE phone = ?
        """

        row = cursor.execute(sql, (phone,)).fetchone()

        return cls.row_to_instance(row)

    @classmethod
    def row_to_instance(cls, row):
        if row == None:
            return None

        user = cls(row[1], row[2])
        user.id = row[0]

        return user

    @classmethod
    def create_table(cls):
      sql =f"""
            CREATE TABLE IF NOT EXISTS{cls.TABLE_NAME}(
              id INTERGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              phone_number TEXT NOT NULL,
              age TEXT NOT NULL,
              )
               
                
                 
                  
                   
                    
                     
                       

