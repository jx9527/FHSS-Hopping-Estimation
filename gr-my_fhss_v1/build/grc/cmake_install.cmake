# Install script for directory: /home/jx/Desktop/gr_origin/gr-my_fhss_v1/grc

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gnuradio/grc/blocks" TYPE FILE FILES
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/grc/my_fhss_v1_AM.xml"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/grc/my_fhss_v1_FM_mod.xml"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/grc/my_fhss_v1_FM_mod.xml"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/grc/my_fhss_v1_add_fhss_cc.xml"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/grc/my_fhss_v1_fhss_list_sink.xml"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/grc/my_fhss_v1_fhss_list_sink.xml"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/grc/my_fhss_v1_addlist_fhss_cc.xml"
    "/home/jx/Desktop/gr_origin/gr-my_fhss_v1/grc/my_fhss_v1_fhss_sink.xml"
    )
endif()

