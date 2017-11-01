import os


class FolderItem:

    def __new__(cls, path: str):
        if os.path.exists(path):
            return super(FolderItem, cls).__new__(cls)
        else:
            raise ValueError('File or Folder does not exist')

    def __init__(self, path: str):
        self.path: str = os.path.abspath(path)
        self.name: str = os.path.basename(self.path)
        self.is_dir: bool = os.path.isdir(self.path)
        self.list_items: list = []
        self.item_paths: list = []
        self.items: list = []

        if self.is_dir:
            self.list_items = os.listdir(self.path)
            self.item_paths = [
                os.path.join(self.path, item) for item in self.list_items
            ]
            self.items = [
                FolderItem(item_path) for item_path in self.item_paths
            ]

    @property
    def item_type(self):
        return 'directory' if self.is_dir else 'file'

    def __repr__(self):
        return f"<FolderItem {self.item_type}:' {self.name}'>"

