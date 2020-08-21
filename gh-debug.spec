# -*- mode: python -*-

block_cipher = None

block_cipher = None
import os
from pathlib import Path
from PyInstaller.utils.hooks import exec_statement

current_path = os.getcwd()
home_path = str(Path.home())
env_path = os.path.join(home_path, 'Anaconda3')
mpl_data_dir = exec_statement("import matplotlib; print(matplotlib._get_data_path())")
linalg_dir = os.path.join(env_path, 'lib\\site-packages\\numpy\\linalg\\')

a = Analysis(['gh.py'],
             pathex=[current_path, os.path.join(env_path, '\\Library\\bin')],
             binaries=[(os.path.join(linalg_dir, "_umath_linalg.cp37-win_amd64.pyd"), "numpy\\linalg"),
                       (os.path.join(linalg_dir, "lapack_lite.cp37-win_amd64.pyd"), "numpy\\linalg"),
                       (os.path.join(env_path, "api-ms-win-crt-stdio-l1-1-0.dll"), "."),
                       (os.path.join(env_path, "api-ms-win-crt-heap-l1-1-0.dll"), "."),
                       (os.path.join(env_path, "api-ms-win-crt-math-l1-1-0.dll"), "."),
                       (os.path.join(env_path, "api-ms-win-crt-runtime-l1-1-0.dll"), "."),
                       (os.path.join(env_path, "api-ms-win-crt-string-l1-1-0.dll"), "."),
                       (os.path.join(env_path, "api-ms-win-crt-convert-l1-1-0.dll"), ".")
             ],
             datas=[('matplotlibrc', '.config'), (mpl_data_dir, 'matplotlib\\mpl-data')],
             hiddenimports=['numpy', 'packaging', 'matplotlib', 'tkinter', 'matplotlib.backends.backend_Qt5Agg', 'gishelper.ui', 'tkinter.filedialog', 'PyQt5'],
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