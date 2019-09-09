def stock():
  file=open("stock1.txt","r")
  lines=file.readlines()
  l=[]
  for line in lines:
     x=line.replace("\n","").split(",")
     y=l.append(x)
     file.close()
  return l




