# Building a Radar

## Principles
  
  Radars work by receiving radio waves reflected from distant objects.  By comparing this wave to the transmitted signal, attributes about the object can be determined, such as range and velocity.
  
## Types of Radar

There are a number of types of radars that have their own advantages.  Continuous Wave (CW) radars work by radiating long pulses of a fixed frequency and looking for the radar echoes.  FMCW works by mixing, yada yada.  There are more advanced types like FSK, OFDM, etc.

Here we will demonstrate the construction and operation of a FMCW Radar using GNU-Radio. FMCW radars are used to measure range and velocity of objects. We will begin by building a demo to measure velocity at 2.4GHz, and then demonstrate using Pi Radio's FR3 Single Channel converter to then operate at X-band (10 GHz).

## First Steps in 2.4 GHz

1. Start GNURadio Companion

2.  Set the Sample rate to 20e6 then Grab the following blocks Variable, import, VCO(complex) , Signal Source, and QT GUI time sink. Connect them to the following (signal source --> VCO(complex) --> time sink) set the signal source type to Float.In the import block use import math and for the variable block, change the id to sensitivity and value to 1e6*math.pi. The waveform should be sawtooth with a freqency of 1Khz.The VCO should be configured as sample rate as samp_rate sensitivity as the variable sensitivity and amplitude to 1 then press start and look at the waveform.

3. Now that you have seen the basic waveform of the fmcw radar we will let you figure this next step, how do you transmit it?

4. We will walk though the basic idea to reciving the radar.When you recieve it you then multipliy it by the conjigate of the transmitted signal then run it throught a fft.

4.By this point you should have something cobbled together and can move on to the next section.


## Experiments with the Radar
### 
    Don't go out in traffic for the experiments it can and will kill you.
    We are not responsible for any injury if you do go out in traffic 

1.Here are a expirement you can do with your new radar, First go to a sidewalk where you will be out of the way of people and has traffic. Set up your sdr with antennas point at an agle almost perpendictular with oncoming traffic but STAY ON THE SIDEWALK. Start your gnuradio script and look at the doppler shift. You'll notice the freqency spike will shift a very small amount the equation to find the velocity goes like this v=(c⋅fd)/(2⋅fc) where c is the speed of light fd is the doppler shift and fc is the carrier wave freqency, for example if i had a shift of 86 hz it would be going 38 km/h.

## Uping the Frequency to FR3 
###
	Do not transmit in the FR3 band Without a license or ATAP.
	The freqency band 10-10.5 GHz is a amuater radio band in 
	the us that requires a license for you to transmit on it.
	We suggest you to go for your amuater radio license.
	
  


## build your own helical antenna for 10.5Ghz

  
