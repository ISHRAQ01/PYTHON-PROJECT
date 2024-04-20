#INVENTORY MANAGEMENT
import os
import mysql.connector
import datetime
now=datetime.datetime.now()

def product_mgmt():
    while True:
        print("\t\t\t 1.Add New product")
        print("\t\t\t 2.List product")
        print("\t\t\t 3.Search product")
        print("\t\t\t 4.Update product")
        print("\t\t\t 5.Delete product")
        print("\t\t\t 6.back(main menu)")
        p=int(input("\t\t Enter Your Choice:"))
        if p==1:
            add_product()
        if p==2:
            list_product()
        if p==3:
            search_product()
        if p==4:
            update_product()
        if p==5:
            delete_product()
        if p==6:
            break


def purchase_mgmt():
    while True:
        print("\t\t\t 1.Add Order")
        print("\t\t\t 2.List order")
        print("\t\t\t 3.Back(main menu)")
        o=int(input("\t\t Enter your choice:"))
        if o==1:
            add_order()
        if o==2:
            list_orders()
        if o==3:
            break
        
def sales_mgmt():
    while True:
        print("\t\t\t 1.Sales Items")
        print("\t\t\t 2.List Sales")
        print("\t\t\t 3.Back(main menu)")
        s=int(input("\t\tEnter Your Choice:"))
        if s==1:
            sale_product()
        if s==2:
            list_sale()
        if s==3:
            break
def user_mgmt():
    while True:
        print("\t\t\t 1.Add user")
        print("\t\t\t 2.List user")
        print("\t\t\t 3.Back(main menu)")
        u=int(input("\t\t Enter Your Choice:"))
        if u==1:
            add_user()
        if u==2:
            list_user()
        if u==3:
            break
