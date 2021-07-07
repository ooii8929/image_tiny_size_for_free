
import os
import tinify
from pathlib import Path

import pathlib

print(pathlib.Path(__file__).parent.absolute())

tinify.key = 'p8ZqCTGdVF0FK2B5wWcF7PFhm7bDRMJG' 
path = '/Users/linpinyou/Desktop/tinysize'

def tinysize():
    for dirpath, dirs, files in os.walk(path):
        print(files) 
        for file in files: 
            imgpath = os.path.join(dirpath, file) 
            print("compressing ..."+ imgpath) 
            try:
                tinify.from_file(imgpath).to_file(imgpath)
            except:
                pass

tinysize()