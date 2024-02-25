"""
f1=open("C:\\python-selenium\\FileIO\\writemode.txt","w")
f1.write("this is line 1")
f1.close()
"""
"""
f1=open("C:\\python-selenium\\FileIO\\writemode.txt","w")
l=[39,35,78,21,73]
for i in l:
    f1.write(str(i)+"\n")
f1.close()
"""
f1=open("C:\\python-selenium\\FileIO\\append_mode.txt","a")
l=[39,35,78,21,73]
for i in l:
    f1.write(str(i)+"\n")
f1.close()