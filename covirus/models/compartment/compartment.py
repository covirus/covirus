from sklearn.base import BaseEstimator
from abc import ABC, abstractmethod


class CompartimentModel(ABC, BaseEstimator):
    @abstractmethod
    def plot(self):
        pass
