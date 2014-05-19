#!/usr/bin/env python
# -*- coding: utf-8; -*-

'''
Generate a Python extension module that exports macros from
/usr/include/linux/input.h
'''

import os, sys, re


template = r'''
#include <Python.h>
#include <linux/input.h>

/* Automatically generated by evdev.genecodes */
/* Generated on %s */

#define MODULE_NAME "_ecodes"
#define MODULE_HELP "linux/input.h macros"

static PyMethodDef MethodTable[] = {
    { NULL, NULL, 0, NULL}
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    MODULE_NAME,
    MODULE_HELP,
    -1,          /* m_size */
    MethodTable, /* m_methods */
    NULL,        /* m_reload */
    NULL,        /* m_traverse */
    NULL,        /* m_clear */
    NULL,        /* m_free */
};
#endif

static PyObject *
moduleinit(void)
{

#if PY_MAJOR_VERSION >= 3
    PyObject* m = PyModule_Create(&moduledef);
#else
    PyObject* m = Py_InitModule3(MODULE_NAME, MethodTable, MODULE_HELP);
#endif

    if (m == NULL) return NULL;

%s

    return m;
}

#if PY_MAJOR_VERSION >= 3
PyMODINIT_FUNC
PyInit__ecodes(void)
{
    return moduleinit();
}
#else
PyMODINIT_FUNC
init_ecodes(void)
{
    moduleinit();
}
#endif
'''

header = '/usr/include/linux/input.h' if len(sys.argv) == 1 else sys.argv[1]
regex = r'#define +((?:KEY|ABS|REL|SW|MSC|LED|BTN|REP|SND|ID|EV|BUS|SYN|FF)_\w+)'
regex = re.compile(regex)

if not os.path.exists(header):
    print('no such file: %s' % header)
    sys.exit(1)

def getmacros():
    for line in open(header):
        macro = regex.search(line)
        if macro:
            yield '    PyModule_AddIntMacro(m, %s);' % macro.group(1)

uname = list(os.uname()); del uname[1]
uname = ' '.join(uname)

macros = os.linesep.join(getmacros())
print(template % (uname, macros))