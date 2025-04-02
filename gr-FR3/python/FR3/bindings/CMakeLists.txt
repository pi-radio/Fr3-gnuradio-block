# Copyright 2020 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

########################################################################
# Check if there is C++ code at all
########################################################################
if(NOT FR3_sources)
    message(STATUS "No C++ sources... skipping python bindings")
    return()
endif(NOT FR3_sources)

########################################################################
# Check for pygccxml
########################################################################
gr_python_check_module_raw("pygccxml" "import pygccxml" PYGCCXML_FOUND)

include(GrPybind)

########################################################################
# Python Bindings
########################################################################

list(APPEND FR3_python_files python_bindings.cc)

gr_pybind_make_oot(FR3 ../../.. gr::FR3 "${FR3_python_files}")

# copy bindings extension for use in QA test module
add_custom_command(
    TARGET FR3_python
    POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:FR3_python>
            ${PROJECT_BINARY_DIR}/test_modules/gnuradio/FR3/)

install(
    TARGETS FR3_python
    DESTINATION ${GR_PYTHON_DIR}/gnuradio/FR3
    COMPONENT pythonapi)
