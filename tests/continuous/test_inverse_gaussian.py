"""Test GeometricBrownianMotion."""
# flake8: noqa
import pytest

from stochastic.continuous import InverseGaussianProcess


def test_inverse_gaussian_process_str_repr(mean_func, scale, t):
    instance = InverseGaussianProcess(mean_func, scale, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_inverse_gaussian_process_sample(mean_func, scale, t, n, zero):
    instance = InverseGaussianProcess(mean_func, scale, t)
    s = instance.sample(n, zero)
    assert len(s) == n + int(zero)

def test_inverse_gaussian_process_sample_invalid(mean_func_invalid, scale, t, n, zero):
    with pytest.raises(ValueError):
        instance = InverseGaussianProcess(mean_func_invalid, scale, t)
        s = instance.sample(n, zero)

def test_inverse_gaussian_process_sample_at(mean_func, scale, t, times):
    instance = InverseGaussianProcess(mean_func, scale, t)
    s = instance.sample_at(times)
    assert len(s) == len(times)
