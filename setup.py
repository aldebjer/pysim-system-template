import setuptools
from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy
import pysim.info
import os.path
import sys

config = Configuration()
config.add_include_dirs([pysim.info.get_include(), numpy.get_include()])

extracompileargs = []
if sys.platform == "win32":
    config.add_include_dirs([os.environ.get('BOOST_ROOT')])
elif sys.platform == "linux":
    extracompileargs.append("-std=c++11")


cpp_ex_dir = "pysim_system_template/systems/example_cpp_systems"
cpp_ex_files = os.listdir(cpp_ex_dir)
cpp_ex_files = filter(lambda x: x.endswith("cpp"),cpp_ex_files)
cpp_ex_files = [os.path.join(cpp_ex_dir,x) for x in cpp_ex_files]
cpp_ex_files.append("pysim_system_template/systems/example_cpp_systems.pyx")

extensions = [Extension("pysim_system_template.systems.example_cpp_systems",
                          cpp_ex_files,
                          language="c++",
                          extra_compile_args=extracompileargs,
                          include_dirs=[pysim.info.get_include(),
                                        cpp_ex_dir],
                          library_dirs=pysim.info.get_library_dir(),
                          libraries= pysim.info.get_libraries(),
                          ),
              Extension("pysim_system_template.systems.example_cython_systems",
                        ['pysim_system_template/systems/example_cython_systems.pyx'],
                        language="c++",
                        extra_compile_args=extracompileargs,
                        ),
             ]

setup(
    name="pysim-example-template",
    version="0.0.1dev1",
    ext_modules=cythonize(extensions),
    packages=['pysim_system_template.systems',
              'pysim_system_template.tests',
             ],
    install_requires = ['pysim>=2.0',
                        'numpy'
                       ],
    **config.todict()
)