def create_database():
    mydb = mysql.connector.connect(host="localhost", user="root", password="123456",auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    print("DATABASE CREATED")
    mycursor.execute("CREATE DATABASE IF NOT EXISTS stock;")
    mycursor.execute("USE stock;")
    print("Creating PRODUCT table")
    sql = "CREATE TABLE if not exists product(pcode int(4) PRIMARY KEY, pname char(30) NOT NULL, price float(8,2),pqty int(4), pcat varchar(30));"
    mycursor.execute(sql)
    print("Creating ORDER table")
    sql = "CREATE TABLE if not exists orders(orderid int(4)PRIMARY KEY,orderdate DATE,pcode char(30) NOT NULL,pprice float(8,2),pqty int(4),supplier char(50),pcat char(30));"
    mycursor.execute(sql)
    print("ORDER table created")
    print("CREATING SALEStable")
    sql = "CREATE TABLE if not exists sales(salesid int(4)PRIMARY KEY, salesdate DATE,pcode char(30)references product(pcode),pprice float(8,2),pqty int(4),total double(8,2));"
    mycursor.execute(sql)
    print("SALES table created")
    print("creating usertable")
    sql = "CREATE TABLE if not exists user(uid varchar(6)PRIMARY KEY,uname varchar(30) NOT NULL,upwd varchar(30));"
    mycursor.execute(sql)
    print("USER table created")
def list_database():
    mydb = mysql.connector.connect(host="localhost",user="root",password="123456",auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    database=mycursor.fetchall()
    database_name=[db[0] for db in database]
    print("DATABASES ARE:",database_name)
    if("stock" in database_name):
        mycursor.execute("use stock")
        print("TABLE OF STOCKS ARE:")
        sql="show tables"
        mycursor.execute(sql)
        for i in mycursor:
            print(i[0])
    else:
        print("DATABASE STOCK IS NOT CREATED YET.")
def add_order():
    mydb=mysql.connector.connect(host="localhost", user="root", password="123456", database="stock",auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    now=datetime.datetime.now()
    sql="INSERT INTO orders(orderid,orderdate,pcode,pprice,pqty,supplier,pcat) values(%s,%s,%s,%s,%s,%s,%s)"
    oid=now.year+now.month+now.day+now.hour+now.minute+now.second
    code=int(input("enter product code:"))
    pprice=float(input("enter product unit price:"))
    qty=int(input("enter product quantity:"))
    supplier=input("enter supplier details:")
    cat=input("enter product category:")
    val=(oid,now,code,pprice,qty,supplier,cat)
    mycursor.execute(sql,val)
    mydb.commit()
def list_orders():
    mydb=mysql.connector.connect(host="localhost", user="root", password="123456", database="stock",auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    sql="SELECT * from orders;"
    mycursor.execute(sql)
    print("\t\t\t\t\t\t\t ORDER DETAILS")
    print("-"*85)
    print("orderid date  productcode  price  quantity  supplier  category")
    print("-"*85)
    for i in mycursor:
        print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5],"\t",i[6])
    print("-"*85)
def db_mgmt():
    while True:
        print("\t\t\t 1.database creation")
        print("\t\t\t 2.list database")
        print("\t\t\t 3.back(main menu)")
        p=int(input("\t\t enter your choice:"))
        if p==1:
            create_database()
        if p==2:
            list_database()
        if p==3:
            break
def add_product():
    mydb=mysql.connector.connect(host="localhost", user="root", password="123456", database="stock",auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    sql="INSERT INTO product(pcode,pname,price,pqty,pcat) values(%s,%s,%s,%s,%s)"
    pcode=int(input("\t\t enter product code:"))
    search="SELECT count(*) FROM product WHERE pcode=%s"
    val=(pcode,)
    mycursor.execute(search,val)
    for x in mycursor:
        cnt=x[0]
    if cnt==0:
        pname=input("\t\t enter product name:")
        pqty=int(input("\t\t enter product quantity:"))
        price=float(input("\t\t enter product unit price:"))
        pcat=input("\t\t enter product category:")
        sql="INSERT INTO product(pcode,pname,price,pqty,pcat) values(%s,%s,%s,%s,%s)"
        val=(pcode,pname,price,pqty,pcat)
        mycursor.execute(sql,val)
        mydb.commit()
    else:
        print("\t\t product already exist")
def update_product():
    mydb=mysql.connector.connect(host="localhost", user="root", password="123456", database="stock",auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    code=int(input("enter the product code:"))
    qty=int(input("enter the quantity:"))
    sql="UPDATE product SET pqty=pqty+%s WHERE pcode=%s;"
    val=(qty,code)
    mycursor.execute(sql,val)
    mydb.commit()
    print("\t\t product details updated")
def delete_product():
    mydb=mysql.connector.connect(host="localhost", user="root", password="123456", database="stock",auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    code=int(input("\t\t enter product code:"))
    sql="DELETE FROM product WHERE pcode=%s;"
    val=(code,)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"record(s) deleted");
def search_product():
    while True:
        print("\t\t\t 1.list all product")
        print("\t\t\t 2.List product code wise")
        print("\t\t\t 3.list product category wise")
        print("\t\t\t 4.Back(main menu)")
        u=int(input("\t\t Enter Your Choice:"))
        if u==1:
            list_product()
        if u==2:
            code=int(input("enter product code:"))
            list_prcode(code)
        if u==3:
            cat=input("enter category:")
            list_prcat(cat)
        if u==4:
            break
def list_product():
    mydb=mysql.connector.connect(host="localhost", user="root", password="123456", database="stock",auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    sql="SELECT * FROM PRODUCT"
    mycursor.execute(sql)
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t","-"*47)
    print("\t\t code name price quantity category")
    print("\t\t","-"*47)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4])
        print("\t\t","-"*47)
def list_prcode(code):
    mydb=mysql.connector.connect(host="localhost", user="root", password="123456", database="stock",auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    sql="SELECT * FROM product WHERE pcode=%s;"
    val=(code,)
    mycursor.execute(sql,val)
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t","-"*47)
    print("\t\t code name price quantity category")
    print("\t\t","-"*47)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4])
        print("\t\t","-"*47)
def sale_product():
    mydb = mysql.connector.connect(host="localhost", user="root", password="123456", database="stock", auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    now=datetime.datetime.now()
    pcode = input("enter product code:")
    # Check if product exists
    sql = "SELECT count(*) FROM product WHERE pcode=%s"
    val = (pcode,)
    mycursor.execute(sql, val)
    for x in mycursor:
        cnt=x[0]
        if cnt != 0:
         # Fetch product details
         sql = "SELECT pcode, pname, price, pqty, pcat FROM product WHERE pcode=%s"
         val = (pcode,)
         mycursor.execute(sql, val)
         print("\t\t\t\t PRODUCT DETAILS")
         print("\t\t","-"*47)
         print("\t\t code name price quantity category")
         print("\t\t","-"*47)
         for i in mycursor:
            print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4])
            print("\t\t","-"*47)
            #PRODUCT TO SELL
            price = i[2]
            pqty = i[3]
            qty = int(input("Enter quantity to sell: "))
            if qty <= pqty:
                total = qty * price
                print("Total Amount: Rs.", total)
                # Update sales table
                sql = "INSERT INTO sales (salesid,salesdate,pcode,pprice,pqty,total) VALUES (%s,%s,%s,%s,%s,%s)"
                salesid=now.year+now.month+now.day+now.hour+now.minute+now.second
                val = (salesid,now,pcode,price,qty,total)
                mycursor.execute(sql,val)
                # Update product quantity
                sql = "UPDATE product SET pqty=pqty-%s WHERE pcode = %s"
                val = (qty,pcode)
                mycursor.execute(sql,val)
                print("Items sold")
                mydb.commit()
            else:
                print("Not enough quantity available.")
        else:
            print("Product does not exist.")
def add_user():
    mydb=mysql.connector.connect(host="localhost", user="root", password="123456", database="stock",auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    uid=input("enter id:")
    name=input("enter name:")
    password=input("enter password:")
    sql="INSERT INTO user(uid,uname,upwd) values(%s,%s,%s)"
    val=(uid,name,password)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"user created")

def list_user():
    mydb=mysql.connector.connect(host="localhost", user="root", password="123456", database="stock",auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    sql="SELECT uid,uname from user"
    mycursor.execute(sql)
    clrscr()
    print("\t\t\t\t USER DETAILS")
    print("\t\t","-"*27)
    print("\t\t UID    name  ")
    print("\t\t","-"*27)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1])
        print("\t\t","-"*27)

