cities={"hyderabad","delhi","banglore","chennai"}
locations={"chennai": {"marina beach":20, "express avenue":15, "guindy park":10},
           "hyderabad": {"charminar":10, "golconda fort":60, "hitech city":30},
           "bengaluru": {"lalbagh":5, "cubbon park":10, "MG road":9},
           "delhi": {"india gate":2, "red fort":7, "qutub minar":8}}
distance=[]
fares={"chennai":{"auto":50,"bike":30,"scooty":30,"suv":200},
       "hyderabad":{"auto":60,"bike":30,"scooty":40,"suv":250},
       "bengaluru":{"auto":70,"bike":40,"scooty":30,"suv":300},
       "delhi":{"auto":70,"bike":50,"scooty":30,"suv":200}}
import time
vehicle=("bike","auto","scooty","mini","suv")
status="waiting"
dict={}
def get_details():
    name=input("enter your name")
    phonenumber=input("enter your phone number")
    city=input("enter city name: ")
    if city not in cities:
       print("we are not providing servies here")
       return False
    source=input("enter start location: ")
    
    destination=input("enter destination location: ")
    dict["name"]=name
    dict["phonenumber"]=phonenumber
    dict["city"]=city
    dict["source"]=source
    dict["destination"]=destination
    
    ride(city,source,destination)
def feedback():
    print("provide feeback 1 being the lowest and 5 being the best")
    feed=input("provide your app feedback: ")
    ride_experience=input("rate your ride experience: ")
    driver_exp=input("rate your driver experience: ")
    dict["app feedback "]=feed
    dict["ride_experience"]=ride_experience
    dict["driver_Experience"]=driver_exp
    
def ride(city,source,destination):  
    
    global status
    decision=input("book?")
    if decision=="YES":
        veh=input("enter which vehicle u want to book")
        print(f"you are trying to book vehicle: {veh} at a fare: {fares[city][veh]+(abs(locations[city][destination]-locations[city][source])*5)}")
        print("searching for drivers")
        time.sleep(5)
    print(status)
    time.sleep(5)
    status="booked"
    print(status)
    print("driver will be arriving in 3 mins")
    dict["fare"]=fares[city][veh]+(abs(locations[city][destination]-locations[city][source])*5)
    print(f"driver has been accepted your ride from {source} to {destination} at a fare :{fares[city][veh]+(abs(locations[city][destination]-locations[city][source])*5)} in {veh}")
    time.sleep(5)
    print("driver arrived")
    print("trip started")
    time.sleep(5)
    print("ride finished")
    feedback()
    bill=input("do u want to download the bill")
    if bill=="YES":
        path=r"C:\Users\91906\Downloads\ill.txt"
        with open(path,"w") as f:
            for key,value in dict.items():
                f.write(f"{key}: {value}\n")
        