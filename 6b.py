import os
import sys
import pathlib
import zipfile

fname=""
if not os.path.exists(fname):
    print("file is not exist")
    sys.exit(0)
curdir=pathlib.Path(fname)

with zipfile.ZipFile("myzip.zip",mode='w')as archieve:
    for fpath in curdir.rglob("*"):
        archieve.write(fpath,arcname=fpath.relative_to(curdir))
if os.path.isfile("myzip.zip"):
    print("sucessfully created")
else:
    print("having issue")