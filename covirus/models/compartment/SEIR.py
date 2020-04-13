from .compartment import CompartmentModel
from scipy.integrate import odeint
import pandas as pd
import matplotlib.pyplot as plt

class SEIR(CompartmentModel):
    def fit(
        self,
        pop_size: int,
        n_exposed: float,
        n_infected: int,
        n_recovered: int,
        infection_probability: float,
        removal_probability: float,
        incubation_period: float,

    ):
        self.pop = pop_size
        self.S0 = pop_size - n_infected - n_recovered - n_exposed
        self.E0 = n_exposed
        self.I0 = n_infected
        self.R0 = n_recovered
        self.beta = infection_probability
        self.gamma = removal_probability
        self.alpha = 1/incubation_period

    def predict(self, days, plot=False) -> pd.DataFrame:
        self.t = range(days)
        self.y0 = self.S0, self.E0, self.I0, self.R0
        S, E, I, R = self.run()
        self.results = pd.DataFrame({'S': S, 'E': E, 'I': I, 'R': R}, index=self.t)
        if plot:
            self.plot()
        return self.results["S"], self.results["E"], self.results["I"], self.results["R"]


    def run(self):
        ret = self.integrate_diff_equations(self.y0)
        return ret.T

    def integrate_diff_equations(self, y0):
        return odeint(
            self.derivate, y0, self.t, args=(self.pop, self.beta, self.gamma, self.alpha)
        )


    def derivate(self, y, t, N, beta, gamma, alpha):
        S, E, I, R = y
        dSdt = -beta * S * I / N
        dEdt = -dSdt - alpha*E
        dIdt = alpha*E - gamma*I
        dRdt = gamma * I
        return dSdt, dEdt, dIdt, dRdt


    def plot(self):
        plt.style.use('ggplot')
        self.results[['E', 'I']].plot(figsize=(8,6), fontsize=20, logy=True)
        params_title = (
            f'SEIR($\gamma$={self.gamma}, $\\beta$={self.beta}, $\\alpha$={1/self.alpha}, $N$={self.pop}, '
            f'$E_0$={self.E0}, $I_0$={self.I0}, $R_0$={self.R0})'
        )
        plt.title(f'Model Parameters:\n' + params_title,
                fontsize=20)
        plt.legend(['Exposed', 'Infected'], fontsize=20)
        plt.xlabel('Days', fontsize=20)
        plt.ylabel('People', fontsize=20)
        plt.show()