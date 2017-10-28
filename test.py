import os
import sys
from folders import FolderItem

try:
    root = FolderItem(sys.argv[1])
except IndexError:
    sys.exit('Please provide a path...')

print(f'Root path -> {root.path} - {root.item_type}')
for item in root.absitems:
    f_item = FolderItem(item)
    print(f'{f_item.path} - {f_item.item_type}')