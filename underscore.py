import os
import shutil


class Underscore:
    def __init__(self, root_path, replacement_char, chars_to_replace):
        self.root_path = root_path
        self.replacement_char = replacement_char
        self.chars_to_replace = chars_to_replace
        self.pic_extensions = ({'png', 'jpg'})

    def start(self):
        self.add_underscores(self.root_path)
        return None

    def add_underscores(self, path):
        if os.path.isdir(path):
            files = os.listdir(path)
            for file in files:
                file_path = os.path.join(path, file)
                if os.path.isdir(file_path):
                    new_file_path = self.new_file_path(path, file)
                    shutil.move(file_path, new_file_path)
                    self.add_underscores(new_file_path)
                else:
                    file_parts = file.split('.')
                    if (len(file_parts)) > 1:
                        extension = file_parts[len(file_parts) - 1].lower()
                        if extension in self.pic_extensions:
                            # this is an image
                            new_file_path = self.new_file_path(path, file)
                            shutil.move(file_path, new_file_path)
        return None

    def new_file_name(self, file):
        for c in self.chars_to_replace:
            file = file.replace(c, self.replacement_char)
        return self.remove_multiple_replacement_chars(file)

    def new_file_path(self, base_path, file):
        new_file = self.new_file_name(file)
        return os.path.join(base_path, new_file)

    def remove_multiple_replacement_chars(self, file):
        indexes = []
        for i in range(len(file)):
            if file[i] == self.replacement_char:
                indexes.append(i)
        indexes.reverse()
        for index in indexes:
            try:
                diff = indexes[index] - indexes[index + 1]
                if diff == 1:
                    file = file[:index + 1] + file[index:]
            except IndexError:
                pass
        return file
