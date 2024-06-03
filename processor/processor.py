import time

while True:
    try:
        with open('/data/output.txt', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("No data found.")
    time.sleep(5)