import time

while True:
    with open('/data/output.txt', 'w') as f:
        f.write(f"Current timestamp: {time.time()}\n")
    time.sleep(5)