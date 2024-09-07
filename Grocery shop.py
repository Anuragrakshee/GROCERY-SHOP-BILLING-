from tqdm import tqdm
import time

from datetime import date
import os
import getpass

import mysql.connector as c
from mysql.connector import Error


print("\t\t\t\t\t")
pwd = getpass.getpass("Enter password:")

if pwd == 'an':
   for i in tqdm (range (100),desc="Loading…",ascii=False, ncols=10):
       time.sleep(0.01)
   cn= c.connect(host="localhost",user="root",password="12345",database="shop")
   if cn.is_connected():
    print("Connection established")
    cr=cn.cursor(buffered=True)
    while True:
        os.system('CLS')
        d=date.today()
        cr=cn.cursor(buffered=True)
        print("\t************************* GROCERY SHOP ******************************\t",d.strftime("%d/%B/%y"))
        print()
        print("\t\t\t----------#### MENU ####---------")
        print("\t\t\t|\t\t\t\t|")
        print("\t\t\t|\t1.Insert\t\t|")
        print("\t\t\t|\t2.Display\t\t|")
        print("\t\t\t|\t3.Search\t\t|")
        print("\t\t\t|\t4.Update\t\t|")
        print("\t\t\t|\t5.Sell\t\t\t|")
        print("\t\t\t|\t6.Display left list\t|")
        print("\t\t\t|\t7.Exit\t\t\t|")
        print("\t\t\t|\t\t\t\t|")
        print("\t\t\t---------------------------------")

        ch=int(input("\tEnter your choice:"))
        print()

        if ch==1:
            sqlf="insert into items values(%s,%s,%s,%s,%s,%s)"
            n=int(input("\tEnter how many items you want to add:"))
            print()
            i=1
            while i<=n:
                slno=int(input("\tEnter slno:"))
                products=input("\tEnter the product name:")
                quantity=int(input("\tEnter quantity:"))
                price=int(input("\tEnter price:"))
                manufacture=input("\tEnter manufacture date:")
                expiry=input("\tEnter expiry date:")
                cr.execute(sqlf,(slno,products,quantity,price,manufacture,expiry))
                print()
                i=i+1
                cn.commit()
        elif ch==2:
            cr.execute("select*from items")
            mytable=cr.fetchall()
            for x in mytable:
                print(x)
            print()    
        elif ch==3:
            print("\t1:Search products according to name")
            print("\t2:Search products acoording to price")
            print("\t3:Search products below  price 500")
            print("\t4:Search for products above price 500")
            print("\t5:Search for products which are available in quantity of more than 10")
            print()
            c=int(input("\tEnter your choice:"))
            print()
            if c==1:
                sqlf="select*from items where products=%s"
                products=input("\tEnter name:")
                cr.execute(sqlf,(products,))
                d=cr.rowcount
                if d==0:
                    print("\tItem not found")
               
                else:
                    rs=cr.fetchall()
                    for i in rs:
                        print(i)
                        print()
            elif c==2:
                sqlf="select*from items where price=%s"
                price=int(input("\tEnter price:"))
                cr.execute(sqlf,(price,))
                d=cr.rowcount
                if d==0:
                    print("\tItem not found")
                else:
                    rs=cr.fetchall()
                    for i in rs:
                        print(i)
                        print()
            elif c==3:
                sqlf="select*from items where price<500"
                cr.execute(sqlf)
                d=cr.rowcount
                if d==0:
                    print("\tItem not found")
                else:
                    rs=cr.fetchall()
                    for i in rs:
                        print(i)
            elif c==4:
                sqlf="select*from items where price>500"
                cr.execute(sqlf)
                d=cr.rowcount
                if d==0:
                    print("\tItem not found")
                else:
                    rs=cr.fetchall()
                    for i in rs:
                        print(i)
                        print()
            elif c==5:
                sqlf="select*from items where quantity>10"
                cr.execute(sqlf)
                d=cr.rowcount
                if d==0:
                    print("\tItem not found")
                else:
                    rs=cr.fetchall()
                    for i in rs:
                        print(i)
                print()       
            else:
               print("\t\tInvalid Input")
               print()
               
             
        elif ch==4:
            print("\tPress 1 : To update details through product number:")
            print("\tPress 2 : To update details through product name:")
            print()
            bp=int(input("\tEnter your choice:"))
            print()
            if bp==1:
               print("\tPress 1 : To change name of the product:")
               print("\tPress 2 : To change price of the product:")
               print("\tPress 3 : To change quantity of the product:")
               print()
               xp=int(input("\tEnter your choice:"))
               print()
               if xp==1:
                     slno=int(input("\tEnter product number:"))
                     products=input("\tEnter new name of the product:")
                     sqlf="update items set products=%s where slno=%s"
                     cr.execute(sqlf,(products,slno,))
                     cn.commit()
                     d=cr.rowcount
                     if d==0:
                        print("\tUpdate not done (check the product number)")
                     else:
                        print("/tUpdate done successfully")
               elif xp==2:
                     slno=int(input("\tEnter product number:"))
                     price=input("\tEnter new price of the product:")
                     sqlf="update items set price=%s where slno=%s"
                     cr.execute(sqlf,(price,slno,))
                     cn.commit()
                     d=cr.rowcount
                     if d==0:
                        print("\tUpdate not done (check the product number)")
                     else:
                        print("\tUpdate done successfully")
               elif xp==3:
                     slno=int(input("\tEnter product number:"))
                     quantity=input("\tEnter new quantity of the product:")
                     sqlf="update items set quantity=%s where slno=%s"
                     cr.execute(sqlf,(quantity,slno,))
                     cn.commit()
                     d=cr.rowcount
                     if d==0:
                        print("\tUpdate not done (check the product number)")
                     else:
                        print("\tUpdate done successfully")
               else:
                         print("\tInvalid choice entered")
            elif bp==2:
                print("\tPress 1 : To change sl number of the product")
                print("\tPress 2 : To change price of the product")
                print("\tPress 3 : To change quantity of the product")
                print()
                xp=int(input("\tEnter your choice:"))
                print()
                if xp==1:
                    products=input("\tEnter name of the product:")
                    slno=int(input("\tEnter new sl number of the product:"))
                    sqlf="update items set slno=%s where products=%s"
                    cr.execute(sqlf,(slno,products,))
                    cn.commit()
                    d=cr.rowcount
                    if d==0:
                        print("\tUpdate not done (check the product name)")
                    else:
                        print("\tUpdate done successfully")
                elif xp==2:
                    products=input("\tEnter name of the product :")
                    price=input("\tEnter new price of the product:")
                    sqlf="update items set price=%s where products=%s"
                    cr.execute(sqlf,(price,products,))
                    cn.commit()
                    d=cr.rowcount
                    if d==0:
                        print("\tUpdate not done (check the product name)")
                        print()
                    else:
                        print("\tUpdate done successfully")
                        print()
                elif xp==3:
                    products=input("\tEnter name of the product :")
                    quantity=input("\tEnter new quantity of the product:")
                    sqlf="update items set quantity=%s where products=%s"
                    cr.execute(sqlf,(quantity,products,))
                    cn.commit()
                    d=cr.rowcount
                    if d==0:
                       print("\tUpdate not done (check the product name)")
                       print()
                    else:
                       print("\tUpdate done successfully")
                       print()
            else:
                print("\tInvalid choice entered")                   
      
        elif ch==5:
            k=10
            i=1
            while i<=1:
                products=input("\tEnter product name:")
                quantity=int(input("\tEnter new quantity:"))
                p=(k-quantity)
                if p<=0:
                    print("\tOut of stock")
                    w=input("\tPress 1 to continue:")
                    print()
                    if w==1:
                        i=1           
                    else:
                        i=i+1                
                else:               
                    sqlf="update items set quantity=%s where products=%s"
                    cr.execute(sqlf,(p,products))       
                    cn.commit()
                    k=p           
                    w=input("\tPress 1 to continue:")
                    print()
                    if w==1:
                        i=1           
                    else:
                        i=i+1           
        elif ch==6:
            cr.execute("select*from items")
            mytable=cr.fetchall()
            for x in mytable:
                print(x)
                cr.close()            
        elif ch==7:
            break
        else:
            print("\tInvalid choice")
            print()
        input("\tEnter any key to come back.....")
 
else:
    print("\tThe password you entered is incorrect.")


