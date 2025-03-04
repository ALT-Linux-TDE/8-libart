/* Libart_LGPL - library of basic graphic primitives
 * Copyright (C) 1998 Raph Levien
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Library General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 *
 * You should have received a copy of the GNU Library General Public
 * License along with this library; if not, write to the
 * Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
 */

#ifndef __ART_VPATH_SVP_H__
#define __ART_VPATH_SVP_H__

/* "Unsort" a sorted vector path into an ordinary vector path. */

#ifdef LIBART_COMPILATION
#include "art_config.h"
#include "art_svp.h"
#include "art_vpath.h"
#else
#include <libart_lgpl/art_config.h>
#include <libart_lgpl/art_svp.h>
#include <libart_lgpl/art_vpath.h>
#endif

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

LIBART_EXPORT ArtVpath *art_vpath_from_svp (const ArtSVP *svp);

#ifdef __cplusplus
}
#endif /* __cplusplus */

#endif /* __ART_VPATH_SVP_H__ */
