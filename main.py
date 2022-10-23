from faker import Faker
import mysql.connector

mydb = mysql.connector.connect(
  host="fastmovie.online:3306",
  user="root",
  password="HackMeIfYouCan@37HahA"
)



if __name__ == "__main__":
    print(mydb)
    # fake = Faker('fa_IR')
    # name = fake.name()
    # address = fake.address()
    # text = fake.text()
    # print(name)