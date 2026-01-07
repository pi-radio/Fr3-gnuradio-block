/* -*- c++ -*- */
/*
 * Copyright 2026 Pi-Radio.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_FR3_MINIFR3_H
#define INCLUDED_FR3_MINIFR3_H

#include <gnuradio/FR3/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace FR3 {

    /*!
     * \brief <+description of block+>
     * \ingroup FR3
     *
     */
    class FR3_API miniFR3 : virtual public gr::sync_block
    {
     public:
      typedef std::shared_ptr<miniFR3> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of FR3::miniFR3.
       *
       * To avoid accidental use of raw pointers, FR3::miniFR3's
       * constructor is in a private implementation
       * class. FR3::miniFR3::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace FR3
} // namespace gr

#endif /* INCLUDED_FR3_MINIFR3_H */
