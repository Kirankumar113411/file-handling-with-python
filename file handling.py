import os
import sys
print("start")
def fun():
    print("choose your option \n1.creat file \n 2.read file\n 3.edit file\n 4.list all file\n 5.delete file\n 6.end program\n")
    d=int(input(""))
    a=d
    match a:
        case 1:
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("CREATING FILE\n")
            print("enter your file name\n: ")
            f=input("")
            h=f+".txt"
            with open(h,'x')as file:   
                print(f,"file is created successfully")
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")    
        case 2:
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("READING FILE\n")
            print("enter the file name that you want to read\n")
            f=input("")
            with open(f+".txt",'r')as file:
                print(file.read())
            print("the file read successfully\n")
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        case 3:
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("EDITING THE FILE\n")
            print("enter the file name that you want to edit\n")
            f=input("")
            with open(f+".txt",'a')as file:
                print(file.write('HELLO WORLD'))
            print("THE FILE IS EDITED SUCCESSFULLY \n")
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        case 4:
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("LISTING ALL FILE\n")
            path='D:\kiran'
            file=os.listdir(path)
            for file in file:
                print(file)
            print("THESE ARE THE LIST OF FILES\n")
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        case 5:
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("DELETE FILE\n")
            f=input("")
            file=os.remove+'.txt'(path)
            print("DELETED THE FILE SUCCESSFULLY\n\n")
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        case 6:
           print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
           print("STOP THE PROGRAM\n")
           sys.exit(0)
           print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            
while 1:
    fun()
            
