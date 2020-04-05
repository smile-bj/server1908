import subprocess
output_file=open("ifconfig.txt1","w")
subprocess.call(['ifconfig'],stdout=output_file)

with open("ifconfig.txt1","r")as f:
    net_name_list=[]
    add_list=[]
    for line in f:
        if "flags" in line:
            net_name=line.split(":")[0]
        if "inet " in line:
            IPV4_addr=line.strip().split(" ")[1]
            add_list.append((net_name,IPV4_addr))
    with open("ifconfig.txt",'a') as m:
        for inet,IPV4 in add_list:
            content=inet+IPV4+"\n"
            m.write(content)
            m.flush()









