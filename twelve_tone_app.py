'''
CREATED BY: Gregory P. Nikol
MOST RECENT UPDATE: June 19, 2019

This script provides a GUI interface for a Twelve Tone Matrix.

It has been adapted from a previous - terminal based application
to work as a Python Kivy Application.

To run KIVY files effectively the following must be run in the command line:
pip --upgrade pip wheel setuptools
pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
pip install kivy.deps.gstreamer
pip install kivy.deps.angle
pip install kivy

'''
import kivy, os, sys
kivy.require('1.10.1')

import kivy.uix.settings

from TTWidgets import RootWidget

from kivy.app import App
from kivy.logger import Logger

def resourcePath():
    '''
    Returns path containing content - either locally or in pyinstaller tmp file
    ***ADDED TO HELP MAKE SINGLE EXE FILE WITH PYINSTALLER***
    * Reference "Twelve Tone Toolbelt.spec" for EXE build file
    * python -m PyInstaller "Twelve Tone Toolbelt.spec"
    '''
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS)

    return os.path.join(os.path.abspath("."))

class TwelveToneApp(App):
    '''
    This class inherits from kivy's app class.
    This is where the application's life cycle begins.
    '''
    def build(self):
        '''
        This method contains some items that need to
        be used and initialized in the app.
        '''
        self.myapp = RootWidget()
        return self.myapp
    
    def on_stop(self):
        '''
        Tests for safe close.
        This will likely contain more function later as the app evolves.
        '''
        Logger.critical('Goodbye!')

if __name__ == "__main__":
    kivy.resources.resource_add_path(resourcePath()) # ADD FOR RESOURCEPATH
    TwelveToneApp().run()