import requests
import os

while True:
    print("== GitHub User Activity == ")
    githubUsername = input("Github Username: ")
    options = input("identify github account [type or repo or payload]: ")

    URL = f"https://api.github.com/users/{githubUsername}/events"

    r = requests.get(URL)
    events = r.json()

    if options == "type".lower():
            for event in events:
                print(event["type"])
    elif options == "repo".lower():
            for event in events:
                print(event["repo"])
    elif options == "payload".lower():
            for event in events:
                print(event["payload"])
    else:
        print("Error Command Try Again!")

    Tryagain = input("Press enter try again... ")

    if Tryagain == "":
        os.system('cls')
        continue