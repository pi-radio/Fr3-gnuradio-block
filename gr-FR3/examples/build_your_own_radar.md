# Building a Radar

## Principles
  
  Radars work by receiving radio waves reflected from distant objects.  By comparing this wave to the transmitted signal, attributes about the object can be determined, such as range and velocity.
  
## Types of Radar

There are a number of types of radars that have their own advantages.  Continuous Wave (CW) radars work by radiating long pulses of a fixed frequency and looking for the radar echoes.  FMCW works by mixing, yada yada.  There are more advanced types like FSK, OFDM, etc.

Here we will demonstrate the construction and operation of a FMCW Radar using GNU-Radio. -- insert what you can do with FMCW -- We will begin by building a demo at 2.4GHz, and then demonstrate using Pi Radio's FR3 Single Channel converter to then operate at X-band (10 GHz).

## First Steps

1. Start GNURadio Companion

2. Every damn little step, as if you had recently recovered from severe brain trauma. Explain why you are doing everything that you do.

## Experiments with the Radar

100. Show what the expected results will be.

## Uping the Frequency to FR3 
  
  
There are multiple types of radars that are used for diffrent purposes countinuos wave(CW), freqency modulated continuos wave(FMCW), freqency shift keying radar(FSK), Orthogonal freqency division multiplexing radar (OFDM),pulsed radar, and pulse doppler.
Each of them have there own uses and limitations. Now your wondering How do radar measure distance ,velocity and Angle of Arrival, measuring velocity is 
quite easy to do using the principle of doppler shifting i.e lets use an ambulance in this example when it is driving towards you you hear the pitch get higher but when it drives away you hear the pitch get lower.
We use this principle all the time with radars, astronomy, medical field, and satilites.[insert image of doppler shift car radar].
Measuring distance there are multiple techniques, you send a pulse and time how long it takes to come back or you could use a FMCW
radar which is a continuos wave radar that the freqency is modulated but it is limited to small distances, and Using phase measurements you can measure small movements.
Direction of arrival or DOA can be found by using a array of antennas and doing beam forming. Beam forming can be used with transmitting and reciving when you transmit 
you use the amplitude and phase in each antenna to steer the beam.When receiving you delay the signal diffrently on each antenna then you add them together[insert image of TXRX BEAM FORMING ].

*build your own helical antenna for 10.5Ghz




