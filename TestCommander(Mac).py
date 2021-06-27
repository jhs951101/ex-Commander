import os

stream = os.popen('cd ..; ls;')
outputs = stream.readlines()

for i in range(0, len(outputs), 1):
    print(outputs[i], end='')