def list_sale():
    mydb=mysql.connector.connect(host="localhost",user="root",password="123456",database="stock",auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    sql="SELECT*FROM sales"
    mycursor.execute(sql)
    print("\t\t\t\t SALES DETAILS")
    print("_"*80)
    print("salesID Date ProductCode Price Quantity Total")
    print("_ "*80)
    for x in mycursor:
        print(x[0],"\t",x[1],"\t",x[2],"\t",x[3],"\t\t",x[4],"\t\t",x[5])
        print("-"*80)
def list_prcat(cat):
    mydb=mysql.connector.connect(host="localhost",user="root",password="123456",database="stock",auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    sql="SELECT* FROM PRODUCT WHERE pcat =%s"
    val=(cat,)
    mycursor.execute(sql,val)
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t","-"*47)
    print("\t\t code name price quantity category")
    print("\t\t","-"*47)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4])
        print("\t\t","-"*47)


def clrscr():
    print("\n"*5)
#main function
while True:
    clrscr()
    print("\t\t\t STOCK MANAGEMENT")
    print("\t\t\t***************\n")
    print("\t\t1. PRODUCT MANAGEMET")
    print("\t\t2. PURCHASE MANAGEMENT")
    print("\t\t3. SALES MANAGEMENT")
    print("\t\t4. USER MANGEMENT")
    print("\t\t5. DATABASE SETUP")
    print("\t\t6.  EXIT\n")
    n =int(input("enter your choice:"))
    if n==1:
        product_mgmt()
    if n==2:
        os.system('cls')
        purchase_mgmt()
    if n==3:
        sales_mgmt()
    if n==4:
        user_mgmt()
    if n==5:
        db_mgmt()
    if n==6:
         break
