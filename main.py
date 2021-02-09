import time
from datetime import datetime as dt


temp="" #local host file location (no admin permission req)
hosts_path="C:\Windows\System32\drivers\etc\hosts" (requires admin previlages)
redirect="127.0.0.1"
website_list=["facebook.com", "www.facebook.com"] #add links ou wish to block


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17): #working hours
        print("Working hours...")
        with open(temp, "r+") as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        with open(temp,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
        
    time.sleep(5)
