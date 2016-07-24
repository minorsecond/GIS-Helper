#cd dist
#del /q *
#cd ../
#activate gisHelper
pyinstaller.exe --distpath C:\Users\Ross\DEV\ghelper\dist --clean --debug --additional-hooks-dir hooks --hidden-import numpy --hidden-import packaging --hidden-import matplotlib --hidden-import tkinter --hidden-import matplotlib.backends.backend_tkagg --hidden-import gishelper.ui --hidden-import tkinter.filedialog C:\Users\Ross\DEV\ghelper\gh.py