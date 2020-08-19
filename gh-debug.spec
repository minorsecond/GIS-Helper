# -*- mode: python -*-

block_cipher = None
from pathlib import Path
import os, glob

home = str(Path.home())
rasterio_library_path = os.path.join(home, 'Anaconda3\\envs\\GIS-Helper\\Lib\\site-packages\\rasterio\\')
print("Rasterio library path {0}".format(rasterio_library_path))
rasterio_imports_paths = glob.glob(str(rasterio_library_path) + '*.py')
print(rasterio_imports_paths)
rasterio_imports = ['numpy', 'packaging', 'matplotlib', 'tkinter', 'matplotlib.backends.backend_tkagg', 'gishelper.ui', 'tkinter.filedialog']

for item in rasterio_imports_paths:
    current_module_filename = os.path.split(item)[-1]
    current_module_filename = 'rasterio.'+current_module_filename.replace('.py', '')
    rasterio_imports.append(current_module_filename)

a = Analysis(['gh.py'],
             pathex=['C:\\Users\\Ross\\anaconda3\\envs\\GIS-Helper\\Library\\bin', 'C:\\Users\\rwardrup\\PycharmProjects\\GIS-Helper'],
             binaries=[],
             datas=[('matplotlibrc', '.config')],
             hiddenimports=rasterio_imports,
             #hookspath=['hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='gh',
          debug=True,
          strip=False,
          upx=True,
          console=True , icon='assets\\map.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='gh')