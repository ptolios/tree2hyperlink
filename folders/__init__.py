import os


class FolderItem:

    def __new__(cls, path):
        if os.path.exists(path):
            return super(FolderItem, cls).__new__(cls)
        else:
            raise ValueError('File or Folder does not exist')

    def __init__(self, path):
        self.path = os.path.abspath(path)
        self.is_dir = os.path.isdir(self.path)
        self.items = os.listdir(self.path)
        self.absitems = [os.path.join(self.path, item) for item in self.items]

    @property
    def item_type(self):
        return 'directory' if self.is_dir else 'file'

