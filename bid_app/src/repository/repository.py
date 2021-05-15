from abc import abstractclassmethod
import sys
import os
sys.path.insert(0,os.sep.join(sys.path[0].split(os.sep)[:-2]))
from src.models.models import *


class Repository:
    __PATH = ''

    @abstractclassmethod
    def __init__(self,className):
        self.__class = className

    def save(self,obj):
        file = open()