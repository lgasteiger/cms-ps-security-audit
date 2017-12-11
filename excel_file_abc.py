'''
 ##############################################################################################
 # excel-file-abc.py - this abstract base class shall provide the contract on how to implement
 #                     Python solutions for processing Microsoft Excel files. It shall use the 
 #                     openpyxl library.
 # 
 # Date: 2017-12-07
 #
 # Author: Leo Gasteiger
 ##############################################################################################
'''

from abc import ABC, abstractmethod

class Excel_File_ABC(ABC):

  __counter = 0
  
  @abstractmethod
  def __init__(self, hebprd_dir_path, fcfsprd_dir_path, cms_scripts_rept_dir_path):
    tyep(self).__counter += 1
    self.__hebprd_dir_path = hebprd_dir_path
    self.__fcfsprd_dir_pat = fcfsprd_dir_path
    self.__cms_scripts_rept_dir_path = cms_scripts_rept_dir_path
  #end __init__
  
  @classmethod
  def Excel_File_Instances(cls):
    return cls.__counter
  #end Excel_File_Instances
  
  @property
  def hebprd_dir_path(self):
    return self.__hebprd_dir_path    
  #end hebprd_dir_path getter
  
  
  @hebprd_dir_path.setter
  def hebprd_dir_path(self, new_hebprd_dir_path):
    self.__hebprd_dir_path = new_hebprd_dir_path
  #end hebprd_dir_path setter
#end Excel_File_ABC class
