from urllib.request import urlretrieve
import urllib.request
import threading
import json
import ssl
def download():
    try:
        url="https://fakestoreapi.com/products"
        headers={
            "User-Agent":"Mozilla/5.0"
        }
        req=urllib.request.Request(url,headers=headers)
        
        context=ssl._create_unverified_context()
        with urllib.request.urlopen(req,context=context) as res:
            data=res.read()
        print("data is downloaded")
        posts=json.loads(data)
        with open("posts.json","w") as f:
            json.dump(posts,f,indent=4)
        print("download complete amd saved to posts.json")
    except Exception as e:
        print(e)
t=threading.Thread(target=download)
t.start()
print("main continyes")

    