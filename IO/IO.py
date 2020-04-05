# filename=(input("请输入文件名称："))
# try:
#     f=open(filename,'rb')
# except FileNotFoundError as e:
#     print("找不到该文件")
# else:
#     file=filename.split("/")[-1]
#     fw=open('/home/baijing/1908/exercise'+file,'wb')
#     while True:
#         data=f.read(1024)
#         if not data:
#             break
#         fw.write(data)
#     f.close()
#     f.close()

with open("file.txt",'rw') as f :
    data=f.read()
    print(data)


