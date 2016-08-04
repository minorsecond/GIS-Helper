# -*- mode: python -*-

block_cipher = None


a = Analysis(['gh.py'],
             pathex=['Z:\\home\\rwardrup\\DEV\\GIS-Helper'],
             binaries=[],
             datas=[],
             hiddenimports=['numpy', 'packaging', 'matplotlib', 'tkinter', 'matplotlib.backends.backend_tkagg', 'gishelper.ui', 'tkinter.filedialog'],
             hookspath=['hooks'],
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