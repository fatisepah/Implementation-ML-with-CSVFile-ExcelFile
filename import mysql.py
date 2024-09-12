import mysql.connector


# اتصال به دیتابیس MySQL
print("connecting to db")
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    port=3306,
    database="university"
)
print("connected to db")
# ایجاد یک cursor برای اجرای دستورات SQL
cursor = conn.cursor()

###########################################################
# تعریف دستور SQL برای ایجاد جدول
#create_table_query = '''
#CREATE TABLE Student (
#    id INT AUTO_INCREMENT PRIMARY KEY,
#    first_name VARCHAR(50),
#    last_name VARCHAR(50),
#    NumStudent VARCHAR(50)
#)
#'''

# اجرای دستور برای ساخت جدول
#cursor.execute(create_table_query)
#
#create_table_query = '''
#CREATE TABLE course (
#    id INT AUTO_INCREMENT PRIMARY KEY,
#    Name VARCHAR(50),
#    NumVahed INT
#)
#'''
## اجرای دستور برای ساخت جدول
#cursor.execute(create_table_query)

##########################################################

# اجرای دستور SHOW TABLES
cursor.execute("SHOW TABLES")

# دریافت و چاپ لیست جداول
tables = cursor.fetchall()

for table in tables:
    print(table[0])
##########################################################

# دستور SQL برای اضافه کردن یک سطر به جدول course
insert_query = '''
INSERT INTO course (Name, NumVahed)
VALUES (%s, %s)
'''

# مقادیر برای اضافه کردن به جدول
values = ("SOC", 3)

# اجرای دستور INSERT
cursor.execute(insert_query, values)
###########################################################
# دستور SQL برای انتخاب تمامی مقادیر جدول course
select_query = "SELECT * FROM course"

# اجرای دستور SELECT
cursor.execute(select_query)

# دریافت تمامی سطرهای جدول
#rows = cursor.fetchall()

# نمایش مقادیر جدول
#for row in rows:
#    print(row)
###########################################################
for (id,name,numVahed) in cursor:
    print('course %s is %i vahed'%(name,numVahed))
###########################################################
# دستور SQL برای حذف جدول
#drop_table_query = "DROP TABLE employees"

# اجرای دستور DROP TABLE
#cursor.execute(drop_table_query)
###########################################################

###########################################################
conn.commit()
# اجرای دستور SHOW TABLES
cursor.execute("SHOW TABLES")

# دریافت و چاپ لیست جداول
tables = cursor.fetchall()

for table in tables:
    print(table[0])
##########################################################


# بستن cursor و اتصال
cursor.close()
conn.close()
