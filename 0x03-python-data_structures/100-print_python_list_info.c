#include "Python.h"

/**
 * print_python_list_info - prints basic info about Python lists
 *
 * @p: Python object list
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t length_list = PyList_Size(p);
	int i = 0;
	PyObject *item = NULL;

	printf("[*] Size of the Python List = %li\n[*] Allocated = %li\n",
	       length_list, ((PyListObject *) p)->allocated);

	i = 0;
	while (i < length_list)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
		i += 1;
	}
}
