#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	int size, allocated, i;
	PyObject *item;

	if (PyList_Check(p))
	{
		size = Py_SIZE(p);
		allocated = ((PyListObject *)p)->allocated;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %d\n", allocated);

		for (i = 0; i < size; i++)
		{
			item = PyList_GetItem(p, i);
			printf("Element %d: ", i);

			if (PyBytes_Check(item))
			{
				print_python_bytes(item);
			}
			else
			{
				printf("%s\n", Py_TYPE(item)->tp_name);
			}
		}
	}
	else
	{
		printf("[*] Invalid Bytes Object\n");
	}
}

void print_python_bytes(PyObject *p)
{
	int size, i;
	char *data;

	if (PyBytes_Check(p))
	{
		size = Py_SIZE(p);
		data = PyBytes_AsString(p);

		printf("[.] bytes object info\n");
		printf("  size: %d\n", size);
		printf("  trying string: %s\n", data);

		printf("  first %d bytes:", (size > 10) ? 10 : size);
		for (i = 0; i < ((size > 10) ? 10 : size); i++)
		{
			printf(" %.2x", data[i] & 0xFF);
		}
		printf("\n");
	}
	else
	{
		printf("[ERROR] Invalid Bytes Object\n");
	}
}

