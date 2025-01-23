include_directories(
  ${CMAKE_BINARY_DIR}
  ${CMAKE_CURRENT_BINARY_DIR}
  ${CMAKE_CURRENT_SOURCE_DIR}
)


##### write configure files

configure_file( art_config.h.cmake art_config.h @ONLY )
configure_file( libart-features.h.cmake libart-features.h @ONLY )


##### src

set( _SRCS art_affine.c art_alphagamma.c
           art_bpath.c art_gray_svp.c
           art_misc.c art_pixbuf.c
           art_rect.c art_rect_svp.c
           art_rect_uta.c art_render.c
           art_render_gradient.c art_render_mask.c
           art_render_svp.c art_rgb.c
           art_rgb_affine.c art_rgb_affine_private.c
           art_rgb_bitmap_affine.c art_rgb_pixbuf_affine.c
           art_rgb_rgba_affine.c art_rgb_a_affine.c
           art_rgba.c art_rgb_svp.c
           art_svp.c art_svp_intersect.c
           art_svp_ops.c art_svp_point.c
           art_svp_render_aa.c art_svp_vpath.c
           art_svp_vpath_stroke.c art_svp_wind.c
           art_uta.c art_uta_ops.c
           art_uta_rect.c art_uta_vpath.c
           art_uta_svp.c art_vpath.c
           art_vpath_bpath.c art_vpath_dash.c
           art_vpath_svp.c libart-features.c
)


## shared

tde_add_library( art_lgpl_2 SHARED

  SOURCES
        ${_SRCS}
  LINK
     ${MATH_LIBC}

  VERSION ${LIBART_VERSION}

  DESTINATION ${LIB_INSTALL_DIR}
)


## static

tde_add_library( art_lgpl_2 STATIC_PIC

  SOURCES
        ${_SRCS}
  LINK
     ${MATH_LIBC}

  VERSION ${LIBART_VERSION}

  DESTINATION ${LIB_INSTALL_DIR}
)


## tests

tde_add_check_executable( testart

    SOURCES
        testart.c

    LINK
        art_lgpl_2-shared
        ${MATH_LIBC}
)

add_test(
    NAME testart-testpat
    COMMAND testart testpat
)

#-- the testart-gradient often ends at sigsegv
#add_test(
#    NAME testart-gradient
#    COMMAND testart gradient
#)

add_test(
    NAME testart-dash
    COMMAND testart dash
)

add_test(
    NAME testart-dist
    COMMAND testart dist
)

add_test(
    NAME testart-intersect
    COMMAND testart intersect
)

tde_add_check_executable( testuta
    SOURCES
        testuta.c

    LINK
        art_lgpl_2-shared
        ${MATH_LIBC}

    TEST
)


##### Headers

set( _headers art_affine.h art_alphagamma.h
              art_bpath.h
              art_filterlevel.h art_gray_svp.h
              art_misc.h art_pathcode.h art_pixbuf.h
              art_point.h art_rect.h art_rect_svp.h
              art_rect_uta.h art_render.h
              art_render_gradient.h art_render_mask.h
              art_render_svp.h art_rgb.h
              art_rgb_affine.h art_rgb_bitmap_affine.h
              art_rgb_pixbuf_affine.h art_rgb_rgba_affine.h
              art_rgb_a_affine.h art_rgb_svp.h
              art_rgba.h art_svp.h
              art_svp_intersect.h art_svp_ops.h
              art_svp_point.h art_svp_render_aa.h
              art_svp_vpath.h art_svp_vpath_stroke.h
              art_svp_wind.h art_uta.h
              art_uta_ops.h art_uta_rect.h
              art_uta_vpath.h art_uta_svp.h
              art_vpath.h art_vpath_bpath.h
              art_vpath_dash.h art_vpath_svp.h
              libart.h
              ${CMAKE_CURRENT_BINARY_DIR}/art_config.h
              ${CMAKE_CURRENT_BINARY_DIR}/libart-features.h
)

install(
    FILES ${_headers}
    DESTINATION ${INCLUDE_INSTALL_DIR}/libart-2.0/libart_lgpl
)


#### pkg-config

set( prefix ${CMAKE_INSTALL_PREFIX} )
string( REGEX REPLACE "^${CMAKE_INSTALL_PREFIX}" "\${prefix}" exec_prefix ${EXEC_INSTALL_PREFIX} )
string( REGEX REPLACE "^${CMAKE_INSTALL_PREFIX}" "\${prefix}" includedir ${INCLUDE_INSTALL_DIR}  )
string( REGEX REPLACE "^${CMAKE_INSTALL_PREFIX}" "\${prefix}" libdir ${LIB_INSTALL_DIR}          )

configure_file( libart-2.0.pc.cmake  libart-2.0.pc  @ONLY )

install(
    FILES ${CMAKE_CURRENT_BINARY_DIR}/libart-2.0.pc
    DESTINATION ${PKGCONFIG_INSTALL_DIR}
)


##### config helper

install(
    PROGRAMS libart2-config
    DESTINATION ${BIN_INSTALL_DIR}
)
