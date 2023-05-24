class Singleton(type):
    """This class storage single classes."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Implement the singleton logic"""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
