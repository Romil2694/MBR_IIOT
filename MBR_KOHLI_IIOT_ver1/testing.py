from django.http import HttpResponse
import mysql.connector
from django.http import JsonResponse

datacollector = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="mbr"
    )
mydata = datacollector.cursor()
mydata.execute("SELECT * FROM kohli_els")
realdata = mydata.fetchall()
ourdata = realdata[0]
sp = ourdata[4]
print(realdata)
print(sp)