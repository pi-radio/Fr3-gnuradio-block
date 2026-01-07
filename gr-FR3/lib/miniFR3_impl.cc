/* -*- c++ -*- */
/*
 * Copyright 2026 Pi-Radio.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include <gnuradio/io_signature.h>
#include "miniFR3_impl.h"

namespace gr {
  namespace FR3 {

    #pragma message("set the following appropriately and remove this warning")
    using input_type = float;
    #pragma message("set the following appropriately and remove this warning")
    using output_type = float;
    miniFR3::sptr
    miniFR3::make()
    {
      return gnuradio::make_block_sptr<miniFR3_impl>(
        );
    }


    /*
     * The private constructor
     */
    miniFR3_impl::miniFR3_impl()
      : gr::sync_block("miniFR3",
              gr::io_signature::make(1 /* min inputs */, 1 /* max inputs */, sizeof(input_type)),
              gr::io_signature::make(1 /* min outputs */, 1 /*max outputs */, sizeof(output_type)))
    {}

    /*
     * Our virtual destructor.
     */
    miniFR3_impl::~miniFR3_impl()
    {
    }

    int
    miniFR3_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      auto in = static_cast<const input_type*>(input_items[0]);
      auto out = static_cast<output_type*>(output_items[0]);

      #pragma message("Implement the signal processing in your block and remove this warning")
      // Do <+signal processing+>

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace FR3 */
} /* namespace gr */
