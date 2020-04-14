from .compartment import CompartmentModel
import pandas as pd
import numpy as np


class SIR(CompartmentModel):
    """SIR modelA simple mathematical description of the spread of a disease in a population is the so-called SIR model, which divides the (fixed) population of N individuals into three "compartments" which may vary as a function of time, t:

        S(t) are those susceptible but not yet infected with the disease;
        I(t) is the number of infectious individuals;
        R(t) are those individuals who have recovered from the disease and now have immunity to it.
        
        The SIR model describes the change in the population of each of these compartments in terms of two parameters, β and γ.
        β - describes the effective contact rate of the disease: an infected individual comes into contact with βN other individuals per unit time (of which the fraction that are susceptible to contracting the disease is S/N). 
        γ -  is the mean recovery rate: that is, 1/γ is the mean period of time during which an infected individual can pass it on.
    
        Reference: https://scipython.com/book/chapter-8-scipy/additional-examples/the-sir-epidemic-model/
    """

    def fit(
        self,
        pop_size: int,
        n_infected: int,
        n_recovered: int,
        contact_rate: float,
        mean_recovery_rate: float,
    ):
        """Fits the SIR Model

            Args:
                pop_size (int): Population size of the region being projected
                n_infected (int): Current number of infected in the region being projected
                n_recovered (int): Current number of recovered in the region being projected
                contact_rate (float) (β): β, contact rate of the disease: an infected individual 
                                        comes into contact with βN other individuals per unit time (of which the fraction that are susceptible to contracting the disease is S/N).
                mean_recovery_rate (float): γ, Passed in the form of 1/γ, where:
                                                γ is the mean recovery rate: that is
                                                1/γ is the mean period of time during which an infected individual can pass it on.
        """
        self.pop = pop_size
        self.s0 = pop_size - n_infected - n_recovered
        self.i0 = n_infected
        self.r0 = n_recovered
        self.beta = contact_rate
        self.gamma = mean_recovery_rate

    def predict(self, days: int = 10, plot=False):
        self.initialize_variables(days)
        self.S, self.I, self.R = self.integrate_diff_equations(
            self.y0, self.t, self.pop, self.beta, self.gamma
        )
        self.results = pd.DataFrame(
            {"S": self.S, "I": self.I, "R": self.R}, index=self.t
        )
        return self.results.S, self.results.I, self.results.R

    def initialize_variables(self, days):
        self.days = days
        self.t = np.linspace(0, self.days, self.days)
        self.y0 = self.s0, self.i0, self.r0

    def derivate(self, y, days, pop, beta, gamma):
        S, I, R = y
        dSdt = self.get_Sdt(S, I, pop, beta)
        dIdt = self.get_Idt(S, I, pop, beta, gamma)
        dRdt = self.get_Rdt(I, gamma)
        return dSdt, dIdt, dRdt

    @staticmethod
    def get_Sdt(S, I, pop, beta):
        return -beta * S * I / pop

    @staticmethod
    def get_Idt(S, I, pop, beta, gamma):
        return beta * S * I / pop - gamma * I

    @staticmethod
    def get_Rdt(I, gamma):
        return gamma * I

    def plot(self, save=False):
        super().plot(
            "Time / days", "Number (1000s)", save=save,
        )

    def plot_model(self, ax):
        ax.plot(self.t, self.S / 1000, "b", alpha=0.5, lw=2, label="Susceptible")
        ax.plot(self.t, self.I / 1000, "r", alpha=0.5, lw=2, label="Infected")
        ax.plot(
            self.t, self.R / 1000, "g", alpha=0.5, lw=2, label="Recovered with immunity"
        )
        return ax
