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
    days = 4

    # Run
    sir_model = SIR()
    sir_model.fit(pop_size, n_infected, n_recovered, contact_rate, mean_recovery_rate)
    S, I, R = sir_model.predict(days=days)

    # Assert
    assert isinstance(sir_model, CompartimentModel)
    assert isinstance(S, np.ndarray)
    assert isinstance(I, np.ndarray)
    assert isinstance(R, np.ndarray)
    assert is_number(S[0])
    assert is_number(I[0])
    assert is_number(R[0])

    expected_S = [999.0, 998.71510673, 998.38979037, 998.01836387]
    expected_I = [1.0, 1.14228371, 1.30470609, 1.49008521]
    expected_R = [0.0, 0.14260956, 0.30550354, 0.49155092]

    variables_to_validate = [zip(S, expected_S), zip(I, expected_I), zip(R, expected_R)]
    for variables in variables_to_validate:
        for real, expected in variables:
            real = real.round(8)
            assert real == expected


def is_number(v):
    try:
        float(v)
        return True
    except:
        return False
