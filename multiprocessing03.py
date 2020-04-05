import multiprocessing as mp
from time import sleep
def work(sec,name):
    for i in range(3):
        sleep(sec)
        print("I am %s"%name)
        print("I am working....")
p=mp.Process(target=work,args=(2,"李白"))
p.start()
p.join(3)
print("============")
