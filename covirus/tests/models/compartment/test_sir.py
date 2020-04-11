from covirus.models.compartment import SIR, CompartimentModel
import numpy as np


def test_sir_model():
    # Initialize
    pop_size, n_infected, n_recovered, contact_rate, mean_recovery_rate = (
        1000,
        1,
        0,
        0.2,
        1 / 10,
    )
    days = 10
    sir_model = SIR()
    sir_model.fit(pop_size, n_infected, n_recovered, contact_rate, mean_recovery_rate)
    S, I, R = sir_model.predict(days=10)

    # Assert
    assert isinstance(sir_model, CompartimentModel)
    assert isinstance(S, np.ndarray)
    assert isinstance(I, np.ndarray)
    assert isinstance(R, np.ndarray)
    assert is_number(S[0])
    assert is_number(I[0])
    assert is_number(R[0])


def is_number(v):
    try:
        float(v)
        return True
    except:
        return False
