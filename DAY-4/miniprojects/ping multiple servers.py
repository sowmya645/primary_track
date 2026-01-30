import os
def ps(hostname):
    param='-n'
    response=os.system(f"ping {param} 1 {hostname}")
    if response==0:
        print("server is up")
    else:
        print("server is down")
ps("google.com")