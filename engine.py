import sys, importlib, multiprocessing, os, socket

args = sys.argv
del sys

modA = importlib.import_module(args[1] +  ".module")
fA = modA.F()
#fA.act()

#modB = importlib.reload(modA)
#fB = modB.F()
#fB.act()

#fA.act()