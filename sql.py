# Python program to connect
# to mysql databse


import mysql.connector


# Connecting from the server
conn = mysql.connector.connect(user='username',
                               host='localhost',
                               database='databse_name')

print(conn)

# Disconnecting from the server
conn.close()
