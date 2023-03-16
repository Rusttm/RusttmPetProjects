# coding="utf-8"
import random
import time
import tqdm
with tqdm.tqdm(total=100, desc="Example") as pbar:
    for i in range(10):
        time.sleep(0.1)
        pbar.update(10)