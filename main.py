from faker import Faker
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  port=3306,
  user="root",
  password="HackMeIfYouCan@37HahA",
  database="blogs"
)


def get_10_admins():
    cursor = db.cursor()
    cursor.execute("SELECT id FROM users WHERE is_admin=1 LIMIT 10;")
    users = cursor.fetchall()
    ids = [user[0] for user in users]
    return ids


if __name__ == "__main__":

    admin_ids = get_10_admins()
    for id in admin_ids:
        print(id)

    # fake = Faker('fa_IR')
    # name = fake.name()
    # address = fake.address()
    # text = fake.text()
    # print(name)