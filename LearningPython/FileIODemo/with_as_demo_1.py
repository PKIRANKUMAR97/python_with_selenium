"""
f1=open("demofile.txt","w")
f1.write("line 4")
f1.close()

f2=open("demofile.txt","r")
print(f2.read())

"""

with open("demofile.txt","w") as f1 :
    f1.write("this is write mode")

with open("demofile.txt","r") as f2 :
    print(f2.read())