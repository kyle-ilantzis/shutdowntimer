from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [], includes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base, targetName="shutdowntimer.exe")
]

setup(name='shutdowntimer',
      version = '1.0',
      description = 'Use a timer to shutdown your computer',
      options = dict(build_exe = buildOptions),
      executables = executables)
