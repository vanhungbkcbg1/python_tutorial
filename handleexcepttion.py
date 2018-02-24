from MyException import MyException
try:
    raise MyException('100')
    i=10

    for i in range(10):
        if i>4:
            continue
        else:
            print i
    else:
        print 'thoat vong for'
except MyException as e:
    print 'my exception'+e.value
else:
    print 'not run'