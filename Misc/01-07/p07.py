"""Test Documentation """

file = open('.\\07 fruits.txt',mode = 'r')
data = file.readlines()
print(type(data))
print(data)
for datas in data:
    datas = datas.rstrip('\n')
    print(datas.__len__())
