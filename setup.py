from distutils.core import setup, Extension
import os


def libs():
    import eigen
    libraries = set()
    libraries.add(os.path.dirname(eigen.__file__))
    return list(libraries)


def extra_link_args():
    return ['-lgomp']


include_dirs = ['/usr/include/eigen3',
                '/usr/local/include/eigen3']

src = ["src/ppm_ext.cpp",      "src/element_influence.cpp",
       "src/panel2.cpp",       "src/panel3.cpp",
       "src/case2.cpp",        "src/case3.cpp",
       "src/lifting_line.cpp"]

headers = ["src/element_influence.h",
           "src/vector.h",         "src/panel2.h",
           "src/panel3.h",         "src/case2.h",
           "src/case3.h",          "src/lifting_line.h"]

files = ["ppm", "ppm.airfoil", "ppm.liftingline", "ppm.mesh",
         "ppm.pan2d", "ppm.pan3d", "ppm.utils", "ppm.vtk_export"]


setup(name='ppm._ppm',
      version='0.0.1',
      author='Loooo',
      requires='eigen',
      author_email='sppedflyer@gmail.com',
      url="https://github.com/looooo/panelmethod",
      description='Wrap PM using pybind11',
      packages=files,
      ext_modules=[Extension('ppm._ppm',
                   sources=src,
                   # library_dirs=libs(),
                   # runtime_library_dirs=libs(),
                   include_dirs=include_dirs,
                   extra_compile_args=['-std=c++11', '-fopenmp'],
                   extra_link_args=extra_link_args())])
