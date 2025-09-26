import requests

def check_app_uptime(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Application is UP. Status code: {response.status_code}")
        else:
            print(f"Application DOWN. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Application DOWN. Error: {e}")

if __name__ == "__main__":
    wisecow_url = "http://localhost:4499"  
    check_app_uptime(wisecow_url)

