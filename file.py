def writeFile(stsr):
    file=open('vanhung.txt','a+')
    for i in range(0,10):
        file.write("set name%s %s"%("vanhung"+str(i),"age"+str(i)))
        file.write('\n')
    file.close()

def readFile():
    file=open('vanhung.txt','r')
    str=file.read(2)
    print(str)
    print(file.tell())
    file.seek(10)
    str=file.read(2)
    print(str)
    file.close()