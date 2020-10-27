INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_MY_FHSS_V1 my_fhss_v1)

FIND_PATH(
    MY_FHSS_V1_INCLUDE_DIRS
    NAMES my_fhss_v1/api.h
    HINTS $ENV{MY_FHSS_V1_DIR}/include
        ${PC_MY_FHSS_V1_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    MY_FHSS_V1_LIBRARIES
    NAMES gnuradio-my_fhss_v1
    HINTS $ENV{MY_FHSS_V1_DIR}/lib
        ${PC_MY_FHSS_V1_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(MY_FHSS_V1 DEFAULT_MSG MY_FHSS_V1_LIBRARIES MY_FHSS_V1_INCLUDE_DIRS)
MARK_AS_ADVANCED(MY_FHSS_V1_LIBRARIES MY_FHSS_V1_INCLUDE_DIRS)

