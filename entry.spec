# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.archive.pyz_crypto import PyiBlockCipher

block_cipher = PyiBlockCipher(key='csbt34.ydhl12s')

a = Analysis(['entry.py'],
             pathex=['E:\\PycharmProjects\\pysw'],
             binaries=[],
             datas=[
                ("res/map/*", "res/map"),
                ("res/pt/*", "res/pt"),
                ("res/*.*", "res"),
                ("dll/*", "dll"),
             ],
             hiddenimports=["PySide2.QtXml"],
             hookspath=[],
             runtime_hooks=[],
             excludes=["Cython", "pymysql", "Pillow"],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name="star",  # 程序名.exe
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False,
          icon="F:\\icon\\2.ico")
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='entry')
