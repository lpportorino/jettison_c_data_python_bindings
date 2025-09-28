r"""Wrapper for preprocessed_jon.h

Generated with:
/usr/bin/ctypesgen /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h -o /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/jon_bindings.py -l libc.so.6

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["libc.so.6"] = load_library("libc.so.6")

# 1 libraries
# End libraries

# No modules

__s8 = c_char# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1

__u8 = c_ubyte# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 2

__s16 = c_short# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 3

__u16 = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 4

__s32 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 5

__u32 = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 6

__s64 = c_longlong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 7

__u64 = c_ulonglong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 8

__int64_t = c_longlong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 9

__uint64_t = c_ulonglong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 10

__time_t = c_int64# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 11

time_t = __time_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 12

ptrdiff_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 13

size_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 14

wchar_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 15

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 21
class struct_anon_1(Structure):
    pass

struct_anon_1.__slots__ = [
    '__clang_max_align_nonce1',
    '__clang_max_align_nonce2',
]
struct_anon_1._fields_ = [
    ('__clang_max_align_nonce1', c_longlong),
    ('__clang_max_align_nonce2', c_longdouble),
]

max_align_t = struct_anon_1# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 21

__u_char = c_ubyte# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 22

__u_short = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 23

__u_int = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 24

__u_long = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 25

__int8_t = c_char# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 26

__uint8_t = c_ubyte# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 27

__int16_t = c_short# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 28

__uint16_t = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 29

__int32_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 30

__uint32_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 31

__int64_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 32

__uint64_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 33

__int_least8_t = c_int8# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 34

__uint_least8_t = __uint8_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 35

__int_least16_t = c_int16# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 36

__uint_least16_t = __uint16_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 37

__int_least32_t = c_int32# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 38

__uint_least32_t = __uint32_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 39

__int_least64_t = c_int64# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 40

__uint_least64_t = __uint64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 41

__quad_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 42

__u_quad_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 43

__intmax_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 44

__uintmax_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 45

__dev_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 46

__uid_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 47

__gid_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 48

__ino_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 49

__ino64_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 50

__mode_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 51

__nlink_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 52

__off_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 53

__off64_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 54

__pid_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 55

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 56
class struct_anon_2(Structure):
    pass

struct_anon_2.__slots__ = [
    '__val',
]
struct_anon_2._fields_ = [
    ('__val', c_int * int(2)),
]

__fsid_t = struct_anon_2# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 56

__clock_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 57

__rlim_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 58

__rlim64_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 59

__id_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 60

__time_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 61

__useconds_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 62

__suseconds_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 63

__suseconds64_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 64

__daddr_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 65

__key_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 66

__clockid_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 67

__timer_t = POINTER(None)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 68

__blksize_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 69

__blkcnt_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 70

__blkcnt64_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 71

__fsblkcnt_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 72

__fsblkcnt64_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 73

__fsfilcnt_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 74

__fsfilcnt64_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 75

__fsword_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 76

__ssize_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 77

__syscall_slong_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 78

__syscall_ulong_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 79

__loff_t = __off64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 80

__caddr_t = String# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 81

__intptr_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 82

__socklen_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 83

__sig_atomic_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 84

int8_t = c_int8# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 85

int16_t = c_int16# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 86

int32_t = c_int32# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 87

int64_t = c_int64# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 88

uint8_t = __uint8_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 89

uint16_t = __uint16_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 90

uint32_t = __uint32_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 91

uint64_t = __uint64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 92

int_least8_t = __int_least8_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 93

int_least16_t = __int_least16_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 94

int_least32_t = __int_least32_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 95

int_least64_t = __int_least64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 96

uint_least8_t = __uint_least8_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 97

uint_least16_t = __uint_least16_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 98

uint_least32_t = __uint_least32_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 99

uint_least64_t = __uint_least64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 100

int_fast8_t = c_char# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 101

int_fast16_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 102

int_fast32_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 103

int_fast64_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 104

uint_fast8_t = c_ubyte# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 105

uint_fast16_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 106

uint_fast32_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 107

uint_fast64_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 108

intptr_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 109

uintptr_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 110

intmax_t = __intmax_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 111

uintmax_t = __uintmax_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 112

enum_memory_order = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 120

memory_order_relaxed = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 120

memory_order_consume = 1# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 120

memory_order_acquire = 2# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 120

memory_order_release = 3# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 120

memory_order_acq_rel = 4# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 120

memory_order_seq_cst = 5# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 120

memory_order = enum_memory_order# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 120

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 121
for _lib in _libs.values():
    if not _lib.has("atomic_thread_fence", "cdecl"):
        continue
    atomic_thread_fence = _lib.get("atomic_thread_fence", "cdecl")
    atomic_thread_fence.argtypes = [memory_order]
    atomic_thread_fence.restype = None
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 122
for _lib in _libs.values():
    if not _lib.has("atomic_signal_fence", "cdecl"):
        continue
    atomic_signal_fence = _lib.get("atomic_signal_fence", "cdecl")
    atomic_signal_fence.argtypes = [memory_order]
    atomic_signal_fence.restype = None
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 178
class struct_jon_gui_data_camera_alignment(Structure):
    pass

struct_jon_gui_data_camera_alignment.__slots__ = [
    'table_row',
    'day_focus_target_pos',
    'heat_focus_target_pos',
    'day_zoom_target_pos',
    'heat_zoom_target_pos',
    'day_cross_hair_offset_ver',
    'heat_cross_hair_offset_ver',
    'day_cross_hair_offset_hor',
    'heat_cross_hair_offset_hor',
    'used',
]
struct_jon_gui_data_camera_alignment._fields_ = [
    ('table_row', c_int32),
    ('day_focus_target_pos', c_int32),
    ('heat_focus_target_pos', c_int32),
    ('day_zoom_target_pos', c_int32),
    ('heat_zoom_target_pos', c_int32),
    ('day_cross_hair_offset_ver', c_int32),
    ('heat_cross_hair_offset_ver', c_int32),
    ('day_cross_hair_offset_hor', c_int32),
    ('heat_cross_hair_offset_hor', c_int32),
    ('used', c_int32),
]

jon_gui_data_camera_alignment = struct_jon_gui_data_camera_alignment# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 178

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 180
for _lib in _libs.values():
    try:
        jon_gui_default_state_camera_calibration = (jon_gui_data_camera_alignment).in_dll(_lib, "jon_gui_default_state_camera_calibration")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 187
class struct_jon_gui_data_colors_value(Structure):
    pass

struct_jon_gui_data_colors_value.__slots__ = [
    'h',
    's',
    'v',
    'a',
]
struct_jon_gui_data_colors_value._fields_ = [
    ('h', c_int32),
    ('s', c_int32),
    ('v', c_int32),
    ('a', c_int32),
]

jon_gui_data_colors_value = struct_jon_gui_data_colors_value# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 187

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 193
class struct_jon_gui_data_colors_menu(Structure):
    pass

struct_jon_gui_data_colors_menu.__slots__ = [
    'bg',
    'text',
    'focused',
]
struct_jon_gui_data_colors_menu._fields_ = [
    ('bg', jon_gui_data_colors_value),
    ('text', jon_gui_data_colors_value),
    ('focused', jon_gui_data_colors_value),
]

jon_gui_data_colors_menu = struct_jon_gui_data_colors_menu# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 193

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 199
class struct_jon_gui_data_colors_osd(Structure):
    pass

struct_jon_gui_data_colors_osd.__slots__ = [
    'main',
    'accent',
    'faded',
]
struct_jon_gui_data_colors_osd._fields_ = [
    ('main', jon_gui_data_colors_value),
    ('accent', jon_gui_data_colors_value),
    ('faded', jon_gui_data_colors_value),
]

jon_gui_data_colors_osd = struct_jon_gui_data_colors_osd# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 199

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 204
class struct_jon_gui_data_colors(Structure):
    pass

struct_jon_gui_data_colors.__slots__ = [
    'menu',
    'osd',
]
struct_jon_gui_data_colors._fields_ = [
    ('menu', jon_gui_data_colors_menu),
    ('osd', jon_gui_data_colors_osd),
]

jon_gui_data_colors = struct_jon_gui_data_colors# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 204

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 205
for _lib in _libs.values():
    try:
        jon_gui_default_state_colors = (jon_gui_data_colors).in_dll(_lib, "jon_gui_default_state_colors")
        break
    except:
        pass

enum_jon_gui_data_video_channel = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 211

JON_GUI_DATA_VIDEO_CNANNEL_DAY = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 211

JON_GUI_DATA_VIDEO_CNANNEL_HEAT = (JON_GUI_DATA_VIDEO_CNANNEL_DAY + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 211

_JON_GUI_DATA_VIDEO_CNANNEL_AFTER_LAST_ = (JON_GUI_DATA_VIDEO_CNANNEL_HEAT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 211

jon_gui_data_video_channel = enum_jon_gui_data_video_channel# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 211

enum_jon_gui_data_video_channel_heat_filters = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 219

JON_GUI_DATA_VIDEO_CNANNEL_HEAT_FILTER_HOT_WHITE = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 219

JON_GUI_DATA_VIDEO_CNANNEL_HEAT_FILTER_HOT_BLACK = (JON_GUI_DATA_VIDEO_CNANNEL_HEAT_FILTER_HOT_WHITE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 219

JON_GUI_DATA_VIDEO_CNANNEL_HEAT_FILTER_SEPIA = (JON_GUI_DATA_VIDEO_CNANNEL_HEAT_FILTER_HOT_BLACK + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 219

JON_GUI_DATA_VIDEO_CNANNEL_HEAT_FILTER_SEPIA_INVERTED = (JON_GUI_DATA_VIDEO_CNANNEL_HEAT_FILTER_SEPIA + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 219

_JON_SHARED_DATA_VIDEO_CNANNEL_HEAT_FILTER_AFTER_LAST_ = (JON_GUI_DATA_VIDEO_CNANNEL_HEAT_FILTER_SEPIA_INVERTED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 219

jon_gui_data_video_channel_heat_filters = enum_jon_gui_data_video_channel_heat_filters# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 219

enum_jon_gui_data_video_channel_day_filters = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 229

JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_0 = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 229

JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_1 = (JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_0 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 229

JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_2 = (JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_1 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 229

JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_3 = (JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_2 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 229

JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_4 = (JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_3 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 229

JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_5 = (JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_4 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 229

_JON_SHARED_DATA_VIDEO_CNANNEL_DAY_FILTER_AFTER_LAST_ = (JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_5 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 229

jon_gui_data_video_channel_day_filters = enum_jon_gui_data_video_channel_day_filters# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 229

enum_jon_gui_data_gps_units = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 236

JON_GUI_DATA_GPS_UNITS_DECIMAL_DEGREES = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 236

JON_GUI_DATA_GPS_UNITS_DEGREES_MINUTES_SECONDS = (JON_GUI_DATA_GPS_UNITS_DECIMAL_DEGREES + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 236

JON_GUI_DATA_GPS_UNITS_DEGREES_DECIMAL_MINUTES = (JON_GUI_DATA_GPS_UNITS_DEGREES_MINUTES_SECONDS + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 236

_JON_GUI_DATA_GPS_UNITS_AFTER_LAST_ = (JON_GUI_DATA_GPS_UNITS_DEGREES_DECIMAL_MINUTES + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 236

jon_gui_data_gps_units = enum_jon_gui_data_gps_units# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 236

enum_jon_gui_data_gps_fix_type = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 244

JON_GUI_DATA_GPS_FIX_TYPE_NONE = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 244

JON_GUI_DATA_GPS_FIX_TYPE_1D = (JON_GUI_DATA_GPS_FIX_TYPE_NONE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 244

JON_GUI_DATA_GPS_FIX_TYPE_2D = (JON_GUI_DATA_GPS_FIX_TYPE_1D + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 244

JON_GUI_DATA_GPS_FIX_TYPE_3D = (JON_GUI_DATA_GPS_FIX_TYPE_2D + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 244

JON_GUI_DATA_GPS_FIX_TYPE_MANUAL = (JON_GUI_DATA_GPS_FIX_TYPE_3D + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 244

jon_gui_data_gps_fix_type = enum_jon_gui_data_gps_fix_type# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 244

enum_jon_gui_data_compass_units = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 252

JON_GUI_DATA_COMPASS_UNITS_DEGREES = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 252

JON_GUI_DATA_COMPASS_UNITS_MILS = (JON_GUI_DATA_COMPASS_UNITS_DEGREES + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 252

JON_GUI_DATA_COMPASS_UNITS_GRAD = (JON_GUI_DATA_COMPASS_UNITS_MILS + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 252

JON_GUI_DATA_COMPASS_UNITS_MRAD = (JON_GUI_DATA_COMPASS_UNITS_GRAD + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 252

_JON_GUI_DATA_COMPASS_UNITS_AFTER_LAST_ = (JON_GUI_DATA_COMPASS_UNITS_MRAD + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 252

jon_gui_data_compass_units = enum_jon_gui_data_compass_units# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 252

enum_jon_gui_data_accumulator_state_idx = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 268

JON_GUI_DATA_ACCUMULATOR_STATE_UNKNOWN = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 268

JON_GUI_DATA_ACCUMULATOR_STATE_EMPTY = (JON_GUI_DATA_ACCUMULATOR_STATE_UNKNOWN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 268

_JON_SHARED_DATA_ACCUMULATOR_STATE_BEFORE_OK_ = (JON_GUI_DATA_ACCUMULATOR_STATE_EMPTY + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 268

JON_GUI_DATA_ACCUMULATOR_STATE_1 = (_JON_SHARED_DATA_ACCUMULATOR_STATE_BEFORE_OK_ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 268

JON_GUI_DATA_ACCUMULATOR_STATE_2 = (JON_GUI_DATA_ACCUMULATOR_STATE_1 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 268

JON_GUI_DATA_ACCUMULATOR_STATE_3 = (JON_GUI_DATA_ACCUMULATOR_STATE_2 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 268

JON_GUI_DATA_ACCUMULATOR_STATE_4 = (JON_GUI_DATA_ACCUMULATOR_STATE_3 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 268

JON_GUI_DATA_ACCUMULATOR_STATE_5 = (JON_GUI_DATA_ACCUMULATOR_STATE_4 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 268

JON_GUI_DATA_ACCUMULATOR_STATE_6 = (JON_GUI_DATA_ACCUMULATOR_STATE_5 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 268

JON_GUI_DATA_ACCUMULATOR_STATE_FULL = (JON_GUI_DATA_ACCUMULATOR_STATE_6 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 268

JON_GUI_DATA_ACCUMULATOR_STATE_CHARGING = (JON_GUI_DATA_ACCUMULATOR_STATE_FULL + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 268

_JON_SHARED_DATA_ACCUMULATOR_STATE_AFTER_OK_ = (JON_GUI_DATA_ACCUMULATOR_STATE_CHARGING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 268

_JON_SHARED_DATA_ACCUMULATOR_STATE_AFTER_LAST_ = (_JON_SHARED_DATA_ACCUMULATOR_STATE_AFTER_OK_ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 268

jon_gui_data_accumulator_state_idx = enum_jon_gui_data_accumulator_state_idx# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 268

enum_jon_gui_data_sd_card_state_idx = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 275

JON_GUI_DATA_SD_CARD_STATE_UNPLUGEED = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 275

JON_GUI_DATA_SD_CARD_STATE_NORMAL = (JON_GUI_DATA_SD_CARD_STATE_UNPLUGEED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 275

JON_GUI_DATA_SD_CARD_STATE_FULL = (JON_GUI_DATA_SD_CARD_STATE_NORMAL + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 275

_JON_GUI_DATA_SD_CARD_STATE_AFTER_LAST_ = (JON_GUI_DATA_SD_CARD_STATE_FULL + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 275

jon_gui_data_sd_card_state_idx = enum_jon_gui_data_sd_card_state_idx# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 275

enum_jon_gui_data_device_status = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 284

JON_SHARED_DATA_DEVICE_STATUS_STOPED = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 284

JON_SHARED_DATA_DEVICE_STATUS_STARTED = (JON_SHARED_DATA_DEVICE_STATUS_STOPED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 284

JON_SHARED_DATA_DEVICE_STATUS_STARTING = (JON_SHARED_DATA_DEVICE_STATUS_STARTED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 284

JON_SHARED_DATA_DEVICE_STATUS_STOPING = (JON_SHARED_DATA_DEVICE_STATUS_STARTING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 284

JON_SHARED_DATA_DEVICE_STATUS_ERROE = (JON_SHARED_DATA_DEVICE_STATUS_STOPING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 284

_JON_SHARED_DATA_DEVICE_STATUS_AFTER_LAST_ = (JON_SHARED_DATA_DEVICE_STATUS_ERROE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 284

jon_gui_data_device_status = enum_jon_gui_data_device_status# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 284

enum_jon_gui_screen_ids = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_EMPTY = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_OSD = (JON_GUI_SCREEN_EMPTY + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_OSD_LRF_RESULT = (JON_GUI_SCREEN_OSD + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_OSD_LRF_ARMING = (JON_GUI_SCREEN_OSD_LRF_RESULT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_OSD_LRF_MEASURING = (JON_GUI_SCREEN_OSD_LRF_ARMING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_OSD_LRF_RESULT_SIMPLIFIED = (JON_GUI_SCREEN_OSD_LRF_MEASURING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

_JON_GUI_SCREEN_BEFORE_MENU_SCREENS_ = (JON_GUI_SCREEN_OSD_LRF_RESULT_SIMPLIFIED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_MAIN_MENU = (_JON_GUI_SCREEN_BEFORE_MENU_SCREENS_ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_FACTORY_MAIN = (JON_GUI_SCREEN_MAIN_MENU + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_FACTORY_METEO = (JON_GUI_SCREEN_FACTORY_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_FACTORY_INFO = (JON_GUI_SCREEN_FACTORY_METEO + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_DISPLAY_MAIN = (JON_GUI_SCREEN_FACTORY_INFO + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_METEO_MAIN = (JON_GUI_SCREEN_DISPLAY_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_TIME_MAIN = (JON_GUI_SCREEN_METEO_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_TIME_MANUAL = (JON_GUI_SCREEN_TIME_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COLOR_MAIN = (JON_GUI_SCREEN_TIME_MANUAL + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COLOR_MENU_BG = (JON_GUI_SCREEN_COLOR_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COLOR_MENU_TEXT = (JON_GUI_SCREEN_COLOR_MENU_BG + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COLOR_MENU_FOCUSED = (JON_GUI_SCREEN_COLOR_MENU_TEXT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COLOR_OSD_COLOR_ACCENT = (JON_GUI_SCREEN_COLOR_MENU_FOCUSED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COLOR_OSD_COLOR_MAIN = (JON_GUI_SCREEN_COLOR_OSD_COLOR_ACCENT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_SYSTEM_MAIN = (JON_GUI_SCREEN_COLOR_OSD_COLOR_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_SYSTEM_INFO = (JON_GUI_SCREEN_SYSTEM_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_SYSTEM_LOC = (JON_GUI_SCREEN_SYSTEM_INFO + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_SYSTEM_VISUAL_SENSORS = (JON_GUI_SCREEN_SYSTEM_LOC + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COMPASS_MAIN = (JON_GUI_SCREEN_SYSTEM_VISUAL_SENSORS + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COMPASS_CALIBRATION_MAIN = (JON_GUI_SCREEN_COMPASS_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COMPASS_CALIBRATION_DONE = (JON_GUI_SCREEN_COMPASS_CALIBRATION_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_GPS_MAIN = (JON_GUI_SCREEN_COMPASS_CALIBRATION_DONE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_GPS_MANUAL = (JON_GUI_SCREEN_GPS_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_LRF_CALIBRATION_CAMERA_DAY = (JON_GUI_SCREEN_GPS_MANUAL + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_LRF_CALIBRATION_CAMERA_HEAT = (JON_GUI_SCREEN_LRF_CALIBRATION_CAMERA_DAY + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_CROSSHAIR = (JON_GUI_SCREEN_LRF_CALIBRATION_CAMERA_HEAT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_OSD_MAIN = (JON_GUI_SCREEN_CROSSHAIR + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_TARGET_MAIN = (JON_GUI_SCREEN_OSD_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_TARGET_EMPTY = (JON_GUI_SCREEN_TARGET_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_TARGET_ACTION = (JON_GUI_SCREEN_TARGET_EMPTY + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_TARGET_DELETE_CONFIRMATION = (JON_GUI_SCREEN_TARGET_ACTION + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_MEDIA_MAIN = (JON_GUI_SCREEN_TARGET_DELETE_CONFIRMATION + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_MEDIA_VIDEO = (JON_GUI_SCREEN_MEDIA_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_MEDIA_SD_ERASE_CONFIRMATION = (JON_GUI_SCREEN_MEDIA_VIDEO + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_MEDIA_SD_ERASE_DONE = (JON_GUI_SCREEN_MEDIA_SD_ERASE_CONFIRMATION + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_CAMERA_DAY_ZOOM_CALIBRATE = (JON_GUI_SCREEN_MEDIA_SD_ERASE_DONE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_CAMERA_HEAT_ZOOM_CALIBRATE = (JON_GUI_SCREEN_CAMERA_DAY_ZOOM_CALIBRATE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

_JON_GUI_SCREEN_AFTER_MENU_SCREENS_ = (JON_GUI_SCREEN_CAMERA_HEAT_ZOOM_CALIBRATE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

_JON_GUI_SCREEN_BEFORE_COMPAS_CALIB_SCREENS_ = (_JON_GUI_SCREEN_AFTER_MENU_SCREENS_ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COMPASS_CALIBRATION_AUTO = (_JON_GUI_SCREEN_BEFORE_COMPAS_CALIB_SCREENS_ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_SHORT = (JON_GUI_SCREEN_COMPASS_CALIBRATION_AUTO + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_LONG = (JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_SHORT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

_JON_GUI_SCREEN_AFTER_COMPAS_CALIB_SCREENS_ = (JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_LONG + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

_JON_GUI_SCREEN_BEFORE_WAIT_SCREENS_ = (_JON_GUI_SCREEN_AFTER_COMPAS_CALIB_SCREENS_ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COMPASS_CALIBRATION_AUTO_INIT = (_JON_GUI_SCREEN_BEFORE_WAIT_SCREENS_ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_SHORT_INIT = (JON_GUI_SCREEN_COMPASS_CALIBRATION_AUTO_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_SHORT_WAIT = (JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_SHORT_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_LONG_INIT = (JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_SHORT_WAIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_LONG_WAIT = (JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_LONG_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_CAMERA_ZOOM_CALIBRATE_INIT = (JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_LONG_WAIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_CAMERA_HEAT_ZOOM_CALIBRATE_INIT = (JON_GUI_SCREEN_CAMERA_ZOOM_CALIBRATE_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_CAMERA_DAY_ZOOM_CALIBRATE_INIT = (JON_GUI_SCREEN_CAMERA_HEAT_ZOOM_CALIBRATE_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_LRF_CALIBRATION_INIT = (JON_GUI_SCREEN_CAMERA_DAY_ZOOM_CALIBRATE_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_LRF_CALIBRATION_CAMERA_DAY_INIT = (JON_GUI_SCREEN_LRF_CALIBRATION_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_LRF_CALIBRATION_CAMERA_HEAT_INIT = (JON_GUI_SCREEN_LRF_CALIBRATION_CAMERA_DAY_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_TARGET_INIT = (JON_GUI_SCREEN_LRF_CALIBRATION_CAMERA_HEAT_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_TARGET_WAITING_FOR_NEXT = (JON_GUI_SCREEN_TARGET_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_TARGET_WAITING_FOR_PREV = (JON_GUI_SCREEN_TARGET_WAITING_FOR_NEXT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_TARGET_WAITING_FOR_DELETE = (JON_GUI_SCREEN_TARGET_WAITING_FOR_PREV + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_MEDIA_SD_ERASE_WAIT = (JON_GUI_SCREEN_TARGET_WAITING_FOR_DELETE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_SYSTEM_POWER_OFF_WAIT = (JON_GUI_SCREEN_MEDIA_SD_ERASE_WAIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_SYSTEM_OVERHEAT_POWER_OFF_WAIT = (JON_GUI_SCREEN_SYSTEM_POWER_OFF_WAIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

JON_GUI_SCREEN_POWER_OFF_COUNTDOWN_WAIT = (JON_GUI_SCREEN_SYSTEM_OVERHEAT_POWER_OFF_WAIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

_JON_GUI_SCREEN_AFTER_WAIT_SCREENS_ = (JON_GUI_SCREEN_POWER_OFF_COUNTDOWN_WAIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

_JON_GUI_SCREEN_AFTER_LAST_ID_ = (_JON_GUI_SCREEN_AFTER_WAIT_SCREENS_ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

jon_gui_screen_ids = enum_jon_gui_screen_ids# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 359

enum_jon_gui_data_time_formats = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 365

JON_GUI_DATA_TIME_FORMAT_H_M_S = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 365

JON_GUI_DATA_TIME_FORMAT_Y_m_D_H_M_S = (JON_GUI_DATA_TIME_FORMAT_H_M_S + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 365

_JON_SHARED_DATA_TIME_FORMAT_AFTER_LAST_ = (JON_GUI_DATA_TIME_FORMAT_Y_m_D_H_M_S + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 365

jon_gui_data_time_formats = enum_jon_gui_data_time_formats# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 365

enum_jon_gui_data_lrf_target_designator_status = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 372

JON_GUI_DATA_LRF_TARGET_DESIGNATOR_STATUS_OFF = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 372

JON_GUI_DATA_LRF_TARGET_DESIGNATOR_STATUS_MODE_1 = (JON_GUI_DATA_LRF_TARGET_DESIGNATOR_STATUS_OFF + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 372

JON_GUI_DATA_LRF_TARGET_DESIGNATOR_STATUS_MODE_2 = (JON_GUI_DATA_LRF_TARGET_DESIGNATOR_STATUS_MODE_1 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 372

_JON_SHARED_DATA_LRF_TARGET_DESIGNATOR_STATUS_AFTER_LAST_ = (JON_GUI_DATA_LRF_TARGET_DESIGNATOR_STATUS_MODE_2 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 372

jon_gui_data_lrf_target_designator_status = enum_jon_gui_data_lrf_target_designator_status# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 372

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 373
for _lib in _libs.values():
    try:
        jon_gui_data_types_time_formats = (POINTER(c_char) * int(_JON_SHARED_DATA_TIME_FORMAT_AFTER_LAST_)).in_dll(_lib, "jon_gui_data_types_time_formats")
        break
    except:
        pass

enum_jon_gui_data_compass_calibrate_status = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 383

JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_NOT_CALIBRATING = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 383

JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_CALIBRATING_SHORT = (JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_NOT_CALIBRATING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 383

JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_CALIBRATING_LONG = (JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_CALIBRATING_SHORT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 383

JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_FINISHED = (JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_CALIBRATING_LONG + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 383

JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_ERROR = (JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_FINISHED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 383

_JON_SHARED_DATA_COMPASS_CALIBRATE_STATUS_AFTER_LAST_ = (JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_ERROR + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 383

jon_gui_data_compass_calibrate_status = enum_jon_gui_data_compass_calibrate_status# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 383

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 389
class struct_jon_gui_data_component_meteo(Structure):
    pass

struct_jon_gui_data_component_meteo.__slots__ = [
    'temperature',
    'humidity',
    'pressure',
]
struct_jon_gui_data_component_meteo._fields_ = [
    ('temperature', c_int32),
    ('humidity', c_int32),
    ('pressure', c_int32),
]

jon_gui_data_component_meteo = struct_jon_gui_data_component_meteo# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 389

enum_anon_3 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 400

JON_GUI_DATA_ROTARY_MODE_UNSPECIFIED = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 400

JON_GUI_DATA_ROTARY_MODE_INITIALIZATION = (JON_GUI_DATA_ROTARY_MODE_UNSPECIFIED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 400

JON_GUI_DATA_ROTARY_MODE_SPEED = (JON_GUI_DATA_ROTARY_MODE_INITIALIZATION + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 400

JON_GUI_DATA_ROTARY_MODE_POSITION = (JON_GUI_DATA_ROTARY_MODE_SPEED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 400

JON_GUI_DATA_ROTARY_MODE_STABILIZATION = (JON_GUI_DATA_ROTARY_MODE_POSITION + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 400

JON_GUI_DATA_ROTARY_MODE_TARGETING = (JON_GUI_DATA_ROTARY_MODE_STABILIZATION + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 400

JON_GUI_DATA_ROTARY_MODE_VIDEO_TRACKER = (JON_GUI_DATA_ROTARY_MODE_TARGETING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 400

_JON_GUI_DATA_ROTARY_MODE_AFTER_LAST_ = (JON_GUI_DATA_ROTARY_MODE_VIDEO_TRACKER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 400

jon_gui_data_rotary_mode = enum_anon_3# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 400

enum_jon_gui_data_power_can_device = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 412

jon_gui_data_power_can_device_none = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 412

jon_gui_data_power_can_device_compass = (jon_gui_data_power_can_device_none + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 412

jon_gui_data_power_can_device_gps = (jon_gui_data_power_can_device_compass + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 412

jon_gui_data_power_can_device_cam_day = (jon_gui_data_power_can_device_gps + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 412

jon_gui_data_power_can_device_cam_heat = (jon_gui_data_power_can_device_cam_day + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 412

jon_gui_data_power_can_device_cam_heat_core = (jon_gui_data_power_can_device_cam_heat + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 412

jon_gui_data_power_can_device_lrf = (jon_gui_data_power_can_device_cam_heat_core + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 412

jon_gui_data_power_can_device_orin = (jon_gui_data_power_can_device_lrf + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 412

_jon_gui_data_power_can_device_after_last_ = (jon_gui_data_power_can_device_orin + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 412

jon_gui_data_power_can_device = enum_jon_gui_data_power_can_device# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 412

enum_jon_gui_data_fx_mode_day = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 423

JON_GUI_DATA_FX_MODE_DAY_DEFAULT = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 423

JON_GUI_DATA_FX_MODE_DAY_A = (JON_GUI_DATA_FX_MODE_DAY_DEFAULT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 423

JON_GUI_DATA_FX_MODE_DAY_B = (JON_GUI_DATA_FX_MODE_DAY_A + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 423

JON_GUI_DATA_FX_MODE_DAY_C = (JON_GUI_DATA_FX_MODE_DAY_B + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 423

JON_GUI_DATA_FX_MODE_DAY_D = (JON_GUI_DATA_FX_MODE_DAY_C + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 423

JON_GUI_DATA_FX_MODE_DAY_E = (JON_GUI_DATA_FX_MODE_DAY_D + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 423

JON_GUI_DATA_FX_MODE_DAY_F = (JON_GUI_DATA_FX_MODE_DAY_E + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 423

_JON_GUI_DATA_FX_MODE_DAY_AFTER_LAST_ = (JON_GUI_DATA_FX_MODE_DAY_F + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 423

jon_gui_data_fx_mode_day = enum_jon_gui_data_fx_mode_day# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 423

enum_jon_gui_data_fx_mode_heat = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 434

JON_GUI_DATA_FX_MODE_HEAT_DEFAULT = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 434

JON_GUI_DATA_FX_MODE_HEAT_A = (JON_GUI_DATA_FX_MODE_HEAT_DEFAULT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 434

JON_GUI_DATA_FX_MODE_HEAT_B = (JON_GUI_DATA_FX_MODE_HEAT_A + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 434

JON_GUI_DATA_FX_MODE_HEAT_C = (JON_GUI_DATA_FX_MODE_HEAT_B + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 434

JON_GUI_DATA_FX_MODE_HEAT_D = (JON_GUI_DATA_FX_MODE_HEAT_C + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 434

JON_GUI_DATA_FX_MODE_HEAT_E = (JON_GUI_DATA_FX_MODE_HEAT_D + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 434

JON_GUI_DATA_FX_MODE_HEAT_F = (JON_GUI_DATA_FX_MODE_HEAT_E + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 434

_JON_GUI_DATA_FX_MODE_HEAT_AFTER_LAST_ = (JON_GUI_DATA_FX_MODE_HEAT_F + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 434

jon_gui_data_fx_mode_heat = enum_jon_gui_data_fx_mode_heat# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 434

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 442
class union_anon_4(Union):
    pass

union_anon_4.__slots__ = [
    'units_idx',
    'units_idx_packed',
]
union_anon_4._fields_ = [
    ('units_idx', jon_gui_data_compass_units),
    ('units_idx_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 447
class union_anon_5(Union):
    pass

union_anon_5.__slots__ = [
    'device_status',
    'device_status_packed',
]
union_anon_5._fields_ = [
    ('device_status', jon_gui_data_device_status),
    ('device_status_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 453
class struct_jon_gui_data_compass(Structure):
    pass

struct_jon_gui_data_compass.__slots__ = [
    'azimuth',
    'elevation',
    'bank',
    'offset',
    'unnamed_1',
    'unnamed_2',
    'meteo',
]
struct_jon_gui_data_compass._anonymous_ = [
    'unnamed_1',
    'unnamed_2',
]
struct_jon_gui_data_compass._fields_ = [
    ('azimuth', c_int32),
    ('elevation', c_int32),
    ('bank', c_int32),
    ('offset', c_int32),
    ('unnamed_1', union_anon_4),
    ('unnamed_2', union_anon_5),
    ('meteo', jon_gui_data_component_meteo),
]

jon_gui_data_compass = struct_jon_gui_data_compass# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 453

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 454
for _lib in _libs.values():
    try:
        jon_gui_default_state_compass = (jon_gui_data_compass).in_dll(_lib, "jon_gui_default_state_compass")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 462
class union_anon_6(Union):
    pass

union_anon_6.__slots__ = [
    'status',
    'jon_gui_data_compass_calibrate_status_packed',
]
union_anon_6._fields_ = [
    ('status', jon_gui_data_compass_calibrate_status),
    ('jon_gui_data_compass_calibrate_status_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 467
class struct_jon_gui_data_compass_calibration(Structure):
    pass

struct_jon_gui_data_compass_calibration.__slots__ = [
    'stage',
    'final_stage',
    'target_azimuth',
    'target_elevation',
    'target_bank',
    'unnamed_1',
]
struct_jon_gui_data_compass_calibration._anonymous_ = [
    'unnamed_1',
]
struct_jon_gui_data_compass_calibration._fields_ = [
    ('stage', c_int32),
    ('final_stage', c_int32),
    ('target_azimuth', c_int32),
    ('target_elevation', c_int32),
    ('target_bank', c_int32),
    ('unnamed_1', union_anon_6),
]

jon_gui_data_compass_calibration = struct_jon_gui_data_compass_calibration# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 467

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 469
for _lib in _libs.values():
    try:
        jon_gui_default_state_compass_calibration = (jon_gui_data_compass_calibration).in_dll(_lib, "jon_gui_default_state_compass_calibration")
        break
    except:
        pass

enum_anon_7 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_READY_FOR_NEW = (-1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_UP = (45 * 2)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_DOWN = (JON_GUI_EVENT_INPUT_UP + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_LEFT = (JON_GUI_EVENT_INPUT_DOWN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_RIGHT = (JON_GUI_EVENT_INPUT_LEFT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_ENTER = (JON_GUI_EVENT_INPUT_RIGHT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_ESC = (JON_GUI_EVENT_INPUT_ENTER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_UP_FASTER = (JON_GUI_EVENT_INPUT_ESC + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_DOWN_FASTER = (JON_GUI_EVENT_INPUT_UP_FASTER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_LEFT_FASTER = (JON_GUI_EVENT_INPUT_DOWN_FASTER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_RIGHT_FASTER = (JON_GUI_EVENT_INPUT_LEFT_FASTER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_ENTER_FASTER = (JON_GUI_EVENT_INPUT_RIGHT_FASTER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_ESC_FASTER = (JON_GUI_EVENT_INPUT_ENTER_FASTER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_UP_FAST = (JON_GUI_EVENT_INPUT_ESC_FASTER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_DOWN_FAST = (JON_GUI_EVENT_INPUT_UP_FAST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_LEFT_FAST = (JON_GUI_EVENT_INPUT_DOWN_FAST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_RIGHT_FAST = (JON_GUI_EVENT_INPUT_LEFT_FAST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_ENTER_FAST = (JON_GUI_EVENT_INPUT_RIGHT_FAST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_ESC_FAST = (JON_GUI_EVENT_INPUT_ENTER_FAST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_UP_FASTEST = (JON_GUI_EVENT_INPUT_ESC_FAST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_DOWN_FASTEST = (JON_GUI_EVENT_INPUT_UP_FASTEST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_LEFT_FASTEST = (JON_GUI_EVENT_INPUT_DOWN_FASTEST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_RIGHT_FASTEST = (JON_GUI_EVENT_INPUT_LEFT_FASTEST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_ENTER_FASTEST = (JON_GUI_EVENT_INPUT_RIGHT_FASTEST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_INPUT_ESC_FASTEST = (JON_GUI_EVENT_INPUT_ENTER_FASTEST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_SYNC = (JON_GUI_EVENT_INPUT_ESC_FASTEST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_PING = (JON_GUI_EVENT_SYNC + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_PONG = (JON_GUI_EVENT_PING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

JON_GUI_EVENT_KILL = (JON_GUI_EVENT_PONG + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

_JON_GUI_EVENT_INPUT_AFTER_LAST_ = (JON_GUI_EVENT_KILL + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

jon_gui_input_event_codes = enum_anon_7# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 502

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 503
class struct_timeval(Structure):
    pass

struct_timeval.__slots__ = [
    'tv_sec',
    'tv_usec',
]
struct_timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 508
class struct_timex(Structure):
    pass

struct_timex.__slots__ = [
    'modes',
    'offset',
    'freq',
    'maxerror',
    'esterror',
    'status',
    'constant',
    'precision',
    'tolerance',
    'time',
    'tick',
    'ppsfreq',
    'jitter',
    'shift',
    'stabil',
    'jitcnt',
    'calcnt',
    'errcnt',
    'stbcnt',
    'tai',
    'unnamed_1',
    'unnamed_2',
    'unnamed_3',
    'unnamed_4',
    'unnamed_5',
    'unnamed_6',
    'unnamed_7',
    'unnamed_8',
    'unnamed_9',
    'unnamed_10',
    'unnamed_11',
]
struct_timex._fields_ = [
    ('modes', c_uint),
    ('offset', __syscall_slong_t),
    ('freq', __syscall_slong_t),
    ('maxerror', __syscall_slong_t),
    ('esterror', __syscall_slong_t),
    ('status', c_int),
    ('constant', __syscall_slong_t),
    ('precision', __syscall_slong_t),
    ('tolerance', __syscall_slong_t),
    ('time', struct_timeval),
    ('tick', __syscall_slong_t),
    ('ppsfreq', __syscall_slong_t),
    ('jitter', __syscall_slong_t),
    ('shift', c_int),
    ('stabil', __syscall_slong_t),
    ('jitcnt', __syscall_slong_t),
    ('calcnt', __syscall_slong_t),
    ('errcnt', __syscall_slong_t),
    ('stbcnt', __syscall_slong_t),
    ('tai', c_int),
    ('unnamed_1', c_int, 32),
    ('unnamed_2', c_int, 32),
    ('unnamed_3', c_int, 32),
    ('unnamed_4', c_int, 32),
    ('unnamed_5', c_int, 32),
    ('unnamed_6', c_int, 32),
    ('unnamed_7', c_int, 32),
    ('unnamed_8', c_int, 32),
    ('unnamed_9', c_int, 32),
    ('unnamed_10', c_int, 32),
    ('unnamed_11', c_int, 32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 534
if _libs["libc.so.6"].has("clock_adjtime", "cdecl"):
    clock_adjtime = _libs["libc.so.6"].get("clock_adjtime", "cdecl")
    clock_adjtime.argtypes = [__clockid_t, POINTER(struct_timex)]
    clock_adjtime.restype = c_int

clock_t = __clock_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 535

time_t = __time_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 536

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 537
class struct_tm(Structure):
    pass

struct_tm.__slots__ = [
    'tm_sec',
    'tm_min',
    'tm_hour',
    'tm_mday',
    'tm_mon',
    'tm_year',
    'tm_wday',
    'tm_yday',
    'tm_isdst',
    'tm_gmtoff',
    'tm_zone',
]
struct_tm._fields_ = [
    ('tm_sec', c_int),
    ('tm_min', c_int),
    ('tm_hour', c_int),
    ('tm_mday', c_int),
    ('tm_mon', c_int),
    ('tm_year', c_int),
    ('tm_wday', c_int),
    ('tm_yday', c_int),
    ('tm_isdst', c_int),
    ('tm_gmtoff', c_long),
    ('tm_zone', String),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 551
class struct_timespec(Structure):
    pass

struct_timespec.__slots__ = [
    'tv_sec',
    'tv_nsec',
]
struct_timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', __syscall_slong_t),
]

clockid_t = __clockid_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 556

timer_t = __timer_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 557

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 558
class struct_itimerspec(Structure):
    pass

struct_itimerspec.__slots__ = [
    'it_interval',
    'it_value',
]
struct_itimerspec._fields_ = [
    ('it_interval', struct_timespec),
    ('it_value', struct_timespec),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 563
class struct_sigevent(Structure):
    pass

pid_t = __pid_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 564

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 567
class struct___locale_data(Structure):
    pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 565
class struct___locale_struct(Structure):
    pass

struct___locale_struct.__slots__ = [
    '__locales',
    '__ctype_b',
    '__ctype_tolower',
    '__ctype_toupper',
    '__names',
]
struct___locale_struct._fields_ = [
    ('__locales', POINTER(struct___locale_data) * int(13)),
    ('__ctype_b', POINTER(c_ushort)),
    ('__ctype_tolower', POINTER(c_int)),
    ('__ctype_toupper', POINTER(c_int)),
    ('__names', POINTER(c_char) * int(13)),
]

__locale_t = POINTER(struct___locale_struct)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 573

locale_t = __locale_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 575

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 576
if _libs["libc.so.6"].has("clock", "cdecl"):
    clock = _libs["libc.so.6"].get("clock", "cdecl")
    clock.argtypes = []
    clock.restype = clock_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 577
if _libs["libc.so.6"].has("time", "cdecl"):
    time = _libs["libc.so.6"].get("time", "cdecl")
    time.argtypes = [POINTER(time_t)]
    time.restype = time_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 578
if _libs["libc.so.6"].has("difftime", "cdecl"):
    difftime = _libs["libc.so.6"].get("difftime", "cdecl")
    difftime.argtypes = [time_t, time_t]
    difftime.restype = c_double

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 579
if _libs["libc.so.6"].has("mktime", "cdecl"):
    mktime = _libs["libc.so.6"].get("mktime", "cdecl")
    mktime.argtypes = [POINTER(struct_tm)]
    mktime.restype = time_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 580
if _libs["libc.so.6"].has("strftime", "cdecl"):
    strftime = _libs["libc.so.6"].get("strftime", "cdecl")
    strftime.argtypes = [String, c_size_t, String, POINTER(struct_tm)]
    strftime.restype = c_size_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 584
if _libs["libc.so.6"].has("strptime", "cdecl"):
    strptime = _libs["libc.so.6"].get("strptime", "cdecl")
    strptime.argtypes = [String, String, POINTER(struct_tm)]
    if sizeof(c_int) == sizeof(c_void_p):
        strptime.restype = ReturnString
    else:
        strptime.restype = String
        strptime.errcheck = ReturnString

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 587
if _libs["libc.so.6"].has("strftime_l", "cdecl"):
    strftime_l = _libs["libc.so.6"].get("strftime_l", "cdecl")
    strftime_l.argtypes = [String, c_size_t, String, POINTER(struct_tm), locale_t]
    strftime_l.restype = c_size_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 591
if _libs["libc.so.6"].has("strptime_l", "cdecl"):
    strptime_l = _libs["libc.so.6"].get("strptime_l", "cdecl")
    strptime_l.argtypes = [String, String, POINTER(struct_tm), locale_t]
    if sizeof(c_int) == sizeof(c_void_p):
        strptime_l.restype = ReturnString
    else:
        strptime_l.restype = String
        strptime_l.errcheck = ReturnString

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 594
if _libs["libc.so.6"].has("gmtime", "cdecl"):
    gmtime = _libs["libc.so.6"].get("gmtime", "cdecl")
    gmtime.argtypes = [POINTER(time_t)]
    gmtime.restype = POINTER(struct_tm)

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 595
if _libs["libc.so.6"].has("localtime", "cdecl"):
    localtime = _libs["libc.so.6"].get("localtime", "cdecl")
    localtime.argtypes = [POINTER(time_t)]
    localtime.restype = POINTER(struct_tm)

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 596
if _libs["libc.so.6"].has("gmtime_r", "cdecl"):
    gmtime_r = _libs["libc.so.6"].get("gmtime_r", "cdecl")
    gmtime_r.argtypes = [POINTER(time_t), POINTER(struct_tm)]
    gmtime_r.restype = POINTER(struct_tm)

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 598
if _libs["libc.so.6"].has("localtime_r", "cdecl"):
    localtime_r = _libs["libc.so.6"].get("localtime_r", "cdecl")
    localtime_r.argtypes = [POINTER(time_t), POINTER(struct_tm)]
    localtime_r.restype = POINTER(struct_tm)

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 600
if _libs["libc.so.6"].has("asctime", "cdecl"):
    asctime = _libs["libc.so.6"].get("asctime", "cdecl")
    asctime.argtypes = [POINTER(struct_tm)]
    if sizeof(c_int) == sizeof(c_void_p):
        asctime.restype = ReturnString
    else:
        asctime.restype = String
        asctime.errcheck = ReturnString

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 601
if _libs["libc.so.6"].has("ctime", "cdecl"):
    ctime = _libs["libc.so.6"].get("ctime", "cdecl")
    ctime.argtypes = [POINTER(time_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        ctime.restype = ReturnString
    else:
        ctime.restype = String
        ctime.errcheck = ReturnString

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 602
if _libs["libc.so.6"].has("asctime_r", "cdecl"):
    asctime_r = _libs["libc.so.6"].get("asctime_r", "cdecl")
    asctime_r.argtypes = [POINTER(struct_tm), String]
    if sizeof(c_int) == sizeof(c_void_p):
        asctime_r.restype = ReturnString
    else:
        asctime_r.restype = String
        asctime_r.errcheck = ReturnString

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 604
if _libs["libc.so.6"].has("ctime_r", "cdecl"):
    ctime_r = _libs["libc.so.6"].get("ctime_r", "cdecl")
    ctime_r.argtypes = [POINTER(time_t), String]
    if sizeof(c_int) == sizeof(c_void_p):
        ctime_r.restype = ReturnString
    else:
        ctime_r.restype = String
        ctime_r.errcheck = ReturnString

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 606
try:
    __tzname = (POINTER(c_char) * int(2)).in_dll(_libs["libc.so.6"], "__tzname")
except:
    pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 607
try:
    __daylight = (c_int).in_dll(_libs["libc.so.6"], "__daylight")
except:
    pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 608
try:
    __timezone = (c_long).in_dll(_libs["libc.so.6"], "__timezone")
except:
    pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 609
try:
    tzname = (POINTER(c_char) * int(2)).in_dll(_libs["libc.so.6"], "tzname")
except:
    pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 610
if _libs["libc.so.6"].has("tzset", "cdecl"):
    tzset = _libs["libc.so.6"].get("tzset", "cdecl")
    tzset.argtypes = []
    tzset.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 611
try:
    daylight = (c_int).in_dll(_libs["libc.so.6"], "daylight")
except:
    pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 612
try:
    timezone = (c_long).in_dll(_libs["libc.so.6"], "timezone")
except:
    pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 613
if _libs["libc.so.6"].has("timegm", "cdecl"):
    timegm = _libs["libc.so.6"].get("timegm", "cdecl")
    timegm.argtypes = [POINTER(struct_tm)]
    timegm.restype = time_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 614
if _libs["libc.so.6"].has("timelocal", "cdecl"):
    timelocal = _libs["libc.so.6"].get("timelocal", "cdecl")
    timelocal.argtypes = [POINTER(struct_tm)]
    timelocal.restype = time_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 615
if _libs["libc.so.6"].has("dysize", "cdecl"):
    dysize = _libs["libc.so.6"].get("dysize", "cdecl")
    dysize.argtypes = [c_int]
    dysize.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 616
if _libs["libc.so.6"].has("nanosleep", "cdecl"):
    nanosleep = _libs["libc.so.6"].get("nanosleep", "cdecl")
    nanosleep.argtypes = [POINTER(struct_timespec), POINTER(struct_timespec)]
    nanosleep.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 618
if _libs["libc.so.6"].has("clock_getres", "cdecl"):
    clock_getres = _libs["libc.so.6"].get("clock_getres", "cdecl")
    clock_getres.argtypes = [clockid_t, POINTER(struct_timespec)]
    clock_getres.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 619
if _libs["libc.so.6"].has("clock_gettime", "cdecl"):
    clock_gettime = _libs["libc.so.6"].get("clock_gettime", "cdecl")
    clock_gettime.argtypes = [clockid_t, POINTER(struct_timespec)]
    clock_gettime.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 621
if _libs["libc.so.6"].has("clock_settime", "cdecl"):
    clock_settime = _libs["libc.so.6"].get("clock_settime", "cdecl")
    clock_settime.argtypes = [clockid_t, POINTER(struct_timespec)]
    clock_settime.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 623
if _libs["libc.so.6"].has("clock_nanosleep", "cdecl"):
    clock_nanosleep = _libs["libc.so.6"].get("clock_nanosleep", "cdecl")
    clock_nanosleep.argtypes = [clockid_t, c_int, POINTER(struct_timespec), POINTER(struct_timespec)]
    clock_nanosleep.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 626
if _libs["libc.so.6"].has("clock_getcpuclockid", "cdecl"):
    clock_getcpuclockid = _libs["libc.so.6"].get("clock_getcpuclockid", "cdecl")
    clock_getcpuclockid.argtypes = [pid_t, POINTER(clockid_t)]
    clock_getcpuclockid.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 627
if _libs["libc.so.6"].has("timer_create", "cdecl"):
    timer_create = _libs["libc.so.6"].get("timer_create", "cdecl")
    timer_create.argtypes = [clockid_t, POINTER(struct_sigevent), POINTER(timer_t)]
    timer_create.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 630
if _libs["libc.so.6"].has("timer_delete", "cdecl"):
    timer_delete = _libs["libc.so.6"].get("timer_delete", "cdecl")
    timer_delete.argtypes = [timer_t]
    timer_delete.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 631
if _libs["libc.so.6"].has("timer_settime", "cdecl"):
    timer_settime = _libs["libc.so.6"].get("timer_settime", "cdecl")
    timer_settime.argtypes = [timer_t, c_int, POINTER(struct_itimerspec), POINTER(struct_itimerspec)]
    timer_settime.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 634
if _libs["libc.so.6"].has("timer_gettime", "cdecl"):
    timer_gettime = _libs["libc.so.6"].get("timer_gettime", "cdecl")
    timer_gettime.argtypes = [timer_t, POINTER(struct_itimerspec)]
    timer_gettime.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 636
if _libs["libc.so.6"].has("timer_getoverrun", "cdecl"):
    timer_getoverrun = _libs["libc.so.6"].get("timer_getoverrun", "cdecl")
    timer_getoverrun.argtypes = [timer_t]
    timer_getoverrun.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 637
if _libs["libc.so.6"].has("timespec_get", "cdecl"):
    timespec_get = _libs["libc.so.6"].get("timespec_get", "cdecl")
    timespec_get.argtypes = [POINTER(struct_timespec), c_int]
    timespec_get.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 639
if _libs["libc.so.6"].has("timespec_getres", "cdecl"):
    timespec_getres = _libs["libc.so.6"].get("timespec_getres", "cdecl")
    timespec_getres.argtypes = [POINTER(struct_timespec), c_int]
    timespec_getres.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 641
try:
    getdate_err = (c_int).in_dll(_libs["libc.so.6"], "getdate_err")
except:
    pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 642
if _libs["libc.so.6"].has("getdate", "cdecl"):
    getdate = _libs["libc.so.6"].get("getdate", "cdecl")
    getdate.argtypes = [String]
    getdate.restype = POINTER(struct_tm)

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 643
if _libs["libc.so.6"].has("getdate_r", "cdecl"):
    getdate_r = _libs["libc.so.6"].get("getdate_r", "cdecl")
    getdate_r.argtypes = [String, POINTER(struct_tm)]
    getdate_r.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 656
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    'timestamp_low',
    'timestamp_hi',
]
struct_anon_8._fields_ = [
    ('timestamp_low', c_int32),
    ('timestamp_hi', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 653
class union_anon_9(Union):
    pass

union_anon_9.__slots__ = [
    'timestamp',
    'unnamed_1',
]
union_anon_9._anonymous_ = [
    'unnamed_1',
]
union_anon_9._fields_ = [
    ('timestamp', time_t),
    ('unnamed_1', struct_anon_8),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 662
class union_anon_10(Union):
    pass

union_anon_10.__slots__ = [
    'fix_type',
    'fix_type_packed',
]
union_anon_10._fields_ = [
    ('fix_type', jon_gui_data_gps_fix_type),
    ('fix_type_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 668
class union_anon_11(Union):
    pass

union_anon_11.__slots__ = [
    'units_idx',
    'units_packed',
]
union_anon_11._fields_ = [
    ('units_idx', jon_gui_data_gps_units),
    ('units_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 673
class union_anon_12(Union):
    pass

union_anon_12.__slots__ = [
    'device_status',
    'device_status_packed',
]
union_anon_12._fields_ = [
    ('device_status', jon_gui_data_device_status),
    ('device_status_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 679
class struct_jon_gui_data_gps(Structure):
    pass

struct_jon_gui_data_gps.__slots__ = [
    'longitude',
    'latitude',
    'height',
    'manual_longitude',
    'manual_latitude',
    'manual_altitude',
    'unnamed_1',
    'unnamed_2',
    'use_manual',
    'unnamed_3',
    'unnamed_4',
    'meteo',
]
struct_jon_gui_data_gps._anonymous_ = [
    'unnamed_1',
    'unnamed_2',
    'unnamed_3',
    'unnamed_4',
]
struct_jon_gui_data_gps._fields_ = [
    ('longitude', c_int32),
    ('latitude', c_int32),
    ('height', c_int32),
    ('manual_longitude', c_int32),
    ('manual_latitude', c_int32),
    ('manual_altitude', c_int32),
    ('unnamed_1', union_anon_9),
    ('unnamed_2', union_anon_10),
    ('use_manual', c_int32),
    ('unnamed_3', union_anon_11),
    ('unnamed_4', union_anon_12),
    ('meteo', jon_gui_data_component_meteo),
]

jon_gui_data_gps = struct_jon_gui_data_gps# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 679

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 680
for _lib in _libs.values():
    try:
        jon_gui_default_state_gps = (jon_gui_data_gps).in_dll(_lib, "jon_gui_default_state_gps")
        break
    except:
        pass

enum_jon_gui_data_mode = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 687

JON_GUI_DATA_MODE_DEFAULT = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 687

JON_GUI_DATA_MODE_FADED = (JON_GUI_DATA_MODE_DEFAULT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 687

JON_GUI_DATA_MODE_OSD_OFF = (JON_GUI_DATA_MODE_FADED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 687

_JON_GUI_DATA_MODE_AFTER_LAST_ = (JON_GUI_DATA_MODE_OSD_OFF + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 687

jon_gui_data_mode = enum_jon_gui_data_mode# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 687

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 693
class union_anon_13(Union):
    pass

union_anon_13.__slots__ = [
    'active_mode_id',
    'active_mode_id_packed',
]
union_anon_13._fields_ = [
    ('active_mode_id', jon_gui_data_mode),
    ('active_mode_id_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 698
class union_anon_14(Union):
    pass

union_anon_14.__slots__ = [
    'active_screen_id',
    'active_screen_id_packed',
]
union_anon_14._fields_ = [
    ('active_screen_id', jon_gui_screen_ids),
    ('active_screen_id_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 703
class struct_jon_gui_data_header(Structure):
    pass

struct_jon_gui_data_header.__slots__ = [
    'version',
    'state_update_counter',
    'system_monotonic_time_us',
    'unnamed_1',
    'unnamed_2',
]
struct_jon_gui_data_header._anonymous_ = [
    'unnamed_1',
    'unnamed_2',
]
struct_jon_gui_data_header._fields_ = [
    ('version', c_int32),
    ('state_update_counter', c_int32),
    ('system_monotonic_time_us', uint64_t),
    ('unnamed_1', union_anon_13),
    ('unnamed_2', union_anon_14),
]

jon_gui_data_header = struct_jon_gui_data_header# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 703

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 704
for _lib in _libs.values():
    try:
        jon_gui_default_state_header = (jon_gui_data_header).in_dll(_lib, "jon_gui_default_state_header")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 743
class union_anon_15(Union):
    pass

union_anon_15.__slots__ = [
    'device_status_day',
    'device_status_day_packed',
]
union_anon_15._fields_ = [
    ('device_status_day', jon_gui_data_device_status),
    ('device_status_day_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 748
class union_anon_16(Union):
    pass

union_anon_16.__slots__ = [
    'device_status_heat',
    'device_status_heat_packed',
]
union_anon_16._fields_ = [
    ('device_status_heat', jon_gui_data_device_status),
    ('device_status_heat_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 753
class union_anon_17(Union):
    pass

union_anon_17.__slots__ = [
    'fx_mode_day',
    'fx_mode_day_packed',
]
union_anon_17._fields_ = [
    ('fx_mode_day', jon_gui_data_fx_mode_day),
    ('fx_mode_day_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 758
class union_anon_18(Union):
    pass

union_anon_18.__slots__ = [
    'fx_mode_heat',
    'fx_mode_heat_packed',
]
union_anon_18._fields_ = [
    ('fx_mode_heat', jon_gui_data_fx_mode_heat),
    ('fx_mode_heat_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 763
class struct_jon_gui_data_lens(Structure):
    pass

struct_jon_gui_data_lens.__slots__ = [
    'day_focus_pos',
    'day_focus_pos_min',
    'day_focus_pos_max',
    'day_zoom_table_index',
    'day_zoom_table_max_index',
    'heat_zoom_table_index',
    'heat_zoom_table_max_index',
    'heat_focus_pos',
    'day_zoom_pos',
    'day_glass_temperature',
    'day_glass_heater_enabled',
    'day_meteo',
    'day_glass_heater_meteo',
    'heat_meteo',
    'day_zoom_pos_min',
    'day_zoom_pos_max',
    'heat_zoom_pos',
    'day_zoom_x',
    'heat_zoom_x',
    'day_iris_pos',
    'day_crop_top',
    'day_crop_bottom',
    'day_crop_left',
    'day_crop_right',
    'heat_iris_pos',
    'heat_crop_top',
    'heat_crop_bottom',
    'heat_crop_left',
    'heat_crop_right',
    'heat_dde_enabled',
    'heat_dde_level',
    'heat_dde_max_level',
    'day_digital_zoom_level',
    'heat_digital_zoom_level',
    'day_clahe_level',
    'heat_clahe_level',
    'unnamed_1',
    'unnamed_2',
    'unnamed_3',
    'unnamed_4',
]
struct_jon_gui_data_lens._anonymous_ = [
    'unnamed_1',
    'unnamed_2',
    'unnamed_3',
    'unnamed_4',
]
struct_jon_gui_data_lens._fields_ = [
    ('day_focus_pos', c_int32),
    ('day_focus_pos_min', c_int32),
    ('day_focus_pos_max', c_int32),
    ('day_zoom_table_index', c_int32),
    ('day_zoom_table_max_index', c_int32),
    ('heat_zoom_table_index', c_int32),
    ('heat_zoom_table_max_index', c_int32),
    ('heat_focus_pos', c_int32),
    ('day_zoom_pos', c_int32),
    ('day_glass_temperature', c_int32),
    ('day_glass_heater_enabled', c_int32),
    ('day_meteo', jon_gui_data_component_meteo),
    ('day_glass_heater_meteo', jon_gui_data_component_meteo),
    ('heat_meteo', jon_gui_data_component_meteo),
    ('day_zoom_pos_min', c_int32),
    ('day_zoom_pos_max', c_int32),
    ('heat_zoom_pos', c_int32),
    ('day_zoom_x', c_int32),
    ('heat_zoom_x', c_int32),
    ('day_iris_pos', c_int32),
    ('day_crop_top', c_int32),
    ('day_crop_bottom', c_int32),
    ('day_crop_left', c_int32),
    ('day_crop_right', c_int32),
    ('heat_iris_pos', c_int32),
    ('heat_crop_top', c_int32),
    ('heat_crop_bottom', c_int32),
    ('heat_crop_left', c_int32),
    ('heat_crop_right', c_int32),
    ('heat_dde_enabled', c_int32),
    ('heat_dde_level', c_int32),
    ('heat_dde_max_level', c_int32),
    ('day_digital_zoom_level', c_int32),
    ('heat_digital_zoom_level', c_int32),
    ('day_clahe_level', c_int32),
    ('heat_clahe_level', c_int32),
    ('unnamed_1', union_anon_15),
    ('unnamed_2', union_anon_16),
    ('unnamed_3', union_anon_17),
    ('unnamed_4', union_anon_18),
]

jon_gui_data_lens = struct_jon_gui_data_lens# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 763

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 764
for _lib in _libs.values():
    try:
        jon_gui_default_state_lens = (jon_gui_data_lens).in_dll(_lib, "jon_gui_default_state_lens")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 776
class union_anon_19(Union):
    pass

union_anon_19.__slots__ = [
    'target_designator_status',
    'target_designator_status_packed',
]
union_anon_19._fields_ = [
    ('target_designator_status', jon_gui_data_lrf_target_designator_status),
    ('target_designator_status_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 782
class union_anon_20(Union):
    pass

union_anon_20.__slots__ = [
    'device_status',
    'device_status_packed',
]
union_anon_20._fields_ = [
    ('device_status', jon_gui_data_device_status),
    ('device_status_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 788
class struct_jon_gui_data_lrf(Structure):
    pass

struct_jon_gui_data_lrf.__slots__ = [
    'scanning',
    'measuring',
    'refining',
    'last_range_measured_val_1',
    'last_range_measured_val_2',
    'last_range_measured_val_3',
    'fog_mode_enabled',
    'scanning_mode_freq',
    'measure_id',
    'unnamed_1',
    'error_bf',
    'unnamed_2',
    'meteo',
]
struct_jon_gui_data_lrf._anonymous_ = [
    'unnamed_1',
    'unnamed_2',
]
struct_jon_gui_data_lrf._fields_ = [
    ('scanning', c_int32),
    ('measuring', c_int32),
    ('refining', c_int32),
    ('last_range_measured_val_1', c_int32),
    ('last_range_measured_val_2', c_int32),
    ('last_range_measured_val_3', c_int32),
    ('fog_mode_enabled', c_int32),
    ('scanning_mode_freq', c_int32),
    ('measure_id', c_int32),
    ('unnamed_1', union_anon_19),
    ('error_bf', c_int32),
    ('unnamed_2', union_anon_20),
    ('meteo', jon_gui_data_component_meteo),
]

jon_gui_data_lrf = struct_jon_gui_data_lrf# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 788

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 789
for _lib in _libs.values():
    try:
        jon_gui_default_state_lrf = (jon_gui_data_lrf).in_dll(_lib, "jon_gui_default_state_lrf")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 794
class struct_jon_gui_data_media(Structure):
    pass

struct_jon_gui_data_media.__slots__ = [
    'space_left_prc',
]
struct_jon_gui_data_media._fields_ = [
    ('space_left_prc', c_int32),
]

jon_gui_data_media = struct_jon_gui_data_media# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 794

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 795
for _lib in _libs.values():
    try:
        jon_gui_default_state_media = (jon_gui_data_media).in_dll(_lib, "jon_gui_default_state_media")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 804
class struct_jon_gui_data_meteo(Structure):
    pass

struct_jon_gui_data_meteo.__slots__ = [
    'internal_temperature',
    'internal_humidity',
    'internal_pressure',
    'external_temperature',
    'external_humidity',
    'external_pressure',
]
struct_jon_gui_data_meteo._fields_ = [
    ('internal_temperature', c_int32),
    ('internal_humidity', c_int32),
    ('internal_pressure', c_int32),
    ('external_temperature', c_int32),
    ('external_humidity', c_int32),
    ('external_pressure', c_int32),
]

jon_gui_data_meteo = struct_jon_gui_data_meteo# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 804

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 805
for _lib in _libs.values():
    try:
        jon_gui_default_state_meteo = (jon_gui_data_meteo).in_dll(_lib, "jon_gui_default_state_meteo")
        break
    except:
        pass

enum_jon_gui_data_osd_pip_pos = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 814

JON_GUI_DATA_OSD_PIP_DISABLED = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 814

JON_GUI_DATA_OSD_PIP_TOP_LEFT = (JON_GUI_DATA_OSD_PIP_DISABLED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 814

JON_GUI_DATA_OSD_PIP_TOP_RIGHT = (JON_GUI_DATA_OSD_PIP_TOP_LEFT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 814

JON_GUI_DATA_OSD_PIP_BOTTOM_RIGHT = (JON_GUI_DATA_OSD_PIP_TOP_RIGHT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 814

JON_GUI_DATA_OSD_PIP_BOTTOM_LEFT = (JON_GUI_DATA_OSD_PIP_BOTTOM_RIGHT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 814

_JON_GUI_DATA_OSD_PIP_AFTER_LAST_ = (JON_GUI_DATA_OSD_PIP_BOTTOM_LEFT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 814

jon_gui_data_osd_pip_pos = enum_jon_gui_data_osd_pip_pos# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 814

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 825
class union_anon_21(Union):
    pass

union_anon_21.__slots__ = [
    'pip_pos_id',
    'pip_pos_id_packed',
]
union_anon_21._fields_ = [
    ('pip_pos_id', jon_gui_data_osd_pip_pos),
    ('pip_pos_id_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 830
class struct_jon_gui_data_osd(Structure):
    pass

struct_jon_gui_data_osd.__slots__ = [
    'show_on_recording',
    'crosshair_index',
    'crosshair_size_indx',
    'faded_opa',
    'fade_enabled',
    'show_photo_indicator',
    'disable_heat_osd',
    'disable_day_osd',
    'unnamed_1',
]
struct_jon_gui_data_osd._anonymous_ = [
    'unnamed_1',
]
struct_jon_gui_data_osd._fields_ = [
    ('show_on_recording', c_int32),
    ('crosshair_index', c_int32),
    ('crosshair_size_indx', c_int32),
    ('faded_opa', c_int32),
    ('fade_enabled', c_int32),
    ('show_photo_indicator', c_int32),
    ('disable_heat_osd', c_int32),
    ('disable_day_osd', c_int32),
    ('unnamed_1', union_anon_21),
]

jon_gui_data_osd = struct_jon_gui_data_osd# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 830

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 831
for _lib in _libs.values():
    try:
        jon_gui_default_state_osd = (jon_gui_data_osd).in_dll(_lib, "jon_gui_default_state_osd")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 861
class union_anon_22(Union):
    pass

union_anon_22.__slots__ = [
    'device_status',
    'device_status_packed',
]
union_anon_22._fields_ = [
    ('device_status', jon_gui_data_device_status),
    ('device_status_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 866
class union_anon_23(Union):
    pass

union_anon_23.__slots__ = [
    'mode',
    'mode_packed',
]
union_anon_23._fields_ = [
    ('mode', jon_gui_data_rotary_mode),
    ('mode_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 875
class struct_jon_gui_data_rotary(Structure):
    pass

struct_jon_gui_data_rotary.__slots__ = [
    'platform_azimuth',
    'platform_elevation',
    'platform_bank',
    'use_platform_positioning',
    'head_azimuth',
    'head_elevation',
    'head_bank',
    'speed_azimuth',
    'speed_elevation',
    'speed_bank',
    'set_azimuth',
    'set_elevation',
    'set_speed_azimuth',
    'set_speed_elevation',
    'set_azimuth_dir',
    'set_elevation_dir',
    'set_azimuth_offset',
    'is_scanning',
    'is_scanning_paused',
    'scan_target',
    'scan_target_max',
    'scan_cur_target_azimuth',
    'scan_cur_target_elevation',
    'scan_cur_target_day_zoom_table_index',
    'scan_cur_target_heat_zoom_table_index',
    'scan_cur_target_linger',
    'scan_cur_target_speed',
    'unnamed_1',
    'unnamed_2',
    'meteo',
    'rotary_init',
    'pan_init',
    'tilt_init',
]
struct_jon_gui_data_rotary._anonymous_ = [
    'unnamed_1',
    'unnamed_2',
]
struct_jon_gui_data_rotary._fields_ = [
    ('platform_azimuth', c_int32),
    ('platform_elevation', c_int32),
    ('platform_bank', c_int32),
    ('use_platform_positioning', c_int32),
    ('head_azimuth', c_int32),
    ('head_elevation', c_int32),
    ('head_bank', c_int32),
    ('speed_azimuth', c_int32),
    ('speed_elevation', c_int32),
    ('speed_bank', c_int32),
    ('set_azimuth', c_int32),
    ('set_elevation', c_int32),
    ('set_speed_azimuth', c_int32),
    ('set_speed_elevation', c_int32),
    ('set_azimuth_dir', c_int32),
    ('set_elevation_dir', c_int32),
    ('set_azimuth_offset', c_int32),
    ('is_scanning', c_int32),
    ('is_scanning_paused', c_int32),
    ('scan_target', c_int32),
    ('scan_target_max', c_int32),
    ('scan_cur_target_azimuth', c_int32),
    ('scan_cur_target_elevation', c_int32),
    ('scan_cur_target_day_zoom_table_index', c_int32),
    ('scan_cur_target_heat_zoom_table_index', c_int32),
    ('scan_cur_target_linger', c_int32),
    ('scan_cur_target_speed', c_int32),
    ('unnamed_1', union_anon_22),
    ('unnamed_2', union_anon_23),
    ('meteo', jon_gui_data_component_meteo),
    ('rotary_init', c_int32),
    ('pan_init', c_int32),
    ('tilt_init', c_int32),
]

jon_gui_data_rotary = struct_jon_gui_data_rotary# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 875

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 876
for _lib in _libs.values():
    try:
        jon_gui_default_state_rotary = (jon_gui_data_rotary).in_dll(_lib, "jon_gui_default_state_rotary")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 886
class union_anon_24(Union):
    pass

union_anon_24.__slots__ = [
    'can_device',
    'can_device_packed',
]
union_anon_24._fields_ = [
    ('can_device', jon_gui_data_power_can_device),
    ('can_device_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 891
class struct_jon_gui_data_power_module_state(Structure):
    pass

struct_jon_gui_data_power_module_state.__slots__ = [
    'voltage',
    'current',
    'power',
    'is_alarm',
    'can_cmd_address',
    'can_data_address',
    'is_power_on',
    'unnamed_1',
]
struct_jon_gui_data_power_module_state._anonymous_ = [
    'unnamed_1',
]
struct_jon_gui_data_power_module_state._fields_ = [
    ('voltage', c_int32),
    ('current', c_int32),
    ('power', c_int32),
    ('is_alarm', c_int32),
    ('can_cmd_address', c_int32),
    ('can_data_address', c_int32),
    ('is_power_on', c_int32),
    ('unnamed_1', union_anon_24),
]

jon_gui_data_power_module_state = struct_jon_gui_data_power_module_state# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 891

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 903
class struct_jon_gui_data_power(Structure):
    pass

struct_jon_gui_data_power.__slots__ = [
    's0',
    's1',
    's2',
    's3',
    's4',
    's5',
    's6',
    's7',
    'meteo',
]
struct_jon_gui_data_power._fields_ = [
    ('s0', jon_gui_data_power_module_state),
    ('s1', jon_gui_data_power_module_state),
    ('s2', jon_gui_data_power_module_state),
    ('s3', jon_gui_data_power_module_state),
    ('s4', jon_gui_data_power_module_state),
    ('s5', jon_gui_data_power_module_state),
    ('s6', jon_gui_data_power_module_state),
    ('s7', jon_gui_data_power_module_state),
    ('meteo', jon_gui_data_component_meteo),
]

jon_gui_data_power = struct_jon_gui_data_power# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 903

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 904
for _lib in _libs.values():
    try:
        jon_gui_default_state_power = (jon_gui_data_power).in_dll(_lib, "jon_gui_default_state_power")
        break
    except:
        pass

enum_jon_gui_data_system_localizations = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 912

jon_gui_data_system_localization_en = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 912

jon_gui_data_system_localization_ua = (jon_gui_data_system_localization_en + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 912

jon_gui_data_system_localization_ar = (jon_gui_data_system_localization_ua + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 912

jon_gui_data_system_localization_cs = (jon_gui_data_system_localization_ar + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 912

_jon_gui_data_system_localization_after_last_ = (jon_gui_data_system_localization_cs + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 912

jon_gui_data_system_localizations = enum_jon_gui_data_system_localizations# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 912

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 932
class union_anon_25(Union):
    pass

union_anon_25.__slots__ = [
    'localization_id',
    'localization_id_packed',
]
union_anon_25._fields_ = [
    ('localization_id', jon_gui_data_system_localizations),
    ('localization_id_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 937
class union_anon_26(Union):
    pass

union_anon_26.__slots__ = [
    'active_video_channel',
    'active_video_channel_packed',
]
union_anon_26._fields_ = [
    ('active_video_channel', jon_gui_data_video_channel),
    ('active_video_channel_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 942
class union_anon_27(Union):
    pass

union_anon_27.__slots__ = [
    'active_thermal_color_filter_idx',
    'active_thermal_color_filter_packed',
]
union_anon_27._fields_ = [
    ('active_thermal_color_filter_idx', jon_gui_data_video_channel_heat_filters),
    ('active_thermal_color_filter_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 948
class union_anon_28(Union):
    pass

union_anon_28.__slots__ = [
    'active_day_filter_idx',
    'active_day_filter_packed',
]
union_anon_28._fields_ = [
    ('active_day_filter_idx', jon_gui_data_video_channel_day_filters),
    ('active_day_filter_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 953
class union_anon_29(Union):
    pass

union_anon_29.__slots__ = [
    'acccumulator_stat_idx',
    'acccumulator_stat_idx_packed',
]
union_anon_29._fields_ = [
    ('acccumulator_stat_idx', jon_gui_data_accumulator_state_idx),
    ('acccumulator_stat_idx_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 958
class union_anon_30(Union):
    pass

union_anon_30.__slots__ = [
    'sd_card_stat_idx',
    'sd_card_stat_idx_packed',
]
union_anon_30._fields_ = [
    ('sd_card_stat_idx', jon_gui_data_sd_card_state_idx),
    ('sd_card_stat_idx_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 971
class struct_jon_gui_data_system(Structure):
    pass

struct_jon_gui_data_system.__slots__ = [
    'enable_video_recording',
    'recording_is_important',
    'disk_space_percent_taken',
    'day_af_enable',
    'day_ae_enable',
    'day_air_enable',
    'heat_af_enable',
    'heat_filter_value',
    'irf_enable',
    'is_enable',
    'agc_mode',
    'enable_zoom_sync',
    'eth_enabled',
    'wifi_enabled',
    'enable_continuous_zoom',
    'shutdown_timer_running',
    'geodesic_mode_enabled',
    'unnamed_1',
    'unnamed_2',
    'unnamed_3',
    'unnamed_4',
    'unnamed_5',
    'unnamed_6',
    'cur_video_rec_dir_year',
    'cur_video_rec_dir_month',
    'cur_video_rec_dir_day',
    'cur_video_rec_dir_hour',
    'cur_video_rec_dir_minute',
    'cur_video_rec_dir_second',
    'low_disk_space',
    'no_disk_space',
]
struct_jon_gui_data_system._anonymous_ = [
    'unnamed_1',
    'unnamed_2',
    'unnamed_3',
    'unnamed_4',
    'unnamed_5',
    'unnamed_6',
]
struct_jon_gui_data_system._fields_ = [
    ('enable_video_recording', c_int32),
    ('recording_is_important', c_int32),
    ('disk_space_percent_taken', c_int32),
    ('day_af_enable', c_int32),
    ('day_ae_enable', c_int32),
    ('day_air_enable', c_int32),
    ('heat_af_enable', c_int32),
    ('heat_filter_value', c_int32),
    ('irf_enable', c_int32),
    ('is_enable', c_int32),
    ('agc_mode', c_int32),
    ('enable_zoom_sync', c_int32),
    ('eth_enabled', c_int32),
    ('wifi_enabled', c_int32),
    ('enable_continuous_zoom', c_int32),
    ('shutdown_timer_running', c_int32),
    ('geodesic_mode_enabled', c_int32),
    ('unnamed_1', union_anon_25),
    ('unnamed_2', union_anon_26),
    ('unnamed_3', union_anon_27),
    ('unnamed_4', union_anon_28),
    ('unnamed_5', union_anon_29),
    ('unnamed_6', union_anon_30),
    ('cur_video_rec_dir_year', c_int32),
    ('cur_video_rec_dir_month', c_int32),
    ('cur_video_rec_dir_day', c_int32),
    ('cur_video_rec_dir_hour', c_int32),
    ('cur_video_rec_dir_minute', c_int32),
    ('cur_video_rec_dir_second', c_int32),
    ('low_disk_space', c_int32),
    ('no_disk_space', c_int32),
]

jon_gui_data_system = struct_jon_gui_data_system# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 971

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 972
for _lib in _libs.values():
    try:
        jon_gui_default_state_system = (jon_gui_data_system).in_dll(_lib, "jon_gui_default_state_system")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 982
class union_anon_31(Union):
    pass

union_anon_31.__slots__ = [
    'observer_timestamp',
    'observer_timestamp_packed',
]
union_anon_31._fields_ = [
    ('observer_timestamp', time_t),
    ('observer_timestamp_packed', c_int64),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 996
class union_anon_32(Union):
    pass

union_anon_32.__slots__ = [
    'observer_fix_type',
    'observer_fix_type_packed',
]
union_anon_32._fields_ = [
    ('observer_fix_type', jon_gui_data_gps_fix_type),
    ('observer_fix_type_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1001
class struct_jon_gui_data_target_spec(Structure):
    pass

struct_jon_gui_data_target_spec.__slots__ = [
    'target_id',
    'target_index',
    'uuid',
    'target_longitude',
    'target_latitude',
    'target_height',
    'observer_id',
    'unnamed_1',
    'observer_longitude',
    'observer_latitude',
    'observer_azimuth',
    'observer_elevation',
    'observer_altitude',
    'distance_a',
    'distance_b',
    'has_range',
    'session_id',
    'unnamed_2',
]
struct_jon_gui_data_target_spec._anonymous_ = [
    'unnamed_1',
    'unnamed_2',
]
struct_jon_gui_data_target_spec._fields_ = [
    ('target_id', c_int32),
    ('target_index', c_int32),
    ('uuid', c_int32 * int(4)),
    ('target_longitude', c_int32),
    ('target_latitude', c_int32),
    ('target_height', c_int32),
    ('observer_id', c_int32),
    ('unnamed_1', union_anon_31),
    ('observer_longitude', c_int32),
    ('observer_latitude', c_int32),
    ('observer_azimuth', c_int32),
    ('observer_elevation', c_int32),
    ('observer_altitude', c_int32),
    ('distance_a', c_int32),
    ('distance_b', c_int32),
    ('has_range', c_int32),
    ('session_id', c_int32),
    ('unnamed_2', union_anon_32),
]

jon_gui_data_target_spec = struct_jon_gui_data_target_spec# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1001

enum_jon_gui_data_targets_screenshot_state = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1008

JON_GUI_DATA_TARGETS_SCREENSHOT_STATE_INFO = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1008

JON_GUI_DATA_TARGETS_SCREENSHOT_STATE_DAY = (JON_GUI_DATA_TARGETS_SCREENSHOT_STATE_INFO + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1008

JON_GUI_DATA_TARGETS_SCREENSHOT_STATE_HEAT = (JON_GUI_DATA_TARGETS_SCREENSHOT_STATE_DAY + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1008

__JON_GUI_DATA_TARGETS_SCREENSHOT_STATE_AFTER_LAST__ = (JON_GUI_DATA_TARGETS_SCREENSHOT_STATE_HEAT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1008

jon_gui_data_targets_screenshot_state = enum_jon_gui_data_targets_screenshot_state# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1008

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1015
class struct_jon_gui_data_targets(Structure):
    pass

struct_jon_gui_data_targets.__slots__ = [
    'last_target',
    'target_viewr_current_target',
    'recorded_targets_count',
    'screenshot_state',
]
struct_jon_gui_data_targets._fields_ = [
    ('last_target', jon_gui_data_target_spec),
    ('target_viewr_current_target', jon_gui_data_target_spec),
    ('recorded_targets_count', c_int32),
    ('screenshot_state', jon_gui_data_targets_screenshot_state),
]

jon_gui_data_targets = struct_jon_gui_data_targets# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1015

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1016
for _lib in _libs.values():
    try:
        jon_gui_default_state_targets = (jon_gui_data_targets).in_dll(_lib, "jon_gui_default_state_targets")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1022
class struct_anon_33(Structure):
    pass

struct_anon_33.__slots__ = [
    'timestamp_low',
    'timestamp_hi',
]
struct_anon_33._fields_ = [
    ('timestamp_low', c_int32),
    ('timestamp_hi', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1019
class union_anon_34(Union):
    pass

union_anon_34.__slots__ = [
    'timestamp',
    'unnamed_1',
]
union_anon_34._anonymous_ = [
    'unnamed_1',
]
union_anon_34._fields_ = [
    ('timestamp', time_t),
    ('unnamed_1', struct_anon_33),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1031
class struct_anon_35(Structure):
    pass

struct_anon_35.__slots__ = [
    'manual_timestamp_low',
    'manual_timestamp_hi',
]
struct_anon_35._fields_ = [
    ('manual_timestamp_low', c_int32),
    ('manual_timestamp_hi', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1028
class union_anon_36(Union):
    pass

union_anon_36.__slots__ = [
    'manual_timestamp',
    'unnamed_1',
]
union_anon_36._anonymous_ = [
    'unnamed_1',
]
union_anon_36._fields_ = [
    ('manual_timestamp', time_t),
    ('unnamed_1', struct_anon_35),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1039
class struct_jon_gui_data_time(Structure):
    pass

struct_jon_gui_data_time.__slots__ = [
    'unnamed_1',
    'unnamed_2',
    'zone_id',
    'use_manual_time',
]
struct_jon_gui_data_time._anonymous_ = [
    'unnamed_1',
    'unnamed_2',
]
struct_jon_gui_data_time._fields_ = [
    ('unnamed_1', union_anon_34),
    ('unnamed_2', union_anon_36),
    ('zone_id', c_int32),
    ('use_manual_time', c_int32),
]

jon_gui_data_time = struct_jon_gui_data_time# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1039

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1040
for _lib in _libs.values():
    try:
        jon_gui_default_state_time = (jon_gui_data_time).in_dll(_lib, "jon_gui_default_state_time")
        break
    except:
        pass

enum_jon_gui_tracking_color = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_RED = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_GREEN = (JON_GUI_TRACKING_COLOR_RED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_BLUE = (JON_GUI_TRACKING_COLOR_GREEN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_YELLOW = (JON_GUI_TRACKING_COLOR_BLUE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_MAGENTA = (JON_GUI_TRACKING_COLOR_YELLOW + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_CYAN = (JON_GUI_TRACKING_COLOR_MAGENTA + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_ORANGE = (JON_GUI_TRACKING_COLOR_CYAN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_PURPLE = (JON_GUI_TRACKING_COLOR_ORANGE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_LIME = (JON_GUI_TRACKING_COLOR_PURPLE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_PINK = (JON_GUI_TRACKING_COLOR_LIME + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_TEAL = (JON_GUI_TRACKING_COLOR_PINK + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_LAVENDER = (JON_GUI_TRACKING_COLOR_TEAL + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_BROWN = (JON_GUI_TRACKING_COLOR_LAVENDER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_BEIGE = (JON_GUI_TRACKING_COLOR_BROWN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_MAROON = (JON_GUI_TRACKING_COLOR_BEIGE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_MINT = (JON_GUI_TRACKING_COLOR_MAROON + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_OLIVE = (JON_GUI_TRACKING_COLOR_MINT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_APRICOT = (JON_GUI_TRACKING_COLOR_OLIVE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_NAVY = (JON_GUI_TRACKING_COLOR_APRICOT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_GREY = (JON_GUI_TRACKING_COLOR_NAVY + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_WHITE = (JON_GUI_TRACKING_COLOR_GREY + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

JON_GUI_TRACKING_COLOR_BLACK = (JON_GUI_TRACKING_COLOR_WHITE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

jon_gui_tracking_color_t = enum_jon_gui_tracking_color# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1066

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1069
class struct_anon_37(Structure):
    pass

struct_anon_37.__slots__ = [
    'r',
    'g',
    'b',
    'a',
]
struct_anon_37._fields_ = [
    ('r', uint8_t),
    ('g', uint8_t),
    ('b', uint8_t),
    ('a', uint8_t),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1077
class union_jon_gui_color_rgba8888(Union):
    pass

union_jon_gui_color_rgba8888.__slots__ = [
    'channels',
    'packed',
]
union_jon_gui_color_rgba8888._fields_ = [
    ('channels', struct_anon_37),
    ('packed', uint32_t),
]

jon_gui_color_rgba8888_t = union_jon_gui_color_rgba8888# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1077

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1080
class struct_anon_38(Structure):
    pass

struct_anon_38.__slots__ = [
    'x',
    'y',
    'color_index',
]
struct_anon_38._fields_ = [
    ('x', uint32_t, 12),
    ('y', uint32_t, 12),
    ('color_index', uint32_t, 8),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1087
class union_jon_gui_tracking_point(Union):
    pass

union_jon_gui_tracking_point.__slots__ = [
    'fields',
    'packed',
]
union_jon_gui_tracking_point._fields_ = [
    ('fields', struct_anon_38),
    ('packed', uint32_t),
]

jon_gui_tracking_point_t = union_jon_gui_tracking_point# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1087

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1092
class struct_jon_gui_tracking_quad(Structure):
    pass

struct_jon_gui_tracking_quad.__slots__ = [
    'p1',
    'p2',
]
struct_jon_gui_tracking_quad._fields_ = [
    ('p1', jon_gui_tracking_point_t),
    ('p2', jon_gui_tracking_point_t),
]

jon_gui_tracking_quad_t = struct_jon_gui_tracking_quad# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1092

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1105
class struct_jon_gui_data_cv(Structure):
    pass

struct_jon_gui_data_cv.__slots__ = [
    'af_day_enabled',
    'af_heat_enabled',
    'tracking_day',
    'tracking_heat',
    'vampire_mode_enabled',
    'stabilization_mode_enabled',
    'recognition_mode_enabled',
    'dumping',
    'tracking_data_day',
    'tracking_data_heat',
]
struct_jon_gui_data_cv._fields_ = [
    ('af_day_enabled', c_int32),
    ('af_heat_enabled', c_int32),
    ('tracking_day', c_int32),
    ('tracking_heat', c_int32),
    ('vampire_mode_enabled', c_int32),
    ('stabilization_mode_enabled', c_int32),
    ('recognition_mode_enabled', c_int32),
    ('dumping', c_int32),
    ('tracking_data_day', jon_gui_tracking_quad_t * int(10)),
    ('tracking_data_heat', jon_gui_tracking_quad_t * int(10)),
]

jon_gui_data_cv_t = struct_jon_gui_data_cv# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1105

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1106
for _lib in _libs.values():
    try:
        jon_gui_default_state_cv = (jon_gui_data_cv_t).in_dll(_lib, "jon_gui_default_state_cv")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1108
for _lib in _libs.values():
    try:
        jon_gui_tracking_colors = (jon_gui_color_rgba8888_t * int(22)).in_dll(_lib, "jon_gui_tracking_colors")
        break
    except:
        pass

enum_anon_39 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

JON_DEBUG_VERTICAL_FOV = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

JON_DEBUG_HORIZONTAL_FOV = (JON_DEBUG_VERTICAL_FOV + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

JON_DEBUG_AF_PROCESSING_TIME = (JON_DEBUG_HORIZONTAL_FOV + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

JON_DEBUG_TRACKING_PROCESSING_TIME = (JON_DEBUG_AF_PROCESSING_TIME + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

JON_DEBUG_FRAME_RATE = (JON_DEBUG_TRACKING_PROCESSING_TIME + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

JON_DEBUG_AF_CONFIDENCE_SCORE = (JON_DEBUG_FRAME_RATE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

JON_DEBUG_TRACKING_CONFIDENCE_SCORE = (JON_DEBUG_AF_CONFIDENCE_SCORE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

JON_DEBUG_DETECTED_FACES = (JON_DEBUG_TRACKING_CONFIDENCE_SCORE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

JON_DEBUG_FACE_DETECTION_TIME = (JON_DEBUG_DETECTED_FACES + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

JON_DEBUG_IMAGE_PREPROCESSING_TIME = (JON_DEBUG_FACE_DETECTION_TIME + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

JON_DEBUG_FEATURE_EXTRACTION_TIME = (JON_DEBUG_IMAGE_PREPROCESSING_TIME + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

JON_DEBUG_AF_ALGORITHM_ITERATIONS = (JON_DEBUG_FEATURE_EXTRACTION_TIME + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

JON_DEBUG_TRACKING_ALGORITHM_ITERATIONS = (JON_DEBUG_AF_ALGORITHM_ITERATIONS + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

JON_DEBUG_MEMORY_USAGE = (JON_DEBUG_TRACKING_ALGORITHM_ITERATIONS + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

JON_DEBUG_GPU_UTILIZATION = (JON_DEBUG_MEMORY_USAGE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

JON_DEBUG_LABEL_COUNT = (JON_DEBUG_GPU_UTILIZATION + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

jon_debug_label_t = enum_anon_39# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1132

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1137
class struct_anon_40(Structure):
    pass

struct_anon_40.__slots__ = [
    'label',
    'divider',
]
struct_anon_40._fields_ = [
    ('label', String),
    ('divider', c_int32),
]

jon_debug_info_t = struct_anon_40# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1137

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1142
class struct_anon_41(Structure):
    pass

struct_anon_41.__slots__ = [
    'values',
    'display_debug',
]
struct_anon_41._fields_ = [
    ('values', c_int32 * int(20)),
    ('display_debug', c_int32),
]

jon_gui_data_debug_t = struct_anon_41# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1142

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1143
for _lib in _libs.values():
    try:
        jon_gui_default_state_debug = (jon_gui_data_debug_t).in_dll(_lib, "jon_gui_default_state_debug")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1144
for _lib in _libs.values():
    try:
        jon_debug_info = (jon_debug_info_t * int(JON_DEBUG_LABEL_COUNT)).in_dll(_lib, "jon_debug_info")
        break
    except:
        pass

enum_jon_bool = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1149

jon_false = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1149

jon_true = 1# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1149

jon_bool = enum_jon_bool# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1149

u_char = __u_char# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1150

u_short = __u_short# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1151

u_int = __u_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1152

u_long = __u_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1153

quad_t = __quad_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1154

u_quad_t = __u_quad_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1155

fsid_t = __fsid_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1156

loff_t = __loff_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1157

ino_t = __ino_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1158

ino64_t = __ino64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1159

dev_t = __dev_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1160

gid_t = __gid_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1161

mode_t = __mode_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1162

nlink_t = __nlink_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1163

uid_t = __uid_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1164

off_t = __off_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1165

off64_t = __off64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1166

id_t = __id_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1167

ssize_t = __ssize_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1168

daddr_t = __daddr_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1169

caddr_t = __caddr_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1170

key_t = __key_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1171

useconds_t = __useconds_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1172

suseconds_t = __suseconds_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1173

ulong = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1174

ushort = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1175

uint = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1176

u_int8_t = __uint8_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1177

u_int16_t = __uint16_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1178

u_int32_t = __uint32_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1179

u_int64_t = __uint64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1180

register_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1181

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1215
class struct_anon_42(Structure):
    pass

struct_anon_42.__slots__ = [
    '__val',
]
struct_anon_42._fields_ = [
    ('__val', c_ulong * int((1024 / (8 * sizeof(c_ulong))))),
]

__sigset_t = struct_anon_42# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1215

sigset_t = __sigset_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1216

__fd_mask = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1217

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1221
class struct_anon_43(Structure):
    pass

struct_anon_43.__slots__ = [
    'fds_bits',
]
struct_anon_43._fields_ = [
    ('fds_bits', __fd_mask * int((1024 / (8 * (c_int (ord_if_char(sizeof(__fd_mask)))).value)))),
]

fd_set = struct_anon_43# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1221

fd_mask = __fd_mask# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1222

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1223
if _libs["libc.so.6"].has("select", "cdecl"):
    select = _libs["libc.so.6"].get("select", "cdecl")
    select.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(struct_timeval)]
    select.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1227
if _libs["libc.so.6"].has("pselect", "cdecl"):
    pselect = _libs["libc.so.6"].get("pselect", "cdecl")
    pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(struct_timespec), POINTER(__sigset_t)]
    pselect.restype = c_int

blksize_t = __blksize_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1232

blkcnt_t = __blkcnt_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1233

fsblkcnt_t = __fsblkcnt_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1234

fsfilcnt_t = __fsfilcnt_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1235

blkcnt64_t = __blkcnt64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1236

fsblkcnt64_t = __fsblkcnt64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1237

fsfilcnt64_t = __fsfilcnt64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1238

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1243
class struct_anon_44(Structure):
    pass

struct_anon_44.__slots__ = [
    '__low',
    '__high',
]
struct_anon_44._fields_ = [
    ('__low', c_uint),
    ('__high', c_uint),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1248
class union_anon_45(Union):
    pass

union_anon_45.__slots__ = [
    '__value64',
    '__value32',
]
union_anon_45._fields_ = [
    ('__value64', c_ulonglong),
    ('__value32', struct_anon_44),
]

__atomic_wide_counter = union_anon_45# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1248

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1249
class struct___pthread_internal_list(Structure):
    pass

struct___pthread_internal_list.__slots__ = [
    '__prev',
    '__next',
]
struct___pthread_internal_list._fields_ = [
    ('__prev', POINTER(struct___pthread_internal_list)),
    ('__next', POINTER(struct___pthread_internal_list)),
]

__pthread_list_t = struct___pthread_internal_list# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1253

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1254
class struct___pthread_internal_slist(Structure):
    pass

struct___pthread_internal_slist.__slots__ = [
    '__next',
]
struct___pthread_internal_slist._fields_ = [
    ('__next', POINTER(struct___pthread_internal_slist)),
]

__pthread_slist_t = struct___pthread_internal_slist# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1257

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1258
class struct___pthread_mutex_s(Structure):
    pass

struct___pthread_mutex_s.__slots__ = [
    '__lock',
    '__count',
    '__owner',
    '__nusers',
    '__kind',
    '__spins',
    '__elision',
    '__list',
]
struct___pthread_mutex_s._fields_ = [
    ('__lock', c_int),
    ('__count', c_uint),
    ('__owner', c_int),
    ('__nusers', c_uint),
    ('__kind', c_int),
    ('__spins', c_short),
    ('__elision', c_short),
    ('__list', __pthread_list_t),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1269
class struct___pthread_rwlock_arch_t(Structure):
    pass

struct___pthread_rwlock_arch_t.__slots__ = [
    '__readers',
    '__writers',
    '__wrphase_futex',
    '__writers_futex',
    '__pad3',
    '__pad4',
    '__cur_writer',
    '__shared',
    '__rwelision',
    '__pad1',
    '__pad2',
    '__flags',
]
struct___pthread_rwlock_arch_t._fields_ = [
    ('__readers', c_uint),
    ('__writers', c_uint),
    ('__wrphase_futex', c_uint),
    ('__writers_futex', c_uint),
    ('__pad3', c_uint),
    ('__pad4', c_uint),
    ('__cur_writer', c_int),
    ('__shared', c_int),
    ('__rwelision', c_char),
    ('__pad1', c_ubyte * int(7)),
    ('__pad2', c_ulong),
    ('__flags', c_uint),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1284
class struct___pthread_cond_s(Structure):
    pass

struct___pthread_cond_s.__slots__ = [
    '__wseq',
    '__g1_start',
    '__g_size',
    '__g1_orig_size',
    '__wrefs',
    '__g_signals',
    '__unused_initialized_1',
    '__unused_initialized_2',
]
struct___pthread_cond_s._fields_ = [
    ('__wseq', __atomic_wide_counter),
    ('__g1_start', __atomic_wide_counter),
    ('__g_size', c_uint * int(2)),
    ('__g1_orig_size', c_uint),
    ('__wrefs', c_uint),
    ('__g_signals', c_uint * int(2)),
    ('__unused_initialized_1', c_uint),
    ('__unused_initialized_2', c_uint),
]

__tss_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1295

__thrd_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1296

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1300
class struct_anon_46(Structure):
    pass

struct_anon_46.__slots__ = [
    '__data',
]
struct_anon_46._fields_ = [
    ('__data', c_int),
]

__once_flag = struct_anon_46# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1300

pthread_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1301

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1306
class union_anon_47(Union):
    pass

union_anon_47.__slots__ = [
    '__size',
    '__align',
]
union_anon_47._fields_ = [
    ('__size', c_char * int(4)),
    ('__align', c_int),
]

pthread_mutexattr_t = union_anon_47# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1306

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1311
class union_anon_48(Union):
    pass

union_anon_48.__slots__ = [
    '__size',
    '__align',
]
union_anon_48._fields_ = [
    ('__size', c_char * int(4)),
    ('__align', c_int),
]

pthread_condattr_t = union_anon_48# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1311

pthread_key_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1312

pthread_once_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1313

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1314
class union_pthread_attr_t(Union):
    pass

union_pthread_attr_t.__slots__ = [
    '__size',
    '__align',
]
union_pthread_attr_t._fields_ = [
    ('__size', c_char * int(56)),
    ('__align', c_long),
]

pthread_attr_t = union_pthread_attr_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1319

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1325
class union_anon_49(Union):
    pass

union_anon_49.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_49._fields_ = [
    ('__data', struct___pthread_mutex_s),
    ('__size', c_char * int(40)),
    ('__align', c_long),
]

pthread_mutex_t = union_anon_49# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1325

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1331
class union_anon_50(Union):
    pass

union_anon_50.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_50._fields_ = [
    ('__data', struct___pthread_cond_s),
    ('__size', c_char * int(48)),
    ('__align', c_longlong),
]

pthread_cond_t = union_anon_50# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1331

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1337
class union_anon_51(Union):
    pass

union_anon_51.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_51._fields_ = [
    ('__data', struct___pthread_rwlock_arch_t),
    ('__size', c_char * int(56)),
    ('__align', c_long),
]

pthread_rwlock_t = union_anon_51# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1337

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1342
class union_anon_52(Union):
    pass

union_anon_52.__slots__ = [
    '__size',
    '__align',
]
union_anon_52._fields_ = [
    ('__size', c_char * int(8)),
    ('__align', c_long),
]

pthread_rwlockattr_t = union_anon_52# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1342

pthread_spinlock_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1343

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1348
class union_anon_53(Union):
    pass

union_anon_53.__slots__ = [
    '__size',
    '__align',
]
union_anon_53._fields_ = [
    ('__size', c_char * int(32)),
    ('__align', c_long),
]

pthread_barrier_t = union_anon_53# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1348

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1353
class union_anon_54(Union):
    pass

union_anon_54.__slots__ = [
    '__size',
    '__align',
]
union_anon_54._fields_ = [
    ('__size', c_char * int(4)),
    ('__align', c_int),
]

pthread_barrierattr_t = union_anon_54# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1353

__s8 = c_char# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1355

__u8 = c_ubyte# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1356

__s16 = c_short# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1357

__u16 = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1358

__s32 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1359

__u32 = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1360

__s64 = c_longlong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1361

__u64 = c_ulonglong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1362

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1365
class struct_anon_55(Structure):
    pass

struct_anon_55.__slots__ = [
    'fds_bits',
]
struct_anon_55._fields_ = [
    ('fds_bits', c_ulong * int((1024 / (8 * sizeof(c_long))))),
]

__kernel_fd_set = struct_anon_55# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1365

__kernel_sighandler_t = CFUNCTYPE(UNCHECKED(None), c_int)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1366

__kernel_key_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1367

__kernel_mqd_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1368

__kernel_old_uid_t = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1369

__kernel_old_gid_t = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1370

__kernel_old_dev_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1371

__kernel_long_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1372

__kernel_ulong_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1373

__kernel_ino_t = __kernel_ulong_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1374

__kernel_mode_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1375

__kernel_pid_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1376

__kernel_ipc_pid_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1377

__kernel_uid_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1378

__kernel_gid_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1379

__kernel_suseconds_t = __kernel_long_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1380

__kernel_daddr_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1381

__kernel_uid32_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1382

__kernel_gid32_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1383

__kernel_size_t = __kernel_ulong_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1384

__kernel_ssize_t = __kernel_long_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1385

__kernel_ptrdiff_t = __kernel_long_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1386

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1389
class struct_anon_56(Structure):
    pass

struct_anon_56.__slots__ = [
    'val',
]
struct_anon_56._fields_ = [
    ('val', c_int * int(2)),
]

__kernel_fsid_t = struct_anon_56# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1389

__kernel_off_t = __kernel_long_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1390

__kernel_loff_t = c_longlong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1391

__kernel_old_time_t = __kernel_long_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1392

__kernel_time_t = __kernel_long_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1393

__kernel_time64_t = c_longlong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1394

__kernel_clock_t = __kernel_long_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1395

__kernel_timer_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1396

__kernel_clockid_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1397

__kernel_caddr_t = String# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1398

__kernel_uid16_t = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1399

__kernel_gid16_t = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1400

__le16 = __u16# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1403

__be16 = __u16# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1404

__le32 = __u32# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1405

__be32 = __u32# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1406

__le64 = __u64# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1407

__be64 = __u64# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1408

__sum16 = __u16# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1409

__wsum = __u32# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1410

__poll_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1411

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1412
class struct_sched_attr(Structure):
    pass

struct_sched_attr.__slots__ = [
    'size',
    'sched_policy',
    'sched_flags',
    'sched_nice',
    'sched_priority',
    'sched_runtime',
    'sched_deadline',
    'sched_period',
    'sched_util_min',
    'sched_util_max',
]
struct_sched_attr._fields_ = [
    ('size', __u32),
    ('sched_policy', __u32),
    ('sched_flags', __u64),
    ('sched_nice', __s32),
    ('sched_priority', __u32),
    ('sched_runtime', __u64),
    ('sched_deadline', __u64),
    ('sched_period', __u64),
    ('sched_util_min', __u32),
    ('sched_util_max', __u32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1424
class struct_sched_param(Structure):
    pass

struct_sched_param.__slots__ = [
    'sched_priority',
]
struct_sched_param._fields_ = [
    ('sched_priority', c_int),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1428
if _libs["libc.so.6"].has("clone", "cdecl"):
    _func = _libs["libc.so.6"].get("clone", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [CFUNCTYPE(UNCHECKED(c_int), POINTER(None)), POINTER(None), c_int, POINTER(None)]
    clone = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1430
if _libs["libc.so.6"].has("unshare", "cdecl"):
    unshare = _libs["libc.so.6"].get("unshare", "cdecl")
    unshare.argtypes = [c_int]
    unshare.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1431
if _libs["libc.so.6"].has("sched_getcpu", "cdecl"):
    sched_getcpu = _libs["libc.so.6"].get("sched_getcpu", "cdecl")
    sched_getcpu.argtypes = []
    sched_getcpu.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1432
if _libs["libc.so.6"].has("getcpu", "cdecl"):
    getcpu = _libs["libc.so.6"].get("getcpu", "cdecl")
    getcpu.argtypes = [POINTER(c_uint), POINTER(c_uint)]
    getcpu.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1433
if _libs["libc.so.6"].has("setns", "cdecl"):
    setns = _libs["libc.so.6"].get("setns", "cdecl")
    setns.argtypes = [c_int, c_int]
    setns.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1434
if _libs["libc.so.6"].has("sched_setattr", "cdecl"):
    sched_setattr = _libs["libc.so.6"].get("sched_setattr", "cdecl")
    sched_setattr.argtypes = [pid_t, POINTER(struct_sched_attr), c_uint]
    sched_setattr.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1436
if _libs["libc.so.6"].has("sched_getattr", "cdecl"):
    sched_getattr = _libs["libc.so.6"].get("sched_getattr", "cdecl")
    sched_getattr.argtypes = [pid_t, POINTER(struct_sched_attr), c_uint, c_uint]
    sched_getattr.restype = c_int

__cpu_mask = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1439

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1443
class struct_anon_57(Structure):
    pass

struct_anon_57.__slots__ = [
    '__bits',
]
struct_anon_57._fields_ = [
    ('__bits', __cpu_mask * int((1024 / (8 * sizeof(__cpu_mask))))),
]

cpu_set_t = struct_anon_57# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1443

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1444
if _libs["libc.so.6"].has("__sched_cpucount", "cdecl"):
    __sched_cpucount = _libs["libc.so.6"].get("__sched_cpucount", "cdecl")
    __sched_cpucount.argtypes = [c_size_t, POINTER(cpu_set_t)]
    __sched_cpucount.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1446
if _libs["libc.so.6"].has("__sched_cpualloc", "cdecl"):
    __sched_cpualloc = _libs["libc.so.6"].get("__sched_cpualloc", "cdecl")
    __sched_cpualloc.argtypes = [c_size_t]
    __sched_cpualloc.restype = POINTER(cpu_set_t)

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1447
if _libs["libc.so.6"].has("__sched_cpufree", "cdecl"):
    __sched_cpufree = _libs["libc.so.6"].get("__sched_cpufree", "cdecl")
    __sched_cpufree.argtypes = [POINTER(cpu_set_t)]
    __sched_cpufree.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1448
if _libs["libc.so.6"].has("sched_setparam", "cdecl"):
    sched_setparam = _libs["libc.so.6"].get("sched_setparam", "cdecl")
    sched_setparam.argtypes = [__pid_t, POINTER(struct_sched_param)]
    sched_setparam.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1450
if _libs["libc.so.6"].has("sched_getparam", "cdecl"):
    sched_getparam = _libs["libc.so.6"].get("sched_getparam", "cdecl")
    sched_getparam.argtypes = [__pid_t, POINTER(struct_sched_param)]
    sched_getparam.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1451
if _libs["libc.so.6"].has("sched_setscheduler", "cdecl"):
    sched_setscheduler = _libs["libc.so.6"].get("sched_setscheduler", "cdecl")
    sched_setscheduler.argtypes = [__pid_t, c_int, POINTER(struct_sched_param)]
    sched_setscheduler.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1453
if _libs["libc.so.6"].has("sched_getscheduler", "cdecl"):
    sched_getscheduler = _libs["libc.so.6"].get("sched_getscheduler", "cdecl")
    sched_getscheduler.argtypes = [__pid_t]
    sched_getscheduler.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1454
if _libs["libc.so.6"].has("sched_yield", "cdecl"):
    sched_yield = _libs["libc.so.6"].get("sched_yield", "cdecl")
    sched_yield.argtypes = []
    sched_yield.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1455
if _libs["libc.so.6"].has("sched_get_priority_max", "cdecl"):
    sched_get_priority_max = _libs["libc.so.6"].get("sched_get_priority_max", "cdecl")
    sched_get_priority_max.argtypes = [c_int]
    sched_get_priority_max.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1456
if _libs["libc.so.6"].has("sched_get_priority_min", "cdecl"):
    sched_get_priority_min = _libs["libc.so.6"].get("sched_get_priority_min", "cdecl")
    sched_get_priority_min.argtypes = [c_int]
    sched_get_priority_min.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1457
if _libs["libc.so.6"].has("sched_rr_get_interval", "cdecl"):
    sched_rr_get_interval = _libs["libc.so.6"].get("sched_rr_get_interval", "cdecl")
    sched_rr_get_interval.argtypes = [__pid_t, POINTER(struct_timespec)]
    sched_rr_get_interval.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1458
if _libs["libc.so.6"].has("sched_setaffinity", "cdecl"):
    sched_setaffinity = _libs["libc.so.6"].get("sched_setaffinity", "cdecl")
    sched_setaffinity.argtypes = [__pid_t, c_size_t, POINTER(cpu_set_t)]
    sched_setaffinity.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1460
if _libs["libc.so.6"].has("sched_getaffinity", "cdecl"):
    sched_getaffinity = _libs["libc.so.6"].get("sched_getaffinity", "cdecl")
    sched_getaffinity.argtypes = [__pid_t, c_size_t, POINTER(cpu_set_t)]
    sched_getaffinity.restype = c_int

__jmp_buf = c_long * int(8)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1462

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1463
class struct___jmp_buf_tag(Structure):
    pass

struct___jmp_buf_tag.__slots__ = [
    '__jmpbuf',
    '__mask_was_saved',
    '__saved_mask',
]
struct___jmp_buf_tag._fields_ = [
    ('__jmpbuf', __jmp_buf),
    ('__mask_was_saved', c_int),
    ('__saved_mask', __sigset_t),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1470
if _libs["libc.so.6"].has("__sysconf", "cdecl"):
    __sysconf = _libs["libc.so.6"].get("__sysconf", "cdecl")
    __sysconf.argtypes = [c_int]
    __sysconf.restype = c_long

enum_anon_58 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1471

PTHREAD_CREATE_JOINABLE = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1471

PTHREAD_CREATE_DETACHED = (PTHREAD_CREATE_JOINABLE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1471

enum_anon_59 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1476

PTHREAD_MUTEX_TIMED_NP = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1476

PTHREAD_MUTEX_RECURSIVE_NP = (PTHREAD_MUTEX_TIMED_NP + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1476

PTHREAD_MUTEX_ERRORCHECK_NP = (PTHREAD_MUTEX_RECURSIVE_NP + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1476

PTHREAD_MUTEX_ADAPTIVE_NP = (PTHREAD_MUTEX_ERRORCHECK_NP + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1476

PTHREAD_MUTEX_NORMAL = PTHREAD_MUTEX_TIMED_NP# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1476

PTHREAD_MUTEX_RECURSIVE = PTHREAD_MUTEX_RECURSIVE_NP# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1476

PTHREAD_MUTEX_ERRORCHECK = PTHREAD_MUTEX_ERRORCHECK_NP# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1476

PTHREAD_MUTEX_DEFAULT = PTHREAD_MUTEX_NORMAL# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1476

PTHREAD_MUTEX_FAST_NP = PTHREAD_MUTEX_TIMED_NP# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1476

enum_anon_60 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1489

PTHREAD_MUTEX_STALLED = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1489

PTHREAD_MUTEX_STALLED_NP = PTHREAD_MUTEX_STALLED# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1489

PTHREAD_MUTEX_ROBUST = (PTHREAD_MUTEX_STALLED_NP + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1489

PTHREAD_MUTEX_ROBUST_NP = PTHREAD_MUTEX_ROBUST# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1489

enum_anon_61 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1496

PTHREAD_PRIO_NONE = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1496

PTHREAD_PRIO_INHERIT = (PTHREAD_PRIO_NONE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1496

PTHREAD_PRIO_PROTECT = (PTHREAD_PRIO_INHERIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1496

enum_anon_62 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1502

PTHREAD_RWLOCK_PREFER_READER_NP = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1502

PTHREAD_RWLOCK_PREFER_WRITER_NP = (PTHREAD_RWLOCK_PREFER_READER_NP + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1502

PTHREAD_RWLOCK_PREFER_WRITER_NONRECURSIVE_NP = (PTHREAD_RWLOCK_PREFER_WRITER_NP + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1502

PTHREAD_RWLOCK_DEFAULT_NP = PTHREAD_RWLOCK_PREFER_READER_NP# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1502

enum_anon_63 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1509

PTHREAD_INHERIT_SCHED = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1509

PTHREAD_EXPLICIT_SCHED = (PTHREAD_INHERIT_SCHED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1509

enum_anon_64 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1514

PTHREAD_SCOPE_SYSTEM = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1514

PTHREAD_SCOPE_PROCESS = (PTHREAD_SCOPE_SYSTEM + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1514

enum_anon_65 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1519

PTHREAD_PROCESS_PRIVATE = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1519

PTHREAD_PROCESS_SHARED = (PTHREAD_PROCESS_PRIVATE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1519

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1524
class struct__pthread_cleanup_buffer(Structure):
    pass

struct__pthread_cleanup_buffer.__slots__ = [
    '__routine',
    '__arg',
    '__canceltype',
    '__prev',
]
struct__pthread_cleanup_buffer._fields_ = [
    ('__routine', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('__arg', POINTER(None)),
    ('__canceltype', c_int),
    ('__prev', POINTER(struct__pthread_cleanup_buffer)),
]

enum_anon_66 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1531

PTHREAD_CANCEL_ENABLE = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1531

PTHREAD_CANCEL_DISABLE = (PTHREAD_CANCEL_ENABLE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1531

enum_anon_67 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1536

PTHREAD_CANCEL_DEFERRED = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1536

PTHREAD_CANCEL_ASYNCHRONOUS = (PTHREAD_CANCEL_DEFERRED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1536

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1541
if _libs["libc.so.6"].has("pthread_create", "cdecl"):
    pthread_create = _libs["libc.so.6"].get("pthread_create", "cdecl")
    pthread_create.argtypes = [POINTER(pthread_t), POINTER(pthread_attr_t), CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(None)), POINTER(None)]
    pthread_create.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1545
if _libs["libc.so.6"].has("pthread_exit", "cdecl"):
    pthread_exit = _libs["libc.so.6"].get("pthread_exit", "cdecl")
    pthread_exit.argtypes = [POINTER(None)]
    pthread_exit.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1546
if _libs["libc.so.6"].has("pthread_join", "cdecl"):
    pthread_join = _libs["libc.so.6"].get("pthread_join", "cdecl")
    pthread_join.argtypes = [pthread_t, POINTER(POINTER(None))]
    pthread_join.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1547
if _libs["libc.so.6"].has("pthread_tryjoin_np", "cdecl"):
    pthread_tryjoin_np = _libs["libc.so.6"].get("pthread_tryjoin_np", "cdecl")
    pthread_tryjoin_np.argtypes = [pthread_t, POINTER(POINTER(None))]
    pthread_tryjoin_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1548
if _libs["libc.so.6"].has("pthread_timedjoin_np", "cdecl"):
    pthread_timedjoin_np = _libs["libc.so.6"].get("pthread_timedjoin_np", "cdecl")
    pthread_timedjoin_np.argtypes = [pthread_t, POINTER(POINTER(None)), POINTER(struct_timespec)]
    pthread_timedjoin_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1550
if _libs["libc.so.6"].has("pthread_clockjoin_np", "cdecl"):
    pthread_clockjoin_np = _libs["libc.so.6"].get("pthread_clockjoin_np", "cdecl")
    pthread_clockjoin_np.argtypes = [pthread_t, POINTER(POINTER(None)), clockid_t, POINTER(struct_timespec)]
    pthread_clockjoin_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1553
if _libs["libc.so.6"].has("pthread_detach", "cdecl"):
    pthread_detach = _libs["libc.so.6"].get("pthread_detach", "cdecl")
    pthread_detach.argtypes = [pthread_t]
    pthread_detach.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1554
if _libs["libc.so.6"].has("pthread_self", "cdecl"):
    pthread_self = _libs["libc.so.6"].get("pthread_self", "cdecl")
    pthread_self.argtypes = []
    pthread_self.restype = pthread_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1555
if _libs["libc.so.6"].has("pthread_equal", "cdecl"):
    pthread_equal = _libs["libc.so.6"].get("pthread_equal", "cdecl")
    pthread_equal.argtypes = [pthread_t, pthread_t]
    pthread_equal.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1557
if _libs["libc.so.6"].has("pthread_attr_init", "cdecl"):
    pthread_attr_init = _libs["libc.so.6"].get("pthread_attr_init", "cdecl")
    pthread_attr_init.argtypes = [POINTER(pthread_attr_t)]
    pthread_attr_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1558
if _libs["libc.so.6"].has("pthread_attr_destroy", "cdecl"):
    pthread_attr_destroy = _libs["libc.so.6"].get("pthread_attr_destroy", "cdecl")
    pthread_attr_destroy.argtypes = [POINTER(pthread_attr_t)]
    pthread_attr_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1560
if _libs["libc.so.6"].has("pthread_attr_getdetachstate", "cdecl"):
    pthread_attr_getdetachstate = _libs["libc.so.6"].get("pthread_attr_getdetachstate", "cdecl")
    pthread_attr_getdetachstate.argtypes = [POINTER(pthread_attr_t), POINTER(c_int)]
    pthread_attr_getdetachstate.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1563
if _libs["libc.so.6"].has("pthread_attr_setdetachstate", "cdecl"):
    pthread_attr_setdetachstate = _libs["libc.so.6"].get("pthread_attr_setdetachstate", "cdecl")
    pthread_attr_setdetachstate.argtypes = [POINTER(pthread_attr_t), c_int]
    pthread_attr_setdetachstate.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1566
if _libs["libc.so.6"].has("pthread_attr_getguardsize", "cdecl"):
    pthread_attr_getguardsize = _libs["libc.so.6"].get("pthread_attr_getguardsize", "cdecl")
    pthread_attr_getguardsize.argtypes = [POINTER(pthread_attr_t), POINTER(c_size_t)]
    pthread_attr_getguardsize.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1569
if _libs["libc.so.6"].has("pthread_attr_setguardsize", "cdecl"):
    pthread_attr_setguardsize = _libs["libc.so.6"].get("pthread_attr_setguardsize", "cdecl")
    pthread_attr_setguardsize.argtypes = [POINTER(pthread_attr_t), c_size_t]
    pthread_attr_setguardsize.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1572
if _libs["libc.so.6"].has("pthread_attr_getschedparam", "cdecl"):
    pthread_attr_getschedparam = _libs["libc.so.6"].get("pthread_attr_getschedparam", "cdecl")
    pthread_attr_getschedparam.argtypes = [POINTER(pthread_attr_t), POINTER(struct_sched_param)]
    pthread_attr_getschedparam.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1575
if _libs["libc.so.6"].has("pthread_attr_setschedparam", "cdecl"):
    pthread_attr_setschedparam = _libs["libc.so.6"].get("pthread_attr_setschedparam", "cdecl")
    pthread_attr_setschedparam.argtypes = [POINTER(pthread_attr_t), POINTER(struct_sched_param)]
    pthread_attr_setschedparam.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1578
if _libs["libc.so.6"].has("pthread_attr_getschedpolicy", "cdecl"):
    pthread_attr_getschedpolicy = _libs["libc.so.6"].get("pthread_attr_getschedpolicy", "cdecl")
    pthread_attr_getschedpolicy.argtypes = [POINTER(pthread_attr_t), POINTER(c_int)]
    pthread_attr_getschedpolicy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1581
if _libs["libc.so.6"].has("pthread_attr_setschedpolicy", "cdecl"):
    pthread_attr_setschedpolicy = _libs["libc.so.6"].get("pthread_attr_setschedpolicy", "cdecl")
    pthread_attr_setschedpolicy.argtypes = [POINTER(pthread_attr_t), c_int]
    pthread_attr_setschedpolicy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1583
if _libs["libc.so.6"].has("pthread_attr_getinheritsched", "cdecl"):
    pthread_attr_getinheritsched = _libs["libc.so.6"].get("pthread_attr_getinheritsched", "cdecl")
    pthread_attr_getinheritsched.argtypes = [POINTER(pthread_attr_t), POINTER(c_int)]
    pthread_attr_getinheritsched.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1586
if _libs["libc.so.6"].has("pthread_attr_setinheritsched", "cdecl"):
    pthread_attr_setinheritsched = _libs["libc.so.6"].get("pthread_attr_setinheritsched", "cdecl")
    pthread_attr_setinheritsched.argtypes = [POINTER(pthread_attr_t), c_int]
    pthread_attr_setinheritsched.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1589
if _libs["libc.so.6"].has("pthread_attr_getscope", "cdecl"):
    pthread_attr_getscope = _libs["libc.so.6"].get("pthread_attr_getscope", "cdecl")
    pthread_attr_getscope.argtypes = [POINTER(pthread_attr_t), POINTER(c_int)]
    pthread_attr_getscope.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1592
if _libs["libc.so.6"].has("pthread_attr_setscope", "cdecl"):
    pthread_attr_setscope = _libs["libc.so.6"].get("pthread_attr_setscope", "cdecl")
    pthread_attr_setscope.argtypes = [POINTER(pthread_attr_t), c_int]
    pthread_attr_setscope.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1594
if _libs["libc.so.6"].has("pthread_attr_getstackaddr", "cdecl"):
    pthread_attr_getstackaddr = _libs["libc.so.6"].get("pthread_attr_getstackaddr", "cdecl")
    pthread_attr_getstackaddr.argtypes = [POINTER(pthread_attr_t), POINTER(POINTER(None))]
    pthread_attr_getstackaddr.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1597
if _libs["libc.so.6"].has("pthread_attr_setstackaddr", "cdecl"):
    pthread_attr_setstackaddr = _libs["libc.so.6"].get("pthread_attr_setstackaddr", "cdecl")
    pthread_attr_setstackaddr.argtypes = [POINTER(pthread_attr_t), POINTER(None)]
    pthread_attr_setstackaddr.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1600
if _libs["libc.so.6"].has("pthread_attr_getstacksize", "cdecl"):
    pthread_attr_getstacksize = _libs["libc.so.6"].get("pthread_attr_getstacksize", "cdecl")
    pthread_attr_getstacksize.argtypes = [POINTER(pthread_attr_t), POINTER(c_size_t)]
    pthread_attr_getstacksize.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1603
if _libs["libc.so.6"].has("pthread_attr_setstacksize", "cdecl"):
    pthread_attr_setstacksize = _libs["libc.so.6"].get("pthread_attr_setstacksize", "cdecl")
    pthread_attr_setstacksize.argtypes = [POINTER(pthread_attr_t), c_size_t]
    pthread_attr_setstacksize.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1606
if _libs["libc.so.6"].has("pthread_attr_getstack", "cdecl"):
    pthread_attr_getstack = _libs["libc.so.6"].get("pthread_attr_getstack", "cdecl")
    pthread_attr_getstack.argtypes = [POINTER(pthread_attr_t), POINTER(POINTER(None)), POINTER(c_size_t)]
    pthread_attr_getstack.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1610
if _libs["libc.so.6"].has("pthread_attr_setstack", "cdecl"):
    pthread_attr_setstack = _libs["libc.so.6"].get("pthread_attr_setstack", "cdecl")
    pthread_attr_setstack.argtypes = [POINTER(pthread_attr_t), POINTER(None), c_size_t]
    pthread_attr_setstack.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1612
if _libs["libc.so.6"].has("pthread_attr_setaffinity_np", "cdecl"):
    pthread_attr_setaffinity_np = _libs["libc.so.6"].get("pthread_attr_setaffinity_np", "cdecl")
    pthread_attr_setaffinity_np.argtypes = [POINTER(pthread_attr_t), c_size_t, POINTER(cpu_set_t)]
    pthread_attr_setaffinity_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1616
if _libs["libc.so.6"].has("pthread_attr_getaffinity_np", "cdecl"):
    pthread_attr_getaffinity_np = _libs["libc.so.6"].get("pthread_attr_getaffinity_np", "cdecl")
    pthread_attr_getaffinity_np.argtypes = [POINTER(pthread_attr_t), c_size_t, POINTER(cpu_set_t)]
    pthread_attr_getaffinity_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1620
if _libs["libc.so.6"].has("pthread_getattr_default_np", "cdecl"):
    pthread_getattr_default_np = _libs["libc.so.6"].get("pthread_getattr_default_np", "cdecl")
    pthread_getattr_default_np.argtypes = [POINTER(pthread_attr_t)]
    pthread_getattr_default_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1622
if _libs["libc.so.6"].has("pthread_attr_setsigmask_np", "cdecl"):
    pthread_attr_setsigmask_np = _libs["libc.so.6"].get("pthread_attr_setsigmask_np", "cdecl")
    pthread_attr_setsigmask_np.argtypes = [POINTER(pthread_attr_t), POINTER(__sigset_t)]
    pthread_attr_setsigmask_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1624
if _libs["libc.so.6"].has("pthread_attr_getsigmask_np", "cdecl"):
    pthread_attr_getsigmask_np = _libs["libc.so.6"].get("pthread_attr_getsigmask_np", "cdecl")
    pthread_attr_getsigmask_np.argtypes = [POINTER(pthread_attr_t), POINTER(__sigset_t)]
    pthread_attr_getsigmask_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1626
if _libs["libc.so.6"].has("pthread_setattr_default_np", "cdecl"):
    pthread_setattr_default_np = _libs["libc.so.6"].get("pthread_setattr_default_np", "cdecl")
    pthread_setattr_default_np.argtypes = [POINTER(pthread_attr_t)]
    pthread_setattr_default_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1628
if _libs["libc.so.6"].has("pthread_getattr_np", "cdecl"):
    pthread_getattr_np = _libs["libc.so.6"].get("pthread_getattr_np", "cdecl")
    pthread_getattr_np.argtypes = [pthread_t, POINTER(pthread_attr_t)]
    pthread_getattr_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1630
if _libs["libc.so.6"].has("pthread_setschedparam", "cdecl"):
    pthread_setschedparam = _libs["libc.so.6"].get("pthread_setschedparam", "cdecl")
    pthread_setschedparam.argtypes = [pthread_t, c_int, POINTER(struct_sched_param)]
    pthread_setschedparam.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1633
if _libs["libc.so.6"].has("pthread_getschedparam", "cdecl"):
    pthread_getschedparam = _libs["libc.so.6"].get("pthread_getschedparam", "cdecl")
    pthread_getschedparam.argtypes = [pthread_t, POINTER(c_int), POINTER(struct_sched_param)]
    pthread_getschedparam.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1637
if _libs["libc.so.6"].has("pthread_setschedprio", "cdecl"):
    pthread_setschedprio = _libs["libc.so.6"].get("pthread_setschedprio", "cdecl")
    pthread_setschedprio.argtypes = [pthread_t, c_int]
    pthread_setschedprio.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1639
if _libs["libc.so.6"].has("pthread_getname_np", "cdecl"):
    pthread_getname_np = _libs["libc.so.6"].get("pthread_getname_np", "cdecl")
    pthread_getname_np.argtypes = [pthread_t, String, c_size_t]
    pthread_getname_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1642
if _libs["libc.so.6"].has("pthread_setname_np", "cdecl"):
    pthread_setname_np = _libs["libc.so.6"].get("pthread_setname_np", "cdecl")
    pthread_setname_np.argtypes = [pthread_t, String]
    pthread_setname_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1644
if _libs["libc.so.6"].has("pthread_getconcurrency", "cdecl"):
    pthread_getconcurrency = _libs["libc.so.6"].get("pthread_getconcurrency", "cdecl")
    pthread_getconcurrency.argtypes = []
    pthread_getconcurrency.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1645
if _libs["libc.so.6"].has("pthread_setconcurrency", "cdecl"):
    pthread_setconcurrency = _libs["libc.so.6"].get("pthread_setconcurrency", "cdecl")
    pthread_setconcurrency.argtypes = [c_int]
    pthread_setconcurrency.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1646
for _lib in _libs.values():
    if not _lib.has("pthread_yield", "cdecl"):
        continue
    pthread_yield = _lib.get("pthread_yield", "cdecl")
    pthread_yield.argtypes = []
    pthread_yield.restype = c_int
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1647
for _lib in _libs.values():
    if not _lib.has("pthread_yield", "cdecl"):
        continue
    pthread_yield = _lib.get("pthread_yield", "cdecl")
    pthread_yield.argtypes = []
    pthread_yield.restype = c_int
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1649
if _libs["libc.so.6"].has("pthread_setaffinity_np", "cdecl"):
    pthread_setaffinity_np = _libs["libc.so.6"].get("pthread_setaffinity_np", "cdecl")
    pthread_setaffinity_np.argtypes = [pthread_t, c_size_t, POINTER(cpu_set_t)]
    pthread_setaffinity_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1652
if _libs["libc.so.6"].has("pthread_getaffinity_np", "cdecl"):
    pthread_getaffinity_np = _libs["libc.so.6"].get("pthread_getaffinity_np", "cdecl")
    pthread_getaffinity_np.argtypes = [pthread_t, c_size_t, POINTER(cpu_set_t)]
    pthread_getaffinity_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1655
if _libs["libc.so.6"].has("pthread_once", "cdecl"):
    pthread_once = _libs["libc.so.6"].get("pthread_once", "cdecl")
    pthread_once.argtypes = [POINTER(pthread_once_t), CFUNCTYPE(UNCHECKED(None), )]
    pthread_once.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1657
if _libs["libc.so.6"].has("pthread_setcancelstate", "cdecl"):
    pthread_setcancelstate = _libs["libc.so.6"].get("pthread_setcancelstate", "cdecl")
    pthread_setcancelstate.argtypes = [c_int, POINTER(c_int)]
    pthread_setcancelstate.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1658
if _libs["libc.so.6"].has("pthread_setcanceltype", "cdecl"):
    pthread_setcanceltype = _libs["libc.so.6"].get("pthread_setcanceltype", "cdecl")
    pthread_setcanceltype.argtypes = [c_int, POINTER(c_int)]
    pthread_setcanceltype.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1659
if _libs["libc.so.6"].has("pthread_cancel", "cdecl"):
    pthread_cancel = _libs["libc.so.6"].get("pthread_cancel", "cdecl")
    pthread_cancel.argtypes = [pthread_t]
    pthread_cancel.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1660
if _libs["libc.so.6"].has("pthread_testcancel", "cdecl"):
    pthread_testcancel = _libs["libc.so.6"].get("pthread_testcancel", "cdecl")
    pthread_testcancel.argtypes = []
    pthread_testcancel.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1661
class struct___cancel_jmp_buf_tag(Structure):
    pass

struct___cancel_jmp_buf_tag.__slots__ = [
    '__cancel_jmp_buf',
    '__mask_was_saved',
]
struct___cancel_jmp_buf_tag._fields_ = [
    ('__cancel_jmp_buf', __jmp_buf),
    ('__mask_was_saved', c_int),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1670
class struct_anon_68(Structure):
    pass

struct_anon_68.__slots__ = [
    '__cancel_jmp_buf',
    '__pad',
]
struct_anon_68._fields_ = [
    ('__cancel_jmp_buf', struct___cancel_jmp_buf_tag * int(1)),
    ('__pad', POINTER(None) * int(4)),
]

__pthread_unwind_buf_t = struct_anon_68# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1670

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1671
class struct___pthread_cleanup_frame(Structure):
    pass

struct___pthread_cleanup_frame.__slots__ = [
    '__cancel_routine',
    '__cancel_arg',
    '__do_it',
    '__cancel_type',
]
struct___pthread_cleanup_frame._fields_ = [
    ('__cancel_routine', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('__cancel_arg', POINTER(None)),
    ('__do_it', c_int),
    ('__cancel_type', c_int),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1678
if _libs["libc.so.6"].has("__pthread_register_cancel", "cdecl"):
    __pthread_register_cancel = _libs["libc.so.6"].get("__pthread_register_cancel", "cdecl")
    __pthread_register_cancel.argtypes = [POINTER(__pthread_unwind_buf_t)]
    __pthread_register_cancel.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1680
if _libs["libc.so.6"].has("__pthread_unregister_cancel", "cdecl"):
    __pthread_unregister_cancel = _libs["libc.so.6"].get("__pthread_unregister_cancel", "cdecl")
    __pthread_unregister_cancel.argtypes = [POINTER(__pthread_unwind_buf_t)]
    __pthread_unregister_cancel.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1682
if _libs["libc.so.6"].has("__pthread_register_cancel_defer", "cdecl"):
    __pthread_register_cancel_defer = _libs["libc.so.6"].get("__pthread_register_cancel_defer", "cdecl")
    __pthread_register_cancel_defer.argtypes = [POINTER(__pthread_unwind_buf_t)]
    __pthread_register_cancel_defer.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1684
if _libs["libc.so.6"].has("__pthread_unregister_cancel_restore", "cdecl"):
    __pthread_unregister_cancel_restore = _libs["libc.so.6"].get("__pthread_unregister_cancel_restore", "cdecl")
    __pthread_unregister_cancel_restore.argtypes = [POINTER(__pthread_unwind_buf_t)]
    __pthread_unregister_cancel_restore.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1686
if _libs["libc.so.6"].has("__pthread_unwind_next", "cdecl"):
    __pthread_unwind_next = _libs["libc.so.6"].get("__pthread_unwind_next", "cdecl")
    __pthread_unwind_next.argtypes = [POINTER(__pthread_unwind_buf_t)]
    __pthread_unwind_next.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1688
if _libs["libc.so.6"].has("__sigsetjmp", "cdecl"):
    __sigsetjmp = _libs["libc.so.6"].get("__sigsetjmp", "cdecl")
    __sigsetjmp.argtypes = [struct___jmp_buf_tag * int(1), c_int]
    __sigsetjmp.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1690
if _libs["libc.so.6"].has("pthread_mutex_init", "cdecl"):
    pthread_mutex_init = _libs["libc.so.6"].get("pthread_mutex_init", "cdecl")
    pthread_mutex_init.argtypes = [POINTER(pthread_mutex_t), POINTER(pthread_mutexattr_t)]
    pthread_mutex_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1693
if _libs["libc.so.6"].has("pthread_mutex_destroy", "cdecl"):
    pthread_mutex_destroy = _libs["libc.so.6"].get("pthread_mutex_destroy", "cdecl")
    pthread_mutex_destroy.argtypes = [POINTER(pthread_mutex_t)]
    pthread_mutex_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1695
if _libs["libc.so.6"].has("pthread_mutex_trylock", "cdecl"):
    pthread_mutex_trylock = _libs["libc.so.6"].get("pthread_mutex_trylock", "cdecl")
    pthread_mutex_trylock.argtypes = [POINTER(pthread_mutex_t)]
    pthread_mutex_trylock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1697
if _libs["libc.so.6"].has("pthread_mutex_lock", "cdecl"):
    pthread_mutex_lock = _libs["libc.so.6"].get("pthread_mutex_lock", "cdecl")
    pthread_mutex_lock.argtypes = [POINTER(pthread_mutex_t)]
    pthread_mutex_lock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1699
if _libs["libc.so.6"].has("pthread_mutex_timedlock", "cdecl"):
    pthread_mutex_timedlock = _libs["libc.so.6"].get("pthread_mutex_timedlock", "cdecl")
    pthread_mutex_timedlock.argtypes = [POINTER(pthread_mutex_t), POINTER(struct_timespec)]
    pthread_mutex_timedlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1702
if _libs["libc.so.6"].has("pthread_mutex_clocklock", "cdecl"):
    pthread_mutex_clocklock = _libs["libc.so.6"].get("pthread_mutex_clocklock", "cdecl")
    pthread_mutex_clocklock.argtypes = [POINTER(pthread_mutex_t), clockid_t, POINTER(struct_timespec)]
    pthread_mutex_clocklock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1706
if _libs["libc.so.6"].has("pthread_mutex_unlock", "cdecl"):
    pthread_mutex_unlock = _libs["libc.so.6"].get("pthread_mutex_unlock", "cdecl")
    pthread_mutex_unlock.argtypes = [POINTER(pthread_mutex_t)]
    pthread_mutex_unlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1708
if _libs["libc.so.6"].has("pthread_mutex_getprioceiling", "cdecl"):
    pthread_mutex_getprioceiling = _libs["libc.so.6"].get("pthread_mutex_getprioceiling", "cdecl")
    pthread_mutex_getprioceiling.argtypes = [POINTER(pthread_mutex_t), POINTER(c_int)]
    pthread_mutex_getprioceiling.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1712
if _libs["libc.so.6"].has("pthread_mutex_setprioceiling", "cdecl"):
    pthread_mutex_setprioceiling = _libs["libc.so.6"].get("pthread_mutex_setprioceiling", "cdecl")
    pthread_mutex_setprioceiling.argtypes = [POINTER(pthread_mutex_t), c_int, POINTER(c_int)]
    pthread_mutex_setprioceiling.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1716
if _libs["libc.so.6"].has("pthread_mutex_consistent", "cdecl"):
    pthread_mutex_consistent = _libs["libc.so.6"].get("pthread_mutex_consistent", "cdecl")
    pthread_mutex_consistent.argtypes = [POINTER(pthread_mutex_t)]
    pthread_mutex_consistent.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1718
for _lib in _libs.values():
    if not _lib.has("pthread_mutex_consistent_np", "cdecl"):
        continue
    pthread_mutex_consistent_np = _lib.get("pthread_mutex_consistent_np", "cdecl")
    pthread_mutex_consistent_np.argtypes = [POINTER(pthread_mutex_t)]
    pthread_mutex_consistent_np.restype = c_int
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1720
if _libs["libc.so.6"].has("pthread_mutexattr_init", "cdecl"):
    pthread_mutexattr_init = _libs["libc.so.6"].get("pthread_mutexattr_init", "cdecl")
    pthread_mutexattr_init.argtypes = [POINTER(pthread_mutexattr_t)]
    pthread_mutexattr_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1722
if _libs["libc.so.6"].has("pthread_mutexattr_destroy", "cdecl"):
    pthread_mutexattr_destroy = _libs["libc.so.6"].get("pthread_mutexattr_destroy", "cdecl")
    pthread_mutexattr_destroy.argtypes = [POINTER(pthread_mutexattr_t)]
    pthread_mutexattr_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1724
if _libs["libc.so.6"].has("pthread_mutexattr_getpshared", "cdecl"):
    pthread_mutexattr_getpshared = _libs["libc.so.6"].get("pthread_mutexattr_getpshared", "cdecl")
    pthread_mutexattr_getpshared.argtypes = [POINTER(pthread_mutexattr_t), POINTER(c_int)]
    pthread_mutexattr_getpshared.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1728
if _libs["libc.so.6"].has("pthread_mutexattr_setpshared", "cdecl"):
    pthread_mutexattr_setpshared = _libs["libc.so.6"].get("pthread_mutexattr_setpshared", "cdecl")
    pthread_mutexattr_setpshared.argtypes = [POINTER(pthread_mutexattr_t), c_int]
    pthread_mutexattr_setpshared.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1731
if _libs["libc.so.6"].has("pthread_mutexattr_gettype", "cdecl"):
    pthread_mutexattr_gettype = _libs["libc.so.6"].get("pthread_mutexattr_gettype", "cdecl")
    pthread_mutexattr_gettype.argtypes = [POINTER(pthread_mutexattr_t), POINTER(c_int)]
    pthread_mutexattr_gettype.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1734
if _libs["libc.so.6"].has("pthread_mutexattr_settype", "cdecl"):
    pthread_mutexattr_settype = _libs["libc.so.6"].get("pthread_mutexattr_settype", "cdecl")
    pthread_mutexattr_settype.argtypes = [POINTER(pthread_mutexattr_t), c_int]
    pthread_mutexattr_settype.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1736
if _libs["libc.so.6"].has("pthread_mutexattr_getprotocol", "cdecl"):
    pthread_mutexattr_getprotocol = _libs["libc.so.6"].get("pthread_mutexattr_getprotocol", "cdecl")
    pthread_mutexattr_getprotocol.argtypes = [POINTER(pthread_mutexattr_t), POINTER(c_int)]
    pthread_mutexattr_getprotocol.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1740
if _libs["libc.so.6"].has("pthread_mutexattr_setprotocol", "cdecl"):
    pthread_mutexattr_setprotocol = _libs["libc.so.6"].get("pthread_mutexattr_setprotocol", "cdecl")
    pthread_mutexattr_setprotocol.argtypes = [POINTER(pthread_mutexattr_t), c_int]
    pthread_mutexattr_setprotocol.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1743
if _libs["libc.so.6"].has("pthread_mutexattr_getprioceiling", "cdecl"):
    pthread_mutexattr_getprioceiling = _libs["libc.so.6"].get("pthread_mutexattr_getprioceiling", "cdecl")
    pthread_mutexattr_getprioceiling.argtypes = [POINTER(pthread_mutexattr_t), POINTER(c_int)]
    pthread_mutexattr_getprioceiling.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1747
if _libs["libc.so.6"].has("pthread_mutexattr_setprioceiling", "cdecl"):
    pthread_mutexattr_setprioceiling = _libs["libc.so.6"].get("pthread_mutexattr_setprioceiling", "cdecl")
    pthread_mutexattr_setprioceiling.argtypes = [POINTER(pthread_mutexattr_t), c_int]
    pthread_mutexattr_setprioceiling.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1750
if _libs["libc.so.6"].has("pthread_mutexattr_getrobust", "cdecl"):
    pthread_mutexattr_getrobust = _libs["libc.so.6"].get("pthread_mutexattr_getrobust", "cdecl")
    pthread_mutexattr_getrobust.argtypes = [POINTER(pthread_mutexattr_t), POINTER(c_int)]
    pthread_mutexattr_getrobust.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1753
for _lib in _libs.values():
    if not _lib.has("pthread_mutexattr_getrobust_np", "cdecl"):
        continue
    pthread_mutexattr_getrobust_np = _lib.get("pthread_mutexattr_getrobust_np", "cdecl")
    pthread_mutexattr_getrobust_np.argtypes = [POINTER(pthread_mutexattr_t), POINTER(c_int)]
    pthread_mutexattr_getrobust_np.restype = c_int
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1755
if _libs["libc.so.6"].has("pthread_mutexattr_setrobust", "cdecl"):
    pthread_mutexattr_setrobust = _libs["libc.so.6"].get("pthread_mutexattr_setrobust", "cdecl")
    pthread_mutexattr_setrobust.argtypes = [POINTER(pthread_mutexattr_t), c_int]
    pthread_mutexattr_setrobust.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1758
for _lib in _libs.values():
    if not _lib.has("pthread_mutexattr_setrobust_np", "cdecl"):
        continue
    pthread_mutexattr_setrobust_np = _lib.get("pthread_mutexattr_setrobust_np", "cdecl")
    pthread_mutexattr_setrobust_np.argtypes = [POINTER(pthread_mutexattr_t), c_int]
    pthread_mutexattr_setrobust_np.restype = c_int
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1760
if _libs["libc.so.6"].has("pthread_rwlock_init", "cdecl"):
    pthread_rwlock_init = _libs["libc.so.6"].get("pthread_rwlock_init", "cdecl")
    pthread_rwlock_init.argtypes = [POINTER(pthread_rwlock_t), POINTER(pthread_rwlockattr_t)]
    pthread_rwlock_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1763
if _libs["libc.so.6"].has("pthread_rwlock_destroy", "cdecl"):
    pthread_rwlock_destroy = _libs["libc.so.6"].get("pthread_rwlock_destroy", "cdecl")
    pthread_rwlock_destroy.argtypes = [POINTER(pthread_rwlock_t)]
    pthread_rwlock_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1765
if _libs["libc.so.6"].has("pthread_rwlock_rdlock", "cdecl"):
    pthread_rwlock_rdlock = _libs["libc.so.6"].get("pthread_rwlock_rdlock", "cdecl")
    pthread_rwlock_rdlock.argtypes = [POINTER(pthread_rwlock_t)]
    pthread_rwlock_rdlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1767
if _libs["libc.so.6"].has("pthread_rwlock_tryrdlock", "cdecl"):
    pthread_rwlock_tryrdlock = _libs["libc.so.6"].get("pthread_rwlock_tryrdlock", "cdecl")
    pthread_rwlock_tryrdlock.argtypes = [POINTER(pthread_rwlock_t)]
    pthread_rwlock_tryrdlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1769
if _libs["libc.so.6"].has("pthread_rwlock_timedrdlock", "cdecl"):
    pthread_rwlock_timedrdlock = _libs["libc.so.6"].get("pthread_rwlock_timedrdlock", "cdecl")
    pthread_rwlock_timedrdlock.argtypes = [POINTER(pthread_rwlock_t), POINTER(struct_timespec)]
    pthread_rwlock_timedrdlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1772
if _libs["libc.so.6"].has("pthread_rwlock_clockrdlock", "cdecl"):
    pthread_rwlock_clockrdlock = _libs["libc.so.6"].get("pthread_rwlock_clockrdlock", "cdecl")
    pthread_rwlock_clockrdlock.argtypes = [POINTER(pthread_rwlock_t), clockid_t, POINTER(struct_timespec)]
    pthread_rwlock_clockrdlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1776
if _libs["libc.so.6"].has("pthread_rwlock_wrlock", "cdecl"):
    pthread_rwlock_wrlock = _libs["libc.so.6"].get("pthread_rwlock_wrlock", "cdecl")
    pthread_rwlock_wrlock.argtypes = [POINTER(pthread_rwlock_t)]
    pthread_rwlock_wrlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1778
if _libs["libc.so.6"].has("pthread_rwlock_trywrlock", "cdecl"):
    pthread_rwlock_trywrlock = _libs["libc.so.6"].get("pthread_rwlock_trywrlock", "cdecl")
    pthread_rwlock_trywrlock.argtypes = [POINTER(pthread_rwlock_t)]
    pthread_rwlock_trywrlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1780
if _libs["libc.so.6"].has("pthread_rwlock_timedwrlock", "cdecl"):
    pthread_rwlock_timedwrlock = _libs["libc.so.6"].get("pthread_rwlock_timedwrlock", "cdecl")
    pthread_rwlock_timedwrlock.argtypes = [POINTER(pthread_rwlock_t), POINTER(struct_timespec)]
    pthread_rwlock_timedwrlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1783
if _libs["libc.so.6"].has("pthread_rwlock_clockwrlock", "cdecl"):
    pthread_rwlock_clockwrlock = _libs["libc.so.6"].get("pthread_rwlock_clockwrlock", "cdecl")
    pthread_rwlock_clockwrlock.argtypes = [POINTER(pthread_rwlock_t), clockid_t, POINTER(struct_timespec)]
    pthread_rwlock_clockwrlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1787
if _libs["libc.so.6"].has("pthread_rwlock_unlock", "cdecl"):
    pthread_rwlock_unlock = _libs["libc.so.6"].get("pthread_rwlock_unlock", "cdecl")
    pthread_rwlock_unlock.argtypes = [POINTER(pthread_rwlock_t)]
    pthread_rwlock_unlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1789
if _libs["libc.so.6"].has("pthread_rwlockattr_init", "cdecl"):
    pthread_rwlockattr_init = _libs["libc.so.6"].get("pthread_rwlockattr_init", "cdecl")
    pthread_rwlockattr_init.argtypes = [POINTER(pthread_rwlockattr_t)]
    pthread_rwlockattr_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1791
if _libs["libc.so.6"].has("pthread_rwlockattr_destroy", "cdecl"):
    pthread_rwlockattr_destroy = _libs["libc.so.6"].get("pthread_rwlockattr_destroy", "cdecl")
    pthread_rwlockattr_destroy.argtypes = [POINTER(pthread_rwlockattr_t)]
    pthread_rwlockattr_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1793
if _libs["libc.so.6"].has("pthread_rwlockattr_getpshared", "cdecl"):
    pthread_rwlockattr_getpshared = _libs["libc.so.6"].get("pthread_rwlockattr_getpshared", "cdecl")
    pthread_rwlockattr_getpshared.argtypes = [POINTER(pthread_rwlockattr_t), POINTER(c_int)]
    pthread_rwlockattr_getpshared.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1797
if _libs["libc.so.6"].has("pthread_rwlockattr_setpshared", "cdecl"):
    pthread_rwlockattr_setpshared = _libs["libc.so.6"].get("pthread_rwlockattr_setpshared", "cdecl")
    pthread_rwlockattr_setpshared.argtypes = [POINTER(pthread_rwlockattr_t), c_int]
    pthread_rwlockattr_setpshared.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1800
if _libs["libc.so.6"].has("pthread_rwlockattr_getkind_np", "cdecl"):
    pthread_rwlockattr_getkind_np = _libs["libc.so.6"].get("pthread_rwlockattr_getkind_np", "cdecl")
    pthread_rwlockattr_getkind_np.argtypes = [POINTER(pthread_rwlockattr_t), POINTER(c_int)]
    pthread_rwlockattr_getkind_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1804
if _libs["libc.so.6"].has("pthread_rwlockattr_setkind_np", "cdecl"):
    pthread_rwlockattr_setkind_np = _libs["libc.so.6"].get("pthread_rwlockattr_setkind_np", "cdecl")
    pthread_rwlockattr_setkind_np.argtypes = [POINTER(pthread_rwlockattr_t), c_int]
    pthread_rwlockattr_setkind_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1806
if _libs["libc.so.6"].has("pthread_cond_init", "cdecl"):
    pthread_cond_init = _libs["libc.so.6"].get("pthread_cond_init", "cdecl")
    pthread_cond_init.argtypes = [POINTER(pthread_cond_t), POINTER(pthread_condattr_t)]
    pthread_cond_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1809
if _libs["libc.so.6"].has("pthread_cond_destroy", "cdecl"):
    pthread_cond_destroy = _libs["libc.so.6"].get("pthread_cond_destroy", "cdecl")
    pthread_cond_destroy.argtypes = [POINTER(pthread_cond_t)]
    pthread_cond_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1811
if _libs["libc.so.6"].has("pthread_cond_signal", "cdecl"):
    pthread_cond_signal = _libs["libc.so.6"].get("pthread_cond_signal", "cdecl")
    pthread_cond_signal.argtypes = [POINTER(pthread_cond_t)]
    pthread_cond_signal.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1813
if _libs["libc.so.6"].has("pthread_cond_broadcast", "cdecl"):
    pthread_cond_broadcast = _libs["libc.so.6"].get("pthread_cond_broadcast", "cdecl")
    pthread_cond_broadcast.argtypes = [POINTER(pthread_cond_t)]
    pthread_cond_broadcast.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1815
if _libs["libc.so.6"].has("pthread_cond_wait", "cdecl"):
    pthread_cond_wait = _libs["libc.so.6"].get("pthread_cond_wait", "cdecl")
    pthread_cond_wait.argtypes = [POINTER(pthread_cond_t), POINTER(pthread_mutex_t)]
    pthread_cond_wait.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1818
if _libs["libc.so.6"].has("pthread_cond_timedwait", "cdecl"):
    pthread_cond_timedwait = _libs["libc.so.6"].get("pthread_cond_timedwait", "cdecl")
    pthread_cond_timedwait.argtypes = [POINTER(pthread_cond_t), POINTER(pthread_mutex_t), POINTER(struct_timespec)]
    pthread_cond_timedwait.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1822
if _libs["libc.so.6"].has("pthread_cond_clockwait", "cdecl"):
    pthread_cond_clockwait = _libs["libc.so.6"].get("pthread_cond_clockwait", "cdecl")
    pthread_cond_clockwait.argtypes = [POINTER(pthread_cond_t), POINTER(pthread_mutex_t), __clockid_t, POINTER(struct_timespec)]
    pthread_cond_clockwait.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1827
if _libs["libc.so.6"].has("pthread_condattr_init", "cdecl"):
    pthread_condattr_init = _libs["libc.so.6"].get("pthread_condattr_init", "cdecl")
    pthread_condattr_init.argtypes = [POINTER(pthread_condattr_t)]
    pthread_condattr_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1829
if _libs["libc.so.6"].has("pthread_condattr_destroy", "cdecl"):
    pthread_condattr_destroy = _libs["libc.so.6"].get("pthread_condattr_destroy", "cdecl")
    pthread_condattr_destroy.argtypes = [POINTER(pthread_condattr_t)]
    pthread_condattr_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1831
if _libs["libc.so.6"].has("pthread_condattr_getpshared", "cdecl"):
    pthread_condattr_getpshared = _libs["libc.so.6"].get("pthread_condattr_getpshared", "cdecl")
    pthread_condattr_getpshared.argtypes = [POINTER(pthread_condattr_t), POINTER(c_int)]
    pthread_condattr_getpshared.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1835
if _libs["libc.so.6"].has("pthread_condattr_setpshared", "cdecl"):
    pthread_condattr_setpshared = _libs["libc.so.6"].get("pthread_condattr_setpshared", "cdecl")
    pthread_condattr_setpshared.argtypes = [POINTER(pthread_condattr_t), c_int]
    pthread_condattr_setpshared.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1837
if _libs["libc.so.6"].has("pthread_condattr_getclock", "cdecl"):
    pthread_condattr_getclock = _libs["libc.so.6"].get("pthread_condattr_getclock", "cdecl")
    pthread_condattr_getclock.argtypes = [POINTER(pthread_condattr_t), POINTER(__clockid_t)]
    pthread_condattr_getclock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1841
if _libs["libc.so.6"].has("pthread_condattr_setclock", "cdecl"):
    pthread_condattr_setclock = _libs["libc.so.6"].get("pthread_condattr_setclock", "cdecl")
    pthread_condattr_setclock.argtypes = [POINTER(pthread_condattr_t), __clockid_t]
    pthread_condattr_setclock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1844
if _libs["libc.so.6"].has("pthread_spin_init", "cdecl"):
    pthread_spin_init = _libs["libc.so.6"].get("pthread_spin_init", "cdecl")
    pthread_spin_init.argtypes = [POINTER(pthread_spinlock_t), c_int]
    pthread_spin_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1846
if _libs["libc.so.6"].has("pthread_spin_destroy", "cdecl"):
    pthread_spin_destroy = _libs["libc.so.6"].get("pthread_spin_destroy", "cdecl")
    pthread_spin_destroy.argtypes = [POINTER(pthread_spinlock_t)]
    pthread_spin_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1848
if _libs["libc.so.6"].has("pthread_spin_lock", "cdecl"):
    pthread_spin_lock = _libs["libc.so.6"].get("pthread_spin_lock", "cdecl")
    pthread_spin_lock.argtypes = [POINTER(pthread_spinlock_t)]
    pthread_spin_lock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1850
if _libs["libc.so.6"].has("pthread_spin_trylock", "cdecl"):
    pthread_spin_trylock = _libs["libc.so.6"].get("pthread_spin_trylock", "cdecl")
    pthread_spin_trylock.argtypes = [POINTER(pthread_spinlock_t)]
    pthread_spin_trylock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1852
if _libs["libc.so.6"].has("pthread_spin_unlock", "cdecl"):
    pthread_spin_unlock = _libs["libc.so.6"].get("pthread_spin_unlock", "cdecl")
    pthread_spin_unlock.argtypes = [POINTER(pthread_spinlock_t)]
    pthread_spin_unlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1854
if _libs["libc.so.6"].has("pthread_barrier_init", "cdecl"):
    pthread_barrier_init = _libs["libc.so.6"].get("pthread_barrier_init", "cdecl")
    pthread_barrier_init.argtypes = [POINTER(pthread_barrier_t), POINTER(pthread_barrierattr_t), c_uint]
    pthread_barrier_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1858
if _libs["libc.so.6"].has("pthread_barrier_destroy", "cdecl"):
    pthread_barrier_destroy = _libs["libc.so.6"].get("pthread_barrier_destroy", "cdecl")
    pthread_barrier_destroy.argtypes = [POINTER(pthread_barrier_t)]
    pthread_barrier_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1860
if _libs["libc.so.6"].has("pthread_barrier_wait", "cdecl"):
    pthread_barrier_wait = _libs["libc.so.6"].get("pthread_barrier_wait", "cdecl")
    pthread_barrier_wait.argtypes = [POINTER(pthread_barrier_t)]
    pthread_barrier_wait.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1862
if _libs["libc.so.6"].has("pthread_barrierattr_init", "cdecl"):
    pthread_barrierattr_init = _libs["libc.so.6"].get("pthread_barrierattr_init", "cdecl")
    pthread_barrierattr_init.argtypes = [POINTER(pthread_barrierattr_t)]
    pthread_barrierattr_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1864
if _libs["libc.so.6"].has("pthread_barrierattr_destroy", "cdecl"):
    pthread_barrierattr_destroy = _libs["libc.so.6"].get("pthread_barrierattr_destroy", "cdecl")
    pthread_barrierattr_destroy.argtypes = [POINTER(pthread_barrierattr_t)]
    pthread_barrierattr_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1866
if _libs["libc.so.6"].has("pthread_barrierattr_getpshared", "cdecl"):
    pthread_barrierattr_getpshared = _libs["libc.so.6"].get("pthread_barrierattr_getpshared", "cdecl")
    pthread_barrierattr_getpshared.argtypes = [POINTER(pthread_barrierattr_t), POINTER(c_int)]
    pthread_barrierattr_getpshared.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1870
if _libs["libc.so.6"].has("pthread_barrierattr_setpshared", "cdecl"):
    pthread_barrierattr_setpshared = _libs["libc.so.6"].get("pthread_barrierattr_setpshared", "cdecl")
    pthread_barrierattr_setpshared.argtypes = [POINTER(pthread_barrierattr_t), c_int]
    pthread_barrierattr_setpshared.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1873
if _libs["libc.so.6"].has("pthread_key_create", "cdecl"):
    pthread_key_create = _libs["libc.so.6"].get("pthread_key_create", "cdecl")
    pthread_key_create.argtypes = [POINTER(pthread_key_t), CFUNCTYPE(UNCHECKED(None), POINTER(None))]
    pthread_key_create.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1876
if _libs["libc.so.6"].has("pthread_key_delete", "cdecl"):
    pthread_key_delete = _libs["libc.so.6"].get("pthread_key_delete", "cdecl")
    pthread_key_delete.argtypes = [pthread_key_t]
    pthread_key_delete.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1877
if _libs["libc.so.6"].has("pthread_getspecific", "cdecl"):
    pthread_getspecific = _libs["libc.so.6"].get("pthread_getspecific", "cdecl")
    pthread_getspecific.argtypes = [pthread_key_t]
    pthread_getspecific.restype = POINTER(c_ubyte)
    pthread_getspecific.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1878
if _libs["libc.so.6"].has("pthread_setspecific", "cdecl"):
    pthread_setspecific = _libs["libc.so.6"].get("pthread_setspecific", "cdecl")
    pthread_setspecific.argtypes = [pthread_key_t, POINTER(None)]
    pthread_setspecific.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1881
if _libs["libc.so.6"].has("pthread_getcpuclockid", "cdecl"):
    pthread_getcpuclockid = _libs["libc.so.6"].get("pthread_getcpuclockid", "cdecl")
    pthread_getcpuclockid.argtypes = [pthread_t, POINTER(__clockid_t)]
    pthread_getcpuclockid.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1884
if _libs["libc.so.6"].has("pthread_gettid_np", "cdecl"):
    pthread_gettid_np = _libs["libc.so.6"].get("pthread_gettid_np", "cdecl")
    pthread_gettid_np.argtypes = [pthread_t]
    pthread_gettid_np.restype = pid_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1885
for _lib in _libs.values():
    if not _lib.has("pthread_atfork", "cdecl"):
        continue
    pthread_atfork = _lib.get("pthread_atfork", "cdecl")
    pthread_atfork.argtypes = [CFUNCTYPE(UNCHECKED(None), ), CFUNCTYPE(UNCHECKED(None), ), CFUNCTYPE(UNCHECKED(None), )]
    pthread_atfork.restype = c_int
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1909
class struct_jon_gui_state(Structure):
    pass

struct_jon_gui_state.__slots__ = [
    'header',
    'compass',
    'compass_calibration',
    'colors',
    'time',
    'gps',
    'lrf',
    'media',
    'system',
    'osd',
    'targets',
    'camera_alignment',
    'meteo',
    'lens',
    'rotary',
    'power',
    'cv',
    'debug',
]
struct_jon_gui_state._fields_ = [
    ('header', jon_gui_data_header),
    ('compass', jon_gui_data_compass),
    ('compass_calibration', jon_gui_data_compass_calibration),
    ('colors', jon_gui_data_colors),
    ('time', jon_gui_data_time),
    ('gps', jon_gui_data_gps),
    ('lrf', jon_gui_data_lrf),
    ('media', jon_gui_data_media),
    ('system', jon_gui_data_system),
    ('osd', jon_gui_data_osd),
    ('targets', jon_gui_data_targets),
    ('camera_alignment', jon_gui_data_camera_alignment),
    ('meteo', jon_gui_data_meteo),
    ('lens', jon_gui_data_lens),
    ('rotary', jon_gui_data_rotary),
    ('power', jon_gui_data_power),
    ('cv', jon_gui_data_cv_t),
    ('debug', jon_gui_data_debug_t),
]

jon_gui_state = struct_jon_gui_state# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1909

jon_gui_state_to_proto_ptr = CFUNCTYPE(UNCHECKED(c_ptrdiff_t), POINTER(uint8_t), POINTER(jon_gui_state))# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1910

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1912
for _lib in _libs.values():
    if not _lib.has("jon_gui_writer_init", "cdecl"):
        continue
    jon_gui_writer_init = _lib.get("jon_gui_writer_init", "cdecl")
    jon_gui_writer_init.argtypes = []
    jon_gui_writer_init.restype = c_bool
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1913
for _lib in _libs.values():
    if not _lib.has("jon_gui_writer_destroy", "cdecl"):
        continue
    jon_gui_writer_destroy = _lib.get("jon_gui_writer_destroy", "cdecl")
    jon_gui_writer_destroy.argtypes = []
    jon_gui_writer_destroy.restype = None
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1914
for _lib in _libs.values():
    if not _lib.has("jon_gui_reader_init", "cdecl"):
        continue
    jon_gui_reader_init = _lib.get("jon_gui_reader_init", "cdecl")
    jon_gui_reader_init.argtypes = []
    jon_gui_reader_init.restype = c_bool
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1915
for _lib in _libs.values():
    if not _lib.has("jon_gui_reader_destroy", "cdecl"):
        continue
    jon_gui_reader_destroy = _lib.get("jon_gui_reader_destroy", "cdecl")
    jon_gui_reader_destroy.argtypes = []
    jon_gui_reader_destroy.restype = None
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1916
for _lib in _libs.values():
    if not _lib.has("jon_gui_writer_write", "cdecl"):
        continue
    jon_gui_writer_write = _lib.get("jon_gui_writer_write", "cdecl")
    jon_gui_writer_write.argtypes = [POINTER(jon_gui_state), jon_gui_state_to_proto_ptr]
    jon_gui_writer_write.restype = None
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1918
for _lib in _libs.values():
    if not _lib.has("jon_gui_reader_read", "cdecl"):
        continue
    jon_gui_reader_read = _lib.get("jon_gui_reader_read", "cdecl")
    jon_gui_reader_read.argtypes = [POINTER(jon_gui_state)]
    jon_gui_reader_read.restype = None
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1919
for _lib in _libs.values():
    if not _lib.has("jon_gui_data_make_default", "cdecl"):
        continue
    jon_gui_data_make_default = _lib.get("jon_gui_data_make_default", "cdecl")
    jon_gui_data_make_default.argtypes = []
    jon_gui_data_make_default.restype = jon_gui_state
    break

enum_anon_69 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1925

jon_gui_data_decr = (-1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1925

jon_gui_data_refresh = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1925

jon_gui_data_incr = 1# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1925

jon_gui_data_update_type = enum_anon_69# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1925

jon_gui_data_camera_alignment = struct_jon_gui_data_camera_alignment# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 178

jon_gui_data_colors_value = struct_jon_gui_data_colors_value# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 187

jon_gui_data_colors_menu = struct_jon_gui_data_colors_menu# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 193

jon_gui_data_colors_osd = struct_jon_gui_data_colors_osd# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 199

jon_gui_data_colors = struct_jon_gui_data_colors# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 204

jon_gui_data_component_meteo = struct_jon_gui_data_component_meteo# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 389

jon_gui_data_compass = struct_jon_gui_data_compass# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 453

jon_gui_data_compass_calibration = struct_jon_gui_data_compass_calibration# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 467

timeval = struct_timeval# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 503

timex = struct_timex# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 508

tm = struct_tm# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 537

timespec = struct_timespec# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 551

itimerspec = struct_itimerspec# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 558

sigevent = struct_sigevent# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 563

__locale_data = struct___locale_data# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 567

__locale_struct = struct___locale_struct# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 565

jon_gui_data_gps = struct_jon_gui_data_gps# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 679

jon_gui_data_header = struct_jon_gui_data_header# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 703

jon_gui_data_lens = struct_jon_gui_data_lens# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 763

jon_gui_data_lrf = struct_jon_gui_data_lrf# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 788

jon_gui_data_media = struct_jon_gui_data_media# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 794

jon_gui_data_meteo = struct_jon_gui_data_meteo# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 804

jon_gui_data_osd = struct_jon_gui_data_osd# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 830

jon_gui_data_rotary = struct_jon_gui_data_rotary# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 875

jon_gui_data_power_module_state = struct_jon_gui_data_power_module_state# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 891

jon_gui_data_power = struct_jon_gui_data_power# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 903

jon_gui_data_system = struct_jon_gui_data_system# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 971

jon_gui_data_target_spec = struct_jon_gui_data_target_spec# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1001

jon_gui_data_targets = struct_jon_gui_data_targets# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1015

jon_gui_data_time = struct_jon_gui_data_time# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1039

jon_gui_color_rgba8888 = union_jon_gui_color_rgba8888# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1077

jon_gui_tracking_point = union_jon_gui_tracking_point# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1087

jon_gui_tracking_quad = struct_jon_gui_tracking_quad# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1092

jon_gui_data_cv = struct_jon_gui_data_cv# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1105

__pthread_internal_list = struct___pthread_internal_list# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1249

__pthread_internal_slist = struct___pthread_internal_slist# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1254

__pthread_mutex_s = struct___pthread_mutex_s# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1258

__pthread_rwlock_arch_t = struct___pthread_rwlock_arch_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1269

__pthread_cond_s = struct___pthread_cond_s# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1284

pthread_attr_t = union_pthread_attr_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1314

sched_attr = struct_sched_attr# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1412

sched_param = struct_sched_param# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1424

__jmp_buf_tag = struct___jmp_buf_tag# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1463

_pthread_cleanup_buffer = struct__pthread_cleanup_buffer# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1524

__cancel_jmp_buf_tag = struct___cancel_jmp_buf_tag# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1661

__pthread_cleanup_frame = struct___pthread_cleanup_frame# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1671

jon_gui_state = struct_jon_gui_state# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_jon.h: 1909

# No inserted files

# No prefix-stripping

