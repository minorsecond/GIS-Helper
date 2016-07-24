#cd dist
#del /q *
#cd ../
#activate gisHelper
pyinstaller.exe --distpath C:\Users\Ross\DEV\ghelper\dist --debug --hidden-import packaging --hidden-import matplotlib --hidden-import tkinter --hidden-import matplotlib.backends.backend_tkagg --hidden-import gishelper.ui --hidden-import tkinter.filedialog C:\Users\Ross\DEV\ghelper\gh.py