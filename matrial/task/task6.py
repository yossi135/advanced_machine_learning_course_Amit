import os
import random
h=r'D:\New folder'
if not os.path.exists(h):
    os.makedirs(h)
num_files=10
for i in range(num_files):
    with open(f'{h}/file_{i}.txt , "w" ') as f :
        