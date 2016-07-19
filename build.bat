#cd dist
#del /q *
#cd ../

pyinstaller.exe --debug --hidden-import matplotlib --hidden-import tkinter --hidden-import matplotlib.backends.backend_tkagg --hidden-import gishelper.ui --hidden-import tkinter.filedialog gh.py