#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import multiprocessing
import time


def calcular_factorial(num: int) -> int:
    """
    Computes the factorial of the given integer.

    Args:
        num (int): number to  be calculated.

    Returns:
        (int): The factorial of nun.
    """
    return math.factorial(num)


def run_sequential(nums: list[int]):
    """
    Computes the factorial of each number sequentially
    and prints the total execution time.

    Args:
        nums (list[int]): List of ints to process.
    """
    print("Sequential mode:")
    start = time.time()
    results = [calcular_factorial(n) for n in nums]
    end = time.time()
    print(f"Total sequential time: {end - start:.4f}s")


def run_multiprocessing(nums: list[int]):
    """
    Computes the factorial of each number using multiprocessing
    and prints the total execution time.

    Args:
        nums (list[int]): List of ints to process.
    """
    print("Multiprocessing mode:")
    start = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(calcular_factorial, nums)
    end = time.time()
    print(f"Total multiprocessing time: {end - start:.4f}s")


nums = [150000, 200000, 250000, 300000, 350000, 400000]

if __name__ == "__main__":
    run_sequential(nums)
    run_multiprocessing(nums)
