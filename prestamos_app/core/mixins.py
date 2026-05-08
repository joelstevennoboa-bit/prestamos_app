class SerializableMixin:

    def to_dict(self):
        return self.__dict__
    
    