############################################
#                                          #
#  Improvements and feedbacks are welcome  #
#                                          #
#  This file is released under GPL >= 3    #
#                                          #
############################################


##### set project version ########################

include( TDEVersion )
cmake_minimum_required( VERSION ${TDE_CMAKE_MINIMUM_VERSION} )
tde_set_project_version( )


#### general package setup

project( libart-lgpl )
set( LIBART_VERSION 2.3.21 )

string( REPLACE "." ";" LIBART_VERSION_LIST ${LIBART_VERSION} )
list( GET LIBART_VERSION_LIST 0 LIBART_MAJOR_VERSION )
list( GET LIBART_VERSION_LIST 1 LIBART_MINOR_VERSION )
list( GET LIBART_VERSION_LIST 2 LIBART_MICRO_VERSION )


#### include essential cmake modules

include( CheckFunctionExists    )
include( CheckSymbolExists      )
include( CheckIncludeFile       )
include( CheckLibraryExists     )
include( CheckCSourceCompiles   )


#### include our cmake modules

include( TDEMacros )


##### setup install paths

include( TDESetupPaths )
tde_setup_paths( )
enable_testing( )


##### optional stuff

option( WITH_ALL_OPTIONS    "Enable all optional support" OFF )
option( WITH_GCC_VISIBILITY "Enable fvisibility and fvisibility-inlines-hidden" ${WITH_ALL_OPTIONS} )


##### user requested modules

option( BUILD_ALL "Build all" ON )
option( BUILD_DOC "Build documentation" ${BUILD_ALL} )


##### configure checks

include( ConfigureChecks.cmake )


###### global compiler settings

add_definitions( -DHAVE_CONFIG_H -DLIBART_COMPILATION )

set( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TQT_CXX_FLAGS}" )
set( CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -Wl,--no-undefined" )
set( CMAKE_MODULE_LINKER_FLAGS "${CMAKE_MODULE_LINKER_FLAGS} -Wl,--no-undefined" )


##### directories

add_subdirectory( src )
tde_conditional_add_subdirectory( BUILD_DOC doc )


##### write configure files

configure_file( config.h.cmake config.h @ONLY )
