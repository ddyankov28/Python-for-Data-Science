from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in tqdm(range(3333)):
    sleep(0.0005)
print()

for elem in ft_tqdm(range(3333)):
    sleep(0.0005)
print()
