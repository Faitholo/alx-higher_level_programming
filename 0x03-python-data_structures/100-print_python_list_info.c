#include "Python.h"
/**
 * print_python_list_info - Prints information about python objects
 * @p: PyObject pointer to print info about
 * Compile with:
 * gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared
 (* -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4
 (* 100-print_python_list_info.c
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, py_list_size;
	PyObject *item;
	const char *item_type;
	PyListObject *list_object_cast;

	list_object_cast = (PyListObject *)p;
	py_list_size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", (int) py_list_size);
	printf("[*] Allocated = %d\n", (int)list_object_cast->allocated);
	for (i = 0; i < py_list_size; i++)
	{
		item = PyList_GetItem(p, i);
		item_type = Py_TYPE(item)->tp_name;
		printf("Element %d: %s\n", (int) i, item_type);
	}
}
