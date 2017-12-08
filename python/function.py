import  os
def add_to_dict(args={'a': 1, 'b': 2}):
      for i in args.keys():
          args[i] += 1
      print args


add_to_dict()


fp=open('test.txt','w')
fp.write('hello')
fp.close()
# remove file
# os.remove('test.txt')
# get absolute path to file
a= os.path.abspath('test.xt')
print a
# base name print file name
print os.path.basename(a)
# get dir name of the file
print os.path.dirname(a)
# check exist file
print os.path.exists('test.txt')
# check is file
print os.path.isfile('test.txt')

# check is absolute path
print os.path.isabs('test.txt')
print os.path.isabs(a)