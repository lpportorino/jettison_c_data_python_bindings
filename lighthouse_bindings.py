r"""Wrapper for preprocessed_lighthouse.h

Generated with:
/usr/bin/ctypesgen /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h -o /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/lighthouse_bindings.py -l libc.so.6 --strip-prefix=CAN_ --strip-prefix=STATE_

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

__s8 = c_char# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1

__u8 = c_ubyte# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2

__s16 = c_short# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 3

__u16 = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 4

__s32 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 5

__u32 = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 6

__s64 = c_longlong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 7

__u64 = c_ulonglong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 8

__int64_t = c_longlong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 9

__uint64_t = c_ulonglong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 10

__time_t = c_int64# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 11

time_t = __time_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 12

__u_char = c_ubyte# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 13

__u_short = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 14

__u_int = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 15

__u_long = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 16

__int8_t = c_char# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 17

__uint8_t = c_ubyte# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 18

__int16_t = c_short# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 19

__uint16_t = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 20

__int32_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 21

__uint32_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 22

__int64_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 23

__uint64_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 24

__int_least8_t = c_int8# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 25

__uint_least8_t = __uint8_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 26

__int_least16_t = c_int16# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 27

__uint_least16_t = __uint16_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 28

__int_least32_t = c_int32# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 29

__uint_least32_t = __uint32_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 30

__int_least64_t = c_int64# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 31

__uint_least64_t = __uint64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 32

__quad_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 33

__u_quad_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 34

__intmax_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 35

__uintmax_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 36

__dev_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 37

__uid_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 38

__gid_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 39

__ino_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 40

__ino64_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 41

__mode_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 42

__nlink_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 43

__off_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 44

__off64_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 45

__pid_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 46

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 47
class struct_anon_1(Structure):
    pass

struct_anon_1.__slots__ = [
    '__val',
]
struct_anon_1._fields_ = [
    ('__val', c_int * int(2)),
]

__fsid_t = struct_anon_1# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 47

__clock_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 48

__rlim_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 49

__rlim64_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 50

__id_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 51

__time_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 52

__useconds_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 53

__suseconds_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 54

__suseconds64_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 55

__daddr_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 56

__key_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 57

__clockid_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 58

__timer_t = POINTER(None)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 59

__blksize_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 60

__blkcnt_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 61

__blkcnt64_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 62

__fsblkcnt_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 63

__fsblkcnt64_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 64

__fsfilcnt_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 65

__fsfilcnt64_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 66

__fsword_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 67

__ssize_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 68

__syscall_slong_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 69

__syscall_ulong_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 70

__loff_t = __off64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 71

__caddr_t = String# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 72

__intptr_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 73

__socklen_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 74

__sig_atomic_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 75

int8_t = c_int8# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 76

int16_t = c_int16# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 77

int32_t = c_int32# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 78

int64_t = c_int64# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 79

uint8_t = __uint8_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 80

uint16_t = __uint16_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 81

uint32_t = __uint32_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 82

uint64_t = __uint64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 83

int_least8_t = __int_least8_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 84

int_least16_t = __int_least16_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 85

int_least32_t = __int_least32_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 86

int_least64_t = __int_least64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 87

uint_least8_t = __uint_least8_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 88

uint_least16_t = __uint_least16_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 89

uint_least32_t = __uint_least32_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 90

uint_least64_t = __uint_least64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 91

int_fast8_t = c_char# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 92

int_fast16_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 93

int_fast32_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 94

int_fast64_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 95

uint_fast8_t = c_ubyte# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 96

uint_fast16_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 97

uint_fast32_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 98

uint_fast64_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 99

intptr_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 100

uintptr_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 101

intmax_t = __intmax_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 102

uintmax_t = __uintmax_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 103

size_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 104

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 105
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

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 110
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

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 136
if _libs["libc.so.6"].has("clock_adjtime", "cdecl"):
    clock_adjtime = _libs["libc.so.6"].get("clock_adjtime", "cdecl")
    clock_adjtime.argtypes = [__clockid_t, POINTER(struct_timex)]
    clock_adjtime.restype = c_int

clock_t = __clock_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 137

time_t = __time_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 138

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 139
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

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 153
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

clockid_t = __clockid_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 158

timer_t = __timer_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 159

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 160
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

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 165
class struct_sigevent(Structure):
    pass

pid_t = __pid_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 166

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 169
class struct___locale_data(Structure):
    pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 167
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

__locale_t = POINTER(struct___locale_struct)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 175

locale_t = __locale_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 177

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 178
if _libs["libc.so.6"].has("clock", "cdecl"):
    clock = _libs["libc.so.6"].get("clock", "cdecl")
    clock.argtypes = []
    clock.restype = clock_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 179
if _libs["libc.so.6"].has("time", "cdecl"):
    time = _libs["libc.so.6"].get("time", "cdecl")
    time.argtypes = [POINTER(time_t)]
    time.restype = time_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 180
if _libs["libc.so.6"].has("difftime", "cdecl"):
    difftime = _libs["libc.so.6"].get("difftime", "cdecl")
    difftime.argtypes = [time_t, time_t]
    difftime.restype = c_double

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 181
if _libs["libc.so.6"].has("mktime", "cdecl"):
    mktime = _libs["libc.so.6"].get("mktime", "cdecl")
    mktime.argtypes = [POINTER(struct_tm)]
    mktime.restype = time_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 182
if _libs["libc.so.6"].has("strftime", "cdecl"):
    strftime = _libs["libc.so.6"].get("strftime", "cdecl")
    strftime.argtypes = [String, c_size_t, String, POINTER(struct_tm)]
    strftime.restype = c_size_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 186
if _libs["libc.so.6"].has("strptime", "cdecl"):
    strptime = _libs["libc.so.6"].get("strptime", "cdecl")
    strptime.argtypes = [String, String, POINTER(struct_tm)]
    if sizeof(c_int) == sizeof(c_void_p):
        strptime.restype = ReturnString
    else:
        strptime.restype = String
        strptime.errcheck = ReturnString

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 189
if _libs["libc.so.6"].has("strftime_l", "cdecl"):
    strftime_l = _libs["libc.so.6"].get("strftime_l", "cdecl")
    strftime_l.argtypes = [String, c_size_t, String, POINTER(struct_tm), locale_t]
    strftime_l.restype = c_size_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 193
if _libs["libc.so.6"].has("strptime_l", "cdecl"):
    strptime_l = _libs["libc.so.6"].get("strptime_l", "cdecl")
    strptime_l.argtypes = [String, String, POINTER(struct_tm), locale_t]
    if sizeof(c_int) == sizeof(c_void_p):
        strptime_l.restype = ReturnString
    else:
        strptime_l.restype = String
        strptime_l.errcheck = ReturnString

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 196
if _libs["libc.so.6"].has("gmtime", "cdecl"):
    gmtime = _libs["libc.so.6"].get("gmtime", "cdecl")
    gmtime.argtypes = [POINTER(time_t)]
    gmtime.restype = POINTER(struct_tm)

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 197
if _libs["libc.so.6"].has("localtime", "cdecl"):
    localtime = _libs["libc.so.6"].get("localtime", "cdecl")
    localtime.argtypes = [POINTER(time_t)]
    localtime.restype = POINTER(struct_tm)

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 198
if _libs["libc.so.6"].has("gmtime_r", "cdecl"):
    gmtime_r = _libs["libc.so.6"].get("gmtime_r", "cdecl")
    gmtime_r.argtypes = [POINTER(time_t), POINTER(struct_tm)]
    gmtime_r.restype = POINTER(struct_tm)

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 200
if _libs["libc.so.6"].has("localtime_r", "cdecl"):
    localtime_r = _libs["libc.so.6"].get("localtime_r", "cdecl")
    localtime_r.argtypes = [POINTER(time_t), POINTER(struct_tm)]
    localtime_r.restype = POINTER(struct_tm)

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 202
if _libs["libc.so.6"].has("asctime", "cdecl"):
    asctime = _libs["libc.so.6"].get("asctime", "cdecl")
    asctime.argtypes = [POINTER(struct_tm)]
    if sizeof(c_int) == sizeof(c_void_p):
        asctime.restype = ReturnString
    else:
        asctime.restype = String
        asctime.errcheck = ReturnString

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 203
if _libs["libc.so.6"].has("ctime", "cdecl"):
    ctime = _libs["libc.so.6"].get("ctime", "cdecl")
    ctime.argtypes = [POINTER(time_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        ctime.restype = ReturnString
    else:
        ctime.restype = String
        ctime.errcheck = ReturnString

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 204
if _libs["libc.so.6"].has("asctime_r", "cdecl"):
    asctime_r = _libs["libc.so.6"].get("asctime_r", "cdecl")
    asctime_r.argtypes = [POINTER(struct_tm), String]
    if sizeof(c_int) == sizeof(c_void_p):
        asctime_r.restype = ReturnString
    else:
        asctime_r.restype = String
        asctime_r.errcheck = ReturnString

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 206
if _libs["libc.so.6"].has("ctime_r", "cdecl"):
    ctime_r = _libs["libc.so.6"].get("ctime_r", "cdecl")
    ctime_r.argtypes = [POINTER(time_t), String]
    if sizeof(c_int) == sizeof(c_void_p):
        ctime_r.restype = ReturnString
    else:
        ctime_r.restype = String
        ctime_r.errcheck = ReturnString

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 208
try:
    __tzname = (POINTER(c_char) * int(2)).in_dll(_libs["libc.so.6"], "__tzname")
except:
    pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 209
try:
    __daylight = (c_int).in_dll(_libs["libc.so.6"], "__daylight")
except:
    pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 210
try:
    __timezone = (c_long).in_dll(_libs["libc.so.6"], "__timezone")
except:
    pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 211
try:
    tzname = (POINTER(c_char) * int(2)).in_dll(_libs["libc.so.6"], "tzname")
except:
    pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 212
if _libs["libc.so.6"].has("tzset", "cdecl"):
    tzset = _libs["libc.so.6"].get("tzset", "cdecl")
    tzset.argtypes = []
    tzset.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 213
try:
    daylight = (c_int).in_dll(_libs["libc.so.6"], "daylight")
except:
    pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 214
try:
    timezone = (c_long).in_dll(_libs["libc.so.6"], "timezone")
except:
    pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 215
if _libs["libc.so.6"].has("timegm", "cdecl"):
    timegm = _libs["libc.so.6"].get("timegm", "cdecl")
    timegm.argtypes = [POINTER(struct_tm)]
    timegm.restype = time_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 216
if _libs["libc.so.6"].has("timelocal", "cdecl"):
    timelocal = _libs["libc.so.6"].get("timelocal", "cdecl")
    timelocal.argtypes = [POINTER(struct_tm)]
    timelocal.restype = time_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 217
if _libs["libc.so.6"].has("dysize", "cdecl"):
    dysize = _libs["libc.so.6"].get("dysize", "cdecl")
    dysize.argtypes = [c_int]
    dysize.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 218
if _libs["libc.so.6"].has("nanosleep", "cdecl"):
    nanosleep = _libs["libc.so.6"].get("nanosleep", "cdecl")
    nanosleep.argtypes = [POINTER(struct_timespec), POINTER(struct_timespec)]
    nanosleep.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 220
if _libs["libc.so.6"].has("clock_getres", "cdecl"):
    clock_getres = _libs["libc.so.6"].get("clock_getres", "cdecl")
    clock_getres.argtypes = [clockid_t, POINTER(struct_timespec)]
    clock_getres.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 221
if _libs["libc.so.6"].has("clock_gettime", "cdecl"):
    clock_gettime = _libs["libc.so.6"].get("clock_gettime", "cdecl")
    clock_gettime.argtypes = [clockid_t, POINTER(struct_timespec)]
    clock_gettime.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 223
if _libs["libc.so.6"].has("clock_settime", "cdecl"):
    clock_settime = _libs["libc.so.6"].get("clock_settime", "cdecl")
    clock_settime.argtypes = [clockid_t, POINTER(struct_timespec)]
    clock_settime.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 225
if _libs["libc.so.6"].has("clock_nanosleep", "cdecl"):
    clock_nanosleep = _libs["libc.so.6"].get("clock_nanosleep", "cdecl")
    clock_nanosleep.argtypes = [clockid_t, c_int, POINTER(struct_timespec), POINTER(struct_timespec)]
    clock_nanosleep.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 228
if _libs["libc.so.6"].has("clock_getcpuclockid", "cdecl"):
    clock_getcpuclockid = _libs["libc.so.6"].get("clock_getcpuclockid", "cdecl")
    clock_getcpuclockid.argtypes = [pid_t, POINTER(clockid_t)]
    clock_getcpuclockid.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 229
if _libs["libc.so.6"].has("timer_create", "cdecl"):
    timer_create = _libs["libc.so.6"].get("timer_create", "cdecl")
    timer_create.argtypes = [clockid_t, POINTER(struct_sigevent), POINTER(timer_t)]
    timer_create.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 232
if _libs["libc.so.6"].has("timer_delete", "cdecl"):
    timer_delete = _libs["libc.so.6"].get("timer_delete", "cdecl")
    timer_delete.argtypes = [timer_t]
    timer_delete.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 233
if _libs["libc.so.6"].has("timer_settime", "cdecl"):
    timer_settime = _libs["libc.so.6"].get("timer_settime", "cdecl")
    timer_settime.argtypes = [timer_t, c_int, POINTER(struct_itimerspec), POINTER(struct_itimerspec)]
    timer_settime.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 236
if _libs["libc.so.6"].has("timer_gettime", "cdecl"):
    timer_gettime = _libs["libc.so.6"].get("timer_gettime", "cdecl")
    timer_gettime.argtypes = [timer_t, POINTER(struct_itimerspec)]
    timer_gettime.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 238
if _libs["libc.so.6"].has("timer_getoverrun", "cdecl"):
    timer_getoverrun = _libs["libc.so.6"].get("timer_getoverrun", "cdecl")
    timer_getoverrun.argtypes = [timer_t]
    timer_getoverrun.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 239
if _libs["libc.so.6"].has("timespec_get", "cdecl"):
    timespec_get = _libs["libc.so.6"].get("timespec_get", "cdecl")
    timespec_get.argtypes = [POINTER(struct_timespec), c_int]
    timespec_get.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 241
if _libs["libc.so.6"].has("timespec_getres", "cdecl"):
    timespec_getres = _libs["libc.so.6"].get("timespec_getres", "cdecl")
    timespec_getres.argtypes = [POINTER(struct_timespec), c_int]
    timespec_getres.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 243
try:
    getdate_err = (c_int).in_dll(_libs["libc.so.6"], "getdate_err")
except:
    pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 244
if _libs["libc.so.6"].has("getdate", "cdecl"):
    getdate = _libs["libc.so.6"].get("getdate", "cdecl")
    getdate.argtypes = [String]
    getdate.restype = POINTER(struct_tm)

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 245
if _libs["libc.so.6"].has("getdate_r", "cdecl"):
    getdate_r = _libs["libc.so.6"].get("getdate_r", "cdecl")
    getdate_r.argtypes = [String, POINTER(struct_tm)]
    getdate_r.restype = c_int

__s8 = c_char# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 247

__u8 = c_ubyte# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 248

__s16 = c_short# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 249

__u16 = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 250

__s32 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 251

__u32 = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 252

__s64 = c_longlong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 253

__u64 = c_ulonglong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 254

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 257
class struct_anon_2(Structure):
    pass

struct_anon_2.__slots__ = [
    'fds_bits',
]
struct_anon_2._fields_ = [
    ('fds_bits', c_ulong * int((1024 / (8 * sizeof(c_long))))),
]

__kernel_fd_set = struct_anon_2# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 257

__kernel_sighandler_t = CFUNCTYPE(UNCHECKED(None), c_int)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 258

__kernel_key_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 259

__kernel_mqd_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 260

__kernel_old_uid_t = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 261

__kernel_old_gid_t = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 262

__kernel_old_dev_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 263

__kernel_long_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 264

__kernel_ulong_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 265

__kernel_ino_t = __kernel_ulong_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 266

__kernel_mode_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 267

__kernel_pid_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 268

__kernel_ipc_pid_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 269

__kernel_uid_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 270

__kernel_gid_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 271

__kernel_suseconds_t = __kernel_long_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 272

__kernel_daddr_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 273

__kernel_uid32_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 274

__kernel_gid32_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 275

__kernel_size_t = __kernel_ulong_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 276

__kernel_ssize_t = __kernel_long_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 277

__kernel_ptrdiff_t = __kernel_long_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 278

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 281
class struct_anon_3(Structure):
    pass

struct_anon_3.__slots__ = [
    'val',
]
struct_anon_3._fields_ = [
    ('val', c_int * int(2)),
]

__kernel_fsid_t = struct_anon_3# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 281

__kernel_off_t = __kernel_long_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 282

__kernel_loff_t = c_longlong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 283

__kernel_old_time_t = __kernel_long_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 284

__kernel_time_t = __kernel_long_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 285

__kernel_time64_t = c_longlong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 286

__kernel_clock_t = __kernel_long_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 287

__kernel_timer_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 288

__kernel_clockid_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 289

__kernel_caddr_t = String# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 290

__kernel_uid16_t = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 291

__kernel_gid16_t = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 292

__le16 = __u16# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 295

__be16 = __u16# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 296

__le32 = __u32# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 297

__be32 = __u32# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 298

__le64 = __u64# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 299

__be64 = __u64# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 300

__sum16 = __u16# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 301

__wsum = __u32# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 302

__poll_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 303

__kernel_sa_family_t = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 304

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 307
class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'ss_family',
    '__data',
]
struct_anon_4._fields_ = [
    ('ss_family', __kernel_sa_family_t),
    ('__data', c_char * int((128 - sizeof(c_ushort)))),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 306
class union_anon_5(Union):
    pass

union_anon_5.__slots__ = [
    'unnamed_1',
    '__align',
]
union_anon_5._anonymous_ = [
    'unnamed_1',
]
union_anon_5._fields_ = [
    ('unnamed_1', struct_anon_4),
    ('__align', POINTER(None)),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 305
class struct___kernel_sockaddr_storage(Structure):
    pass

struct___kernel_sockaddr_storage.__slots__ = [
    'unnamed_1',
]
struct___kernel_sockaddr_storage._anonymous_ = [
    'unnamed_1',
]
struct___kernel_sockaddr_storage._fields_ = [
    ('unnamed_1', union_anon_5),
]

canid_t = __u32# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 314

can_err_mask_t = __u32# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 315

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 318
class union_anon_6(Union):
    pass

union_anon_6.__slots__ = [
    'len',
    'can_dlc',
]
union_anon_6._fields_ = [
    ('len', __u8),
    ('can_dlc', __u8),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 316
class struct_can_frame(Structure):
    pass

struct_can_frame.__slots__ = [
    'can_id',
    'unnamed_1',
    '__pad',
    '__res0',
    'len8_dlc',
    'data',
]
struct_can_frame._anonymous_ = [
    'unnamed_1',
]
struct_can_frame._fields_ = [
    ('can_id', canid_t),
    ('unnamed_1', union_anon_6),
    ('__pad', __u8),
    ('__res0', __u8),
    ('len8_dlc', __u8),
    ('data', __u8 * int(8)),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 327
class struct_canfd_frame(Structure):
    pass

struct_canfd_frame.__slots__ = [
    'can_id',
    'len',
    'flags',
    '__res0',
    '__res1',
    'data',
]
struct_canfd_frame._fields_ = [
    ('can_id', canid_t),
    ('len', __u8),
    ('flags', __u8),
    ('__res0', __u8),
    ('__res1', __u8),
    ('data', __u8 * int(64)),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 335
class struct_canxl_frame(Structure):
    pass

struct_canxl_frame.__slots__ = [
    'prio',
    'flags',
    'sdt',
    'len',
    'af',
    'data',
]
struct_canxl_frame._fields_ = [
    ('prio', canid_t),
    ('flags', __u8),
    ('sdt', __u8),
    ('len', __u16),
    ('af', __u32),
    ('data', __u8 * int(2048)),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 347
class struct_anon_7(Structure):
    pass

struct_anon_7.__slots__ = [
    'rx_id',
    'tx_id',
]
struct_anon_7._fields_ = [
    ('rx_id', canid_t),
    ('tx_id', canid_t),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 348
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    'name',
    'pgn',
    'addr',
]
struct_anon_8._fields_ = [
    ('name', __u64),
    ('pgn', __u32),
    ('addr', __u8),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 346
class union_anon_9(Union):
    pass

union_anon_9.__slots__ = [
    'tp',
    'j1939',
]
union_anon_9._fields_ = [
    ('tp', struct_anon_7),
    ('j1939', struct_anon_8),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 343
class struct_sockaddr_can(Structure):
    pass

struct_sockaddr_can.__slots__ = [
    'can_family',
    'can_ifindex',
    'can_addr',
]
struct_sockaddr_can._fields_ = [
    ('can_family', __kernel_sa_family_t),
    ('can_ifindex', c_int),
    ('can_addr', union_anon_9),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 355
class struct_can_filter(Structure):
    pass

struct_can_filter.__slots__ = [
    'can_id',
    'can_mask',
]
struct_can_filter._fields_ = [
    ('can_id', canid_t),
    ('can_mask', canid_t),
]

ptrdiff_t = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 359

wchar_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 360

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 366
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    '__clang_max_align_nonce1',
    '__clang_max_align_nonce2',
]
struct_anon_10._fields_ = [
    ('__clang_max_align_nonce1', c_longlong),
    ('__clang_max_align_nonce2', c_longdouble),
]

max_align_t = struct_anon_10# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 366

enum_memory_order = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 374

memory_order_relaxed = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 374

memory_order_consume = 1# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 374

memory_order_acquire = 2# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 374

memory_order_release = 3# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 374

memory_order_acq_rel = 4# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 374

memory_order_seq_cst = 5# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 374

memory_order = enum_memory_order# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 374

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 375
for _lib in _libs.values():
    if not _lib.has("atomic_thread_fence", "cdecl"):
        continue
    atomic_thread_fence = _lib.get("atomic_thread_fence", "cdecl")
    atomic_thread_fence.argtypes = [memory_order]
    atomic_thread_fence.restype = None
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 376
for _lib in _libs.values():
    if not _lib.has("atomic_signal_fence", "cdecl"):
        continue
    atomic_signal_fence = _lib.get("atomic_signal_fence", "cdecl")
    atomic_signal_fence.argtypes = [memory_order]
    atomic_signal_fence.restype = None
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 432
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

jon_gui_data_camera_alignment = struct_jon_gui_data_camera_alignment# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 432

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 434
for _lib in _libs.values():
    try:
        jon_gui_default_state_camera_calibration = (jon_gui_data_camera_alignment).in_dll(_lib, "jon_gui_default_state_camera_calibration")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 441
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

jon_gui_data_colors_value = struct_jon_gui_data_colors_value# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 441

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 447
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

jon_gui_data_colors_menu = struct_jon_gui_data_colors_menu# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 447

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 453
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

jon_gui_data_colors_osd = struct_jon_gui_data_colors_osd# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 453

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 458
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

jon_gui_data_colors = struct_jon_gui_data_colors# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 458

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 459
for _lib in _libs.values():
    try:
        jon_gui_default_state_colors = (jon_gui_data_colors).in_dll(_lib, "jon_gui_default_state_colors")
        break
    except:
        pass

enum_jon_gui_data_video_channel = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 465

JON_GUI_DATA_VIDEO_CNANNEL_DAY = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 465

JON_GUI_DATA_VIDEO_CNANNEL_HEAT = (JON_GUI_DATA_VIDEO_CNANNEL_DAY + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 465

_JON_GUI_DATA_VIDEO_CNANNEL_AFTER_LAST_ = (JON_GUI_DATA_VIDEO_CNANNEL_HEAT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 465

jon_gui_data_video_channel = enum_jon_gui_data_video_channel# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 465

enum_jon_gui_data_video_channel_heat_filters = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 473

JON_GUI_DATA_VIDEO_CNANNEL_HEAT_FILTER_HOT_WHITE = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 473

JON_GUI_DATA_VIDEO_CNANNEL_HEAT_FILTER_HOT_BLACK = (JON_GUI_DATA_VIDEO_CNANNEL_HEAT_FILTER_HOT_WHITE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 473

JON_GUI_DATA_VIDEO_CNANNEL_HEAT_FILTER_SEPIA = (JON_GUI_DATA_VIDEO_CNANNEL_HEAT_FILTER_HOT_BLACK + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 473

JON_GUI_DATA_VIDEO_CNANNEL_HEAT_FILTER_SEPIA_INVERTED = (JON_GUI_DATA_VIDEO_CNANNEL_HEAT_FILTER_SEPIA + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 473

_JON_SHARED_DATA_VIDEO_CNANNEL_HEAT_FILTER_AFTER_LAST_ = (JON_GUI_DATA_VIDEO_CNANNEL_HEAT_FILTER_SEPIA_INVERTED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 473

jon_gui_data_video_channel_heat_filters = enum_jon_gui_data_video_channel_heat_filters# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 473

enum_jon_gui_data_video_channel_day_filters = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 483

JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_0 = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 483

JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_1 = (JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_0 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 483

JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_2 = (JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_1 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 483

JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_3 = (JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_2 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 483

JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_4 = (JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_3 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 483

JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_5 = (JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_4 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 483

_JON_SHARED_DATA_VIDEO_CNANNEL_DAY_FILTER_AFTER_LAST_ = (JON_GUI_DATA_VIDEO_CNANNEL_DAY_FILTER_5 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 483

jon_gui_data_video_channel_day_filters = enum_jon_gui_data_video_channel_day_filters# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 483

enum_jon_gui_data_gps_units = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 490

JON_GUI_DATA_GPS_UNITS_DECIMAL_DEGREES = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 490

JON_GUI_DATA_GPS_UNITS_DEGREES_MINUTES_SECONDS = (JON_GUI_DATA_GPS_UNITS_DECIMAL_DEGREES + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 490

JON_GUI_DATA_GPS_UNITS_DEGREES_DECIMAL_MINUTES = (JON_GUI_DATA_GPS_UNITS_DEGREES_MINUTES_SECONDS + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 490

_JON_GUI_DATA_GPS_UNITS_AFTER_LAST_ = (JON_GUI_DATA_GPS_UNITS_DEGREES_DECIMAL_MINUTES + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 490

jon_gui_data_gps_units = enum_jon_gui_data_gps_units# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 490

enum_jon_gui_data_gps_fix_type = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 498

JON_GUI_DATA_GPS_FIX_TYPE_NONE = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 498

JON_GUI_DATA_GPS_FIX_TYPE_1D = (JON_GUI_DATA_GPS_FIX_TYPE_NONE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 498

JON_GUI_DATA_GPS_FIX_TYPE_2D = (JON_GUI_DATA_GPS_FIX_TYPE_1D + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 498

JON_GUI_DATA_GPS_FIX_TYPE_3D = (JON_GUI_DATA_GPS_FIX_TYPE_2D + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 498

JON_GUI_DATA_GPS_FIX_TYPE_MANUAL = (JON_GUI_DATA_GPS_FIX_TYPE_3D + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 498

jon_gui_data_gps_fix_type = enum_jon_gui_data_gps_fix_type# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 498

enum_jon_gui_data_compass_units = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 506

JON_GUI_DATA_COMPASS_UNITS_DEGREES = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 506

JON_GUI_DATA_COMPASS_UNITS_MILS = (JON_GUI_DATA_COMPASS_UNITS_DEGREES + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 506

JON_GUI_DATA_COMPASS_UNITS_GRAD = (JON_GUI_DATA_COMPASS_UNITS_MILS + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 506

JON_GUI_DATA_COMPASS_UNITS_MRAD = (JON_GUI_DATA_COMPASS_UNITS_GRAD + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 506

_JON_GUI_DATA_COMPASS_UNITS_AFTER_LAST_ = (JON_GUI_DATA_COMPASS_UNITS_MRAD + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 506

jon_gui_data_compass_units = enum_jon_gui_data_compass_units# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 506

enum_jon_gui_data_accumulator_state_idx = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 522

JON_GUI_DATA_ACCUMULATOR_STATE_UNKNOWN = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 522

JON_GUI_DATA_ACCUMULATOR_STATE_EMPTY = (JON_GUI_DATA_ACCUMULATOR_STATE_UNKNOWN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 522

_JON_SHARED_DATA_ACCUMULATOR_STATE_BEFORE_OK_ = (JON_GUI_DATA_ACCUMULATOR_STATE_EMPTY + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 522

JON_GUI_DATA_ACCUMULATOR_STATE_1 = (_JON_SHARED_DATA_ACCUMULATOR_STATE_BEFORE_OK_ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 522

JON_GUI_DATA_ACCUMULATOR_STATE_2 = (JON_GUI_DATA_ACCUMULATOR_STATE_1 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 522

JON_GUI_DATA_ACCUMULATOR_STATE_3 = (JON_GUI_DATA_ACCUMULATOR_STATE_2 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 522

JON_GUI_DATA_ACCUMULATOR_STATE_4 = (JON_GUI_DATA_ACCUMULATOR_STATE_3 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 522

JON_GUI_DATA_ACCUMULATOR_STATE_5 = (JON_GUI_DATA_ACCUMULATOR_STATE_4 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 522

JON_GUI_DATA_ACCUMULATOR_STATE_6 = (JON_GUI_DATA_ACCUMULATOR_STATE_5 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 522

JON_GUI_DATA_ACCUMULATOR_STATE_FULL = (JON_GUI_DATA_ACCUMULATOR_STATE_6 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 522

JON_GUI_DATA_ACCUMULATOR_STATE_CHARGING = (JON_GUI_DATA_ACCUMULATOR_STATE_FULL + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 522

_JON_SHARED_DATA_ACCUMULATOR_STATE_AFTER_OK_ = (JON_GUI_DATA_ACCUMULATOR_STATE_CHARGING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 522

_JON_SHARED_DATA_ACCUMULATOR_STATE_AFTER_LAST_ = (_JON_SHARED_DATA_ACCUMULATOR_STATE_AFTER_OK_ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 522

jon_gui_data_accumulator_state_idx = enum_jon_gui_data_accumulator_state_idx# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 522

enum_jon_gui_data_sd_card_state_idx = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 529

JON_GUI_DATA_SD_CARD_STATE_UNPLUGEED = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 529

JON_GUI_DATA_SD_CARD_STATE_NORMAL = (JON_GUI_DATA_SD_CARD_STATE_UNPLUGEED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 529

JON_GUI_DATA_SD_CARD_STATE_FULL = (JON_GUI_DATA_SD_CARD_STATE_NORMAL + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 529

_JON_GUI_DATA_SD_CARD_STATE_AFTER_LAST_ = (JON_GUI_DATA_SD_CARD_STATE_FULL + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 529

jon_gui_data_sd_card_state_idx = enum_jon_gui_data_sd_card_state_idx# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 529

enum_jon_gui_data_device_status = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 538

JON_SHARED_DATA_DEVICE_STATUS_STOPED = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 538

JON_SHARED_DATA_DEVICE_STATUS_STARTED = (JON_SHARED_DATA_DEVICE_STATUS_STOPED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 538

JON_SHARED_DATA_DEVICE_STATUS_STARTING = (JON_SHARED_DATA_DEVICE_STATUS_STARTED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 538

JON_SHARED_DATA_DEVICE_STATUS_STOPING = (JON_SHARED_DATA_DEVICE_STATUS_STARTING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 538

JON_SHARED_DATA_DEVICE_STATUS_ERROE = (JON_SHARED_DATA_DEVICE_STATUS_STOPING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 538

_JON_SHARED_DATA_DEVICE_STATUS_AFTER_LAST_ = (JON_SHARED_DATA_DEVICE_STATUS_ERROE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 538

jon_gui_data_device_status = enum_jon_gui_data_device_status# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 538

enum_jon_gui_screen_ids = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_EMPTY = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_OSD = (JON_GUI_SCREEN_EMPTY + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_OSD_LRF_RESULT = (JON_GUI_SCREEN_OSD + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_OSD_LRF_ARMING = (JON_GUI_SCREEN_OSD_LRF_RESULT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_OSD_LRF_MEASURING = (JON_GUI_SCREEN_OSD_LRF_ARMING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_OSD_LRF_RESULT_SIMPLIFIED = (JON_GUI_SCREEN_OSD_LRF_MEASURING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

_JON_GUI_SCREEN_BEFORE_MENU_SCREENS_ = (JON_GUI_SCREEN_OSD_LRF_RESULT_SIMPLIFIED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_MAIN_MENU = (_JON_GUI_SCREEN_BEFORE_MENU_SCREENS_ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_FACTORY_MAIN = (JON_GUI_SCREEN_MAIN_MENU + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_FACTORY_METEO = (JON_GUI_SCREEN_FACTORY_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_FACTORY_INFO = (JON_GUI_SCREEN_FACTORY_METEO + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_DISPLAY_MAIN = (JON_GUI_SCREEN_FACTORY_INFO + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_METEO_MAIN = (JON_GUI_SCREEN_DISPLAY_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_TIME_MAIN = (JON_GUI_SCREEN_METEO_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_TIME_MANUAL = (JON_GUI_SCREEN_TIME_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COLOR_MAIN = (JON_GUI_SCREEN_TIME_MANUAL + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COLOR_MENU_BG = (JON_GUI_SCREEN_COLOR_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COLOR_MENU_TEXT = (JON_GUI_SCREEN_COLOR_MENU_BG + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COLOR_MENU_FOCUSED = (JON_GUI_SCREEN_COLOR_MENU_TEXT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COLOR_OSD_COLOR_ACCENT = (JON_GUI_SCREEN_COLOR_MENU_FOCUSED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COLOR_OSD_COLOR_MAIN = (JON_GUI_SCREEN_COLOR_OSD_COLOR_ACCENT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_SYSTEM_MAIN = (JON_GUI_SCREEN_COLOR_OSD_COLOR_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_SYSTEM_INFO = (JON_GUI_SCREEN_SYSTEM_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_SYSTEM_LOC = (JON_GUI_SCREEN_SYSTEM_INFO + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_SYSTEM_VISUAL_SENSORS = (JON_GUI_SCREEN_SYSTEM_LOC + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COMPASS_MAIN = (JON_GUI_SCREEN_SYSTEM_VISUAL_SENSORS + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COMPASS_CALIBRATION_MAIN = (JON_GUI_SCREEN_COMPASS_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COMPASS_CALIBRATION_DONE = (JON_GUI_SCREEN_COMPASS_CALIBRATION_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_GPS_MAIN = (JON_GUI_SCREEN_COMPASS_CALIBRATION_DONE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_GPS_MANUAL = (JON_GUI_SCREEN_GPS_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_LRF_CALIBRATION_CAMERA_DAY = (JON_GUI_SCREEN_GPS_MANUAL + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_LRF_CALIBRATION_CAMERA_HEAT = (JON_GUI_SCREEN_LRF_CALIBRATION_CAMERA_DAY + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_CROSSHAIR = (JON_GUI_SCREEN_LRF_CALIBRATION_CAMERA_HEAT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_OSD_MAIN = (JON_GUI_SCREEN_CROSSHAIR + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_TARGET_MAIN = (JON_GUI_SCREEN_OSD_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_TARGET_EMPTY = (JON_GUI_SCREEN_TARGET_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_TARGET_ACTION = (JON_GUI_SCREEN_TARGET_EMPTY + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_TARGET_DELETE_CONFIRMATION = (JON_GUI_SCREEN_TARGET_ACTION + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_MEDIA_MAIN = (JON_GUI_SCREEN_TARGET_DELETE_CONFIRMATION + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_MEDIA_VIDEO = (JON_GUI_SCREEN_MEDIA_MAIN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_MEDIA_SD_ERASE_CONFIRMATION = (JON_GUI_SCREEN_MEDIA_VIDEO + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_MEDIA_SD_ERASE_DONE = (JON_GUI_SCREEN_MEDIA_SD_ERASE_CONFIRMATION + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_CAMERA_DAY_ZOOM_CALIBRATE = (JON_GUI_SCREEN_MEDIA_SD_ERASE_DONE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_CAMERA_HEAT_ZOOM_CALIBRATE = (JON_GUI_SCREEN_CAMERA_DAY_ZOOM_CALIBRATE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

_JON_GUI_SCREEN_AFTER_MENU_SCREENS_ = (JON_GUI_SCREEN_CAMERA_HEAT_ZOOM_CALIBRATE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

_JON_GUI_SCREEN_BEFORE_COMPAS_CALIB_SCREENS_ = (_JON_GUI_SCREEN_AFTER_MENU_SCREENS_ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COMPASS_CALIBRATION_AUTO = (_JON_GUI_SCREEN_BEFORE_COMPAS_CALIB_SCREENS_ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_SHORT = (JON_GUI_SCREEN_COMPASS_CALIBRATION_AUTO + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_LONG = (JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_SHORT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

_JON_GUI_SCREEN_AFTER_COMPAS_CALIB_SCREENS_ = (JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_LONG + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

_JON_GUI_SCREEN_BEFORE_WAIT_SCREENS_ = (_JON_GUI_SCREEN_AFTER_COMPAS_CALIB_SCREENS_ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COMPASS_CALIBRATION_AUTO_INIT = (_JON_GUI_SCREEN_BEFORE_WAIT_SCREENS_ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_SHORT_INIT = (JON_GUI_SCREEN_COMPASS_CALIBRATION_AUTO_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_SHORT_WAIT = (JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_SHORT_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_LONG_INIT = (JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_SHORT_WAIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_LONG_WAIT = (JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_LONG_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_CAMERA_ZOOM_CALIBRATE_INIT = (JON_GUI_SCREEN_COMPASS_CALIBRATION_STAGED_LONG_WAIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_CAMERA_HEAT_ZOOM_CALIBRATE_INIT = (JON_GUI_SCREEN_CAMERA_ZOOM_CALIBRATE_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_CAMERA_DAY_ZOOM_CALIBRATE_INIT = (JON_GUI_SCREEN_CAMERA_HEAT_ZOOM_CALIBRATE_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_LRF_CALIBRATION_INIT = (JON_GUI_SCREEN_CAMERA_DAY_ZOOM_CALIBRATE_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_LRF_CALIBRATION_CAMERA_DAY_INIT = (JON_GUI_SCREEN_LRF_CALIBRATION_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_LRF_CALIBRATION_CAMERA_HEAT_INIT = (JON_GUI_SCREEN_LRF_CALIBRATION_CAMERA_DAY_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_TARGET_INIT = (JON_GUI_SCREEN_LRF_CALIBRATION_CAMERA_HEAT_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_TARGET_WAITING_FOR_NEXT = (JON_GUI_SCREEN_TARGET_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_TARGET_WAITING_FOR_PREV = (JON_GUI_SCREEN_TARGET_WAITING_FOR_NEXT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_TARGET_WAITING_FOR_DELETE = (JON_GUI_SCREEN_TARGET_WAITING_FOR_PREV + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_MEDIA_SD_ERASE_WAIT = (JON_GUI_SCREEN_TARGET_WAITING_FOR_DELETE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_SYSTEM_POWER_OFF_WAIT = (JON_GUI_SCREEN_MEDIA_SD_ERASE_WAIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_SYSTEM_OVERHEAT_POWER_OFF_WAIT = (JON_GUI_SCREEN_SYSTEM_POWER_OFF_WAIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

JON_GUI_SCREEN_POWER_OFF_COUNTDOWN_WAIT = (JON_GUI_SCREEN_SYSTEM_OVERHEAT_POWER_OFF_WAIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

_JON_GUI_SCREEN_AFTER_WAIT_SCREENS_ = (JON_GUI_SCREEN_POWER_OFF_COUNTDOWN_WAIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

_JON_GUI_SCREEN_AFTER_LAST_ID_ = (_JON_GUI_SCREEN_AFTER_WAIT_SCREENS_ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

jon_gui_screen_ids = enum_jon_gui_screen_ids# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 613

enum_jon_gui_data_time_formats = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 619

JON_GUI_DATA_TIME_FORMAT_H_M_S = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 619

JON_GUI_DATA_TIME_FORMAT_Y_m_D_H_M_S = (JON_GUI_DATA_TIME_FORMAT_H_M_S + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 619

_JON_SHARED_DATA_TIME_FORMAT_AFTER_LAST_ = (JON_GUI_DATA_TIME_FORMAT_Y_m_D_H_M_S + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 619

jon_gui_data_time_formats = enum_jon_gui_data_time_formats# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 619

enum_jon_gui_data_lrf_target_designator_status = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 626

JON_GUI_DATA_LRF_TARGET_DESIGNATOR_STATUS_OFF = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 626

JON_GUI_DATA_LRF_TARGET_DESIGNATOR_STATUS_MODE_1 = (JON_GUI_DATA_LRF_TARGET_DESIGNATOR_STATUS_OFF + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 626

JON_GUI_DATA_LRF_TARGET_DESIGNATOR_STATUS_MODE_2 = (JON_GUI_DATA_LRF_TARGET_DESIGNATOR_STATUS_MODE_1 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 626

_JON_SHARED_DATA_LRF_TARGET_DESIGNATOR_STATUS_AFTER_LAST_ = (JON_GUI_DATA_LRF_TARGET_DESIGNATOR_STATUS_MODE_2 + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 626

jon_gui_data_lrf_target_designator_status = enum_jon_gui_data_lrf_target_designator_status# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 626

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 627
for _lib in _libs.values():
    try:
        jon_gui_data_types_time_formats = (POINTER(c_char) * int(_JON_SHARED_DATA_TIME_FORMAT_AFTER_LAST_)).in_dll(_lib, "jon_gui_data_types_time_formats")
        break
    except:
        pass

enum_jon_gui_data_compass_calibrate_status = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 637

JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_NOT_CALIBRATING = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 637

JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_CALIBRATING_SHORT = (JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_NOT_CALIBRATING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 637

JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_CALIBRATING_LONG = (JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_CALIBRATING_SHORT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 637

JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_FINISHED = (JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_CALIBRATING_LONG + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 637

JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_ERROR = (JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_FINISHED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 637

_JON_SHARED_DATA_COMPASS_CALIBRATE_STATUS_AFTER_LAST_ = (JON_GUI_DATA_COMPASS_CALIBRATE_STATUS_ERROR + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 637

jon_gui_data_compass_calibrate_status = enum_jon_gui_data_compass_calibrate_status# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 637

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 643
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

jon_gui_data_component_meteo = struct_jon_gui_data_component_meteo# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 643

enum_anon_11 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 654

JON_GUI_DATA_ROTARY_MODE_UNSPECIFIED = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 654

JON_GUI_DATA_ROTARY_MODE_INITIALIZATION = (JON_GUI_DATA_ROTARY_MODE_UNSPECIFIED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 654

JON_GUI_DATA_ROTARY_MODE_SPEED = (JON_GUI_DATA_ROTARY_MODE_INITIALIZATION + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 654

JON_GUI_DATA_ROTARY_MODE_POSITION = (JON_GUI_DATA_ROTARY_MODE_SPEED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 654

JON_GUI_DATA_ROTARY_MODE_STABILIZATION = (JON_GUI_DATA_ROTARY_MODE_POSITION + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 654

JON_GUI_DATA_ROTARY_MODE_TARGETING = (JON_GUI_DATA_ROTARY_MODE_STABILIZATION + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 654

JON_GUI_DATA_ROTARY_MODE_VIDEO_TRACKER = (JON_GUI_DATA_ROTARY_MODE_TARGETING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 654

_JON_GUI_DATA_ROTARY_MODE_AFTER_LAST_ = (JON_GUI_DATA_ROTARY_MODE_VIDEO_TRACKER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 654

jon_gui_data_rotary_mode = enum_anon_11# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 654

enum_jon_gui_data_power_can_device = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 666

jon_gui_data_power_can_device_none = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 666

jon_gui_data_power_can_device_compass = (jon_gui_data_power_can_device_none + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 666

jon_gui_data_power_can_device_gps = (jon_gui_data_power_can_device_compass + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 666

jon_gui_data_power_can_device_cam_day = (jon_gui_data_power_can_device_gps + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 666

jon_gui_data_power_can_device_cam_heat = (jon_gui_data_power_can_device_cam_day + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 666

jon_gui_data_power_can_device_cam_heat_core = (jon_gui_data_power_can_device_cam_heat + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 666

jon_gui_data_power_can_device_lrf = (jon_gui_data_power_can_device_cam_heat_core + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 666

jon_gui_data_power_can_device_orin = (jon_gui_data_power_can_device_lrf + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 666

_jon_gui_data_power_can_device_after_last_ = (jon_gui_data_power_can_device_orin + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 666

jon_gui_data_power_can_device = enum_jon_gui_data_power_can_device# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 666

enum_jon_gui_data_fx_mode_day = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 677

JON_GUI_DATA_FX_MODE_DAY_DEFAULT = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 677

JON_GUI_DATA_FX_MODE_DAY_A = (JON_GUI_DATA_FX_MODE_DAY_DEFAULT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 677

JON_GUI_DATA_FX_MODE_DAY_B = (JON_GUI_DATA_FX_MODE_DAY_A + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 677

JON_GUI_DATA_FX_MODE_DAY_C = (JON_GUI_DATA_FX_MODE_DAY_B + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 677

JON_GUI_DATA_FX_MODE_DAY_D = (JON_GUI_DATA_FX_MODE_DAY_C + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 677

JON_GUI_DATA_FX_MODE_DAY_E = (JON_GUI_DATA_FX_MODE_DAY_D + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 677

JON_GUI_DATA_FX_MODE_DAY_F = (JON_GUI_DATA_FX_MODE_DAY_E + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 677

_JON_GUI_DATA_FX_MODE_DAY_AFTER_LAST_ = (JON_GUI_DATA_FX_MODE_DAY_F + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 677

jon_gui_data_fx_mode_day = enum_jon_gui_data_fx_mode_day# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 677

enum_jon_gui_data_fx_mode_heat = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 688

JON_GUI_DATA_FX_MODE_HEAT_DEFAULT = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 688

JON_GUI_DATA_FX_MODE_HEAT_A = (JON_GUI_DATA_FX_MODE_HEAT_DEFAULT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 688

JON_GUI_DATA_FX_MODE_HEAT_B = (JON_GUI_DATA_FX_MODE_HEAT_A + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 688

JON_GUI_DATA_FX_MODE_HEAT_C = (JON_GUI_DATA_FX_MODE_HEAT_B + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 688

JON_GUI_DATA_FX_MODE_HEAT_D = (JON_GUI_DATA_FX_MODE_HEAT_C + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 688

JON_GUI_DATA_FX_MODE_HEAT_E = (JON_GUI_DATA_FX_MODE_HEAT_D + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 688

JON_GUI_DATA_FX_MODE_HEAT_F = (JON_GUI_DATA_FX_MODE_HEAT_E + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 688

_JON_GUI_DATA_FX_MODE_HEAT_AFTER_LAST_ = (JON_GUI_DATA_FX_MODE_HEAT_F + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 688

jon_gui_data_fx_mode_heat = enum_jon_gui_data_fx_mode_heat# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 688

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 696
class union_anon_12(Union):
    pass

union_anon_12.__slots__ = [
    'units_idx',
    'units_idx_packed',
]
union_anon_12._fields_ = [
    ('units_idx', jon_gui_data_compass_units),
    ('units_idx_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 701
class union_anon_13(Union):
    pass

union_anon_13.__slots__ = [
    'device_status',
    'device_status_packed',
]
union_anon_13._fields_ = [
    ('device_status', jon_gui_data_device_status),
    ('device_status_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 707
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
    ('unnamed_1', union_anon_12),
    ('unnamed_2', union_anon_13),
    ('meteo', jon_gui_data_component_meteo),
]

jon_gui_data_compass = struct_jon_gui_data_compass# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 707

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 708
for _lib in _libs.values():
    try:
        jon_gui_default_state_compass = (jon_gui_data_compass).in_dll(_lib, "jon_gui_default_state_compass")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 716
class union_anon_14(Union):
    pass

union_anon_14.__slots__ = [
    'status',
    'jon_gui_data_compass_calibrate_status_packed',
]
union_anon_14._fields_ = [
    ('status', jon_gui_data_compass_calibrate_status),
    ('jon_gui_data_compass_calibrate_status_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 721
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
    ('unnamed_1', union_anon_14),
]

jon_gui_data_compass_calibration = struct_jon_gui_data_compass_calibration# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 721

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 723
for _lib in _libs.values():
    try:
        jon_gui_default_state_compass_calibration = (jon_gui_data_compass_calibration).in_dll(_lib, "jon_gui_default_state_compass_calibration")
        break
    except:
        pass

enum_anon_15 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_READY_FOR_NEW = (-1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_UP = (45 * 2)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_DOWN = (JON_GUI_EVENT_INPUT_UP + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_LEFT = (JON_GUI_EVENT_INPUT_DOWN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_RIGHT = (JON_GUI_EVENT_INPUT_LEFT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_ENTER = (JON_GUI_EVENT_INPUT_RIGHT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_ESC = (JON_GUI_EVENT_INPUT_ENTER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_UP_FASTER = (JON_GUI_EVENT_INPUT_ESC + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_DOWN_FASTER = (JON_GUI_EVENT_INPUT_UP_FASTER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_LEFT_FASTER = (JON_GUI_EVENT_INPUT_DOWN_FASTER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_RIGHT_FASTER = (JON_GUI_EVENT_INPUT_LEFT_FASTER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_ENTER_FASTER = (JON_GUI_EVENT_INPUT_RIGHT_FASTER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_ESC_FASTER = (JON_GUI_EVENT_INPUT_ENTER_FASTER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_UP_FAST = (JON_GUI_EVENT_INPUT_ESC_FASTER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_DOWN_FAST = (JON_GUI_EVENT_INPUT_UP_FAST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_LEFT_FAST = (JON_GUI_EVENT_INPUT_DOWN_FAST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_RIGHT_FAST = (JON_GUI_EVENT_INPUT_LEFT_FAST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_ENTER_FAST = (JON_GUI_EVENT_INPUT_RIGHT_FAST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_ESC_FAST = (JON_GUI_EVENT_INPUT_ENTER_FAST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_UP_FASTEST = (JON_GUI_EVENT_INPUT_ESC_FAST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_DOWN_FASTEST = (JON_GUI_EVENT_INPUT_UP_FASTEST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_LEFT_FASTEST = (JON_GUI_EVENT_INPUT_DOWN_FASTEST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_RIGHT_FASTEST = (JON_GUI_EVENT_INPUT_LEFT_FASTEST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_ENTER_FASTEST = (JON_GUI_EVENT_INPUT_RIGHT_FASTEST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_INPUT_ESC_FASTEST = (JON_GUI_EVENT_INPUT_ENTER_FASTEST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_SYNC = (JON_GUI_EVENT_INPUT_ESC_FASTEST + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_PING = (JON_GUI_EVENT_SYNC + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_PONG = (JON_GUI_EVENT_PING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

JON_GUI_EVENT_KILL = (JON_GUI_EVENT_PONG + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

_JON_GUI_EVENT_INPUT_AFTER_LAST_ = (JON_GUI_EVENT_KILL + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

jon_gui_input_event_codes = enum_anon_15# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 756

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 768
class struct_anon_16(Structure):
    pass

struct_anon_16.__slots__ = [
    'timestamp_low',
    'timestamp_hi',
]
struct_anon_16._fields_ = [
    ('timestamp_low', c_int32),
    ('timestamp_hi', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 765
class union_anon_17(Union):
    pass

union_anon_17.__slots__ = [
    'timestamp',
    'unnamed_1',
]
union_anon_17._anonymous_ = [
    'unnamed_1',
]
union_anon_17._fields_ = [
    ('timestamp', time_t),
    ('unnamed_1', struct_anon_16),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 774
class union_anon_18(Union):
    pass

union_anon_18.__slots__ = [
    'fix_type',
    'fix_type_packed',
]
union_anon_18._fields_ = [
    ('fix_type', jon_gui_data_gps_fix_type),
    ('fix_type_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 780
class union_anon_19(Union):
    pass

union_anon_19.__slots__ = [
    'units_idx',
    'units_packed',
]
union_anon_19._fields_ = [
    ('units_idx', jon_gui_data_gps_units),
    ('units_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 785
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

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 791
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
    ('unnamed_1', union_anon_17),
    ('unnamed_2', union_anon_18),
    ('use_manual', c_int32),
    ('unnamed_3', union_anon_19),
    ('unnamed_4', union_anon_20),
    ('meteo', jon_gui_data_component_meteo),
]

jon_gui_data_gps = struct_jon_gui_data_gps# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 791

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 792
for _lib in _libs.values():
    try:
        jon_gui_default_state_gps = (jon_gui_data_gps).in_dll(_lib, "jon_gui_default_state_gps")
        break
    except:
        pass

enum_jon_gui_data_mode = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 799

JON_GUI_DATA_MODE_DEFAULT = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 799

JON_GUI_DATA_MODE_FADED = (JON_GUI_DATA_MODE_DEFAULT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 799

JON_GUI_DATA_MODE_OSD_OFF = (JON_GUI_DATA_MODE_FADED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 799

_JON_GUI_DATA_MODE_AFTER_LAST_ = (JON_GUI_DATA_MODE_OSD_OFF + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 799

jon_gui_data_mode = enum_jon_gui_data_mode# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 799

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 805
class union_anon_21(Union):
    pass

union_anon_21.__slots__ = [
    'active_mode_id',
    'active_mode_id_packed',
]
union_anon_21._fields_ = [
    ('active_mode_id', jon_gui_data_mode),
    ('active_mode_id_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 810
class union_anon_22(Union):
    pass

union_anon_22.__slots__ = [
    'active_screen_id',
    'active_screen_id_packed',
]
union_anon_22._fields_ = [
    ('active_screen_id', jon_gui_screen_ids),
    ('active_screen_id_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 815
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
    ('unnamed_1', union_anon_21),
    ('unnamed_2', union_anon_22),
]

jon_gui_data_header = struct_jon_gui_data_header# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 815

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 816
for _lib in _libs.values():
    try:
        jon_gui_default_state_header = (jon_gui_data_header).in_dll(_lib, "jon_gui_default_state_header")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 855
class union_anon_23(Union):
    pass

union_anon_23.__slots__ = [
    'device_status_day',
    'device_status_day_packed',
]
union_anon_23._fields_ = [
    ('device_status_day', jon_gui_data_device_status),
    ('device_status_day_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 860
class union_anon_24(Union):
    pass

union_anon_24.__slots__ = [
    'device_status_heat',
    'device_status_heat_packed',
]
union_anon_24._fields_ = [
    ('device_status_heat', jon_gui_data_device_status),
    ('device_status_heat_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 865
class union_anon_25(Union):
    pass

union_anon_25.__slots__ = [
    'fx_mode_day',
    'fx_mode_day_packed',
]
union_anon_25._fields_ = [
    ('fx_mode_day', jon_gui_data_fx_mode_day),
    ('fx_mode_day_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 870
class union_anon_26(Union):
    pass

union_anon_26.__slots__ = [
    'fx_mode_heat',
    'fx_mode_heat_packed',
]
union_anon_26._fields_ = [
    ('fx_mode_heat', jon_gui_data_fx_mode_heat),
    ('fx_mode_heat_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 875
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
    ('unnamed_1', union_anon_23),
    ('unnamed_2', union_anon_24),
    ('unnamed_3', union_anon_25),
    ('unnamed_4', union_anon_26),
]

jon_gui_data_lens = struct_jon_gui_data_lens# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 875

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 876
for _lib in _libs.values():
    try:
        jon_gui_default_state_lens = (jon_gui_data_lens).in_dll(_lib, "jon_gui_default_state_lens")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 888
class union_anon_27(Union):
    pass

union_anon_27.__slots__ = [
    'target_designator_status',
    'target_designator_status_packed',
]
union_anon_27._fields_ = [
    ('target_designator_status', jon_gui_data_lrf_target_designator_status),
    ('target_designator_status_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 894
class union_anon_28(Union):
    pass

union_anon_28.__slots__ = [
    'device_status',
    'device_status_packed',
]
union_anon_28._fields_ = [
    ('device_status', jon_gui_data_device_status),
    ('device_status_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 900
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
    ('unnamed_1', union_anon_27),
    ('error_bf', c_int32),
    ('unnamed_2', union_anon_28),
    ('meteo', jon_gui_data_component_meteo),
]

jon_gui_data_lrf = struct_jon_gui_data_lrf# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 900

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 901
for _lib in _libs.values():
    try:
        jon_gui_default_state_lrf = (jon_gui_data_lrf).in_dll(_lib, "jon_gui_default_state_lrf")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 906
class struct_jon_gui_data_media(Structure):
    pass

struct_jon_gui_data_media.__slots__ = [
    'space_left_prc',
]
struct_jon_gui_data_media._fields_ = [
    ('space_left_prc', c_int32),
]

jon_gui_data_media = struct_jon_gui_data_media# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 906

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 907
for _lib in _libs.values():
    try:
        jon_gui_default_state_media = (jon_gui_data_media).in_dll(_lib, "jon_gui_default_state_media")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 916
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

jon_gui_data_meteo = struct_jon_gui_data_meteo# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 916

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 917
for _lib in _libs.values():
    try:
        jon_gui_default_state_meteo = (jon_gui_data_meteo).in_dll(_lib, "jon_gui_default_state_meteo")
        break
    except:
        pass

enum_jon_gui_data_osd_pip_pos = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 926

JON_GUI_DATA_OSD_PIP_DISABLED = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 926

JON_GUI_DATA_OSD_PIP_TOP_LEFT = (JON_GUI_DATA_OSD_PIP_DISABLED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 926

JON_GUI_DATA_OSD_PIP_TOP_RIGHT = (JON_GUI_DATA_OSD_PIP_TOP_LEFT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 926

JON_GUI_DATA_OSD_PIP_BOTTOM_RIGHT = (JON_GUI_DATA_OSD_PIP_TOP_RIGHT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 926

JON_GUI_DATA_OSD_PIP_BOTTOM_LEFT = (JON_GUI_DATA_OSD_PIP_BOTTOM_RIGHT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 926

_JON_GUI_DATA_OSD_PIP_AFTER_LAST_ = (JON_GUI_DATA_OSD_PIP_BOTTOM_LEFT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 926

jon_gui_data_osd_pip_pos = enum_jon_gui_data_osd_pip_pos# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 926

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 937
class union_anon_29(Union):
    pass

union_anon_29.__slots__ = [
    'pip_pos_id',
    'pip_pos_id_packed',
]
union_anon_29._fields_ = [
    ('pip_pos_id', jon_gui_data_osd_pip_pos),
    ('pip_pos_id_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 942
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
    ('unnamed_1', union_anon_29),
]

jon_gui_data_osd = struct_jon_gui_data_osd# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 942

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 943
for _lib in _libs.values():
    try:
        jon_gui_default_state_osd = (jon_gui_data_osd).in_dll(_lib, "jon_gui_default_state_osd")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 973
class union_anon_30(Union):
    pass

union_anon_30.__slots__ = [
    'device_status',
    'device_status_packed',
]
union_anon_30._fields_ = [
    ('device_status', jon_gui_data_device_status),
    ('device_status_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 978
class union_anon_31(Union):
    pass

union_anon_31.__slots__ = [
    'mode',
    'mode_packed',
]
union_anon_31._fields_ = [
    ('mode', jon_gui_data_rotary_mode),
    ('mode_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 987
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
    ('unnamed_1', union_anon_30),
    ('unnamed_2', union_anon_31),
    ('meteo', jon_gui_data_component_meteo),
    ('rotary_init', c_int32),
    ('pan_init', c_int32),
    ('tilt_init', c_int32),
]

jon_gui_data_rotary = struct_jon_gui_data_rotary# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 987

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 988
for _lib in _libs.values():
    try:
        jon_gui_default_state_rotary = (jon_gui_data_rotary).in_dll(_lib, "jon_gui_default_state_rotary")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 998
class union_anon_32(Union):
    pass

union_anon_32.__slots__ = [
    'can_device',
    'can_device_packed',
]
union_anon_32._fields_ = [
    ('can_device', jon_gui_data_power_can_device),
    ('can_device_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1003
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
    ('unnamed_1', union_anon_32),
]

jon_gui_data_power_module_state = struct_jon_gui_data_power_module_state# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1003

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1015
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

jon_gui_data_power = struct_jon_gui_data_power# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1015

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1016
for _lib in _libs.values():
    try:
        jon_gui_default_state_power = (jon_gui_data_power).in_dll(_lib, "jon_gui_default_state_power")
        break
    except:
        pass

enum_jon_gui_data_system_localizations = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1024

jon_gui_data_system_localization_en = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1024

jon_gui_data_system_localization_ua = (jon_gui_data_system_localization_en + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1024

jon_gui_data_system_localization_ar = (jon_gui_data_system_localization_ua + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1024

jon_gui_data_system_localization_cs = (jon_gui_data_system_localization_ar + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1024

_jon_gui_data_system_localization_after_last_ = (jon_gui_data_system_localization_cs + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1024

jon_gui_data_system_localizations = enum_jon_gui_data_system_localizations# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1024

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1044
class union_anon_33(Union):
    pass

union_anon_33.__slots__ = [
    'localization_id',
    'localization_id_packed',
]
union_anon_33._fields_ = [
    ('localization_id', jon_gui_data_system_localizations),
    ('localization_id_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1049
class union_anon_34(Union):
    pass

union_anon_34.__slots__ = [
    'active_video_channel',
    'active_video_channel_packed',
]
union_anon_34._fields_ = [
    ('active_video_channel', jon_gui_data_video_channel),
    ('active_video_channel_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1054
class union_anon_35(Union):
    pass

union_anon_35.__slots__ = [
    'active_thermal_color_filter_idx',
    'active_thermal_color_filter_packed',
]
union_anon_35._fields_ = [
    ('active_thermal_color_filter_idx', jon_gui_data_video_channel_heat_filters),
    ('active_thermal_color_filter_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1060
class union_anon_36(Union):
    pass

union_anon_36.__slots__ = [
    'active_day_filter_idx',
    'active_day_filter_packed',
]
union_anon_36._fields_ = [
    ('active_day_filter_idx', jon_gui_data_video_channel_day_filters),
    ('active_day_filter_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1065
class union_anon_37(Union):
    pass

union_anon_37.__slots__ = [
    'acccumulator_stat_idx',
    'acccumulator_stat_idx_packed',
]
union_anon_37._fields_ = [
    ('acccumulator_stat_idx', jon_gui_data_accumulator_state_idx),
    ('acccumulator_stat_idx_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1070
class union_anon_38(Union):
    pass

union_anon_38.__slots__ = [
    'sd_card_stat_idx',
    'sd_card_stat_idx_packed',
]
union_anon_38._fields_ = [
    ('sd_card_stat_idx', jon_gui_data_sd_card_state_idx),
    ('sd_card_stat_idx_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1083
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
    ('unnamed_1', union_anon_33),
    ('unnamed_2', union_anon_34),
    ('unnamed_3', union_anon_35),
    ('unnamed_4', union_anon_36),
    ('unnamed_5', union_anon_37),
    ('unnamed_6', union_anon_38),
    ('cur_video_rec_dir_year', c_int32),
    ('cur_video_rec_dir_month', c_int32),
    ('cur_video_rec_dir_day', c_int32),
    ('cur_video_rec_dir_hour', c_int32),
    ('cur_video_rec_dir_minute', c_int32),
    ('cur_video_rec_dir_second', c_int32),
    ('low_disk_space', c_int32),
    ('no_disk_space', c_int32),
]

jon_gui_data_system = struct_jon_gui_data_system# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1083

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1084
for _lib in _libs.values():
    try:
        jon_gui_default_state_system = (jon_gui_data_system).in_dll(_lib, "jon_gui_default_state_system")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1094
class union_anon_39(Union):
    pass

union_anon_39.__slots__ = [
    'observer_timestamp',
    'observer_timestamp_packed',
]
union_anon_39._fields_ = [
    ('observer_timestamp', time_t),
    ('observer_timestamp_packed', c_int64),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1108
class union_anon_40(Union):
    pass

union_anon_40.__slots__ = [
    'observer_fix_type',
    'observer_fix_type_packed',
]
union_anon_40._fields_ = [
    ('observer_fix_type', jon_gui_data_gps_fix_type),
    ('observer_fix_type_packed', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1113
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
    ('unnamed_1', union_anon_39),
    ('observer_longitude', c_int32),
    ('observer_latitude', c_int32),
    ('observer_azimuth', c_int32),
    ('observer_elevation', c_int32),
    ('observer_altitude', c_int32),
    ('distance_a', c_int32),
    ('distance_b', c_int32),
    ('has_range', c_int32),
    ('session_id', c_int32),
    ('unnamed_2', union_anon_40),
]

jon_gui_data_target_spec = struct_jon_gui_data_target_spec# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1113

enum_jon_gui_data_targets_screenshot_state = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1120

JON_GUI_DATA_TARGETS_SCREENSHOT_STATE_INFO = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1120

JON_GUI_DATA_TARGETS_SCREENSHOT_STATE_DAY = (JON_GUI_DATA_TARGETS_SCREENSHOT_STATE_INFO + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1120

JON_GUI_DATA_TARGETS_SCREENSHOT_STATE_HEAT = (JON_GUI_DATA_TARGETS_SCREENSHOT_STATE_DAY + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1120

__JON_GUI_DATA_TARGETS_SCREENSHOT_STATE_AFTER_LAST__ = (JON_GUI_DATA_TARGETS_SCREENSHOT_STATE_HEAT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1120

jon_gui_data_targets_screenshot_state = enum_jon_gui_data_targets_screenshot_state# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1120

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1127
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

jon_gui_data_targets = struct_jon_gui_data_targets# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1127

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1128
for _lib in _libs.values():
    try:
        jon_gui_default_state_targets = (jon_gui_data_targets).in_dll(_lib, "jon_gui_default_state_targets")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1134
class struct_anon_41(Structure):
    pass

struct_anon_41.__slots__ = [
    'timestamp_low',
    'timestamp_hi',
]
struct_anon_41._fields_ = [
    ('timestamp_low', c_int32),
    ('timestamp_hi', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1131
class union_anon_42(Union):
    pass

union_anon_42.__slots__ = [
    'timestamp',
    'unnamed_1',
]
union_anon_42._anonymous_ = [
    'unnamed_1',
]
union_anon_42._fields_ = [
    ('timestamp', time_t),
    ('unnamed_1', struct_anon_41),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1143
class struct_anon_43(Structure):
    pass

struct_anon_43.__slots__ = [
    'manual_timestamp_low',
    'manual_timestamp_hi',
]
struct_anon_43._fields_ = [
    ('manual_timestamp_low', c_int32),
    ('manual_timestamp_hi', c_int32),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1140
class union_anon_44(Union):
    pass

union_anon_44.__slots__ = [
    'manual_timestamp',
    'unnamed_1',
]
union_anon_44._anonymous_ = [
    'unnamed_1',
]
union_anon_44._fields_ = [
    ('manual_timestamp', time_t),
    ('unnamed_1', struct_anon_43),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1151
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
    ('unnamed_1', union_anon_42),
    ('unnamed_2', union_anon_44),
    ('zone_id', c_int32),
    ('use_manual_time', c_int32),
]

jon_gui_data_time = struct_jon_gui_data_time# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1151

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1152
for _lib in _libs.values():
    try:
        jon_gui_default_state_time = (jon_gui_data_time).in_dll(_lib, "jon_gui_default_state_time")
        break
    except:
        pass

enum_jon_gui_tracking_color = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_RED = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_GREEN = (JON_GUI_TRACKING_COLOR_RED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_BLUE = (JON_GUI_TRACKING_COLOR_GREEN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_YELLOW = (JON_GUI_TRACKING_COLOR_BLUE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_MAGENTA = (JON_GUI_TRACKING_COLOR_YELLOW + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_CYAN = (JON_GUI_TRACKING_COLOR_MAGENTA + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_ORANGE = (JON_GUI_TRACKING_COLOR_CYAN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_PURPLE = (JON_GUI_TRACKING_COLOR_ORANGE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_LIME = (JON_GUI_TRACKING_COLOR_PURPLE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_PINK = (JON_GUI_TRACKING_COLOR_LIME + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_TEAL = (JON_GUI_TRACKING_COLOR_PINK + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_LAVENDER = (JON_GUI_TRACKING_COLOR_TEAL + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_BROWN = (JON_GUI_TRACKING_COLOR_LAVENDER + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_BEIGE = (JON_GUI_TRACKING_COLOR_BROWN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_MAROON = (JON_GUI_TRACKING_COLOR_BEIGE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_MINT = (JON_GUI_TRACKING_COLOR_MAROON + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_OLIVE = (JON_GUI_TRACKING_COLOR_MINT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_APRICOT = (JON_GUI_TRACKING_COLOR_OLIVE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_NAVY = (JON_GUI_TRACKING_COLOR_APRICOT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_GREY = (JON_GUI_TRACKING_COLOR_NAVY + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_WHITE = (JON_GUI_TRACKING_COLOR_GREY + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

JON_GUI_TRACKING_COLOR_BLACK = (JON_GUI_TRACKING_COLOR_WHITE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

jon_gui_tracking_color_t = enum_jon_gui_tracking_color# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1178

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1181
class struct_anon_45(Structure):
    pass

struct_anon_45.__slots__ = [
    'r',
    'g',
    'b',
    'a',
]
struct_anon_45._fields_ = [
    ('r', uint8_t),
    ('g', uint8_t),
    ('b', uint8_t),
    ('a', uint8_t),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1189
class union_jon_gui_color_rgba8888(Union):
    pass

union_jon_gui_color_rgba8888.__slots__ = [
    'channels',
    'packed',
]
union_jon_gui_color_rgba8888._fields_ = [
    ('channels', struct_anon_45),
    ('packed', uint32_t),
]

jon_gui_color_rgba8888_t = union_jon_gui_color_rgba8888# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1189

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1192
class struct_anon_46(Structure):
    pass

struct_anon_46.__slots__ = [
    'x',
    'y',
    'color_index',
]
struct_anon_46._fields_ = [
    ('x', uint32_t, 12),
    ('y', uint32_t, 12),
    ('color_index', uint32_t, 8),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1199
class union_jon_gui_tracking_point(Union):
    pass

union_jon_gui_tracking_point.__slots__ = [
    'fields',
    'packed',
]
union_jon_gui_tracking_point._fields_ = [
    ('fields', struct_anon_46),
    ('packed', uint32_t),
]

jon_gui_tracking_point_t = union_jon_gui_tracking_point# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1199

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1204
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

jon_gui_tracking_quad_t = struct_jon_gui_tracking_quad# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1204

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1217
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

jon_gui_data_cv_t = struct_jon_gui_data_cv# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1217

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1218
for _lib in _libs.values():
    try:
        jon_gui_default_state_cv = (jon_gui_data_cv_t).in_dll(_lib, "jon_gui_default_state_cv")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1220
for _lib in _libs.values():
    try:
        jon_gui_tracking_colors = (jon_gui_color_rgba8888_t * int(22)).in_dll(_lib, "jon_gui_tracking_colors")
        break
    except:
        pass

enum_anon_47 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

JON_DEBUG_VERTICAL_FOV = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

JON_DEBUG_HORIZONTAL_FOV = (JON_DEBUG_VERTICAL_FOV + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

JON_DEBUG_AF_PROCESSING_TIME = (JON_DEBUG_HORIZONTAL_FOV + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

JON_DEBUG_TRACKING_PROCESSING_TIME = (JON_DEBUG_AF_PROCESSING_TIME + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

JON_DEBUG_FRAME_RATE = (JON_DEBUG_TRACKING_PROCESSING_TIME + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

JON_DEBUG_AF_CONFIDENCE_SCORE = (JON_DEBUG_FRAME_RATE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

JON_DEBUG_TRACKING_CONFIDENCE_SCORE = (JON_DEBUG_AF_CONFIDENCE_SCORE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

JON_DEBUG_DETECTED_FACES = (JON_DEBUG_TRACKING_CONFIDENCE_SCORE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

JON_DEBUG_FACE_DETECTION_TIME = (JON_DEBUG_DETECTED_FACES + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

JON_DEBUG_IMAGE_PREPROCESSING_TIME = (JON_DEBUG_FACE_DETECTION_TIME + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

JON_DEBUG_FEATURE_EXTRACTION_TIME = (JON_DEBUG_IMAGE_PREPROCESSING_TIME + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

JON_DEBUG_AF_ALGORITHM_ITERATIONS = (JON_DEBUG_FEATURE_EXTRACTION_TIME + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

JON_DEBUG_TRACKING_ALGORITHM_ITERATIONS = (JON_DEBUG_AF_ALGORITHM_ITERATIONS + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

JON_DEBUG_MEMORY_USAGE = (JON_DEBUG_TRACKING_ALGORITHM_ITERATIONS + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

JON_DEBUG_GPU_UTILIZATION = (JON_DEBUG_MEMORY_USAGE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

JON_DEBUG_LABEL_COUNT = (JON_DEBUG_GPU_UTILIZATION + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

jon_debug_label_t = enum_anon_47# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1244

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1249
class struct_anon_48(Structure):
    pass

struct_anon_48.__slots__ = [
    'label',
    'divider',
]
struct_anon_48._fields_ = [
    ('label', String),
    ('divider', c_int32),
]

jon_debug_info_t = struct_anon_48# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1249

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1254
class struct_anon_49(Structure):
    pass

struct_anon_49.__slots__ = [
    'values',
    'display_debug',
]
struct_anon_49._fields_ = [
    ('values', c_int32 * int(20)),
    ('display_debug', c_int32),
]

jon_gui_data_debug_t = struct_anon_49# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1254

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1255
for _lib in _libs.values():
    try:
        jon_gui_default_state_debug = (jon_gui_data_debug_t).in_dll(_lib, "jon_gui_default_state_debug")
        break
    except:
        pass

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1256
for _lib in _libs.values():
    try:
        jon_debug_info = (jon_debug_info_t * int(JON_DEBUG_LABEL_COUNT)).in_dll(_lib, "jon_debug_info")
        break
    except:
        pass

enum_jon_bool = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1261

jon_false = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1261

jon_true = 1# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1261

jon_bool = enum_jon_bool# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1261

u_char = __u_char# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1263

u_short = __u_short# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1264

u_int = __u_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1265

u_long = __u_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1266

quad_t = __quad_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1267

u_quad_t = __u_quad_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1268

fsid_t = __fsid_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1269

loff_t = __loff_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1270

ino_t = __ino_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1271

ino64_t = __ino64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1272

dev_t = __dev_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1273

gid_t = __gid_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1274

mode_t = __mode_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1275

nlink_t = __nlink_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1276

uid_t = __uid_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1277

off_t = __off_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1278

off64_t = __off64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1279

id_t = __id_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1280

ssize_t = __ssize_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1281

daddr_t = __daddr_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1282

caddr_t = __caddr_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1283

key_t = __key_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1284

useconds_t = __useconds_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1285

suseconds_t = __suseconds_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1286

ulong = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1287

ushort = c_ushort# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1288

uint = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1289

u_int8_t = __uint8_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1290

u_int16_t = __uint16_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1291

u_int32_t = __uint32_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1292

u_int64_t = __uint64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1293

register_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1294

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1328
class struct_anon_50(Structure):
    pass

struct_anon_50.__slots__ = [
    '__val',
]
struct_anon_50._fields_ = [
    ('__val', c_ulong * int((1024 / (8 * sizeof(c_ulong))))),
]

__sigset_t = struct_anon_50# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1328

sigset_t = __sigset_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1329

__fd_mask = c_long# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1330

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1334
class struct_anon_51(Structure):
    pass

struct_anon_51.__slots__ = [
    'fds_bits',
]
struct_anon_51._fields_ = [
    ('fds_bits', __fd_mask * int((1024 / (8 * (c_int (ord_if_char(sizeof(__fd_mask)))).value)))),
]

fd_set = struct_anon_51# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1334

fd_mask = __fd_mask# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1335

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1336
if _libs["libc.so.6"].has("select", "cdecl"):
    select = _libs["libc.so.6"].get("select", "cdecl")
    select.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(struct_timeval)]
    select.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1340
if _libs["libc.so.6"].has("pselect", "cdecl"):
    pselect = _libs["libc.so.6"].get("pselect", "cdecl")
    pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(struct_timespec), POINTER(__sigset_t)]
    pselect.restype = c_int

blksize_t = __blksize_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1345

blkcnt_t = __blkcnt_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1346

fsblkcnt_t = __fsblkcnt_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1347

fsfilcnt_t = __fsfilcnt_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1348

blkcnt64_t = __blkcnt64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1349

fsblkcnt64_t = __fsblkcnt64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1350

fsfilcnt64_t = __fsfilcnt64_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1351

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1356
class struct_anon_52(Structure):
    pass

struct_anon_52.__slots__ = [
    '__low',
    '__high',
]
struct_anon_52._fields_ = [
    ('__low', c_uint),
    ('__high', c_uint),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1361
class union_anon_53(Union):
    pass

union_anon_53.__slots__ = [
    '__value64',
    '__value32',
]
union_anon_53._fields_ = [
    ('__value64', c_ulonglong),
    ('__value32', struct_anon_52),
]

__atomic_wide_counter = union_anon_53# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1361

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1362
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

__pthread_list_t = struct___pthread_internal_list# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1366

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1367
class struct___pthread_internal_slist(Structure):
    pass

struct___pthread_internal_slist.__slots__ = [
    '__next',
]
struct___pthread_internal_slist._fields_ = [
    ('__next', POINTER(struct___pthread_internal_slist)),
]

__pthread_slist_t = struct___pthread_internal_slist# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1370

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1371
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

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1382
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

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1397
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

__tss_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1408

__thrd_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1409

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1413
class struct_anon_54(Structure):
    pass

struct_anon_54.__slots__ = [
    '__data',
]
struct_anon_54._fields_ = [
    ('__data', c_int),
]

__once_flag = struct_anon_54# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1413

pthread_t = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1414

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1419
class union_anon_55(Union):
    pass

union_anon_55.__slots__ = [
    '__size',
    '__align',
]
union_anon_55._fields_ = [
    ('__size', c_char * int(4)),
    ('__align', c_int),
]

pthread_mutexattr_t = union_anon_55# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1419

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1424
class union_anon_56(Union):
    pass

union_anon_56.__slots__ = [
    '__size',
    '__align',
]
union_anon_56._fields_ = [
    ('__size', c_char * int(4)),
    ('__align', c_int),
]

pthread_condattr_t = union_anon_56# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1424

pthread_key_t = c_uint# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1425

pthread_once_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1426

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1427
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

pthread_attr_t = union_pthread_attr_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1432

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1438
class union_anon_57(Union):
    pass

union_anon_57.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_57._fields_ = [
    ('__data', struct___pthread_mutex_s),
    ('__size', c_char * int(40)),
    ('__align', c_long),
]

pthread_mutex_t = union_anon_57# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1438

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1444
class union_anon_58(Union):
    pass

union_anon_58.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_58._fields_ = [
    ('__data', struct___pthread_cond_s),
    ('__size', c_char * int(48)),
    ('__align', c_longlong),
]

pthread_cond_t = union_anon_58# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1444

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1450
class union_anon_59(Union):
    pass

union_anon_59.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_59._fields_ = [
    ('__data', struct___pthread_rwlock_arch_t),
    ('__size', c_char * int(56)),
    ('__align', c_long),
]

pthread_rwlock_t = union_anon_59# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1450

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1455
class union_anon_60(Union):
    pass

union_anon_60.__slots__ = [
    '__size',
    '__align',
]
union_anon_60._fields_ = [
    ('__size', c_char * int(8)),
    ('__align', c_long),
]

pthread_rwlockattr_t = union_anon_60# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1455

pthread_spinlock_t = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1456

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1461
class union_anon_61(Union):
    pass

union_anon_61.__slots__ = [
    '__size',
    '__align',
]
union_anon_61._fields_ = [
    ('__size', c_char * int(32)),
    ('__align', c_long),
]

pthread_barrier_t = union_anon_61# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1461

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1466
class union_anon_62(Union):
    pass

union_anon_62.__slots__ = [
    '__size',
    '__align',
]
union_anon_62._fields_ = [
    ('__size', c_char * int(4)),
    ('__align', c_int),
]

pthread_barrierattr_t = union_anon_62# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1466

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1468
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

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1480
class struct_sched_param(Structure):
    pass

struct_sched_param.__slots__ = [
    'sched_priority',
]
struct_sched_param._fields_ = [
    ('sched_priority', c_int),
]

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1484
if _libs["libc.so.6"].has("clone", "cdecl"):
    _func = _libs["libc.so.6"].get("clone", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [CFUNCTYPE(UNCHECKED(c_int), POINTER(None)), POINTER(None), c_int, POINTER(None)]
    clone = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1486
if _libs["libc.so.6"].has("unshare", "cdecl"):
    unshare = _libs["libc.so.6"].get("unshare", "cdecl")
    unshare.argtypes = [c_int]
    unshare.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1487
if _libs["libc.so.6"].has("sched_getcpu", "cdecl"):
    sched_getcpu = _libs["libc.so.6"].get("sched_getcpu", "cdecl")
    sched_getcpu.argtypes = []
    sched_getcpu.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1488
if _libs["libc.so.6"].has("getcpu", "cdecl"):
    getcpu = _libs["libc.so.6"].get("getcpu", "cdecl")
    getcpu.argtypes = [POINTER(c_uint), POINTER(c_uint)]
    getcpu.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1489
if _libs["libc.so.6"].has("setns", "cdecl"):
    setns = _libs["libc.so.6"].get("setns", "cdecl")
    setns.argtypes = [c_int, c_int]
    setns.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1490
if _libs["libc.so.6"].has("sched_setattr", "cdecl"):
    sched_setattr = _libs["libc.so.6"].get("sched_setattr", "cdecl")
    sched_setattr.argtypes = [pid_t, POINTER(struct_sched_attr), c_uint]
    sched_setattr.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1492
if _libs["libc.so.6"].has("sched_getattr", "cdecl"):
    sched_getattr = _libs["libc.so.6"].get("sched_getattr", "cdecl")
    sched_getattr.argtypes = [pid_t, POINTER(struct_sched_attr), c_uint, c_uint]
    sched_getattr.restype = c_int

__cpu_mask = c_ulong# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1495

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1499
class struct_anon_63(Structure):
    pass

struct_anon_63.__slots__ = [
    '__bits',
]
struct_anon_63._fields_ = [
    ('__bits', __cpu_mask * int((1024 / (8 * sizeof(__cpu_mask))))),
]

cpu_set_t = struct_anon_63# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1499

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1500
if _libs["libc.so.6"].has("__sched_cpucount", "cdecl"):
    __sched_cpucount = _libs["libc.so.6"].get("__sched_cpucount", "cdecl")
    __sched_cpucount.argtypes = [c_size_t, POINTER(cpu_set_t)]
    __sched_cpucount.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1502
if _libs["libc.so.6"].has("__sched_cpualloc", "cdecl"):
    __sched_cpualloc = _libs["libc.so.6"].get("__sched_cpualloc", "cdecl")
    __sched_cpualloc.argtypes = [c_size_t]
    __sched_cpualloc.restype = POINTER(cpu_set_t)

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1503
if _libs["libc.so.6"].has("__sched_cpufree", "cdecl"):
    __sched_cpufree = _libs["libc.so.6"].get("__sched_cpufree", "cdecl")
    __sched_cpufree.argtypes = [POINTER(cpu_set_t)]
    __sched_cpufree.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1504
if _libs["libc.so.6"].has("sched_setparam", "cdecl"):
    sched_setparam = _libs["libc.so.6"].get("sched_setparam", "cdecl")
    sched_setparam.argtypes = [__pid_t, POINTER(struct_sched_param)]
    sched_setparam.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1506
if _libs["libc.so.6"].has("sched_getparam", "cdecl"):
    sched_getparam = _libs["libc.so.6"].get("sched_getparam", "cdecl")
    sched_getparam.argtypes = [__pid_t, POINTER(struct_sched_param)]
    sched_getparam.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1507
if _libs["libc.so.6"].has("sched_setscheduler", "cdecl"):
    sched_setscheduler = _libs["libc.so.6"].get("sched_setscheduler", "cdecl")
    sched_setscheduler.argtypes = [__pid_t, c_int, POINTER(struct_sched_param)]
    sched_setscheduler.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1509
if _libs["libc.so.6"].has("sched_getscheduler", "cdecl"):
    sched_getscheduler = _libs["libc.so.6"].get("sched_getscheduler", "cdecl")
    sched_getscheduler.argtypes = [__pid_t]
    sched_getscheduler.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1510
if _libs["libc.so.6"].has("sched_yield", "cdecl"):
    sched_yield = _libs["libc.so.6"].get("sched_yield", "cdecl")
    sched_yield.argtypes = []
    sched_yield.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1511
if _libs["libc.so.6"].has("sched_get_priority_max", "cdecl"):
    sched_get_priority_max = _libs["libc.so.6"].get("sched_get_priority_max", "cdecl")
    sched_get_priority_max.argtypes = [c_int]
    sched_get_priority_max.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1512
if _libs["libc.so.6"].has("sched_get_priority_min", "cdecl"):
    sched_get_priority_min = _libs["libc.so.6"].get("sched_get_priority_min", "cdecl")
    sched_get_priority_min.argtypes = [c_int]
    sched_get_priority_min.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1513
if _libs["libc.so.6"].has("sched_rr_get_interval", "cdecl"):
    sched_rr_get_interval = _libs["libc.so.6"].get("sched_rr_get_interval", "cdecl")
    sched_rr_get_interval.argtypes = [__pid_t, POINTER(struct_timespec)]
    sched_rr_get_interval.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1514
if _libs["libc.so.6"].has("sched_setaffinity", "cdecl"):
    sched_setaffinity = _libs["libc.so.6"].get("sched_setaffinity", "cdecl")
    sched_setaffinity.argtypes = [__pid_t, c_size_t, POINTER(cpu_set_t)]
    sched_setaffinity.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1516
if _libs["libc.so.6"].has("sched_getaffinity", "cdecl"):
    sched_getaffinity = _libs["libc.so.6"].get("sched_getaffinity", "cdecl")
    sched_getaffinity.argtypes = [__pid_t, c_size_t, POINTER(cpu_set_t)]
    sched_getaffinity.restype = c_int

__jmp_buf = c_long * int(8)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1518

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1519
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

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1526
if _libs["libc.so.6"].has("__sysconf", "cdecl"):
    __sysconf = _libs["libc.so.6"].get("__sysconf", "cdecl")
    __sysconf.argtypes = [c_int]
    __sysconf.restype = c_long

enum_anon_64 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1527

PTHREAD_CREATE_JOINABLE = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1527

PTHREAD_CREATE_DETACHED = (PTHREAD_CREATE_JOINABLE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1527

enum_anon_65 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1532

PTHREAD_MUTEX_TIMED_NP = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1532

PTHREAD_MUTEX_RECURSIVE_NP = (PTHREAD_MUTEX_TIMED_NP + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1532

PTHREAD_MUTEX_ERRORCHECK_NP = (PTHREAD_MUTEX_RECURSIVE_NP + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1532

PTHREAD_MUTEX_ADAPTIVE_NP = (PTHREAD_MUTEX_ERRORCHECK_NP + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1532

PTHREAD_MUTEX_NORMAL = PTHREAD_MUTEX_TIMED_NP# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1532

PTHREAD_MUTEX_RECURSIVE = PTHREAD_MUTEX_RECURSIVE_NP# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1532

PTHREAD_MUTEX_ERRORCHECK = PTHREAD_MUTEX_ERRORCHECK_NP# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1532

PTHREAD_MUTEX_DEFAULT = PTHREAD_MUTEX_NORMAL# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1532

PTHREAD_MUTEX_FAST_NP = PTHREAD_MUTEX_TIMED_NP# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1532

enum_anon_66 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1545

PTHREAD_MUTEX_STALLED = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1545

PTHREAD_MUTEX_STALLED_NP = PTHREAD_MUTEX_STALLED# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1545

PTHREAD_MUTEX_ROBUST = (PTHREAD_MUTEX_STALLED_NP + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1545

PTHREAD_MUTEX_ROBUST_NP = PTHREAD_MUTEX_ROBUST# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1545

enum_anon_67 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1552

PTHREAD_PRIO_NONE = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1552

PTHREAD_PRIO_INHERIT = (PTHREAD_PRIO_NONE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1552

PTHREAD_PRIO_PROTECT = (PTHREAD_PRIO_INHERIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1552

enum_anon_68 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1558

PTHREAD_RWLOCK_PREFER_READER_NP = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1558

PTHREAD_RWLOCK_PREFER_WRITER_NP = (PTHREAD_RWLOCK_PREFER_READER_NP + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1558

PTHREAD_RWLOCK_PREFER_WRITER_NONRECURSIVE_NP = (PTHREAD_RWLOCK_PREFER_WRITER_NP + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1558

PTHREAD_RWLOCK_DEFAULT_NP = PTHREAD_RWLOCK_PREFER_READER_NP# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1558

enum_anon_69 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1565

PTHREAD_INHERIT_SCHED = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1565

PTHREAD_EXPLICIT_SCHED = (PTHREAD_INHERIT_SCHED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1565

enum_anon_70 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1570

PTHREAD_SCOPE_SYSTEM = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1570

PTHREAD_SCOPE_PROCESS = (PTHREAD_SCOPE_SYSTEM + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1570

enum_anon_71 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1575

PTHREAD_PROCESS_PRIVATE = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1575

PTHREAD_PROCESS_SHARED = (PTHREAD_PROCESS_PRIVATE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1575

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1580
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

enum_anon_72 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1587

PTHREAD_CANCEL_ENABLE = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1587

PTHREAD_CANCEL_DISABLE = (PTHREAD_CANCEL_ENABLE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1587

enum_anon_73 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1592

PTHREAD_CANCEL_DEFERRED = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1592

PTHREAD_CANCEL_ASYNCHRONOUS = (PTHREAD_CANCEL_DEFERRED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1592

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1597
if _libs["libc.so.6"].has("pthread_create", "cdecl"):
    pthread_create = _libs["libc.so.6"].get("pthread_create", "cdecl")
    pthread_create.argtypes = [POINTER(pthread_t), POINTER(pthread_attr_t), CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(None)), POINTER(None)]
    pthread_create.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1601
if _libs["libc.so.6"].has("pthread_exit", "cdecl"):
    pthread_exit = _libs["libc.so.6"].get("pthread_exit", "cdecl")
    pthread_exit.argtypes = [POINTER(None)]
    pthread_exit.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1602
if _libs["libc.so.6"].has("pthread_join", "cdecl"):
    pthread_join = _libs["libc.so.6"].get("pthread_join", "cdecl")
    pthread_join.argtypes = [pthread_t, POINTER(POINTER(None))]
    pthread_join.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1603
if _libs["libc.so.6"].has("pthread_tryjoin_np", "cdecl"):
    pthread_tryjoin_np = _libs["libc.so.6"].get("pthread_tryjoin_np", "cdecl")
    pthread_tryjoin_np.argtypes = [pthread_t, POINTER(POINTER(None))]
    pthread_tryjoin_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1604
if _libs["libc.so.6"].has("pthread_timedjoin_np", "cdecl"):
    pthread_timedjoin_np = _libs["libc.so.6"].get("pthread_timedjoin_np", "cdecl")
    pthread_timedjoin_np.argtypes = [pthread_t, POINTER(POINTER(None)), POINTER(struct_timespec)]
    pthread_timedjoin_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1606
if _libs["libc.so.6"].has("pthread_clockjoin_np", "cdecl"):
    pthread_clockjoin_np = _libs["libc.so.6"].get("pthread_clockjoin_np", "cdecl")
    pthread_clockjoin_np.argtypes = [pthread_t, POINTER(POINTER(None)), clockid_t, POINTER(struct_timespec)]
    pthread_clockjoin_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1609
if _libs["libc.so.6"].has("pthread_detach", "cdecl"):
    pthread_detach = _libs["libc.so.6"].get("pthread_detach", "cdecl")
    pthread_detach.argtypes = [pthread_t]
    pthread_detach.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1610
if _libs["libc.so.6"].has("pthread_self", "cdecl"):
    pthread_self = _libs["libc.so.6"].get("pthread_self", "cdecl")
    pthread_self.argtypes = []
    pthread_self.restype = pthread_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1611
if _libs["libc.so.6"].has("pthread_equal", "cdecl"):
    pthread_equal = _libs["libc.so.6"].get("pthread_equal", "cdecl")
    pthread_equal.argtypes = [pthread_t, pthread_t]
    pthread_equal.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1613
if _libs["libc.so.6"].has("pthread_attr_init", "cdecl"):
    pthread_attr_init = _libs["libc.so.6"].get("pthread_attr_init", "cdecl")
    pthread_attr_init.argtypes = [POINTER(pthread_attr_t)]
    pthread_attr_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1614
if _libs["libc.so.6"].has("pthread_attr_destroy", "cdecl"):
    pthread_attr_destroy = _libs["libc.so.6"].get("pthread_attr_destroy", "cdecl")
    pthread_attr_destroy.argtypes = [POINTER(pthread_attr_t)]
    pthread_attr_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1616
if _libs["libc.so.6"].has("pthread_attr_getdetachstate", "cdecl"):
    pthread_attr_getdetachstate = _libs["libc.so.6"].get("pthread_attr_getdetachstate", "cdecl")
    pthread_attr_getdetachstate.argtypes = [POINTER(pthread_attr_t), POINTER(c_int)]
    pthread_attr_getdetachstate.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1619
if _libs["libc.so.6"].has("pthread_attr_setdetachstate", "cdecl"):
    pthread_attr_setdetachstate = _libs["libc.so.6"].get("pthread_attr_setdetachstate", "cdecl")
    pthread_attr_setdetachstate.argtypes = [POINTER(pthread_attr_t), c_int]
    pthread_attr_setdetachstate.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1622
if _libs["libc.so.6"].has("pthread_attr_getguardsize", "cdecl"):
    pthread_attr_getguardsize = _libs["libc.so.6"].get("pthread_attr_getguardsize", "cdecl")
    pthread_attr_getguardsize.argtypes = [POINTER(pthread_attr_t), POINTER(c_size_t)]
    pthread_attr_getguardsize.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1625
if _libs["libc.so.6"].has("pthread_attr_setguardsize", "cdecl"):
    pthread_attr_setguardsize = _libs["libc.so.6"].get("pthread_attr_setguardsize", "cdecl")
    pthread_attr_setguardsize.argtypes = [POINTER(pthread_attr_t), c_size_t]
    pthread_attr_setguardsize.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1628
if _libs["libc.so.6"].has("pthread_attr_getschedparam", "cdecl"):
    pthread_attr_getschedparam = _libs["libc.so.6"].get("pthread_attr_getschedparam", "cdecl")
    pthread_attr_getschedparam.argtypes = [POINTER(pthread_attr_t), POINTER(struct_sched_param)]
    pthread_attr_getschedparam.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1631
if _libs["libc.so.6"].has("pthread_attr_setschedparam", "cdecl"):
    pthread_attr_setschedparam = _libs["libc.so.6"].get("pthread_attr_setschedparam", "cdecl")
    pthread_attr_setschedparam.argtypes = [POINTER(pthread_attr_t), POINTER(struct_sched_param)]
    pthread_attr_setschedparam.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1634
if _libs["libc.so.6"].has("pthread_attr_getschedpolicy", "cdecl"):
    pthread_attr_getschedpolicy = _libs["libc.so.6"].get("pthread_attr_getschedpolicy", "cdecl")
    pthread_attr_getschedpolicy.argtypes = [POINTER(pthread_attr_t), POINTER(c_int)]
    pthread_attr_getschedpolicy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1637
if _libs["libc.so.6"].has("pthread_attr_setschedpolicy", "cdecl"):
    pthread_attr_setschedpolicy = _libs["libc.so.6"].get("pthread_attr_setschedpolicy", "cdecl")
    pthread_attr_setschedpolicy.argtypes = [POINTER(pthread_attr_t), c_int]
    pthread_attr_setschedpolicy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1639
if _libs["libc.so.6"].has("pthread_attr_getinheritsched", "cdecl"):
    pthread_attr_getinheritsched = _libs["libc.so.6"].get("pthread_attr_getinheritsched", "cdecl")
    pthread_attr_getinheritsched.argtypes = [POINTER(pthread_attr_t), POINTER(c_int)]
    pthread_attr_getinheritsched.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1642
if _libs["libc.so.6"].has("pthread_attr_setinheritsched", "cdecl"):
    pthread_attr_setinheritsched = _libs["libc.so.6"].get("pthread_attr_setinheritsched", "cdecl")
    pthread_attr_setinheritsched.argtypes = [POINTER(pthread_attr_t), c_int]
    pthread_attr_setinheritsched.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1645
if _libs["libc.so.6"].has("pthread_attr_getscope", "cdecl"):
    pthread_attr_getscope = _libs["libc.so.6"].get("pthread_attr_getscope", "cdecl")
    pthread_attr_getscope.argtypes = [POINTER(pthread_attr_t), POINTER(c_int)]
    pthread_attr_getscope.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1648
if _libs["libc.so.6"].has("pthread_attr_setscope", "cdecl"):
    pthread_attr_setscope = _libs["libc.so.6"].get("pthread_attr_setscope", "cdecl")
    pthread_attr_setscope.argtypes = [POINTER(pthread_attr_t), c_int]
    pthread_attr_setscope.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1650
if _libs["libc.so.6"].has("pthread_attr_getstackaddr", "cdecl"):
    pthread_attr_getstackaddr = _libs["libc.so.6"].get("pthread_attr_getstackaddr", "cdecl")
    pthread_attr_getstackaddr.argtypes = [POINTER(pthread_attr_t), POINTER(POINTER(None))]
    pthread_attr_getstackaddr.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1653
if _libs["libc.so.6"].has("pthread_attr_setstackaddr", "cdecl"):
    pthread_attr_setstackaddr = _libs["libc.so.6"].get("pthread_attr_setstackaddr", "cdecl")
    pthread_attr_setstackaddr.argtypes = [POINTER(pthread_attr_t), POINTER(None)]
    pthread_attr_setstackaddr.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1656
if _libs["libc.so.6"].has("pthread_attr_getstacksize", "cdecl"):
    pthread_attr_getstacksize = _libs["libc.so.6"].get("pthread_attr_getstacksize", "cdecl")
    pthread_attr_getstacksize.argtypes = [POINTER(pthread_attr_t), POINTER(c_size_t)]
    pthread_attr_getstacksize.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1659
if _libs["libc.so.6"].has("pthread_attr_setstacksize", "cdecl"):
    pthread_attr_setstacksize = _libs["libc.so.6"].get("pthread_attr_setstacksize", "cdecl")
    pthread_attr_setstacksize.argtypes = [POINTER(pthread_attr_t), c_size_t]
    pthread_attr_setstacksize.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1662
if _libs["libc.so.6"].has("pthread_attr_getstack", "cdecl"):
    pthread_attr_getstack = _libs["libc.so.6"].get("pthread_attr_getstack", "cdecl")
    pthread_attr_getstack.argtypes = [POINTER(pthread_attr_t), POINTER(POINTER(None)), POINTER(c_size_t)]
    pthread_attr_getstack.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1666
if _libs["libc.so.6"].has("pthread_attr_setstack", "cdecl"):
    pthread_attr_setstack = _libs["libc.so.6"].get("pthread_attr_setstack", "cdecl")
    pthread_attr_setstack.argtypes = [POINTER(pthread_attr_t), POINTER(None), c_size_t]
    pthread_attr_setstack.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1668
if _libs["libc.so.6"].has("pthread_attr_setaffinity_np", "cdecl"):
    pthread_attr_setaffinity_np = _libs["libc.so.6"].get("pthread_attr_setaffinity_np", "cdecl")
    pthread_attr_setaffinity_np.argtypes = [POINTER(pthread_attr_t), c_size_t, POINTER(cpu_set_t)]
    pthread_attr_setaffinity_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1672
if _libs["libc.so.6"].has("pthread_attr_getaffinity_np", "cdecl"):
    pthread_attr_getaffinity_np = _libs["libc.so.6"].get("pthread_attr_getaffinity_np", "cdecl")
    pthread_attr_getaffinity_np.argtypes = [POINTER(pthread_attr_t), c_size_t, POINTER(cpu_set_t)]
    pthread_attr_getaffinity_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1676
if _libs["libc.so.6"].has("pthread_getattr_default_np", "cdecl"):
    pthread_getattr_default_np = _libs["libc.so.6"].get("pthread_getattr_default_np", "cdecl")
    pthread_getattr_default_np.argtypes = [POINTER(pthread_attr_t)]
    pthread_getattr_default_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1678
if _libs["libc.so.6"].has("pthread_attr_setsigmask_np", "cdecl"):
    pthread_attr_setsigmask_np = _libs["libc.so.6"].get("pthread_attr_setsigmask_np", "cdecl")
    pthread_attr_setsigmask_np.argtypes = [POINTER(pthread_attr_t), POINTER(__sigset_t)]
    pthread_attr_setsigmask_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1680
if _libs["libc.so.6"].has("pthread_attr_getsigmask_np", "cdecl"):
    pthread_attr_getsigmask_np = _libs["libc.so.6"].get("pthread_attr_getsigmask_np", "cdecl")
    pthread_attr_getsigmask_np.argtypes = [POINTER(pthread_attr_t), POINTER(__sigset_t)]
    pthread_attr_getsigmask_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1682
if _libs["libc.so.6"].has("pthread_setattr_default_np", "cdecl"):
    pthread_setattr_default_np = _libs["libc.so.6"].get("pthread_setattr_default_np", "cdecl")
    pthread_setattr_default_np.argtypes = [POINTER(pthread_attr_t)]
    pthread_setattr_default_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1684
if _libs["libc.so.6"].has("pthread_getattr_np", "cdecl"):
    pthread_getattr_np = _libs["libc.so.6"].get("pthread_getattr_np", "cdecl")
    pthread_getattr_np.argtypes = [pthread_t, POINTER(pthread_attr_t)]
    pthread_getattr_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1686
if _libs["libc.so.6"].has("pthread_setschedparam", "cdecl"):
    pthread_setschedparam = _libs["libc.so.6"].get("pthread_setschedparam", "cdecl")
    pthread_setschedparam.argtypes = [pthread_t, c_int, POINTER(struct_sched_param)]
    pthread_setschedparam.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1689
if _libs["libc.so.6"].has("pthread_getschedparam", "cdecl"):
    pthread_getschedparam = _libs["libc.so.6"].get("pthread_getschedparam", "cdecl")
    pthread_getschedparam.argtypes = [pthread_t, POINTER(c_int), POINTER(struct_sched_param)]
    pthread_getschedparam.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1693
if _libs["libc.so.6"].has("pthread_setschedprio", "cdecl"):
    pthread_setschedprio = _libs["libc.so.6"].get("pthread_setschedprio", "cdecl")
    pthread_setschedprio.argtypes = [pthread_t, c_int]
    pthread_setschedprio.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1695
if _libs["libc.so.6"].has("pthread_getname_np", "cdecl"):
    pthread_getname_np = _libs["libc.so.6"].get("pthread_getname_np", "cdecl")
    pthread_getname_np.argtypes = [pthread_t, String, c_size_t]
    pthread_getname_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1698
if _libs["libc.so.6"].has("pthread_setname_np", "cdecl"):
    pthread_setname_np = _libs["libc.so.6"].get("pthread_setname_np", "cdecl")
    pthread_setname_np.argtypes = [pthread_t, String]
    pthread_setname_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1700
if _libs["libc.so.6"].has("pthread_getconcurrency", "cdecl"):
    pthread_getconcurrency = _libs["libc.so.6"].get("pthread_getconcurrency", "cdecl")
    pthread_getconcurrency.argtypes = []
    pthread_getconcurrency.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1701
if _libs["libc.so.6"].has("pthread_setconcurrency", "cdecl"):
    pthread_setconcurrency = _libs["libc.so.6"].get("pthread_setconcurrency", "cdecl")
    pthread_setconcurrency.argtypes = [c_int]
    pthread_setconcurrency.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1702
for _lib in _libs.values():
    if not _lib.has("pthread_yield", "cdecl"):
        continue
    pthread_yield = _lib.get("pthread_yield", "cdecl")
    pthread_yield.argtypes = []
    pthread_yield.restype = c_int
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1703
for _lib in _libs.values():
    if not _lib.has("pthread_yield", "cdecl"):
        continue
    pthread_yield = _lib.get("pthread_yield", "cdecl")
    pthread_yield.argtypes = []
    pthread_yield.restype = c_int
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1705
if _libs["libc.so.6"].has("pthread_setaffinity_np", "cdecl"):
    pthread_setaffinity_np = _libs["libc.so.6"].get("pthread_setaffinity_np", "cdecl")
    pthread_setaffinity_np.argtypes = [pthread_t, c_size_t, POINTER(cpu_set_t)]
    pthread_setaffinity_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1708
if _libs["libc.so.6"].has("pthread_getaffinity_np", "cdecl"):
    pthread_getaffinity_np = _libs["libc.so.6"].get("pthread_getaffinity_np", "cdecl")
    pthread_getaffinity_np.argtypes = [pthread_t, c_size_t, POINTER(cpu_set_t)]
    pthread_getaffinity_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1711
if _libs["libc.so.6"].has("pthread_once", "cdecl"):
    pthread_once = _libs["libc.so.6"].get("pthread_once", "cdecl")
    pthread_once.argtypes = [POINTER(pthread_once_t), CFUNCTYPE(UNCHECKED(None), )]
    pthread_once.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1713
if _libs["libc.so.6"].has("pthread_setcancelstate", "cdecl"):
    pthread_setcancelstate = _libs["libc.so.6"].get("pthread_setcancelstate", "cdecl")
    pthread_setcancelstate.argtypes = [c_int, POINTER(c_int)]
    pthread_setcancelstate.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1714
if _libs["libc.so.6"].has("pthread_setcanceltype", "cdecl"):
    pthread_setcanceltype = _libs["libc.so.6"].get("pthread_setcanceltype", "cdecl")
    pthread_setcanceltype.argtypes = [c_int, POINTER(c_int)]
    pthread_setcanceltype.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1715
if _libs["libc.so.6"].has("pthread_cancel", "cdecl"):
    pthread_cancel = _libs["libc.so.6"].get("pthread_cancel", "cdecl")
    pthread_cancel.argtypes = [pthread_t]
    pthread_cancel.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1716
if _libs["libc.so.6"].has("pthread_testcancel", "cdecl"):
    pthread_testcancel = _libs["libc.so.6"].get("pthread_testcancel", "cdecl")
    pthread_testcancel.argtypes = []
    pthread_testcancel.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1717
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

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1726
class struct_anon_74(Structure):
    pass

struct_anon_74.__slots__ = [
    '__cancel_jmp_buf',
    '__pad',
]
struct_anon_74._fields_ = [
    ('__cancel_jmp_buf', struct___cancel_jmp_buf_tag * int(1)),
    ('__pad', POINTER(None) * int(4)),
]

__pthread_unwind_buf_t = struct_anon_74# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1726

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1727
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

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1734
if _libs["libc.so.6"].has("__pthread_register_cancel", "cdecl"):
    __pthread_register_cancel = _libs["libc.so.6"].get("__pthread_register_cancel", "cdecl")
    __pthread_register_cancel.argtypes = [POINTER(__pthread_unwind_buf_t)]
    __pthread_register_cancel.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1736
if _libs["libc.so.6"].has("__pthread_unregister_cancel", "cdecl"):
    __pthread_unregister_cancel = _libs["libc.so.6"].get("__pthread_unregister_cancel", "cdecl")
    __pthread_unregister_cancel.argtypes = [POINTER(__pthread_unwind_buf_t)]
    __pthread_unregister_cancel.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1738
if _libs["libc.so.6"].has("__pthread_register_cancel_defer", "cdecl"):
    __pthread_register_cancel_defer = _libs["libc.so.6"].get("__pthread_register_cancel_defer", "cdecl")
    __pthread_register_cancel_defer.argtypes = [POINTER(__pthread_unwind_buf_t)]
    __pthread_register_cancel_defer.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1740
if _libs["libc.so.6"].has("__pthread_unregister_cancel_restore", "cdecl"):
    __pthread_unregister_cancel_restore = _libs["libc.so.6"].get("__pthread_unregister_cancel_restore", "cdecl")
    __pthread_unregister_cancel_restore.argtypes = [POINTER(__pthread_unwind_buf_t)]
    __pthread_unregister_cancel_restore.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1742
if _libs["libc.so.6"].has("__pthread_unwind_next", "cdecl"):
    __pthread_unwind_next = _libs["libc.so.6"].get("__pthread_unwind_next", "cdecl")
    __pthread_unwind_next.argtypes = [POINTER(__pthread_unwind_buf_t)]
    __pthread_unwind_next.restype = None

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1744
if _libs["libc.so.6"].has("__sigsetjmp", "cdecl"):
    __sigsetjmp = _libs["libc.so.6"].get("__sigsetjmp", "cdecl")
    __sigsetjmp.argtypes = [struct___jmp_buf_tag * int(1), c_int]
    __sigsetjmp.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1746
if _libs["libc.so.6"].has("pthread_mutex_init", "cdecl"):
    pthread_mutex_init = _libs["libc.so.6"].get("pthread_mutex_init", "cdecl")
    pthread_mutex_init.argtypes = [POINTER(pthread_mutex_t), POINTER(pthread_mutexattr_t)]
    pthread_mutex_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1749
if _libs["libc.so.6"].has("pthread_mutex_destroy", "cdecl"):
    pthread_mutex_destroy = _libs["libc.so.6"].get("pthread_mutex_destroy", "cdecl")
    pthread_mutex_destroy.argtypes = [POINTER(pthread_mutex_t)]
    pthread_mutex_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1751
if _libs["libc.so.6"].has("pthread_mutex_trylock", "cdecl"):
    pthread_mutex_trylock = _libs["libc.so.6"].get("pthread_mutex_trylock", "cdecl")
    pthread_mutex_trylock.argtypes = [POINTER(pthread_mutex_t)]
    pthread_mutex_trylock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1753
if _libs["libc.so.6"].has("pthread_mutex_lock", "cdecl"):
    pthread_mutex_lock = _libs["libc.so.6"].get("pthread_mutex_lock", "cdecl")
    pthread_mutex_lock.argtypes = [POINTER(pthread_mutex_t)]
    pthread_mutex_lock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1755
if _libs["libc.so.6"].has("pthread_mutex_timedlock", "cdecl"):
    pthread_mutex_timedlock = _libs["libc.so.6"].get("pthread_mutex_timedlock", "cdecl")
    pthread_mutex_timedlock.argtypes = [POINTER(pthread_mutex_t), POINTER(struct_timespec)]
    pthread_mutex_timedlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1758
if _libs["libc.so.6"].has("pthread_mutex_clocklock", "cdecl"):
    pthread_mutex_clocklock = _libs["libc.so.6"].get("pthread_mutex_clocklock", "cdecl")
    pthread_mutex_clocklock.argtypes = [POINTER(pthread_mutex_t), clockid_t, POINTER(struct_timespec)]
    pthread_mutex_clocklock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1762
if _libs["libc.so.6"].has("pthread_mutex_unlock", "cdecl"):
    pthread_mutex_unlock = _libs["libc.so.6"].get("pthread_mutex_unlock", "cdecl")
    pthread_mutex_unlock.argtypes = [POINTER(pthread_mutex_t)]
    pthread_mutex_unlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1764
if _libs["libc.so.6"].has("pthread_mutex_getprioceiling", "cdecl"):
    pthread_mutex_getprioceiling = _libs["libc.so.6"].get("pthread_mutex_getprioceiling", "cdecl")
    pthread_mutex_getprioceiling.argtypes = [POINTER(pthread_mutex_t), POINTER(c_int)]
    pthread_mutex_getprioceiling.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1768
if _libs["libc.so.6"].has("pthread_mutex_setprioceiling", "cdecl"):
    pthread_mutex_setprioceiling = _libs["libc.so.6"].get("pthread_mutex_setprioceiling", "cdecl")
    pthread_mutex_setprioceiling.argtypes = [POINTER(pthread_mutex_t), c_int, POINTER(c_int)]
    pthread_mutex_setprioceiling.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1772
if _libs["libc.so.6"].has("pthread_mutex_consistent", "cdecl"):
    pthread_mutex_consistent = _libs["libc.so.6"].get("pthread_mutex_consistent", "cdecl")
    pthread_mutex_consistent.argtypes = [POINTER(pthread_mutex_t)]
    pthread_mutex_consistent.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1774
for _lib in _libs.values():
    if not _lib.has("pthread_mutex_consistent_np", "cdecl"):
        continue
    pthread_mutex_consistent_np = _lib.get("pthread_mutex_consistent_np", "cdecl")
    pthread_mutex_consistent_np.argtypes = [POINTER(pthread_mutex_t)]
    pthread_mutex_consistent_np.restype = c_int
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1776
if _libs["libc.so.6"].has("pthread_mutexattr_init", "cdecl"):
    pthread_mutexattr_init = _libs["libc.so.6"].get("pthread_mutexattr_init", "cdecl")
    pthread_mutexattr_init.argtypes = [POINTER(pthread_mutexattr_t)]
    pthread_mutexattr_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1778
if _libs["libc.so.6"].has("pthread_mutexattr_destroy", "cdecl"):
    pthread_mutexattr_destroy = _libs["libc.so.6"].get("pthread_mutexattr_destroy", "cdecl")
    pthread_mutexattr_destroy.argtypes = [POINTER(pthread_mutexattr_t)]
    pthread_mutexattr_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1780
if _libs["libc.so.6"].has("pthread_mutexattr_getpshared", "cdecl"):
    pthread_mutexattr_getpshared = _libs["libc.so.6"].get("pthread_mutexattr_getpshared", "cdecl")
    pthread_mutexattr_getpshared.argtypes = [POINTER(pthread_mutexattr_t), POINTER(c_int)]
    pthread_mutexattr_getpshared.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1784
if _libs["libc.so.6"].has("pthread_mutexattr_setpshared", "cdecl"):
    pthread_mutexattr_setpshared = _libs["libc.so.6"].get("pthread_mutexattr_setpshared", "cdecl")
    pthread_mutexattr_setpshared.argtypes = [POINTER(pthread_mutexattr_t), c_int]
    pthread_mutexattr_setpshared.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1787
if _libs["libc.so.6"].has("pthread_mutexattr_gettype", "cdecl"):
    pthread_mutexattr_gettype = _libs["libc.so.6"].get("pthread_mutexattr_gettype", "cdecl")
    pthread_mutexattr_gettype.argtypes = [POINTER(pthread_mutexattr_t), POINTER(c_int)]
    pthread_mutexattr_gettype.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1790
if _libs["libc.so.6"].has("pthread_mutexattr_settype", "cdecl"):
    pthread_mutexattr_settype = _libs["libc.so.6"].get("pthread_mutexattr_settype", "cdecl")
    pthread_mutexattr_settype.argtypes = [POINTER(pthread_mutexattr_t), c_int]
    pthread_mutexattr_settype.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1792
if _libs["libc.so.6"].has("pthread_mutexattr_getprotocol", "cdecl"):
    pthread_mutexattr_getprotocol = _libs["libc.so.6"].get("pthread_mutexattr_getprotocol", "cdecl")
    pthread_mutexattr_getprotocol.argtypes = [POINTER(pthread_mutexattr_t), POINTER(c_int)]
    pthread_mutexattr_getprotocol.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1796
if _libs["libc.so.6"].has("pthread_mutexattr_setprotocol", "cdecl"):
    pthread_mutexattr_setprotocol = _libs["libc.so.6"].get("pthread_mutexattr_setprotocol", "cdecl")
    pthread_mutexattr_setprotocol.argtypes = [POINTER(pthread_mutexattr_t), c_int]
    pthread_mutexattr_setprotocol.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1799
if _libs["libc.so.6"].has("pthread_mutexattr_getprioceiling", "cdecl"):
    pthread_mutexattr_getprioceiling = _libs["libc.so.6"].get("pthread_mutexattr_getprioceiling", "cdecl")
    pthread_mutexattr_getprioceiling.argtypes = [POINTER(pthread_mutexattr_t), POINTER(c_int)]
    pthread_mutexattr_getprioceiling.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1803
if _libs["libc.so.6"].has("pthread_mutexattr_setprioceiling", "cdecl"):
    pthread_mutexattr_setprioceiling = _libs["libc.so.6"].get("pthread_mutexattr_setprioceiling", "cdecl")
    pthread_mutexattr_setprioceiling.argtypes = [POINTER(pthread_mutexattr_t), c_int]
    pthread_mutexattr_setprioceiling.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1806
if _libs["libc.so.6"].has("pthread_mutexattr_getrobust", "cdecl"):
    pthread_mutexattr_getrobust = _libs["libc.so.6"].get("pthread_mutexattr_getrobust", "cdecl")
    pthread_mutexattr_getrobust.argtypes = [POINTER(pthread_mutexattr_t), POINTER(c_int)]
    pthread_mutexattr_getrobust.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1809
for _lib in _libs.values():
    if not _lib.has("pthread_mutexattr_getrobust_np", "cdecl"):
        continue
    pthread_mutexattr_getrobust_np = _lib.get("pthread_mutexattr_getrobust_np", "cdecl")
    pthread_mutexattr_getrobust_np.argtypes = [POINTER(pthread_mutexattr_t), POINTER(c_int)]
    pthread_mutexattr_getrobust_np.restype = c_int
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1811
if _libs["libc.so.6"].has("pthread_mutexattr_setrobust", "cdecl"):
    pthread_mutexattr_setrobust = _libs["libc.so.6"].get("pthread_mutexattr_setrobust", "cdecl")
    pthread_mutexattr_setrobust.argtypes = [POINTER(pthread_mutexattr_t), c_int]
    pthread_mutexattr_setrobust.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1814
for _lib in _libs.values():
    if not _lib.has("pthread_mutexattr_setrobust_np", "cdecl"):
        continue
    pthread_mutexattr_setrobust_np = _lib.get("pthread_mutexattr_setrobust_np", "cdecl")
    pthread_mutexattr_setrobust_np.argtypes = [POINTER(pthread_mutexattr_t), c_int]
    pthread_mutexattr_setrobust_np.restype = c_int
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1816
if _libs["libc.so.6"].has("pthread_rwlock_init", "cdecl"):
    pthread_rwlock_init = _libs["libc.so.6"].get("pthread_rwlock_init", "cdecl")
    pthread_rwlock_init.argtypes = [POINTER(pthread_rwlock_t), POINTER(pthread_rwlockattr_t)]
    pthread_rwlock_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1819
if _libs["libc.so.6"].has("pthread_rwlock_destroy", "cdecl"):
    pthread_rwlock_destroy = _libs["libc.so.6"].get("pthread_rwlock_destroy", "cdecl")
    pthread_rwlock_destroy.argtypes = [POINTER(pthread_rwlock_t)]
    pthread_rwlock_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1821
if _libs["libc.so.6"].has("pthread_rwlock_rdlock", "cdecl"):
    pthread_rwlock_rdlock = _libs["libc.so.6"].get("pthread_rwlock_rdlock", "cdecl")
    pthread_rwlock_rdlock.argtypes = [POINTER(pthread_rwlock_t)]
    pthread_rwlock_rdlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1823
if _libs["libc.so.6"].has("pthread_rwlock_tryrdlock", "cdecl"):
    pthread_rwlock_tryrdlock = _libs["libc.so.6"].get("pthread_rwlock_tryrdlock", "cdecl")
    pthread_rwlock_tryrdlock.argtypes = [POINTER(pthread_rwlock_t)]
    pthread_rwlock_tryrdlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1825
if _libs["libc.so.6"].has("pthread_rwlock_timedrdlock", "cdecl"):
    pthread_rwlock_timedrdlock = _libs["libc.so.6"].get("pthread_rwlock_timedrdlock", "cdecl")
    pthread_rwlock_timedrdlock.argtypes = [POINTER(pthread_rwlock_t), POINTER(struct_timespec)]
    pthread_rwlock_timedrdlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1828
if _libs["libc.so.6"].has("pthread_rwlock_clockrdlock", "cdecl"):
    pthread_rwlock_clockrdlock = _libs["libc.so.6"].get("pthread_rwlock_clockrdlock", "cdecl")
    pthread_rwlock_clockrdlock.argtypes = [POINTER(pthread_rwlock_t), clockid_t, POINTER(struct_timespec)]
    pthread_rwlock_clockrdlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1832
if _libs["libc.so.6"].has("pthread_rwlock_wrlock", "cdecl"):
    pthread_rwlock_wrlock = _libs["libc.so.6"].get("pthread_rwlock_wrlock", "cdecl")
    pthread_rwlock_wrlock.argtypes = [POINTER(pthread_rwlock_t)]
    pthread_rwlock_wrlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1834
if _libs["libc.so.6"].has("pthread_rwlock_trywrlock", "cdecl"):
    pthread_rwlock_trywrlock = _libs["libc.so.6"].get("pthread_rwlock_trywrlock", "cdecl")
    pthread_rwlock_trywrlock.argtypes = [POINTER(pthread_rwlock_t)]
    pthread_rwlock_trywrlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1836
if _libs["libc.so.6"].has("pthread_rwlock_timedwrlock", "cdecl"):
    pthread_rwlock_timedwrlock = _libs["libc.so.6"].get("pthread_rwlock_timedwrlock", "cdecl")
    pthread_rwlock_timedwrlock.argtypes = [POINTER(pthread_rwlock_t), POINTER(struct_timespec)]
    pthread_rwlock_timedwrlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1839
if _libs["libc.so.6"].has("pthread_rwlock_clockwrlock", "cdecl"):
    pthread_rwlock_clockwrlock = _libs["libc.so.6"].get("pthread_rwlock_clockwrlock", "cdecl")
    pthread_rwlock_clockwrlock.argtypes = [POINTER(pthread_rwlock_t), clockid_t, POINTER(struct_timespec)]
    pthread_rwlock_clockwrlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1843
if _libs["libc.so.6"].has("pthread_rwlock_unlock", "cdecl"):
    pthread_rwlock_unlock = _libs["libc.so.6"].get("pthread_rwlock_unlock", "cdecl")
    pthread_rwlock_unlock.argtypes = [POINTER(pthread_rwlock_t)]
    pthread_rwlock_unlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1845
if _libs["libc.so.6"].has("pthread_rwlockattr_init", "cdecl"):
    pthread_rwlockattr_init = _libs["libc.so.6"].get("pthread_rwlockattr_init", "cdecl")
    pthread_rwlockattr_init.argtypes = [POINTER(pthread_rwlockattr_t)]
    pthread_rwlockattr_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1847
if _libs["libc.so.6"].has("pthread_rwlockattr_destroy", "cdecl"):
    pthread_rwlockattr_destroy = _libs["libc.so.6"].get("pthread_rwlockattr_destroy", "cdecl")
    pthread_rwlockattr_destroy.argtypes = [POINTER(pthread_rwlockattr_t)]
    pthread_rwlockattr_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1849
if _libs["libc.so.6"].has("pthread_rwlockattr_getpshared", "cdecl"):
    pthread_rwlockattr_getpshared = _libs["libc.so.6"].get("pthread_rwlockattr_getpshared", "cdecl")
    pthread_rwlockattr_getpshared.argtypes = [POINTER(pthread_rwlockattr_t), POINTER(c_int)]
    pthread_rwlockattr_getpshared.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1853
if _libs["libc.so.6"].has("pthread_rwlockattr_setpshared", "cdecl"):
    pthread_rwlockattr_setpshared = _libs["libc.so.6"].get("pthread_rwlockattr_setpshared", "cdecl")
    pthread_rwlockattr_setpshared.argtypes = [POINTER(pthread_rwlockattr_t), c_int]
    pthread_rwlockattr_setpshared.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1856
if _libs["libc.so.6"].has("pthread_rwlockattr_getkind_np", "cdecl"):
    pthread_rwlockattr_getkind_np = _libs["libc.so.6"].get("pthread_rwlockattr_getkind_np", "cdecl")
    pthread_rwlockattr_getkind_np.argtypes = [POINTER(pthread_rwlockattr_t), POINTER(c_int)]
    pthread_rwlockattr_getkind_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1860
if _libs["libc.so.6"].has("pthread_rwlockattr_setkind_np", "cdecl"):
    pthread_rwlockattr_setkind_np = _libs["libc.so.6"].get("pthread_rwlockattr_setkind_np", "cdecl")
    pthread_rwlockattr_setkind_np.argtypes = [POINTER(pthread_rwlockattr_t), c_int]
    pthread_rwlockattr_setkind_np.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1862
if _libs["libc.so.6"].has("pthread_cond_init", "cdecl"):
    pthread_cond_init = _libs["libc.so.6"].get("pthread_cond_init", "cdecl")
    pthread_cond_init.argtypes = [POINTER(pthread_cond_t), POINTER(pthread_condattr_t)]
    pthread_cond_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1865
if _libs["libc.so.6"].has("pthread_cond_destroy", "cdecl"):
    pthread_cond_destroy = _libs["libc.so.6"].get("pthread_cond_destroy", "cdecl")
    pthread_cond_destroy.argtypes = [POINTER(pthread_cond_t)]
    pthread_cond_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1867
if _libs["libc.so.6"].has("pthread_cond_signal", "cdecl"):
    pthread_cond_signal = _libs["libc.so.6"].get("pthread_cond_signal", "cdecl")
    pthread_cond_signal.argtypes = [POINTER(pthread_cond_t)]
    pthread_cond_signal.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1869
if _libs["libc.so.6"].has("pthread_cond_broadcast", "cdecl"):
    pthread_cond_broadcast = _libs["libc.so.6"].get("pthread_cond_broadcast", "cdecl")
    pthread_cond_broadcast.argtypes = [POINTER(pthread_cond_t)]
    pthread_cond_broadcast.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1871
if _libs["libc.so.6"].has("pthread_cond_wait", "cdecl"):
    pthread_cond_wait = _libs["libc.so.6"].get("pthread_cond_wait", "cdecl")
    pthread_cond_wait.argtypes = [POINTER(pthread_cond_t), POINTER(pthread_mutex_t)]
    pthread_cond_wait.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1874
if _libs["libc.so.6"].has("pthread_cond_timedwait", "cdecl"):
    pthread_cond_timedwait = _libs["libc.so.6"].get("pthread_cond_timedwait", "cdecl")
    pthread_cond_timedwait.argtypes = [POINTER(pthread_cond_t), POINTER(pthread_mutex_t), POINTER(struct_timespec)]
    pthread_cond_timedwait.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1878
if _libs["libc.so.6"].has("pthread_cond_clockwait", "cdecl"):
    pthread_cond_clockwait = _libs["libc.so.6"].get("pthread_cond_clockwait", "cdecl")
    pthread_cond_clockwait.argtypes = [POINTER(pthread_cond_t), POINTER(pthread_mutex_t), __clockid_t, POINTER(struct_timespec)]
    pthread_cond_clockwait.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1883
if _libs["libc.so.6"].has("pthread_condattr_init", "cdecl"):
    pthread_condattr_init = _libs["libc.so.6"].get("pthread_condattr_init", "cdecl")
    pthread_condattr_init.argtypes = [POINTER(pthread_condattr_t)]
    pthread_condattr_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1885
if _libs["libc.so.6"].has("pthread_condattr_destroy", "cdecl"):
    pthread_condattr_destroy = _libs["libc.so.6"].get("pthread_condattr_destroy", "cdecl")
    pthread_condattr_destroy.argtypes = [POINTER(pthread_condattr_t)]
    pthread_condattr_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1887
if _libs["libc.so.6"].has("pthread_condattr_getpshared", "cdecl"):
    pthread_condattr_getpshared = _libs["libc.so.6"].get("pthread_condattr_getpshared", "cdecl")
    pthread_condattr_getpshared.argtypes = [POINTER(pthread_condattr_t), POINTER(c_int)]
    pthread_condattr_getpshared.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1891
if _libs["libc.so.6"].has("pthread_condattr_setpshared", "cdecl"):
    pthread_condattr_setpshared = _libs["libc.so.6"].get("pthread_condattr_setpshared", "cdecl")
    pthread_condattr_setpshared.argtypes = [POINTER(pthread_condattr_t), c_int]
    pthread_condattr_setpshared.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1893
if _libs["libc.so.6"].has("pthread_condattr_getclock", "cdecl"):
    pthread_condattr_getclock = _libs["libc.so.6"].get("pthread_condattr_getclock", "cdecl")
    pthread_condattr_getclock.argtypes = [POINTER(pthread_condattr_t), POINTER(__clockid_t)]
    pthread_condattr_getclock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1897
if _libs["libc.so.6"].has("pthread_condattr_setclock", "cdecl"):
    pthread_condattr_setclock = _libs["libc.so.6"].get("pthread_condattr_setclock", "cdecl")
    pthread_condattr_setclock.argtypes = [POINTER(pthread_condattr_t), __clockid_t]
    pthread_condattr_setclock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1900
if _libs["libc.so.6"].has("pthread_spin_init", "cdecl"):
    pthread_spin_init = _libs["libc.so.6"].get("pthread_spin_init", "cdecl")
    pthread_spin_init.argtypes = [POINTER(pthread_spinlock_t), c_int]
    pthread_spin_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1902
if _libs["libc.so.6"].has("pthread_spin_destroy", "cdecl"):
    pthread_spin_destroy = _libs["libc.so.6"].get("pthread_spin_destroy", "cdecl")
    pthread_spin_destroy.argtypes = [POINTER(pthread_spinlock_t)]
    pthread_spin_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1904
if _libs["libc.so.6"].has("pthread_spin_lock", "cdecl"):
    pthread_spin_lock = _libs["libc.so.6"].get("pthread_spin_lock", "cdecl")
    pthread_spin_lock.argtypes = [POINTER(pthread_spinlock_t)]
    pthread_spin_lock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1906
if _libs["libc.so.6"].has("pthread_spin_trylock", "cdecl"):
    pthread_spin_trylock = _libs["libc.so.6"].get("pthread_spin_trylock", "cdecl")
    pthread_spin_trylock.argtypes = [POINTER(pthread_spinlock_t)]
    pthread_spin_trylock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1908
if _libs["libc.so.6"].has("pthread_spin_unlock", "cdecl"):
    pthread_spin_unlock = _libs["libc.so.6"].get("pthread_spin_unlock", "cdecl")
    pthread_spin_unlock.argtypes = [POINTER(pthread_spinlock_t)]
    pthread_spin_unlock.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1910
if _libs["libc.so.6"].has("pthread_barrier_init", "cdecl"):
    pthread_barrier_init = _libs["libc.so.6"].get("pthread_barrier_init", "cdecl")
    pthread_barrier_init.argtypes = [POINTER(pthread_barrier_t), POINTER(pthread_barrierattr_t), c_uint]
    pthread_barrier_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1914
if _libs["libc.so.6"].has("pthread_barrier_destroy", "cdecl"):
    pthread_barrier_destroy = _libs["libc.so.6"].get("pthread_barrier_destroy", "cdecl")
    pthread_barrier_destroy.argtypes = [POINTER(pthread_barrier_t)]
    pthread_barrier_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1916
if _libs["libc.so.6"].has("pthread_barrier_wait", "cdecl"):
    pthread_barrier_wait = _libs["libc.so.6"].get("pthread_barrier_wait", "cdecl")
    pthread_barrier_wait.argtypes = [POINTER(pthread_barrier_t)]
    pthread_barrier_wait.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1918
if _libs["libc.so.6"].has("pthread_barrierattr_init", "cdecl"):
    pthread_barrierattr_init = _libs["libc.so.6"].get("pthread_barrierattr_init", "cdecl")
    pthread_barrierattr_init.argtypes = [POINTER(pthread_barrierattr_t)]
    pthread_barrierattr_init.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1920
if _libs["libc.so.6"].has("pthread_barrierattr_destroy", "cdecl"):
    pthread_barrierattr_destroy = _libs["libc.so.6"].get("pthread_barrierattr_destroy", "cdecl")
    pthread_barrierattr_destroy.argtypes = [POINTER(pthread_barrierattr_t)]
    pthread_barrierattr_destroy.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1922
if _libs["libc.so.6"].has("pthread_barrierattr_getpshared", "cdecl"):
    pthread_barrierattr_getpshared = _libs["libc.so.6"].get("pthread_barrierattr_getpshared", "cdecl")
    pthread_barrierattr_getpshared.argtypes = [POINTER(pthread_barrierattr_t), POINTER(c_int)]
    pthread_barrierattr_getpshared.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1926
if _libs["libc.so.6"].has("pthread_barrierattr_setpshared", "cdecl"):
    pthread_barrierattr_setpshared = _libs["libc.so.6"].get("pthread_barrierattr_setpshared", "cdecl")
    pthread_barrierattr_setpshared.argtypes = [POINTER(pthread_barrierattr_t), c_int]
    pthread_barrierattr_setpshared.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1929
if _libs["libc.so.6"].has("pthread_key_create", "cdecl"):
    pthread_key_create = _libs["libc.so.6"].get("pthread_key_create", "cdecl")
    pthread_key_create.argtypes = [POINTER(pthread_key_t), CFUNCTYPE(UNCHECKED(None), POINTER(None))]
    pthread_key_create.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1932
if _libs["libc.so.6"].has("pthread_key_delete", "cdecl"):
    pthread_key_delete = _libs["libc.so.6"].get("pthread_key_delete", "cdecl")
    pthread_key_delete.argtypes = [pthread_key_t]
    pthread_key_delete.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1933
if _libs["libc.so.6"].has("pthread_getspecific", "cdecl"):
    pthread_getspecific = _libs["libc.so.6"].get("pthread_getspecific", "cdecl")
    pthread_getspecific.argtypes = [pthread_key_t]
    pthread_getspecific.restype = POINTER(c_ubyte)
    pthread_getspecific.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1934
if _libs["libc.so.6"].has("pthread_setspecific", "cdecl"):
    pthread_setspecific = _libs["libc.so.6"].get("pthread_setspecific", "cdecl")
    pthread_setspecific.argtypes = [pthread_key_t, POINTER(None)]
    pthread_setspecific.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1937
if _libs["libc.so.6"].has("pthread_getcpuclockid", "cdecl"):
    pthread_getcpuclockid = _libs["libc.so.6"].get("pthread_getcpuclockid", "cdecl")
    pthread_getcpuclockid.argtypes = [pthread_t, POINTER(__clockid_t)]
    pthread_getcpuclockid.restype = c_int

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1940
if _libs["libc.so.6"].has("pthread_gettid_np", "cdecl"):
    pthread_gettid_np = _libs["libc.so.6"].get("pthread_gettid_np", "cdecl")
    pthread_gettid_np.argtypes = [pthread_t]
    pthread_gettid_np.restype = pid_t

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1941
for _lib in _libs.values():
    if not _lib.has("pthread_atfork", "cdecl"):
        continue
    pthread_atfork = _lib.get("pthread_atfork", "cdecl")
    pthread_atfork.argtypes = [CFUNCTYPE(UNCHECKED(None), ), CFUNCTYPE(UNCHECKED(None), ), CFUNCTYPE(UNCHECKED(None), )]
    pthread_atfork.restype = c_int
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1965
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

jon_gui_state = struct_jon_gui_state# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1965

jon_gui_state_to_proto_ptr = CFUNCTYPE(UNCHECKED(c_ptrdiff_t), POINTER(uint8_t), POINTER(jon_gui_state))# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1966

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1968
for _lib in _libs.values():
    if not _lib.has("jon_gui_writer_init", "cdecl"):
        continue
    jon_gui_writer_init = _lib.get("jon_gui_writer_init", "cdecl")
    jon_gui_writer_init.argtypes = []
    jon_gui_writer_init.restype = c_bool
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1969
for _lib in _libs.values():
    if not _lib.has("jon_gui_writer_destroy", "cdecl"):
        continue
    jon_gui_writer_destroy = _lib.get("jon_gui_writer_destroy", "cdecl")
    jon_gui_writer_destroy.argtypes = []
    jon_gui_writer_destroy.restype = None
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1970
for _lib in _libs.values():
    if not _lib.has("jon_gui_reader_init", "cdecl"):
        continue
    jon_gui_reader_init = _lib.get("jon_gui_reader_init", "cdecl")
    jon_gui_reader_init.argtypes = []
    jon_gui_reader_init.restype = c_bool
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1971
for _lib in _libs.values():
    if not _lib.has("jon_gui_reader_destroy", "cdecl"):
        continue
    jon_gui_reader_destroy = _lib.get("jon_gui_reader_destroy", "cdecl")
    jon_gui_reader_destroy.argtypes = []
    jon_gui_reader_destroy.restype = None
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1972
for _lib in _libs.values():
    if not _lib.has("jon_gui_writer_write", "cdecl"):
        continue
    jon_gui_writer_write = _lib.get("jon_gui_writer_write", "cdecl")
    jon_gui_writer_write.argtypes = [POINTER(jon_gui_state), jon_gui_state_to_proto_ptr]
    jon_gui_writer_write.restype = None
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1974
for _lib in _libs.values():
    if not _lib.has("jon_gui_reader_read", "cdecl"):
        continue
    jon_gui_reader_read = _lib.get("jon_gui_reader_read", "cdecl")
    jon_gui_reader_read.argtypes = [POINTER(jon_gui_state)]
    jon_gui_reader_read.restype = None
    break

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1975
for _lib in _libs.values():
    if not _lib.has("jon_gui_data_make_default", "cdecl"):
        continue
    jon_gui_data_make_default = _lib.get("jon_gui_data_make_default", "cdecl")
    jon_gui_data_make_default.argtypes = []
    jon_gui_data_make_default.restype = jon_gui_state
    break

enum_anon_75 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1981

jon_gui_data_decr = (-1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1981

jon_gui_data_refresh = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1981

jon_gui_data_incr = 1# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1981

jon_gui_data_update_type = enum_anon_75# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1981

enum_anon_76 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1989

MSG_CAN_FRAME = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1989

MSG_STATE_UPDATE = 1# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1989

MSG_STATUS_UPDATE = 2# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1989

MSG_TEMP_UPDATE = 3# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1989

MessageType = enum_anon_76# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1989

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1995
class struct_anon_77(Structure):
    pass

struct_anon_77._pack_ = 1
struct_anon_77.__slots__ = [
    'frame_type',
    'can_id',
    'can_dlc',
    'data',
]
struct_anon_77._fields_ = [
    ('frame_type', uint8_t),
    ('can_id', uint32_t),
    ('can_dlc', uint8_t),
    ('data', uint8_t * int(64)),
]

CANFrameData = struct_anon_77# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1995

enum_anon_78 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2001

CAN_INTERFACE_UP = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2001

CAN_INTERFACE_DOWN = (CAN_INTERFACE_UP + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2001

CAN_INTERFACE_MISSING = (CAN_INTERFACE_DOWN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2001

CAN_INTERFACE_UNKNOWN = (CAN_INTERFACE_MISSING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2001

CANInterfaceState = enum_anon_78# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2001

enum_anon_79 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2012

CAN_OK = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2012

CAN_ERROR_SOCKET_INIT = (CAN_OK + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2012

CAN_ERROR_SOCKET_READ = (CAN_ERROR_SOCKET_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2012

CAN_ERROR_INVALID_INTERFACE = (CAN_ERROR_SOCKET_READ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2012

CAN_ERROR_BIND_FAILED = (CAN_ERROR_INVALID_INTERFACE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2012

CAN_ERROR_FD_MODE_FAILED = (CAN_ERROR_BIND_FAILED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2012

CAN_ERROR_INTERFACE_DOWN = (CAN_ERROR_FD_MODE_FAILED + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2012

CAN_ERROR_INTERFACE_MISSING = (CAN_ERROR_INTERFACE_DOWN + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2012

CAN_ERROR_RECONNECTING = (CAN_ERROR_INTERFACE_MISSING + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2012

CANErrorCode = enum_anon_79# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2012

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2024
class struct_anon_80(Structure):
    pass

struct_anon_80._pack_ = 1
struct_anon_80.__slots__ = [
    'connected',
    'error_code',
    'interface_state',
    'frames_received',
    'fd_frames_received',
    'invalid_frames',
    'reconnect_attempts',
    'last_frame',
    'last_reconnect_attempt',
    'interface_name',
]
struct_anon_80._fields_ = [
    ('connected', c_bool),
    ('error_code', CANErrorCode),
    ('interface_state', CANInterfaceState),
    ('frames_received', uint32_t),
    ('fd_frames_received', uint32_t),
    ('invalid_frames', uint32_t),
    ('reconnect_attempts', uint32_t),
    ('last_frame', time_t),
    ('last_reconnect_attempt', time_t),
    ('interface_name', c_char * int(64)),
]

CANHandlerStatus = struct_anon_80# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2024

enum_anon_81 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2029

STATE_OK = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2029

STATE_ERROR_SHM_INIT = (STATE_OK + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2029

STATE_ERROR_SHM_READ = (STATE_ERROR_SHM_INIT + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2029

StateErrorCode = enum_anon_81# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2029

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2039
class struct_anon_82(Structure):
    pass

struct_anon_82._pack_ = 1
struct_anon_82.__slots__ = [
    'connected',
    'error_code',
    'updates_received',
    'invalid_updates',
    'reconnect_attempts',
    'last_update',
    'last_error_time',
    'state_size',
]
struct_anon_82._fields_ = [
    ('connected', c_bool),
    ('error_code', StateErrorCode),
    ('updates_received', uint64_t),
    ('invalid_updates', uint64_t),
    ('reconnect_attempts', uint64_t),
    ('last_update', time_t),
    ('last_error_time', time_t),
    ('state_size', c_size_t),
]

StateHandlerStatus = struct_anon_82# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2039

enum_anon_83 = c_int# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2045

TEMP_OK = 0# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2045

TEMP_ERROR_SENSOR_READ = (TEMP_OK + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2045

TEMP_ERROR_SENSOR_OFFLINE = (TEMP_ERROR_SENSOR_READ + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2045

TEMP_ERROR_INVALID_DATA = (TEMP_ERROR_SENSOR_OFFLINE + 1)# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2045

TempErrorCode = enum_anon_83# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2045

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2051
class struct_anon_84(Structure):
    pass

struct_anon_84._pack_ = 1
struct_anon_84.__slots__ = [
    'name',
    'type',
    'temperature',
    'valid',
]
struct_anon_84._fields_ = [
    ('name', c_char * int(64)),
    ('type', c_char * int(64)),
    ('temperature', c_float),
    ('valid', c_bool),
]

TempSensorReading = struct_anon_84# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2051

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2061
class struct_anon_85(Structure):
    pass

struct_anon_85._pack_ = 1
struct_anon_85.__slots__ = [
    'connected',
    'error_code',
    'updates_received',
    'invalid_readings',
    'num_active_sensors',
    'last_update',
    'last_error_time',
    'readings',
]
struct_anon_85._fields_ = [
    ('connected', c_bool),
    ('error_code', TempErrorCode),
    ('updates_received', uint32_t),
    ('invalid_readings', uint32_t),
    ('num_active_sensors', uint32_t),
    ('last_update', time_t),
    ('last_error_time', time_t),
    ('readings', TempSensorReading * int(11)),
]

TempHandlerStatus = struct_anon_85# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2061

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2068
class struct_anon_86(Structure):
    pass

struct_anon_86._pack_ = 1
struct_anon_86.__slots__ = [
    'can_status',
    'state_status',
    'temp_status',
    'active_clients',
    'server_start_time',
]
struct_anon_86._fields_ = [
    ('can_status', CANHandlerStatus),
    ('state_status', StateHandlerStatus),
    ('temp_status', TempHandlerStatus),
    ('active_clients', uint32_t),
    ('server_start_time', time_t),
]

SystemStatus = struct_anon_86# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2068

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2074
class union_anon_87(Union):
    pass

union_anon_87._pack_ = 1
union_anon_87.__slots__ = [
    'can_data',
    'state_data',
    'temp_data',
    'system_status',
]
union_anon_87._fields_ = [
    ('can_data', CANFrameData),
    ('state_data', jon_gui_state),
    ('temp_data', TempHandlerStatus),
    ('system_status', SystemStatus),
]

MessageData = union_anon_87# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2074

# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2078
class struct_anon_88(Structure):
    pass

struct_anon_88._pack_ = 1
struct_anon_88.__slots__ = [
    'type',
    'data',
]
struct_anon_88._fields_ = [
    ('type', MessageType),
    ('data', MessageData),
]

Message = struct_anon_88# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 2078

timeval = struct_timeval# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 105

timex = struct_timex# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 110

tm = struct_tm# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 139

timespec = struct_timespec# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 153

itimerspec = struct_itimerspec# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 160

sigevent = struct_sigevent# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 165

__locale_data = struct___locale_data# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 169

__locale_struct = struct___locale_struct# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 167

__kernel_sockaddr_storage = struct___kernel_sockaddr_storage# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 305

can_frame = struct_can_frame# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 316

canfd_frame = struct_canfd_frame# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 327

canxl_frame = struct_canxl_frame# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 335

sockaddr_can = struct_sockaddr_can# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 343

can_filter = struct_can_filter# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 355

jon_gui_data_camera_alignment = struct_jon_gui_data_camera_alignment# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 432

jon_gui_data_colors_value = struct_jon_gui_data_colors_value# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 441

jon_gui_data_colors_menu = struct_jon_gui_data_colors_menu# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 447

jon_gui_data_colors_osd = struct_jon_gui_data_colors_osd# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 453

jon_gui_data_colors = struct_jon_gui_data_colors# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 458

jon_gui_data_component_meteo = struct_jon_gui_data_component_meteo# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 643

jon_gui_data_compass = struct_jon_gui_data_compass# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 707

jon_gui_data_compass_calibration = struct_jon_gui_data_compass_calibration# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 721

jon_gui_data_gps = struct_jon_gui_data_gps# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 791

jon_gui_data_header = struct_jon_gui_data_header# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 815

jon_gui_data_lens = struct_jon_gui_data_lens# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 875

jon_gui_data_lrf = struct_jon_gui_data_lrf# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 900

jon_gui_data_media = struct_jon_gui_data_media# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 906

jon_gui_data_meteo = struct_jon_gui_data_meteo# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 916

jon_gui_data_osd = struct_jon_gui_data_osd# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 942

jon_gui_data_rotary = struct_jon_gui_data_rotary# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 987

jon_gui_data_power_module_state = struct_jon_gui_data_power_module_state# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1003

jon_gui_data_power = struct_jon_gui_data_power# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1015

jon_gui_data_system = struct_jon_gui_data_system# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1083

jon_gui_data_target_spec = struct_jon_gui_data_target_spec# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1113

jon_gui_data_targets = struct_jon_gui_data_targets# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1127

jon_gui_data_time = struct_jon_gui_data_time# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1151

jon_gui_color_rgba8888 = union_jon_gui_color_rgba8888# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1189

jon_gui_tracking_point = union_jon_gui_tracking_point# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1199

jon_gui_tracking_quad = struct_jon_gui_tracking_quad# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1204

jon_gui_data_cv = struct_jon_gui_data_cv# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1217

__pthread_internal_list = struct___pthread_internal_list# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1362

__pthread_internal_slist = struct___pthread_internal_slist# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1367

__pthread_mutex_s = struct___pthread_mutex_s# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1371

__pthread_rwlock_arch_t = struct___pthread_rwlock_arch_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1382

__pthread_cond_s = struct___pthread_cond_s# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1397

pthread_attr_t = union_pthread_attr_t# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1427

sched_attr = struct_sched_attr# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1468

sched_param = struct_sched_param# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1480

__jmp_buf_tag = struct___jmp_buf_tag# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1519

_pthread_cleanup_buffer = struct__pthread_cleanup_buffer# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1580

__cancel_jmp_buf_tag = struct___cancel_jmp_buf_tag# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1717

__pthread_cleanup_frame = struct___pthread_cleanup_frame# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1727

jon_gui_state = struct_jon_gui_state# /home/jare/git/cc/jettison_6_2/scripts/factory/panopticon/src/bindings/preprocessed_lighthouse.h: 1965

# No inserted files

# Begin prefix-stripping

# Strip prefixes from all symbols following regular expression:
# (CAN_|STATE_)

import re as __re_module

__strip_expr = __re_module.compile('(CAN_|STATE_)')
for __k, __v in globals().copy().items():
    __m = __strip_expr.match(__k)
    if __m:
        globals()[__k[__m.end():]] = __v
        # remove symbol with prefix(?)
        # globals().pop(__k)
del __re_module, __k, __v, __m, __strip_expr

# End prefix-stripping

