import requests
import json
import os.path 
x=requests.get('https://api.merakilearn.org/courses')
print(x.json())
if os.path.exists("API_data.json"):
    print("file exists")
    f=open("API_data.json","r")
    file =f.read()
    data=json.loads(file)
else:
    print("file not exists")
    x=requests.get("https://api.merakilearn.org/courses")
    convert=x.json()
    with open("API_data.json","w") as re:
        json.dump(convert,re,indent=4)
    red=open("API_data.json","r") 
    q=red.read()
    data=json.loads(q)
i=0
while i<len(data):
    print(str(i+1),".",data[i]["name"],data[i]["id"])  
    i+=1
print("") 
user=int(input("enter the course name:-"))
print(data[user-1]["name"])
print(user)
y=requests.get('https://api.merakilearn.org/courses'+data[user-1]["id"]+"/exercise")
y1=y.json()
a=data[user-1]["name"]+"_"+".join"
with open(a,"w") as f:
    json.dump(y1,f,indent=4)
s=open(a,"r") 
read=s.read()
data=json.loads(read)
i=0
while i<len(data["course"]["exercises"]):
    print(i+1,data["course"]["exercises"][i]["name"])
    i+=1
topic=int(input("choose the topic name:-")) 
print(data["course"]["exercises"][topic-1]["name"]) 
i=1
while i<len(data["course"]["exercises"][topic-1]["content"]):
    print(data["course"]["exercises"][topic-1]["content"][i]["name"])
    i+=1
    pre_topic=input("enter the previous or next:-")
    if pre_topic!="Next" and pre_topic=="previous":
        if pre_topic=="previous" and topic>1:
            print(data["course"]["exercises"][topic-1]["name"])
            i=0
            while i<len(data["course"]["exercises"][topic-1]["content"]):
                print(data["course"]["exercises"][topic-1]["content"][i]["value"])
                i+=1
            topic-=1
        else:
            i=0 
            while i<len(data["course"]["exercises"]) :
                print(str(i+1),data["course"]["exercises"][i]["name"])
                i+=1
    elif pre_topic!="previous" and pre_topic=="Next":
        if pre_topic=="Next" and topic<len(data["course"]["exercises"]):
            print(data["course"]["exercises"][topic]["name"])
            i=0
            while i<len(data["course"]["exercises"][topic]["content"]):
                print(data["course"]["exercises"][topic]["content"][i]["value"])
                i+=1
            topic-=1
        if topic== len(data["course"]["exercises"]) :
            print("Topic is completed")
    else:
        print("wrong user input")





    


















	
