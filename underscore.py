import os
import shutil

class Underscore:
    def __init__(self, root_path, replacement_char, chars_to_replace):
        self.root_path = root_path
        self.replacement_char = replacement_char
        self.pic_extensions = ({'png', 'jpg'})
        self.chars_to_replace = chars_to_replace

    def start(self):
        self.add_underscores(self.root_path)
        return None

    def add_underscores(self, path):
        if os.path.isdir(path):
            files = os.listdir(path)
            for file in files:
                file_path = os.path.join(path, file)
                if os.path.isdir(file_path):
                    self.add_underscores(file_path)
                else:
                    file_parts = file.split('.')
                    if (len(file_parts)) > 1:
                        extension = file_parts[len(file_parts) - 1].lower()
                        if extension in self.pic_extensions:
                            # this is an image
                            new_file = self.new_file_name(file)
                            new_file_path = os.path.join(path, new_file.lower())
                            shutil.move(file_path, new_file_path)
        return None

    def new_file_name(self, file):
        new_file = file
        for c in self.chars_to_replace:
            new_file = new_file.replace(c, self.replacement_char)
        return new_file
