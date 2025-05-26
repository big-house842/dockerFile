import time
import os

n = os.environ.get("N")
n = int(n)

for i in range(1,10):
    print(i, flush=True)
    time.sleep(1)