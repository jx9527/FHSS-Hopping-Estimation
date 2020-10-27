# Copyright 2011,2012,2016 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})

list(APPEND my_fhss_v1_sources
)

set(my_fhss_v1_sources "${my_fhss_v1_sources}" PARENT_SCOPE)
if(NOT my_fhss_v1_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT my_fhss_v1_sources)

add_library(gnuradio-my_fhss_v1 SHARED ${my_fhss_v1_sources})
target_link_libraries(gnuradio-my_fhss_v1 ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-my_fhss_v1 PROPERTIES DEFINE_SYMBOL "gnuradio_my_fhss_v1_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-my_fhss_v1 PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
include(GrMiscUtils)
GR_LIBRARY_FOO(gnuradio-my_fhss_v1 RUNTIME_COMPONENT "my_fhss_v1_runtime" DEVEL_COMPONENT "my_fhss_v1_devel")

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_my_fhss_v1_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_my_fhss_v1.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_my_fhss_v1.cc
)

add_executable(test-my_fhss_v1 ${test_my_fhss_v1_sources})

target_link_libraries(
  test-my_fhss_v1
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-my_fhss_v1
)

GR_ADD_TEST(test_my_fhss_v1 test-my_fhss_v1)

########################################################################
# Print summary
########################################################################
message(STATUS "Using install prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "Building for version: ${VERSION} / ${LIBVER}")

