EXECUTE_PROCESS(COMMAND ${PYTHON_EXECUTABLE} -c
"from distutils.sysconfig import get_python_lib; import os; print(get_python_lib())"
OUTPUT_VARIABLE _PYTHON_INSTALL_DIR OUTPUT_STRIP_TRAILING_WHITESPACE )

string(REPLACE "\\" "/" PYTHON_INSTALL_DIR ${_PYTHON_INSTALL_DIR})


MESSAGE(STATUS "python-py${PYTHON_VERSION_MAJOR}${PYTHON_VERSION_MINOR}")
MESSAGE(STATUS "installing to ${python_libs}")

INCLUDE_DIRECTORIES( ${PYTHON_INCLUDE_DIRS})    # python.h

# Build the python shared library
# PYTHON_ADD_MODULE(parabem_cpp SHARED parabem_ext.cpp)
pybind11_add_module(parabem_cpp SHARED parabem_ext.cpp)
#set_target_properties(parabem_cpp PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/parabem)

#set_target_properties(parabem_cpp PROPERTIES PREFIX "")
# set_target_properties(parabem_cpp PROPERTIES INSTALL_RPATH ${CMAKE_INSTALL_PREFIX}/lib)
if( WIN32 )
    set_target_properties(parabem_cpp PROPERTIES SUFFIX ".pyd")
endif()

target_link_libraries(parabem_cpp PUBLIC pm)

install(DIRECTORY "../../parabem/" DESTINATION ${PYTHON_INSTALL_DIR}/parabem FILES_MATCHING PATTERN "*.py")
install(TARGETS parabem_cpp DESTINATION ${PYTHON_INSTALL_DIR})
