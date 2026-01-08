/* -*- c++ -*- */
/*
 * Copyright 2026 Pi-Radio.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_FR3_MINIFR3_IMPL_H
#define INCLUDED_FR3_MINIFR3_IMPL_H

#include <gnuradio/FR3/miniFR3.h>

namespace gr {
  namespace FR3 {

    class miniFR3_impl : public miniFR3
    {
     private:
      // Nothing to declare in this block.

     public:
      miniFR3_impl();
      ~miniFR3_impl();

      virtual void set_frequency(float set_freq) = 0; // RF
      virtual void set_frequency(float set_freq2) = 0; // IF
      virtual void set_frequency(float set_gain1) = 0; // RX
      virtual void set_frequency(float set_gain2) = 0; // TX
      int work(
              int noutput_items,
              gr_vector_const_void_star &input_items,
              gr_vector_void_star &output_items
      );
    };

  } // namespace FR3
} // namespace gr

#endif /* INCLUDED_FR3_MINIFR3_IMPL_H */
