import importlib, sys

sys.path = ["../A"]
mod = importlib.import_module("module")

class F(mod.F):
    def __init__(self):
        super().__init__