/*
 * art_render_svp.h: SVP mask source for modular rendering.
 *
 * Libart_LGPL - library of basic graphic primitives
 * Copyright (C) 2000 Raph Levien
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
 *
 * Authors: Raph Levien <raph@acm.org>
 */

#ifndef __ART_RENDER_SVP_H__
#define __ART_RENDER_SVP_H__

#ifdef LIBART_COMPILATION
#include "art_config.h"
#include "art_render.h"
#include "art_svp.h"
#else
#include <libart_lgpl/art_config.h>
#include <libart_lgpl/art_render.h>
#include <libart_lgpl/art_svp.h>
#endif

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

LIBART_EXPORT void
art_render_svp (ArtRender *render, const ArtSVP *svp);

#ifdef __cplusplus
}
#endif /* __cplusplus */

#endif /* __ART_RENDER_SVP_H__ */
