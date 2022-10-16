#/usr/bin/env bash

export doctests="fizzbuzz fizzbuzz_static"
for doctest in ${doctests}; do
    test="src/${doctest}.py"
    echo "doctest: ${test}"
    python3 -m doctest "${test}"
done

export pytests="fizzbuzz fizzbuzz_static"
for pytest in ${pytests}; do
    test="tests/test_${pytest}.py"
    echo "pytest: ${test}"
    pytest -q "${test}"
done
