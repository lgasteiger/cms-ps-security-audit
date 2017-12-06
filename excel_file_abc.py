'''
 ##############################################################################################
 # excel-file-abc.py - this abstract base class shall provide the contract on how to implement
 #                     Python solutions for processing Microsoft Excel files. It shall use the 
 #                     openpyxl library.
 # 
 # Date: 2017-12-06
 #
 # Author: Leo Gasteiger
 ##############################################################################################
'''

from abc import ABC, abstractmethod

class Excel_File_ABC(ABC):

  __counter = 0
  
  @classmethod
  def Excel_File_Instances(cls):
    return cls.__counter
  #end Excel_File_Instances
#end Excel_File_ABC class
