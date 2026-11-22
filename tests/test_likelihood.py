from bayesian_random_effects.likelihood import log_likelihood


def test_likelihood_import():
    assert log_likelihood() == 42.0