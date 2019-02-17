import os
from datetime import datetime

# print(dir(os))
# print(os.getcwd())

os.chdir('/Users/john/Desktop')

# os.mkdir('OS-Demo-2/Sub-Dir-1')
# os.makedirs('OS-Demo-2/Sub-Dir-1')
# os.rmdir('OS-Demo-2/Sub-Dir-1')
# os.removedirs('OS-Demo-2/Sub-Dir-1')
# os.rename('test.txt', 'demo.txt')

# print(os.getcwd())
# print(os.listdir())

# print(os.stat('eBooks').st_size)
# print(os.stat('eBooks').st_mtime)

# mod_time = os.stat('eBooks').st_mtime
# print(datetime.fromtimestamp(mod_time))

"""
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()
"""

# print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

# with open(file_path, 'w') as file:
#     file.write()

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))
print()
print(dir(os.path))
