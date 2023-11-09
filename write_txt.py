import os
# train val test
with open("train.txt", "w") as f:
    path = r"C:\Users\shuailuyu\AllTea\data_RGBDIR_tea2\DataSet\c2d\train"
    for foldName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            # filename=filename.split(".")[0]
            line = str(os.path.join(foldName, filename))
            line = line + '\n'
            f.write(line)
# C:\Users\shuailuyu\AllTea\apple\DataSet\depth
