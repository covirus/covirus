from covirus.models.compartment import SEIR, CompartmentModel
import pandas as pd
from covirus.tests.models.utils import is_number


def test_seir_model():
    # Initialize
    N = 13_000_000
    E0, I0, R0 = 0, 152, 2
    beta, gamma, alpha = 1.75, 0.5, 5
    days = 4

    # Run
    sir_model = SEIR()
    sir_model.fit(N, E0, I0, R0, beta, gamma, alpha)
    S, E, I, R = sir_model.predict(days=days)

    # Assert
    assert isinstance(sir_model, CompartmentModel)
    assert isinstance(S, pd.Series)
    assert isinstance(E, pd.Series)
    assert isinstance(I, pd.Series)
    assert isinstance(R, pd.Series)
    assert is_number(S[0])
    assert is_number(E[0])
    assert is_number(I[0])
    assert is_number(R[0])

    # Values
    expected_S = [12999846.0, 12999624.93174401, 12999435.52653244, 12999227.08508175]
    expected_E = [0.0, 199.29874694, 334.84248468, 463.60144161]
    expected_I = [152.0, 110.60586489, 110.34960838, 130.47433841]
    expected_R = [2.0, 65.16364416, 119.28137451, 178.83913824]

    variables_to_validate = [
        zip(S, expected_S),
        zip(E, expected_E),
        zip(I, expected_I),
        zip(R, expected_R),
    ]
    for variables in variables_to_validate:
        for real, expected in variables:
            real = round(real, 8)
            assert real == expected
