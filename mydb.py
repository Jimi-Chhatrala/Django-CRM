"""
Install MySQL on your computer
https://dev.mysql.com/downloads/installer
https://dev.mysql.com/downloads/file/?id=526408
pip install mysql
pip install mysql-connector
pip install mysql-connector-python
"""

import mysql.connector

dataBase = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = 'Admin@123'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute('CREATE DATABASE elderco')

print('All Done')