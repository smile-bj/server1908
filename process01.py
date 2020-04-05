import os,sys
from time import sleep
pid=os.fork()
if pid<0:
  print("创建失败")
elif pid==0:
    sleep(3)
    print("child ",os.getpid())
    sleep(2)
    os._exit(1)
else:
    pid,status=os.wait()
    print(status)
    print(pid)
    while True:
        pass
# os._exit(0)
# sys.exit("===========")
# print("===========")

