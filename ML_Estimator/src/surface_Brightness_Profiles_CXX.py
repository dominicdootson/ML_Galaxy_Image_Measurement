# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_surface_Brightness_Profiles_CXX')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_surface_Brightness_Profiles_CXX')
    _surface_Brightness_Profiles_CXX = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_surface_Brightness_Profiles_CXX', [dirname(__file__)])
        except ImportError:
            import _surface_Brightness_Profiles_CXX
            return _surface_Brightness_Profiles_CXX
        if fp is not None:
            try:
                _mod = imp.load_module('_surface_Brightness_Profiles_CXX', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _surface_Brightness_Profiles_CXX = swig_import_helper()
    del swig_import_helper
else:
    import _surface_Brightness_Profiles_CXX
del _swig_python_version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _surface_Brightness_Profiles_CXX.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _surface_Brightness_Profiles_CXX.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _surface_Brightness_Profiles_CXX.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _surface_Brightness_Profiles_CXX.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _surface_Brightness_Profiles_CXX.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _surface_Brightness_Profiles_CXX.SwigPyIterator_equal(self, x)

    def copy(self):
        return _surface_Brightness_Profiles_CXX.SwigPyIterator_copy(self)

    def next(self):
        return _surface_Brightness_Profiles_CXX.SwigPyIterator_next(self)

    def __next__(self):
        return _surface_Brightness_Profiles_CXX.SwigPyIterator___next__(self)

    def previous(self):
        return _surface_Brightness_Profiles_CXX.SwigPyIterator_previous(self)

    def advance(self, n):
        return _surface_Brightness_Profiles_CXX.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _surface_Brightness_Profiles_CXX.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _surface_Brightness_Profiles_CXX.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _surface_Brightness_Profiles_CXX.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _surface_Brightness_Profiles_CXX.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _surface_Brightness_Profiles_CXX.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _surface_Brightness_Profiles_CXX.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _surface_Brightness_Profiles_CXX.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _surface_Brightness_Profiles_CXX.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _surface_Brightness_Profiles_CXX.IntVector___nonzero__(self)

    def __bool__(self):
        return _surface_Brightness_Profiles_CXX.IntVector___bool__(self)

    def __len__(self):
        return _surface_Brightness_Profiles_CXX.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _surface_Brightness_Profiles_CXX.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _surface_Brightness_Profiles_CXX.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _surface_Brightness_Profiles_CXX.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _surface_Brightness_Profiles_CXX.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _surface_Brightness_Profiles_CXX.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _surface_Brightness_Profiles_CXX.IntVector___setitem__(self, *args)

    def pop(self):
        return _surface_Brightness_Profiles_CXX.IntVector_pop(self)

    def append(self, x):
        return _surface_Brightness_Profiles_CXX.IntVector_append(self, x)

    def empty(self):
        return _surface_Brightness_Profiles_CXX.IntVector_empty(self)

    def size(self):
        return _surface_Brightness_Profiles_CXX.IntVector_size(self)

    def swap(self, v):
        return _surface_Brightness_Profiles_CXX.IntVector_swap(self, v)

    def begin(self):
        return _surface_Brightness_Profiles_CXX.IntVector_begin(self)

    def end(self):
        return _surface_Brightness_Profiles_CXX.IntVector_end(self)

    def rbegin(self):
        return _surface_Brightness_Profiles_CXX.IntVector_rbegin(self)

    def rend(self):
        return _surface_Brightness_Profiles_CXX.IntVector_rend(self)

    def clear(self):
        return _surface_Brightness_Profiles_CXX.IntVector_clear(self)

    def get_allocator(self):
        return _surface_Brightness_Profiles_CXX.IntVector_get_allocator(self)

    def pop_back(self):
        return _surface_Brightness_Profiles_CXX.IntVector_pop_back(self)

    def erase(self, *args):
        return _surface_Brightness_Profiles_CXX.IntVector_erase(self, *args)

    def __init__(self, *args):
        this = _surface_Brightness_Profiles_CXX.new_IntVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _surface_Brightness_Profiles_CXX.IntVector_push_back(self, x)

    def front(self):
        return _surface_Brightness_Profiles_CXX.IntVector_front(self)

    def back(self):
        return _surface_Brightness_Profiles_CXX.IntVector_back(self)

    def assign(self, n, x):
        return _surface_Brightness_Profiles_CXX.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _surface_Brightness_Profiles_CXX.IntVector_resize(self, *args)

    def insert(self, *args):
        return _surface_Brightness_Profiles_CXX.IntVector_insert(self, *args)

    def reserve(self, n):
        return _surface_Brightness_Profiles_CXX.IntVector_reserve(self, n)

    def capacity(self):
        return _surface_Brightness_Profiles_CXX.IntVector_capacity(self)
    __swig_destroy__ = _surface_Brightness_Profiles_CXX.delete_IntVector
    __del__ = lambda self: None
IntVector_swigregister = _surface_Brightness_Profiles_CXX.IntVector_swigregister
IntVector_swigregister(IntVector)

class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector___bool__(self)

    def __len__(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _surface_Brightness_Profiles_CXX.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _surface_Brightness_Profiles_CXX.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _surface_Brightness_Profiles_CXX.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _surface_Brightness_Profiles_CXX.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _surface_Brightness_Profiles_CXX.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _surface_Brightness_Profiles_CXX.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector_pop(self)

    def append(self, x):
        return _surface_Brightness_Profiles_CXX.DoubleVector_append(self, x)

    def empty(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector_empty(self)

    def size(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector_size(self)

    def swap(self, v):
        return _surface_Brightness_Profiles_CXX.DoubleVector_swap(self, v)

    def begin(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector_begin(self)

    def end(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector_end(self)

    def rbegin(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector_rbegin(self)

    def rend(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector_rend(self)

    def clear(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector_clear(self)

    def get_allocator(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _surface_Brightness_Profiles_CXX.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        this = _surface_Brightness_Profiles_CXX.new_DoubleVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _surface_Brightness_Profiles_CXX.DoubleVector_push_back(self, x)

    def front(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector_front(self)

    def back(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector_back(self)

    def assign(self, n, x):
        return _surface_Brightness_Profiles_CXX.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _surface_Brightness_Profiles_CXX.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _surface_Brightness_Profiles_CXX.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _surface_Brightness_Profiles_CXX.DoubleVector_reserve(self, n)

    def capacity(self):
        return _surface_Brightness_Profiles_CXX.DoubleVector_capacity(self)
    __swig_destroy__ = _surface_Brightness_Profiles_CXX.delete_DoubleVector
    __del__ = lambda self: None
DoubleVector_swigregister = _surface_Brightness_Profiles_CXX.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)


def cxx_GaussSB(flux, e1, e2, size, dx, dy):
    return _surface_Brightness_Profiles_CXX.cxx_GaussSB(flux, e1, e2, size, dx, dy)
cxx_GaussSB = _surface_Brightness_Profiles_CXX.cxx_GaussSB

def cxx_GaussSB_dT(flux, e1, e2, size, dx, dy):
    return _surface_Brightness_Profiles_CXX.cxx_GaussSB_dT(flux, e1, e2, size, dx, dy)
cxx_GaussSB_dT = _surface_Brightness_Profiles_CXX.cxx_GaussSB_dT

def cxx_GaussSB_de1(flux, e1, e2, size, dx, dy):
    return _surface_Brightness_Profiles_CXX.cxx_GaussSB_de1(flux, e1, e2, size, dx, dy)
cxx_GaussSB_de1 = _surface_Brightness_Profiles_CXX.cxx_GaussSB_de1

def cxx_GaussSB_de2(flux, e1, e2, size, dx, dy):
    return _surface_Brightness_Profiles_CXX.cxx_GaussSB_de2(flux, e1, e2, size, dx, dy)
cxx_GaussSB_de2 = _surface_Brightness_Profiles_CXX.cxx_GaussSB_de2

def cxx_GaussSB_dde1(flux, e1, e2, size, dx, dy):
    return _surface_Brightness_Profiles_CXX.cxx_GaussSB_dde1(flux, e1, e2, size, dx, dy)
cxx_GaussSB_dde1 = _surface_Brightness_Profiles_CXX.cxx_GaussSB_dde1

def cxx_GaussSB_dde2(flux, e1, e2, size, dx, dy):
    return _surface_Brightness_Profiles_CXX.cxx_GaussSB_dde2(flux, e1, e2, size, dx, dy)
cxx_GaussSB_dde2 = _surface_Brightness_Profiles_CXX.cxx_GaussSB_dde2

def cxx_GaussSB_ddT(flux, e1, e2, size, dx, dy):
    return _surface_Brightness_Profiles_CXX.cxx_GaussSB_ddT(flux, e1, e2, size, dx, dy)
cxx_GaussSB_ddT = _surface_Brightness_Profiles_CXX.cxx_GaussSB_ddT

def cxx_GaussSB_de1dT(flux, e1, e2, size, dx, dy):
    return _surface_Brightness_Profiles_CXX.cxx_GaussSB_de1dT(flux, e1, e2, size, dx, dy)
cxx_GaussSB_de1dT = _surface_Brightness_Profiles_CXX.cxx_GaussSB_de1dT

def cxx_GaussSB_de2dT(flux, e1, e2, size, dx, dy):
    return _surface_Brightness_Profiles_CXX.cxx_GaussSB_de2dT(flux, e1, e2, size, dx, dy)
cxx_GaussSB_de2dT = _surface_Brightness_Profiles_CXX.cxx_GaussSB_de2dT

def cxx_GaussSB_de1de2(flux, e1, e2, size, dx, dy):
    return _surface_Brightness_Profiles_CXX.cxx_GaussSB_de1de2(flux, e1, e2, size, dx, dy)
cxx_GaussSB_de1de2 = _surface_Brightness_Profiles_CXX.cxx_GaussSB_de1de2
# This file is compatible with both classic and new-style classes.


