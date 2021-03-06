import csv
import random
import inspect


def get_classes(mod):
    """Return a list of all classes in module 'mod'"""
    return [name for name, obj in inspect.getmembers(mod) if inspect.isclass(obj) if name[0].isupper() and name[0].isalpha()]


#if __name__ == "__main__":
    #print(get_classes(random))
    #print(get_classes(csv))