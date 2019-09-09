from invoice import invoice
from stock1 import stock
def update():    
    a=invoice()
    b=stock()
    for i in range(len(b)):
        for j in range(len(a)):
            if a[j][0]==b[i][0]:
                b[i][2]=int(b[i][2])-int(a[j][1])   
    file=open("stock1.txt","w")
    for k in range(len(b)):
        y=b[k][0]+","+b[k][1]+","
        z=str(b[k][2])
        file.write((str(y+z)))
        file.write('\n')
    file.close()
    return("the stocklist is updated")
