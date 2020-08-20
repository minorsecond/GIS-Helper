# -*- mode: python -*-

block_cipher = None

from PyInstaller.utils.hooks import exec_statement
mpl_data_dir = exec_statement("import matplotlib; print(matplotlib._get_data_path())")

a = Analysis(['gh.py'],
             pathex=['C:\\Users\\Ross\\anaconda3\\envs\\GIS-Helper\\Library\\bin', 'C:\\Users\\rwardrup\\PycharmProjects\\GIS-Helper'],
             binaries=[],
             datas=[('matplotlibrc', '.config'), (mpl_data_dir, 'matplotlib\\mpl-data')],
             hiddenimports=['numpy', 'packaging', 'matplotlib', 'tkinter', 'matplotlib.backends.backend_Qt5Agg', 'gishelper.ui', 'tkinter.filedialog'],
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