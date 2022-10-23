from faker import Faker
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  port=3306,
  user="root",
  password="HackMeIfYouCan@37HahA",
  database="blogs"
)

if __name__ == "__main__":
    
    cursor = db.cursor()
    # sql = "SELECT * FROM users ;"
    # val = ("John", "Highway 21")
    # cursor.execute(sql, val)

    # db.commit()

    # print(cursor.rowcount, "record inserted.")


    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    for user in users:
        print(user)





    # fake = Faker('fa_IR')
    # name = fake.name()
    # address = fake.address()
    # text = fake.text()
    # print(name)