"""
Find nearest neighbors in multi-dimensional space,
with a friendly API.
"""
from scikits.ann import kdtree
from numpy import array

class Topospace(list):

    def __init__(self):
        self._scikitA = None

    def as_array(self):
        return array(self)

    def nearest(self, location, count = 1):
        if not self._scikitA:
            self._scikitA = kdtree(self.as_array())
        (index_array, distance_array,) = self._scikitA.knn(location, count)
        count = len(index_array[0])
        results = []
        for x in range(count):
            results.append((self[index_array[0][x]], distance_array[0][x]))

        return results
