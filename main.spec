# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\123\\PycharmProjects\\auto inward'],
             binaries=[('D:/dlls/7z.dll', '.'), ('D:/dlls/7-zip.dll', '.'), ('D:/dlls/libcrypto-1_1.dll', '.'), ('D:/dlls/libcrypto-1_1-x64.dll', '.'), ('D:/dlls/libcurl.dll', '.'), ('D:/dlls/libpng3.dll', '.'), ('D:/dlls/libpng12.dll', '.'), ('D:/dlls/libssl-1_1.dll', '.'), ('D:/dlls/libssl-1_1-x64.dll', '.'), ('D:/dlls/libui.dll', '.'), ('D:/dlls/pcre.dll', '.'), ('D:/dlls/pcre3.dll', '.'), ('D:/dlls/pcre32.dll', '.'), ('D:/dlls/pcre64.dll', '.'), ('D:/dlls/pdcurses32.dll', '.'), ('D:/dlls/pdcurses64.dll', '.'), ('D:/dlls/png.dll', '.'), ('D:/dlls/SDL2.dll', '.'), ('D:/dlls/SDL2_ttf.dll', '.'), ('D:/dlls/sqlite3_32.dll', '.'), ('D:/dlls/sqlite3_64.dll', '.'), ('D:/dlls/zlib1.dll', '.')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
