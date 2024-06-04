import mysql.connector

from tabulate import tabulate

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="bank_management"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE new_account_detail ( cust_id int NOT NULL, name varchar(45) DEFAULT NULL, email varchar(45) DEFAULT NULL, aadhar varchar(45) DEFAULT NULL, PRIMARY KEY (`cust_id`))")


sql = "INSERT INTO new_account_detail (cust_id, name, email, aadhar) VALUES (%s, %s, %s, %s)"
val = (3, "Naru", "test@hotmail.com", "123434")
mycursor.execute(sql, val)

mycursor.execute("SELECT * FROM new_account_detail")

myresult = mycursor.fetchall()

headers = ["cust_id", "name", "email", "aadhar"]

for x in myresult:
  print(tabulate(myresult, headers, tablefmt="plain"))

mydb.commit()

print(mycursor.rowcount, "record inserted.")