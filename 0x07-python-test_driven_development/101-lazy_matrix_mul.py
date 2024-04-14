#!/usr/bin/python3

"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))


0x07-python-test_driven_development/102-python.c

#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
