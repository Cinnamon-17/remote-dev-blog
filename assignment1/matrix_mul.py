import argparse
import random
import time


def matrix_multiply(A, B):
    """
    Multiply two matrices A and B using the standard triple-loop algorithm.

    A has shape m x n.
    B has shape n x p.
    The result C has shape m x p.
    """
    m = len(A)
    n = len(A[0])
    p = len(B[0])

    # Check whether the matrix dimensions are valid
    if len(B) != n:
        raise ValueError("Matrix dimensions do not match for multiplication.")

    # Initialize result matrix C with zeros
    C = [[0 for _ in range(p)] for _ in range(m)]

    # Standard matrix multiplication:
    # C[i][j] = sum(A[i][k] * B[k][j])
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += A[i][k] * B[k][j]
            C[i][j] = total

    return C


def generate_matrix(rows, cols, seed=0):
    """
    Generate a random integer matrix for testing.
    """
    random.seed(seed)
    return [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]


def verify_small_case():
    """
    Verify the algorithm using a small 2x2 matrix example.
    """
    A = [
        [1, 2],
        [3, 4]
    ]

    B = [
        [5, 6],
        [7, 8]
    ]

    expected = [
        [19, 22],
        [43, 50]
    ]

    result = matrix_multiply(A, B)

    print("Small matrix verification:")
    print("A =", A)
    print("B =", B)
    print("Result =", result)
    print("Expected =", expected)
    print("Correct:", result == expected)
    print()

    return result == expected


def verify_with_numpy(size):
    """
    Verify the result by comparing it with NumPy matrix multiplication.
    NumPy is only used for verification, not for the main algorithm.
    """
    try:
        import numpy as np
    except ImportError:
        print("NumPy is not installed. Skipping NumPy verification.")
        return None

    A = generate_matrix(size, size, seed=1)
    B = generate_matrix(size, size, seed=2)

    my_result = matrix_multiply(A, B)
    numpy_result = (np.array(A) @ np.array(B)).tolist()

    print("NumPy verification:")
    print("Matrix size:", size, "x", size)
    print("Correct:", my_result == numpy_result)
    print()

    return my_result == numpy_result


def benchmark(size):
    """
    Measure execution time of the pure Python matrix multiplication.
    """
    A = generate_matrix(size, size, seed=3)
    B = generate_matrix(size, size, seed=4)

    start_time = time.perf_counter()
    matrix_multiply(A, B)
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    print("Python benchmark:")
    print("Matrix size:", size, "x", size)
    print("Execution time:", elapsed_time, "seconds")
    print()

    return elapsed_time


def main():
    parser = argparse.ArgumentParser(
        description="Pure Python implementation of matrix multiplication."
    )
    parser.add_argument(
        "--size",
        type=int,
        default=100,
        help="Size of the square matrices used for benchmark and NumPy verification."
    )

    args = parser.parse_args()

    verify_small_case()
    verify_with_numpy(args.size)
    benchmark(args.size)


if __name__ == "__main__":
    main()

