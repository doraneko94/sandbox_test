import hashlib, importlib, os, shutil, sys, types
from pyfakefs.fake_filesystem_unittest import Patcher
import multiprocessing

def hash_folder_name(folder_name):
    return hashlib.sha256(folder_name.encode()).hexdigest()

folders = ["A", "B"]
filelists = [os.listdir(folder) for folder in folders]
mods = []

def reset_fs():
    fs.reset()
    for folder in os.listdir("."):
        shutil.rmtree(folder)

def import_module(module_code, module):
    with Patcher() as patcher:
        fs = patcher.fs
        exec(module_code, module.__dict__)


with Patcher() as patcher:
    fs = patcher.fs

    reset_fs()

    for i, (folder, files) in enumerate(zip(folders, filelists)):
        hashed_name = folder + "c"#hash_folder_name(folder)
        for file in files:
            fs.add_real_file(os.path.join(folder, file), target_path=file)
        with open("module.py", "r") as f:
            module_code = f.read()
        mods.append(types.ModuleType(f"module_{folder}"))
        
        process = multiprocessing.Process(target=import_module, args=(module_code, mods[i]))
        process.start()
        process.join(1)
        if process.is_alive():
            process.terminate()

        reset_fs()
    
    fA = mods[0].F()
    fA.act()