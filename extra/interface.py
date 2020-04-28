class Extra:
    
    def __name__(self):
        return "extra.Extra()"
    

    def _validate_item(self, item):
        if item is None:
            raise ValueError(\
                f"Can't use `None` as an initial value for {self.__name__()}!!")
        elif isinstance(item, Extra):
            raise TypeError(\
            f"Can't create {self.__name__()} object using {item.__name__()}!!")
