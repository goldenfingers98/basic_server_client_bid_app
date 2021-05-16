from abc import abstractmethod
import sys
import os
from lib.repository.Repository import Repository
from datetime import datetime


class Entity:
    FILE = ''
    PATH = f'{sys.path[0]}{os.sep}public{os.sep}'+'{}'
    def __init__(self):
        pass
        
    @classmethod
    def serialize(cls,string):
        """
            Transform a file entry to Entity.
        """
        attributes = []
        # Getting the class attributes params
        params = list(cls.__slots__.values())
        for item,attr in zip(string.split('\t'),params):
            if issubclass(attr['type'],Entity): # That means if the attribute is an Entity
                if item == 'None':
                    obj = None
                else:
                    # Preparing the entity
                    attr_params = list(attr['type'].__slots__.values())
                    # Preparing the id
                    id = attr_params[0]['type'](item)
                    # obj = attr['type'](id)
                    obj = Repository.repositoryMap[attr['type']].findById(id)
                    # # Synchronize the attribute
                    # Repository.repositoryMap[type(obj)].synchronize(obj)
                # Pushing the attribute
                attributes.append(obj)
            elif attr['type'] == datetime:
                 attributes.append(datetime.strptime(item,"%Y-%m-%d %H:%M:%S"))
            else:
                # Pushing the attribute
                attributes.append(attr['type'](item))
        return cls.__constructor(*attributes)

    @classmethod
    def __constructor(cls,*args):
        obj = cls()
        # Getting the class attributes params
        params = list(cls.__slots__.values())
        # 
        for attr,arg in zip(params,args):
            setter=getattr(obj,attr['setter'])
            setter(arg)
        return obj

    def update(self,obj):
        # Getting Class attributes params
        params = list(self.__slots__.values())
        for param in params:
            getattr(self,param['setter'])(getattr(obj,param['getter'])())