from abc import ABCMeta, abstractmethod

"""
.. module:: point
   :platform: Unix, Windows
   :synopsis: implementation of points of n-dimensions (e.g, ideal point, nadir point, etc.

.. moduleauthor:: Antonio J. Nebro <antonio@lcc.uma.es>
"""


class Point:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self) -> []:
        pass

    @abstractmethod
    def update(self, vector: []) -> None:
        pass


class IdealPoint(Point):
    def __init__(self, dimension: int):
        self.point = dimension * [float("inf")]

    def get(self):
        return self.point

    def update(self, vector: []) -> None:
        self.point = [y if x > y else x for x, y in zip(self.point, vector)]
