from fileinput import input
import sys

with input('/home/mehul/Documents/training/python/yannick/filehandling/message.txt', inplace=True) as f:
    for line in f:
        line = line.replace('night', 'morning')
        sys.stdout.write(line)
