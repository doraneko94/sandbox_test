import tempfile
import os

with tempfile.TemporaryDirectory() as tmpdir:
    os.chdir(tmpdir)
    with open("test.txt", "w") as f:
        f.write("This is allowed")

while True:
    pass