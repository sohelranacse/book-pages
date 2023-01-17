import glob
import os

directory = input(str("Type directory: "))
file_pattern = '*.jpg'

files = glob.glob(os.path.join(directory, file_pattern))

for i in range(len(files)):
    new_file_name = str(i+1)+'.jpg'

    new_file_path = os.path.join(directory, new_file_name)

    os.rename(files[i], new_file_path) 
    print(i, new_file_name)