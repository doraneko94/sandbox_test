from pyfakefs.fake_filesystem_unittest import Patcher
import os, shutil

folders = ["A", "B"]
filelists = [os.listdir(folder) for folder in folders]
with Patcher() as patcher:
    fs = patcher.fs
    for folder in os.listdir("."):
        shutil.rmtree(folder)
    
    for folder, files in zip(folders, filelists):
        for file in files:
            path = os.path.join(folder, file)
            fs.add_real_file(path)
            with open(path, "r") as f:
                content = f.read()
            with open(file, "w") as f:
                f.write(content)

    print(os.listdir("."))