import asyncio
from bleak import discover
from threading import Thread
import argparse
import warnings

warnings.filterwarnings("ignore")

thread = int (input("Enter 1 for threads , 0 otherwise : "))
num_threads = 1
if thread == 1:
    num_threads = int(input("Enter the number of threads : "))

dev = [] # to append the bluetooth devices

async def scan():
    devices = await discover()
    for d in devices:
        s=str(d)
        if s in dev:
            continue
        dev.append(s)
        print(s)

def run():
    asyncio.run(scan(), debug=True)

threads = []
for _ in range(num_threads): 
    t = Thread(target=run)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
