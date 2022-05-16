import json
import socket
import sys
import requests
import pyfiglet

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + "<url>")
    sys.exit(1)

req = requests.get("https://" + sys.argv[1])
print("\n" + str(req.headers))

gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of " + sys.argv[1] + " is: " + gethostby_ + "\n")

# ipinfo.io

req_two = requests.get("https://ipinfo.io/" + gethostby_ + "/json")
resp_ = json.loads(req_two.text)

result = pyfiglet.figlet_format("InfoRecon", font="3-d")
print(result)

print("Location: " + resp_["loc"])
print("Country: " + resp_["country"])
print("Region: " + resp_["region"])
print("City: " + resp_["city"])
print("Organisation: " + resp_["org"])
print("Postal: " + resp_["postal"])
print("Timezone: " + resp_["timezone"])

#This program requires pyfiglet to run