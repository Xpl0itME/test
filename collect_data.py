import requests
import platform
import socket
import json
import os

def collect_and_send_data():
    # Collect system information
    system_info = {
        "system": platform.system(),
        "release": platform.release(),
        # ... add other information as needed
    }

    # Send data to server
    server_url = "https://your-server.com/collect-data"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(server_url, data=json.dumps(system_info), headers=headers)

        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print(f"Failed to send data. Server returned {response.status_code}.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    collect_and_send_data()

if __name__ == "__main__":
    main()
