# THIS SCRIPT SHOULD BE CALLED SETUP.PY
import cx_Freeze
import os
executables = [
        #                   name of your game script
        cx_Freeze.Executable("snake.py")
]

os.environ['TCL_LIBRARY']=r'C:\Users\aljas\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY']=r'C:\Users\aljas\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'

cx_Freeze.setup(
        name = "ClassicSnake",
        options = {"build_exe": {"packages":["pygame"],"include_files":[]}},
        description = "",
        executables = executables)


#python setup.py build
#python setup.py bdist_msi
