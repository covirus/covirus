from sklearn.base import BaseEstimator
from scipy.integrate import odeint
from ..plotable import Plotable


class CompartmentModel(BaseEstimator, Plotable):
    def integrate_diff_equations(self, y0, t, *args):
        return odeint(self.derivate, y0, t, args=args).T
