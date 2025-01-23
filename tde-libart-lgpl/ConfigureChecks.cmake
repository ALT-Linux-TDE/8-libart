###########################################
#                                         #
#  Improvements and feedback are welcome  #
#                                         #
#  This file is released under GPL >= 3   #
#                                         #
###########################################

# required stuff
tde_setup_architecture_flags( )

include(TestBigEndian)
test_big_endian(WORDS_BIGENDIAN)

tde_setup_largefiles( )


##### check for gcc visibility support

if( WITH_GCC_VISIBILITY )
  tde_setup_gcc_visibility( )
endif( WITH_GCC_VISIBILITY )


##### check of type size

check_type_size( char  ART_SIZEOF_CHAR  )
check_type_size( short ART_SIZEOF_SHORT )
check_type_size( int   ART_SIZEOF_INT   )
check_type_size( long  ART_SIZEOF_LONG  )

if( ${ART_SIZEOF_CHAR} EQUAL 1 )
  set( ART_U8_TYPE "unsigned char" )
else( )
  tde_message_fatal( "sizeof(char) != 1" )
endif( )

if( ${ART_SIZEOF_SHORT} EQUAL 2 )
  set( ART_U16_TYPE "unsigned short" )
else( )
  tde_message_fatal( "sizeof(short) != 2" )
endif( )

if( ${ART_SIZEOF_INT} EQUAL 4 )
  set( ART_U32_TYPE "unsigned int" )
else( )
  if( ${ART_SIZEOF_LONG} EQUAL 4 )
    set( ART_U32_TYPE "unsigned long" )
  else( )
    tde_message_fatal( "sizeof(int) != 4 and sizeof(long) != 4" )
  endif( )
endif( )


##### check for the math libc

find_library( MATH_LIBC m )
