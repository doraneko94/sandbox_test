import hashlib, importlib, os, shutil, sys, types
from pyfakefs.fake_filesystem_unittest import Patcher
import multiprocessing

def hash_folder_name(folder_name):
    return hashlib.sha256(folder_name.encode()).hexdigest()

users = ["A", "B"]
mods = []

def import_module(user):
    files = os.listdir(user)

    with Patcher() as patcher:
        fs = patcher.fs
        fs.reset()
        print(os.listdir("."))
        for folder in os.listdir("."):
            shutil.rmtree(folder)
        
        for file in files:
            fs.add_real_file(os.path.join(user, file), target_path=file)
        with open("module.py", "r") as f:
            module_code = f.read()
        module = types.ModuleType(f"module_{user}")

        exec(module_code, module.__dict__)
        mods.append(module)
    return

if __name__ == "__main__":
    process = multiprocessing.Process(target=import_module, args=(users[0], ))
    process.start()
    process.join(1)
    if process.is_alive():
        process.terminate()

#fA = mods[0].F()
#fA.act()