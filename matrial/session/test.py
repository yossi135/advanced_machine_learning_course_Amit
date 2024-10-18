import os
import random
h = r'D:\New folder'
if not os.path.exists(h):
    os.makedirs(h)
num_files = 20  
for i in range(num_files):
    with open(f"{h}/file_{i}.txt", "w") as f: 
        f.write(f"File {i}")
files = os.listdir(h)
print(files)
#print(f"عدد الملفات بعد الإنشاء: {len(files)}")
#files_to_delete = random.sample(files, len(files) // 2)
#for file in files_to_delete:
 #   os.remove(os.path.join(h, file)) 
#remaining_files = os.listdir(h)
#print(f"عدد الملفات المتبقية: {len(remaining_files)}")