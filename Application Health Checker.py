import requests

url = "https://opensource-demo.orangehrmlive.com"

try:
    response = requests.get(url)

    if response.status_code == 200:
        print("Application is UP")
    else:
        print(f"Application is DOWN. Status Code: {response.status_code}")

except Exception as e:
    print(f"Application is DOWN: {e}")