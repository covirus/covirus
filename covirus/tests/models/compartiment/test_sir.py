from covirus.models.compartiment import SIR, CompartimentModel
import numpy as np

def test_sir_model():
    #Initialize
    pop_size, n_infected, n_recovered, contact_rate, mean_recovery_rate = 1000, 1, 0, 0.2, 1/10
    days = 10
    sir_model = SIR(pop_size, n_infected, n_recovered, contact_rate, mean_recovery_rate, days)
    sir_model.fit()

    #Assert
    assert isinstance(sir_model, CompartimentModel)
    assert isinstance(sir_model.S, np.ndarray)
    assert isinstance(sir_model.I, np.ndarray)
    assert isinstance(sir_model.R, np.ndarray)
    assert is_number(sir_model.S[0])
    assert is_number(sir_model.I[0])
    assert is_number(sir_model.R[0])


def is_number(v):
    try:
        float(v)
        return True
    except:
        return False