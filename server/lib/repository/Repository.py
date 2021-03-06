from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
from threading import Lock

def replace_line(file_path, index, subst):
    """
        Replaces a line pattern with subst.
    """
    # Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                if index > 0:
                    new_file.write(line)
                    index -= 1
                elif index == 0:
                    new_file.write(subst)
                    index -= 1
                else:
                    new_file.write(line)
    # Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)

class Repository:
    PATH = ''
    HEADERS = ''
    entities = []
    __Lock = Lock()
    CLASS = None
    repositoryMap = {}

    def __init__(self):
        type(self).PATH=type(self).CLASS.PATH.format(type(self).CLASS.FILE)
        # type(self).CLASS = className
        type(self).HEADERS = '\t'.join(type(self).CLASS.HEADERS)+'\n'
        Repository.repositoryMap[type(self).CLASS] = self
        file = None
        try:
            # Getting permission
            type(self).__Lock.acquire()
            file = open(type(self).PATH,'r')
            type(self).entities = [type(self).CLASS.serialize(item.strip('\n')) for item in file.readlines()[1:]]
            # type(self).entities.append(None)
        except Repository.RepositoryException as err:
            raise err
        except Exception as err:
            file = open(type(self).PATH,'w')
            file.write(type(self).HEADERS)
        finally:
            file.close()
            type(self).__Lock.release() # Release the critical ressource        

    @classmethod
    def save(cls,obj):
        cls.__Lock.acquire() # Getting permission
        if(obj in cls.entities): # If the object exists already in the file
            index = cls.entities.index(obj)+1
            replace_line(cls.PATH,index,str(obj))
        else:
            try:
                file = open(cls.PATH,'a')
            except:
                file = open(cls.PATH,'w')
            finally:
                file.write(str(obj))
                cls.entities.append(obj)
                file.close()
        cls.__Lock.release() # Release the critical ressource   

    @classmethod
    def delete(cls,obj):
        if(obj in cls.entities):# If the object exists already in the file
            cls.__Lock.acquire() # Getting permission
            index = cls.entities.index(obj)
            replace_line(cls.PATH,index+1,"")
            cls.entities.pop(index)
            cls.__Lock.release() # Release the critical ressource  
        else:
            raise Repository.RepositoryException('Entity not found.')

    @classmethod
    def findById(cls,id):
        # Getting Class attributes params
        params = list(cls.CLASS.__slot__.values())
        # Seeking the item
        for item in cls.entities:
            if item != None:
                if getattr(item,params[0]['getter'])() == id:
                    return item
        raise Repository.RepositoryException('Entity not found.')
        
    class RepositoryException(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)
