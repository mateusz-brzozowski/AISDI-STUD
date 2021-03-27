import pytest
import pytest_benchmark
import time

from quicksort_recursive import quicksort, inbuild
from insertion_sort import insertion_sort
from import_words import import_words
from import_numbers import generate_sorted_numbers

FUNCTIONS = {quicksort, insertion_sort, inbuild}
SIZES = {1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000}
TEXT = import_words("pan-tadeusz.txt", 10000)
NUMBERS = generate_sorted_numbers(10000)


def test_import_text():
    assert import_words("pan-tadeusz.txt", 4) == [
        "Adam", "Mickiewicz", "Pan", "Tadeusz"]


def test_import_sorted_numbers():
    assert generate_sorted_numbers(6) == [1, 2, 3, 4, 5, 6]


@pytest.mark.parametrize("functions", FUNCTIONS)
def test_sorted_numbers(functions):
    assert functions(NUMBERS) == NUMBERS


@pytest.mark.parametrize("functions", FUNCTIONS)
def test_sorted_text(functions):
    assert functions(TEXT) == sorted(TEXT)


@pytest.mark.benchmark(
    group="Benchmark Sortowania"
)

@pytest.mark.parametrize("functions", FUNCTIONS)
@pytest.mark.parametrize("sizes", SIZES)
def test_time(functions, sizes, benchmark):
    benchmark.extra_info["functions"] = functions.__name__
    benchmark.extra_info["sizes"] = sizes
    benchmark(functions, TEXT[:sizes])
