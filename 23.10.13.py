""" file = open ("temp.txt", "w")

for i in range(100):
    file.write(f"{i}\n")
    
file.close() """


""" file = open ("C:\\Users\\Catholic\\temp.txt", "w")

for i in range(100):
    file.write(f"{i}\n")
    
file.close()
 """

""" f = open ("C:\\Users\\Catholic\\temp.txt", "w")

for i in range(100):
    f.write(f"{i}\n")
    
f.close()
 """

#
""" f = open ("C:\\Users\\Catholic\\temp.txt", "a")

f.write("hello\n")
f.write("world\n")

f.close()
 """
 
 
#파일읽기

""" f = open ("C:\\Users\\Catholic\\temp.txt", "r")

res=f.read()
print(res)

f.close() """


#
""" f = open ("C:\\Users\\Catholic\\temp.txt", "r")

res=f.readline()
print(res)

f.close()
 """

#
""" f = open ("C:\\Users\\Catholic\\temp.txt", "r")

for i in range(110) :
    res=f.readline()
    print(res)

f.close()
 """

#
""" f = open ("C:\\Users\\Catholic\\temp.txt", "r")

res=f.readlines()
print(res)

f.close() """

#
""" f = open ("C:\\Users\\Catholic\\temp.txt", "r")
line =f.readlines()
for l in line :
    print(1)
    
f.close() """

#
f = open ("C:\\Users\\Catholic\\temp.txt", "r")
for line in f:
    print(line)
    
f.close()
