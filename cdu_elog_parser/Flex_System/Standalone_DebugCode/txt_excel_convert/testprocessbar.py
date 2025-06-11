from tqdm import tqdm
import time


with tqdm(total=100, desc="Processing File") as pbar:
    pbar.update(30)  # Moves the bar to 30%
    time.sleep(1.4)
    pbar.update(50)  # Moves the bar to 80%
    time.sleep(1.4)
    pbar.update(20)  # Completes the bar to 100%