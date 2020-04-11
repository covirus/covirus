from sklearn.base import BaseEstimator
from abc import ABC, abstractmethod


class CompartmentModel(ABC, BaseEstimator):
    @abstractmethod
    def plot(self):
        pass
