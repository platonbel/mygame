import pygame

class Group():
    def __init__(self):
        self._objects = set()
    
    def add(self, _object):
        self._objects.add(_object)

    def remove(self, _object):
        self._objects.remove(_object)

    def has(self, _object):
        return _object in self._objects

    def objects(self):
        return self._objects

    def update(self, *args):
        tuple(map(lambda _object: _object.update(*args), self._objects))