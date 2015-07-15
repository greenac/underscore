import os
import shutil


class IOSExtentionHandler:
    def __init__(self, root_dir, exts_to_change):
        self.root_dir = root_dir
        self.exts_to_change = exts_to_change
        self.ext_keys = self.exts_to_change.keys()

    def rename(self):
        self._change_extension(self.root_dir)
        return None

    def _change_extension(self, dir_path):
        files = os.listdir(dir_path)
        for file in files:
            file_path = os.path.join(dir_path, file)
            if os.path.isdir(file_path):
                self._change_extension(file_path)
            else:
                new_file = self._modify_file(file)
                new_file_path = os.path.join(dir_path, new_file)
                shutil.move(file_path, new_file_path)
        return None

    def _modify_file(self, file):
        print('changing', file, ' --> ')
        for ext in self.ext_keys:
            if ext in file:
                file = file.replace(ext, self.exts_to_change[ext])
                break
        print(file)
        return file
