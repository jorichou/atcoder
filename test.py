import glob

file_list = glob.glob("./*.py")
for file in file_list:
    print(file)