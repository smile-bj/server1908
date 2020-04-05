import multiprocessing03 as mp
import os
filename="home/baijing/1908/11.jpeg"
size=os.path.getsize(filename)
fr=open(filename,'rb')
def top():
    fr=open("filename",'rb')
    print(fr.fileno())
    fw=open("top.jpg","wb")
    n=size//2
    fw.write(fr.read(n))
    fr.close()
    fw.close()
def bot():
    fr=open(filename,'rb')
    fw=open('bot.jpg','wb')
    fr.seek(size//2,0)
    fw.write(fr.read())
    fr.close()
    fw.close()
p1=mp.Process(target=top)
p2=mp.Process(target=bot)
p1.start()
p2.start()
p1.join()
p2.join()

