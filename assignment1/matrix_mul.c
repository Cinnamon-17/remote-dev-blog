#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
 * Matrix multiplication using the standard triple-loop algorithm.
 * Matrices are stored as one-dimensional arrays.
 * Element M[i][j] is accessed as M[i * n + j].
 */
void matrix_multiply(int *A, int *B, int *C, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int total = 0;
            for (int k = 0; k < n; k++) {
                total += A[i * n + k] * B[k * n + j];
            }
            C[i * n + j] = total;
        }
    }
}

/*
 * Fill a matrix with deterministic integer values.
 * This makes the benchmark repeatable.
 */
void fill_matrix(int *M, int n, int seed) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            M[i * n + j] = (i + j + seed) % 10;
        }
    }
}

/*
 * Verify the implementation using a fixed 2 x 2 example.
 */
int verify_small_case() {
    int A[4] = {
        1, 2,
        3, 4
    };

    int B[4] = {
        5, 6,
        7, 8
    };

    int C[4] = {0, 0, 0, 0};

    int expected[4] = {
        19, 22,
        43, 50
    };

    matrix_multiply(A, B, C, 2);

    printf("Small matrix verification:\n");
    printf("Result = [[%d, %d], [%d, %d]]\n", C[0], C[1], C[2], C[3]);
    printf("Expected = [[%d, %d], [%d, %d]]\n",
           expected[0], expected[1], expected[2], expected[3]);

    int correct = 1;
    for (int i = 0; i < 4; i++) {
        if (C[i] != expected[i]) {
            correct = 0;
        }
    }

    printf("Correct: %s\n\n", correct ? "True" : "False");
    return correct;
}

int main(int argc, char *argv[]) {
    int n = 100;

    if (argc > 1) {
        n = atoi(argv[1]);
    }

    verify_small_case();

    int *A = (int *)malloc(n * n * sizeof(int));
    int *B = (int *)malloc(n * n * sizeof(int));
    int *C = (int *)malloc(n * n * sizeof(int));

    if (A == NULL || B == NULL || C == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    fill_matrix(A, n, 1);
    fill_matrix(B, n, 2);

    clock_t start = clock();
    matrix_multiply(A, B, C, n);
    clock_t end = clock();

    double elapsed_time = (double)(end - start) / CLOCKS_PER_SEC;

    printf("C benchmark:\n");
    printf("Matrix size: %d x %d\n", n, n);
    printf("Execution time: %.8f seconds\n", elapsed_time);

    free(A);
    free(B);
    free(C);

    return 0;
}

