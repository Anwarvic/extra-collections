from numpy import sort
class Extra:
    """Extra is the package interface which means that all objects inherits from
    this class. So, each object in this pacakge is an Extra object in the fisrt
    place."""
    __name__ = "extra.Extra()"


    def _validate_item(self, item):
        """
        Makes sure the input variable type can be processed. The main use for 
        this method is to make sure we can't create nested objects from the 
        package.
        
        Parameters
        ----------
        item: object
            The input object of any type.
        
        Raises
        -------
        ValueError: If `item` is `None`
        TypeError: If `item` is an `Extra` object.
        """
        if item is None:
            raise ValueError(
                f"Can't use `None` as an element within `{self.__name__}`!!"
            )
        elif isinstance(item, Extra):
            raise TypeError(
                f"Can't use `{self.__name__}` with `{item.__name__}`!!"
              )
