from faker import Faker
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port=3306,
  user="root",
  password="HackMeIfYouCan@37HahA",
  database="blogs"
)



if __name__ == "__main__":
    print(mydb)
    # fake = Faker('fa_IR')
    # name = fake.name()
    # address = fake.address()
    # text = fake.text()
    # print(name)