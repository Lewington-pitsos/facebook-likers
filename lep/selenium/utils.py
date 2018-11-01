import time
import random

def slow_fill(element, keys: str):
    for key in keys:
        element.send_keys(key)
        time.sleep(random.uniform(0.005, 0.3))
    
    time.sleep(random.uniform(0.1, 1.5))
