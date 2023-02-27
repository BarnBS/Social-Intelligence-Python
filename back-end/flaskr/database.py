import mysql.connector

import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

db = mysql.connector.connect(
    host = "localhost",
    user = os.getenv("DB_USER"),
    passwd = os.getenv("DB_PASSWORD"),
    database = "maindatabase"
)

dbcursor = db.cursor()

# dbcursor.execute("CREATE TABLE user (user_id int PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50) NOT NULL, email VARCHAR(200) NOT NULL UNIQUE)")
# dbcursor.execute("DESCRIBE user")
# for x in dbcursor :
#     print(x)