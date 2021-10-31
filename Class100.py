import os
import shutil

source = "C:/Users/Raghav/Desktop/Madhav/New folder (9)/madhav/Python1/Text2"
destination = "C:/Users/Raghav/Desktop/Madhav/New folder (9)/madhav/Python1/Text1"

source = source + "/"
destination = destination + "/"

files = os.listdir(source)

for i in files:
    shutil.copy((source + i),destination)
