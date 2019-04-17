# bwrenamer

## Basic usage

Add files to the file list using "Add files" or "Add folder" menubar (or
toolbar) selections. Edit the file names using the tools provided in the tab
pages below. These tools include:

- Counter, adds a numbering to file names.
- Crop, crops a specified portion of file names.
- Extension, changes the extension of file names.
- Insert, inserts a string to specified position in the file names.
- RegEx, perform complex string operations to file names using regular expressions.
- Replace, replaces a string from file names with specified replacement string.
- Text case, convert the letters case from the file names.
- Trim, trim a portion of file names.

When you change the values from these tools, the file names in the "Preview"
column will change accordingly. By pressing a button named "Set" from the tool,
the application will add your changes to the file names in the "Modified"
column. The "Modified" column contains the file names that are used when finally
renaming the files. When you are done editing, select the "Rename files"
selection from the menubar (or toolbar).


## Menu/toolbar commands

### File > Add files
Select files using a dialog window. The application will add them to the file
list.

### File > Add folder
Select a folder using a dialog window. The application will add all the files
from the selected folder to the file list.

### File > Remove files
Remove the selected files from the file list.

### File > Clear list
Clears the whole file list.

### File > Rename files
Renames the files in the file list using the file names from the "Modified"
column.

### File > Quit
Quits the application.

### Help > About...
Application information.


## Running on Linux

### Installing dependencies (Debian-based systems)
Open your terminal application and type:
`sudo apt install python3 python3-pyqt4`

Hit enter. Enter your password when prompted. Answer yes to the question about
using additional disk space.

### Downloading the source
git clone https://github.com/bulkware/bwrenamer.git

### Running the application
Enter the application directory using this command:
`cd bwrenamer`

You can run the application from the source code using this command:
`python3 main.py`
