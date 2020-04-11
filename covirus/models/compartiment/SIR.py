from .compartiment import CompartimentModel
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


class SIR(CompartimentModel):
    def __init__(self, pop_size=1000, n_infected=1, n_recovered=0, contact_rate=0.2, mean_recovery_rate=1/10, days=10):
        self.pop = pop_size
        self.s0 = pop_size - n_infected - n_recovered
        self.i0 = n_infected
        self.r0 = n_recovered
        self.days = days
        self.beta = contact_rate
        self.gamma = mean_recovery_rate

    def fit(self):
        ret = self.integrate_diff_SIR_equations_over_t()
        self.S, self.I, self.R = ret.T

    def predict(self):
        return self.S, self.I, self.R

    def integrate_diff_SIR_equations_over_t(self):
        self.y0 = self.s0, self.i0, self.r0
        self.t = np.linspace(0, self.days, self.days)
        return odeint(self.derivate, self.y0, self.t, args=(self.pop, self.beta, self.gamma))

    def derivate(self, y, days, pop, beta, gamma):
        S, I, R = y
        dSdt = self.get_Sdt(S, I, pop, beta)
        dIdt = self.get_Idt(S, I, pop, beta, gamma)
        dRdt = self.get_Rdt(pop, gamma)
        return dSdt, dIdt, dRdt

    @staticmethod
    def get_Sdt(S, I, pop, beta):
        return -beta * S * I / pop

    @staticmethod
    def get_Idt(S, I, pop, beta, gamma):
        return beta * S * I / pop - gamma * I

    @staticmethod
    def get_Rdt(pop, gamma):
        return gamma * pop

    def plot(self):
        ax = self.initialize_plot()
        ax = self.plot_SIR(ax)
        ax = self.format_plot(ax)
        plt.show()

    @staticmethod
    def initialize_plot():
        fig = plt.figure(facecolor='w')
        ax = fig.add_subplot(111, axisbelow=True)
        return ax

    def plot_SIR(self, ax):
        ax.plot(self.t, self.S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
        ax.plot(self.t, self.I/1000, 'r', alpha=0.5, lw=2, label='Infected')
        ax.plot(self.t, self.R/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
        return ax

    def format_plot(self, ax):
        ax.set_xlabel('Time /days')
        ax.set_ylabel('Number (1000s)')
        ax.set_ylim(0,1.2)
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        ax.grid(b=True, which='major', c='w', lw=2, ls='-')
        legend = ax.legend()
        legend.get_frame().set_alpha(0.5)
        for spine in ('top', 'right', 'bottom', 'left'):
            ax.spines[spine].set_visible(False)
        return ax



