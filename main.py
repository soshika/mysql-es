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
    cursor.execute("SELECT id FROM users WHERE is_admin=1 ORDER BY rand() LIMIT 10;")
    users = cursor.fetchall()
    ids = [user[0] for user in users]
    return ids

def get_5_non_admins():
    cursor = db.cursor()
    cursor.execute("SELECT id FROM users WHERE is_admin=0 ORDER BY rand() LIMIT 5;")
    users = cursor.fetchall()
    ids = [user[0] for user in users]
    return ids


def create_random_post(sender_id):
    fake = Faker()

    title = str(fake.text()).split('.')[0]
    content = fake.text()

    cursor = db.cursor()
    sql = "INSERT INTO posts (title, content, sender_id) VALUES (%s, %s, %s);"
    val = (title, content, str(sender_id))
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "record inserted.")

if __name__ == "__main__":

    admin_ids = get_10_admins()
    # non_admin_ids = get_5_non_admins()

    for admin in admin_ids:
        create_random_post(admin)