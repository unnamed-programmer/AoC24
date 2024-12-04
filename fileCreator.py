import os

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

for i in range(1, 26):
    # make folders for each day
    dayFolderPath = os.path.join(currentPath, f"day0{i}") if i < 10 else os.path.join(currentPath, f"day{i}")
    os.makedirs(dayFolderPath)

    # make files in folders
    for file in ["testin.txt", "input.txt", "solution1.py", "solution2.py"]:
        try: open(os.path.join(dayFolderPath, file), "x")
        except: pass



print(currentPath)