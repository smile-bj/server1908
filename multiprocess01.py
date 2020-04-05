import multiprocessing03 as mp
from time import sleep
a=1
def fun():
    print("开始一个进程")
    sleep(2)
    global a
    a=1000
    print("a",a)
    # a=1000
    print("结束一个进程")
p=mp.Process(target=fun)
p.start()
sleep(1)
print("父进程干点事")
p.join()
print("a",a)