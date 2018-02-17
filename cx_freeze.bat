@ECHO OFF
CLS

ECHO Removing cache directory...
RMDIR /Q /S "__pycache__"
RMDIR /Q /S "__pycache__"

ECHO Removing build directory...
RMDIR /Q /S "build"
RMDIR /Q /S "build"

ECHO Removing installers directory...
RMDIR /Q /S "installers"
RMDIR /Q /S "installers"

ECHO Creating installers directory...
MD "installers"

ECHO Compiling executable...
setup.py build

ECHO.

ECHO Copying application files...
COPY /Y "about.png" "build"
COPY /Y "add_files.png" "build"
COPY /Y "add_folder.png" "build"
COPY /Y "clear.png" "build"
COPY /Y "counter.png" "build"
COPY /Y "crop.png" "build"
COPY /Y "extension.png" "build"
COPY /Y "help.png" "build"
COPY /Y "icon.png" "build"
COPY /Y "insert.png" "build"
COPY /Y "quit.png" "build"
COPY /Y "regex.png" "build"
COPY /Y "remove.png" "build"
COPY /Y "rename.png" "build"
COPY /Y "replace.png" "build"
COPY /Y "text_case.png" "build"
COPY /Y "trim.png" "build"

COPY /Y "gpl.txt" "build"
COPY /Y "icons.txt" "build"
COPY /Y "license.txt" "build"
COPY /Y "whats_new.txt" "build"
