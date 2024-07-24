import os

rows, columns = os.popen('stty size', 'r').read().split()
print(f"Number of rows: {rows}, Number of columns: {columns}")