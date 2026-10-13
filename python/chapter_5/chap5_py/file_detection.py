# Python file detection

import os

file_path = r"d:\python\chapter_5\chap5_py\test.txt"  # Full path

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist")