import importlib, sys

sys.path = ["A"]

modA = importlib.import_module("module")
fA = modA.F()
fA.act()

sys.path = ["B"]

modB = importlib.reload(modA)
fB = modB.F()
fB.act()

fA.act()