# Remote Development Project Report

**Student Name**: Dai Kaixuan  
**Student ID**: [ZY2557202]

## 1. Project Overview

This project practices command line operations, Markdown documentation, and matrix multiplication implementation. The main task is to implement matrix multiplication in Python, verify the correctness of the algorithm, and document the process in a Markdown report.

## 2. System Configuration

Since this project was developed on macOS, I used macOS command line tools to collect system information.

| Item | Command Used | Result |
|---|---|---|
| CPU Model | `sysctl -n machdep.cpu.brand_string` | Apple M1 |
| Memory Size | `system_profiler SPHardwareDataType \| grep "Memory"` | 8 GB |
| Operating System | `sw_vers` | macOS 14.7.4 |
| Kernel Version | `uname -a` | Darwin 23.6.0 |
| Compiler Version | `gcc --version` | Apple clang version 16.0.0 |
| Python Version | `python --version` | Python 3.9.13 |
## 3. Python Language Implementation

The Python implementation is stored in `assignment1/matrix_mul.py`.

The program implements matrix multiplication using the standard triple-loop algorithm. If matrix `A` has shape `m x n` and matrix `B` has shape `n x p`, then the output matrix `C` has shape `m x p`.

For each element `C[i][j]`, the algorithm multiplies the `i`-th row of matrix `A` with the `j`-th column of matrix `B`, and then sums the products.

The mathematical expression is:

```text
C[i][j] = sum(A[i][k] * B[k][j])
```

The core part of the Python implementation is:

```python
for i in range(m):
    for j in range(p):
        total = 0
        for k in range(n):
            total += A[i][k] * B[k][j]
        C[i][j] = total
```

This implementation does not use built-in matrix multiplication functions for the main algorithm. NumPy is only used later to verify the correctness of the result.

### Execution Command

The Python program can be executed with:

```bash
python assignment1/matrix_mul.py --size 3
```

The `--size` argument controls the size of the square matrices used for NumPy verification and benchmarking.

## 4. Algorithm Verification

The correctness of the matrix multiplication algorithm was verified in two ways.

First, I used a small 2 x 2 matrix example. The input matrices were:

```text
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]
```

According to the definition of matrix multiplication, the expected result is:

```text
[[19, 22],
 [43, 50]]
```

The program output was:

```text
Small matrix verification:
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
Result = [[19, 22], [43, 50]]
Expected = [[19, 22], [43, 50]]
Correct: True
```

This shows that the implementation correctly handles a simple manually verified case.

Second, I compared my implementation with NumPy matrix multiplication. NumPy was only used as a reference result, not as the main implementation.

For matrix size 3 x 3, the output was:

```text
NumPy verification:
Matrix size: 3 x 3
Correct: True
```

Since the result of my implementation matched NumPy's result, the algorithm passed the NumPy-based correctness check.

## 5. Python Benchmark

The program also measures the execution time of the pure Python implementation.

For matrix size 3 x 3, the benchmark result was:

```text
Python benchmark:
Matrix size: 3 x 3
Execution time: 5.708999999964881e-06 seconds
```

This is a very small test case, so the execution time is extremely short. Larger matrix sizes are more useful for observing performance differences between different programming languages or implementations.

