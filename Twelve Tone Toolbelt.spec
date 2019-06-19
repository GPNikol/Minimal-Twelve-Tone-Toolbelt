# -*- mode: python -*-
from kivy.deps import sdl2, glew

block_cipher = None


a = Analysis(['twelve_tone_app.py'],
             pathex=['C:\\Users\\gnikol\\Documents\\Python Dev\\TwelveTone-Minimal\\Minimal-Twelve-Tone-Toolbelt',
             '.\\MyHiddenImports'],
             binaries=None,
             datas=None,
             hiddenimports=['MyHiddenImports'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
a.datas += [('twelvetone.kv', './twelvetone.kv', 'DATA')]
exe = EXE(pyz, Tree('.'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='Twelve Tone Toolbelt',
          debug=False,
          strip=False,
          upx=True,
          console=False, icon='.\\matrix.ico')
