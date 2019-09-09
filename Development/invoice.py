from random import randint
from stock1 import stock
import datetime
def invoice():
    l=[]
    b=stock()
    new_filename = str(randint(0,5000))
    file=open(new_filename+".txt","w")
    file.write("                    Gadget STORE                ")
    file.write('\n')
    file.write("                     KATHMANDU NEPAL                         ")
    file.write('\n')
    file.write("                     CONTACT NUMBER: 014114297              ")
    file.write('\n')
    file.write("                     Fax number: 977-454637                ")
    file.write('\n')
    file.write("                     EMAIL:infogadget@starmail.com.np              ")
    file.write('\n')
    file.write("                     VAT NUMBER : 001345                    ")
    file.write('\n')
    file.write("                                             INVOICE NUMBER:"+str (randint(1,500)))
    file.write('\n')
    file.write("Date:")
    file.write(str(datetime.datetime.now().year))
    file.write('/')
    file.write(str(datetime.datetime.now().month))
    file.write('/')
    file.write(str(datetime.datetime.now().day))
    file.write('\t')
    file.write('\n')
    file.write("Time:")
    file.write(str(datetime.datetime.now().hour))
    file.write(':')
    file.write(str(datetime.datetime.now().minute))
    file.write(':')
    file.write(str(datetime.datetime.now().second))
    file.write('\n')
    name= input ("enter customer name:")
    file.write(str("customer name:"+name.upper()))
    file.write('\n')
    
    file.write('\n')
    total=0
    
    net=0
    more_product="y"
    while more_product=="y":
        pro=""
        file.write(str("Product Name:"))
        
        success = False
        while success == False:
            i=0
            p=str(input('ENTER PRODUCT: '))
            for i in range(len(b)):
                if p==b[i][0]:
                    pro=p
                    success =True
                    break
            if pro=="":
                print("invalid value: ")
        file.write(str(p))        
        sales= False
        while sales == False:
            try:
                quantity=int(input("enter quantity:"))
                if quantity>0 and (int(b[i][2])-quantity)>0:
                    sales = True
                    break
                else:
                    print("enter value again")
            except:
                print("invalid value")
        file.write('\n')
        price=0
        for j in range(len(b)):
            if p==str(b[j][0]):
                price=int(b[j][1])
                total=price*quantity
                          
        file.write(str("Amount per product:"+str(price)))
        file.write('\n')
        file.write(str("quantity:"))
        file.write(str(quantity))
        l.append([p,quantity])
        more_product=input("do you want to buy more products y/n:")
        file.write('\n')
            
        file.write("total:"+str(total))
        file.write('\n')
        total=price*quantity
        net=net+total
    file.write('\n')
    file.write(str("                  discount amount:"))
    sales= False
    while sales == False:
        try:
            discount=float(input("enter discount percentage:"))
            if discount>=0 and discount<100:
                 sales = True
                 break
            else:
                print("invalid value.")
        except:
            print("invalid")
    damount=(discount/100)*(price)
    file.write(str(damount))
    file.write('\n')
    fprice=(net)-damount
    file.write(str("                  final price:"))
    d=str(fprice)
    file.write(str(d))
    total=total+float(d)
    file.write('\n')
    file.write("-------------------------------------------------------------------------------")
    file.write('\n')
    file.write("           THANK YOU FOR VISITING HERE          ")
    file.write('\n\n')
    file.close()
    
    return l


