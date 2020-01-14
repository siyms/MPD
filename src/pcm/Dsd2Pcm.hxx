/*

Copyright 2009, 2011 Sebastian Gesemann. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list of
      conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice, this list
      of conditions and the following disclaimer in the documentation and/or other materials
      provided with the distribution.

THIS SOFTWARE IS PROVIDED BY SEBASTIAN GESEMANN ''AS IS'' AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL SEBASTIAN GESEMANN OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those of the
authors and should not be interpreted as representing official policies, either expressed
or implied, of Sebastian Gesemann.

 */

#ifndef DSD2PCM_H_INCLUDED
#define DSD2PCM_H_INCLUDED

#include <stddef.h>
#include <stdint.h>

/**
 * A "dsd2pcm engine" for one channel.
 */
class Dsd2Pcm {
public:
	/* must be a power of two */
	static constexpr size_t FIFOSIZE = 16;

private:
	/** bit mask for FIFO offsets */
	static constexpr size_t FIFOMASK = FIFOSIZE - 1;

	uint8_t fifo[FIFOSIZE];
	size_t fifopos;

public:
	Dsd2Pcm() noexcept {
		Reset();
	}

	/**
	 * resets the internal state for a fresh new stream
	 */
	void Reset() noexcept;

	/**
	 * "translates" a stream of octets to a stream of floats
	 * (8:1 decimation)
	 * @param ctx -- pointer to abstract context (buffers)
	 * @param samples -- number of octets/samples to "translate"
	 * @param src -- pointer to first octet (input)
	 * @param src_stride -- src pointer increment
	 * @param lsbitfirst -- bitorder, 0=msb first, 1=lsbfirst
	 * @param dst -- pointer to first float (output)
	 * @param dst_stride -- dst pointer increment
	 */
	void Translate(size_t samples,
		       const uint8_t *src, ptrdiff_t src_stride,
		       bool lsbitfirst,
		       float *dst, ptrdiff_t dst_stride) noexcept;

private:
	float CalcOutputSample(size_t ffp) const noexcept;
};

#endif /* include guard DSD2PCM_H_INCLUDED */

