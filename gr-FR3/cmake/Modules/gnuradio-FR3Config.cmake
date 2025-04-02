find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_FR3 gnuradio-FR3)

FIND_PATH(
    GR_FR3_INCLUDE_DIRS
    NAMES gnuradio/FR3/api.h
    HINTS $ENV{FR3_DIR}/include
        ${PC_FR3_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_FR3_LIBRARIES
    NAMES gnuradio-FR3
    HINTS $ENV{FR3_DIR}/lib
        ${PC_FR3_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-FR3Target.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_FR3 DEFAULT_MSG GR_FR3_LIBRARIES GR_FR3_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_FR3_LIBRARIES GR_FR3_INCLUDE_DIRS)
