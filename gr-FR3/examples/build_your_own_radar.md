# Building a Radar

## Principles
  
  Radars work by receiving radio waves reflected from distant objects.  By comparing this wave to the transmitted signal, attributes about the object can be determined, such as range and velocity.
  
## Types of Radar

There are a number of types of radars that have their own advantages.  Continuous Wave (CW) radars work by radiating long pulses of a fixed frequency and looking for the radar echoes.  FMCW works by mixing, yada yada.  There are more advanced types like FSK, OFDM, etc.

Here we will demonstrate the construction and operation of a FMCW Radar using GNU-Radio. FMCW radars are used to measure range and velocity of objects. We will begin by building a demo at 2.4GHz, and then demonstrate using Pi Radio's FR3 Single Channel converter to then operate at X-band (10 GHz).

## First Steps

1. Start GNURadio Companion

2. Every damn little step, as if you had recently recovered from severe brain trauma. Explain why you are doing everything that you do.

3. Grab the following blocks VCO , Signal Source, and QT GUI time sink. Connect them to the following (signal source --> VCO --> time sink) set the type for all of the to float.The waveform should be sawtooth with a freqency of 1Khz press start and look at the waveform.
4. 
## Experiments with the Radar

1. Show what the expected results will be.

## Uping the Frequency to FR3 
  
  


## build your own helical antenna for 10.5Ghz

  
