f=open("/home/baijing/1908/file.txt",'w+',1)
while True:
    data=input("请输入:")
    if not data:
        break
    f.write(data+'\n')
    # f.flush()
f.close()
