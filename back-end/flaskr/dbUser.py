import mysql.connector

import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

dbUser = mysql.connector.connect(
    host = "localhost",
    user = os.getenv("DBUSERS_USER"),
    passwd = os.getenv("DBUSERS_PASSWORD")
)