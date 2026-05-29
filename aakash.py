#for creating file
a=open(r"C:\Users\Livewire\Desktop\aakash.txt",'a')
print("file created")
a.write("hi aakash"
        "1,madhan,anbu,karthi"
        "preethi"
        "kavi")
a.flush()#to push data in the file
a.close()#to close file
print("file writer")
#to read the file fro, the open statement
a=open(r"C:\Users\Livewire\Desktop\aakash.txt",'r')
print(a.read())

#to read line by line
print(a.readline())
print(a.readlines())

#to delete file
 #import os
#os.remove(r"C:\Users\Livewire\Desktop\aakash.txt",'r')

#to enter the bill

aakash=str(input("enter the name"))
bill=open("C:\\Users\\Livewire\\Desktop\\\\aakash.txt",'r')
print(bill)
bill=open(r"C:\Users\Livewire\Desktop\aakash.txt",'a+')
bill.write("---------virthiya shop---------")
price=5
count=3
bill.write("food in data biriyani 2  $200")
bill.write(input(str(price*count)))
bill.flush
bill.close()
bill=open(r"C:\Users\Livewire\Desktop\aakash.txt",'a+')
print(bill.read())
a.close()
