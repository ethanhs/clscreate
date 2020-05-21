# cython: language_level=3
cdef class Example:
    def __cinit__(self):
        self.a = 4
        self.b = "Test"
    cdef public long a
    cdef public str b