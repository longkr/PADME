#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class AnalysisFile:
===================

  Dummy class to record what is happening to files in PADME analysis.


  Class attributes:
  -----------------
  __Debug   : Boolean: set for debug print out
  instances : List of instances if the WorkPackage class.
      
  Instance attributes:
  --------------------
   _FileName   = File name relative to _FilePath
   _FilePath   = Path to file
   _ReadStatus = Boolean, True if file is read, False if file has not
                 been read, None if not initialised

    
  Methods:
  --------
  Built-in methods __new__, __repr__ and __str__.
      __init__: Creates instance and prints some parameters if __Debug is 
                True.
      __repr__: One liner with call.
      __str__ : Dump of attributes.


  I/o and data-constructor methods:


  Get/set methods:
    setFilePath      : Sets _FilePath.  Checks path exisits.
    setFileName      : Sets _FileName.  Checks that _FilePath/_FileName exists
    setFileReadStatus: Sets read status.
    getFilePath      : Returns file path
    getFileName      : Returns file name
    getReadStatus    : Returns _ReadStatus


  Exceptions:
    NoFilePathProvided     : File path not provided
    NonExistantPath        : File path does not exist
    NoFileNameProvided     : File name not provided
    NonExistantAnalysysFile: File name (at file path) does not exist
    ReadStatusNotBoolean   : Read status not boolean


Created on Sat 16Jul22. Version history:
----------------------------------------
 1.0: 16Jul22: First implementation

@author: kennethlong
"""

import os

class AnalysisFile:
    __Debug    = False
    __instances  = []


#--------  "Built-in methods":
    def __init__(self, _Fpath=None, _Fname=None):

        if AnalysisFile.__Debug:
            print(" AnalysisFile.__init__: file path, file name:", \
                  _Fpath, _Fname)
            
        self.setFilePath(_Fpath)
        self.setFileName(_Fname)
        self.setFileReadStatus(False)

        AnalysisFile.__instances.append(self)

    def __repr__(self):
        return "Analysis(FileName, FilePath)"

    def __str__(self):
        _filename = self.getFileName()
        _filepath = self.getFilePath()
        _ReadStatus     = self.getReadStatus()
        
        if _filename == None:
            _filename = "None"
        if _filepath == None:
            _FilePath = None
        FullPath = _filepath + _filename
        
        print(" AnalyisisFile:", FullPath, ": \n", \
              "          ----> ReadStatus:", _ReadStatus)

        return "     <--- Done."
    
#--------  I/o and data-constructor methods:


#--------  Get/set methods:
    def setFilePath(self, _Fpath=None):

        if AnalysisFile.__Debug:
            print(" AnalysisFile.setFilePath: file path:", _Fpath)
            
        if _Fpath == None:
            raise NoFilePathProvided( \
                'Analysis file path required; execution termimated.')
        elif not os.path.isdir(_Fpath):
            raise NonExistantPath('Analysis path', _Fpath,  \
                                  ' does not exist; execution termimated.')

        self._FilePath = _Fpath
    
    def setFileName(self, _Fname=None):
        
        if AnalysisFile.__Debug:
            print(" AnalysisFile.setFileName: file name:", _Fname)
            
        _filename = None
        
        if _Fname == None or not isinstance(_Fname, str):
            raise NoFilenameProvided( \
                'Analysis file name required; execution termimated.')

        _fullpath = os.path.join(self.getFilePath(), _Fname)
        
        if AnalysisFile.__Debug:
            print("     ----> Full path:", _fullpath)
        
        if not os.path.isfile(_fullpath):
            raise NonExistantAnalysysFile('Analysis file', _Fname, \
                                  ' does not exist; execution termimated.')

        self._FileName = _Fname

    def setFileReadStatus(self, _ReadStatus=None):
        if not isinstance(_ReadStatus, bool):
            raise ReadStatusNotBoolean()
        self._ReadStatus = _ReadStatus

    def getFilePath(self):
        return self._FilePath

    def getFileName(self):
        return self._FileName

    def getReadStatus(self):
        return self._ReadStatus

    
#--------  Print methods:


#--------  Processing methods
                
        
#--------  Exceptions:
class NoFilePathProvided(Exception):
    pass

class NonExistantPath(Exception):
    pass

class NoFileNameProvided(Exception):
    pass

class NonExistantAnalysysFile(Exception):
    pass

class ReadStatusNotBoolean(Exception):
    pass
