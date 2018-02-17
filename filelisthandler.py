# !/usr/bin/env python3
# -*- coding: utf-8 -*-

""" A class to handle file lists. """

# Imports
import os # Miscellaneous operating system interfaces
import re # Regular expression operations
import sys # System-specific parameters and functions

# A class to handle file lists
class FileListHandler(object):

    # Initialization
    def __init__(self):

        # Declare class variables
        self.count = 0 # File counter
        self.error = "" # String for errors
        self.filelist = [] # File list

        # File list items are lists with these columns:
        # 0 = Original file path
        # 1 = Extension
        # 2 = Original file name
        # 3 = Modified file name (when we setSomething)
        # 4 = Preview file name (when we viewSomething)


    # Add file
    def addfile(self, fp):
        self.count += 1
        ext = os.path.splitext(fp)[1][1:]
        fn = os.path.basename(fp)
        self.filelist.append([fp, ext, fn, fn, fn])
        return True


    # Clear
    def clear(self):
        self.count = 0
        self.error = ""
        self.filelist[:] = []


    # Exists
    def exists(self, fp):
        if self.count < 1:
            return False
        for item in self.filelist:
            if item[0] == fp:
                return True
        return False


    # Remove
    def remove(self, index):
        if index < len(self.filelist):
            del self.filelist[index]
            self.count -= 1


    # Rename
    def rename(self):

        # Check if filelist is empty
        if self.count < 1:
            self.error = "File list is empty."
            return False

        # Check for files before renaming
        filesdiff = False
        uniques = []
        for item in self.filelist:
            if not os.path.exists(item[0]):
                self.error = "File does not exist:\n" + item[0]
                return False

            if not os.path.isfile(item[0]):
                self.error = "File is not an existing regular file:\n" + item[0]
                return False

            if item[2] != item[3]:
                filesdiff = True

        # Check if filenames differ
        if not filesdiff:
            self.error = "Filenames are the same."
            return False

        try:
            for item in self.filelist:
                old = item[0]
                new = os.path.split(old)[0]
                new = os.path.join(new, item[3])
                if old == new:
                    continue
                elif os.path.exists(new):
                    self.error = "There exists a file with the same name:\n" \
                        + new
                    return False
                os.rename(old, new)
                item[0] = new
        except:
            self.error = "Unexpected error: " + str(sys.exc_info()[1])
            return False
        else:
            return True


    # Reset
    def reset(self):

        # Check if filelist is empty
        if self.count < 1:
            self.error = "File list is empty."
            return False

        for item in self.filelist:
            ext = os.path.splitext(item[0])[1][1:]
            fn = os.path.basename(item[0])
            item[1] = ext
            item[2] = fn
            item[3] = fn
            item[4] = fn
        return True


    # Sort
    def sort(self):

        # Check if filelist is empty
        if self.count < 1:
            self.error = "File list is empty."
            return False

        self.filelist.sort()
        return True


    # Counter
    def counter(self, pos, side, zeros, replace=False, preview=True):

        # Check if filelist is empty
        if self.count < 1:
            self.error = "File list is empty."
            return False

        for i, item in enumerate(self.filelist, start=1):
            number = str(i).zfill(zeros)
            if replace:
                name = number + os.extsep + item[1]
            else:
                name = os.path.splitext(item[3])[0]
                if pos == 0 and side == 0:
                    name = number + name
                elif pos == 0 and side == 1:
                    name = name + number
                elif side == 1:
                    name = name[0:-pos] + number + name[-pos:]
                else:
                    name = name[:pos] + number + name[pos:]
                name = name + os.extsep + item[1]
            if preview:
                item[4] = name
            else:
                item[3] = name

        return True


    # Crop
    def crop(self, start, end, invert=False, preview=True):

        # Check if filelist is empty
        if self.count < 1:
            self.error = "File list is empty."
            return False

        for i, item in enumerate(self.filelist, start=1):
            name = os.path.splitext(item[3])[0]
            if invert:
                name = name[-end:-start]
            else:
                name = name[start:end]
            name = name + os.extsep + item[1]
            if preview:
                item[4] = name
            else:
                item[3] = name
        return True


    # Extension
    def extension(self, ext, preview=True):

        # Check if filelist is empty
        if self.count < 1:
            self.error = "File list is empty."
            return False

        # Check if extension is empty
        if ext == "" and not preview:
            self.error = "Extension cannot be empty."
            return False

        for item in self.filelist:
            name = item[3]
            if ext != "":
                name = os.path.splitext(name)[0]
                name = name + os.extsep + ext
            if preview:
                item[4] = name
            else:
                item[1] = ext
                item[3] = name

        return True


    # Insert
    def insert(self, text, pos, side, preview=True):

        # Check if filelist is empty
        if self.count < 1:
            self.error = "File list is empty."
            return False

        # Check if string is empty
        if text == "" and not preview:
            self.error = "No text to insert."
            return False

        for item in self.filelist:
            name = os.path.splitext(item[3])[0]
            if text == "":
                pass
            elif pos == 0 and side == 0:
                name = text + name
            elif pos == 0 and side == 1:
                name = name + text
            elif side == 1:
                name = name[0:-pos] + text + name[-pos:]
            else:
                name = name[:pos] + text + name[pos:]
            name = name + os.extsep + item[1]
            if preview:
                item[4] = name
            else:
                item[3] = name

        return True


    # RegEx
    def regex(self, old, new, preview=True):

        # Check if filelist is empty
        if self.count < 1:
            self.error = "File list is empty."
            return False

        # Check if search string is empty
        if old == "" and not preview:
            self.error = "Search string cannot be empty."
            return False

        try:
            for item in self.filelist:
                name = os.path.splitext(item[3])[0]
                if old != "":
                    name = re.sub(old, new, name)
                name = name + os.extsep + item[1]
                if preview:
                    item[4] = name
                else:
                    item[3] = name
        except re.error as e:
            self.error = "Regular expression error: " + str(e)
            return False
        except:
            self.error = "Unexpected error: " + str(sys.exc_info()[1])
            return False
        else:
            return True


    # Replace
    def replace(self, old, new, preview=True):

        # Check if filelist is empty
        if self.count < 1:
            self.error = "File list is empty."
            return False

        # Check if search string is empty
        if old == "" and not preview:
            self.error = "Search string cannot be empty."
            return False

        # Check if the strings are the same
        if old == new and not preview:
            self.error = "Search string cannot be the same as replace string."
            return False

        for item in self.filelist:
            name = os.path.splitext(item[3])[0]
            if old != "" and old != new:
                name = name.replace(old, new)
            name = name + os.extsep + item[1]
            if preview:
                item[4] = name
            else:
                item[3] = name

        return True


    # Text case
    def textcase(self, mode, preview=True):

        # Check if filelist is empty
        if self.count < 1:
            self.error = "File list is empty."
            return False

        # Check if mode is valid
        if mode < 0 or mode > 3:
            self.error = "Text case mode is invalid."
            return False

        for item in self.filelist:
            name = os.path.splitext(item[3])[0]
            if mode == 0:
                name = name.capitalize()
            elif mode == 1:
                name = name.title()
            elif mode == 2:
                name = name.lower()
            elif mode == 3:
                name = name.upper()
            name = name + os.extsep + item[1]
            if preview:
                item[4] = name
            else:
                item[3] = name

        return True


    # Trim
    def trim(self, length, side, preview=True):

        # Check if filelist is empty
        if self.count < 1:
            self.error = "File list is empty."
            return False

        # Check if extension is empty
        if length < 1:
            self.error = "Trim length is not enough."
            return False

        for item in self.filelist:
            name = os.path.splitext(item[3])[0]
            if side == 0:
                name = name[length:]
            elif side == 1:
                name = name[0:-length]
            name = name + os.extsep + item[1]
            if preview:
                item[4] = name
            else:
                item[3] = name

        return True
