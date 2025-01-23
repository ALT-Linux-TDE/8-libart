
#ifndef _ART_CONFIG_H_
#define _ART_CONFIG_H_

#define ART_SIZEOF_CHAR  @ART_SIZEOF_CHAR@
#define ART_SIZEOF_SHORT @ART_SIZEOF_SHORT@
#define ART_SIZEOF_INT   @ART_SIZEOF_INT@
#define ART_SIZEOF_LONG  @ART_SIZEOF_LONG@

typedef @ART_U8_TYPE@ art_u8;
typedef @ART_U16_TYPE@ art_u16;
typedef @ART_U32_TYPE@ art_u32;

#if defined(__TDE_HAVE_GCC_VISIBILITY) || defined(G_HAVE_GCC_VISIBILITY)
#define LIBART_NO_EXPORT __attribute__ ((visibility("hidden")))
#define LIBART_EXPORT __attribute__ ((visibility("default")))
#elif defined(_WIN32)
#define LIBART_NO_EXPORT
#define LIBART_EXPORT __declspec(dllexport)
#else
#define LIBART_NO_EXPORT
#define LIBART_EXPORT
#endif

#endif /* _ART_CONFIG_H_ */
