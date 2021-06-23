import pymysql

myDB=pymysql.connect(host='localhost', port=3306, user='root', passwd='', database='busbooking')
#print(myDB)
myCursor=myDB.cursor()
#print(myCursor)
