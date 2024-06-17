import mysql.connector
import json
class user_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="Meenusree@9",database="flask_tutorial")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection successful")
        except:
            print("Some error")

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No Data Found"

    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO users(ID,name, email, phone, role, password) VALUES( '{data['ID']}', '{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        return "User created succesfully"

    def user_update_model(self,data):
        self.cur.execute(f"UPDATE users SET ID='{data['ID']}', name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' WHERE ID={data['ID']}")
        if self.cur.rowcount>0:
            return "User created succesfully"
        else:
            return "Nothing to update"