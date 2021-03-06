import time

import pytest

from clscreate_cython import Example as Example_cy
from clscreate_rs import Example as Example_rs

class Example:
    def __init__(self):
        self.a = 4
        self.b = "Test"

@pytest.mark.benchmark(
    timer=time.perf_counter, disable_gc=True, warmup=False,
)
def test_Example_rust(benchmark):
    benchmark(Example_rs)

@pytest.mark.benchmark(
    timer=time.perf_counter, disable_gc=True, warmup=False,
)
def test_Example_cython(benchmark):
    benchmark(Example_cy)

@pytest.mark.benchmark(
    timer=time.perf_counter, disable_gc=True, warmup=False,
)
def test_Example_python(benchmark):
    benchmark(Example)
