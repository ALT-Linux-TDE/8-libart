prefix=@prefix@
exec_prefix=@exec_prefix@
libdir=@libdir@
includedir=@includedir@

Name: libart
Description: LGPL version of the libart library
Version: @LIBART_VERSION@
Libs: -L${libdir} -lart_lgpl_2
Cflags: -I${includedir}/libart-2.0
