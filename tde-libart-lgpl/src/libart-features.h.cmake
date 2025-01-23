#ifndef LIBART_FEATURES_H
#define LIBART_FEATURES_H 1

#if !defined( _ART_CONFIG_H_ )
#ifdef LIBART_COMPILATION
#include "art_config.h"
#else
#include <libart_lgpl/art_config.h>
#endif
#endif

#define LIBART_MAJOR_VERSION (@LIBART_MAJOR_VERSION@)
#define LIBART_MINOR_VERSION (@LIBART_MINOR_VERSION@)
#define LIBART_MICRO_VERSION (@LIBART_MICRO_VERSION@)
#define LIBART_VERSION "@LIBART_VERSION@"

#ifdef _WIN32
#  ifdef LIBART_COMPILATION
#    define LIBART_VAR __declspec(dllexport)
#  else
#    define LIBART_VAR extern __declspec(dllimport)
#  endif
#else
#  ifdef LIBART_COMPILATION
#    define LIBART_VAR LIBART_EXPORT
#  else
#    define LIBART_VAR extern
#  endif
#endif

LIBART_VAR const unsigned int libart_major_version, libart_minor_version, libart_micro_version;
LIBART_VAR const char *libart_version;

LIBART_EXPORT void libart_preinit(void *app, void *modinfo);
LIBART_EXPORT void libart_postinit(void *app, void *modinfo);
#endif
