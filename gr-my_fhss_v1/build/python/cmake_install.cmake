# Install script for directory: /home/jx/Desktop/gr_origin/gr-my_fhss_v1/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/my_fhss_v1" TYPE FILE FILES
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/python/__init__.py"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/python/AM.py"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/python/FM_mod.py"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/python/FM_mod.py"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/python/add_fhss_cc.py"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/python/fhss_list_sink.py"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/python/fhss_list_sink.py"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/python/addlist_fhss_cc.py"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/python/fhss_sink.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/my_fhss_v1" TYPE FILE FILES
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/__init__.pyc"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/AM.pyc"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/FM_mod.pyc"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/FM_mod.pyc"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/add_fhss_cc.pyc"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/fhss_list_sink.pyc"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/fhss_list_sink.pyc"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/addlist_fhss_cc.pyc"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/fhss_sink.pyc"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/__init__.pyo"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/AM.pyo"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/FM_mod.pyo"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/FM_mod.pyo"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/add_fhss_cc.pyo"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/fhss_list_sink.pyo"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/fhss_list_sink.pyo"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/addlist_fhss_cc.pyo"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/build/python/fhss_sink.pyo"
    )
endif()

