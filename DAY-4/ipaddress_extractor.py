ip_address=[]
with open("samples_log.log","r") as log:
    lines=log.readlines()
    for line in lines:
        words=line.split("[")
        ip_addr=words[1].split("]")
        ip_address.append(ip_addr[0])

with open("ip_addr_out.csv","w") as ip:
    for addr in ip_address:
        ip.write(addr+"\n")
print("IP addresses extracted successfully")