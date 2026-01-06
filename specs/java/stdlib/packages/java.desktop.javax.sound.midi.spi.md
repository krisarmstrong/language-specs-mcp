Module[java.desktop](../../../../module-summary.html)

# Package javax.sound.midi.spi

package javax.sound.midi.spiSupplies interfaces for service providers to implement when offering new MIDI devices, MIDI file readers and writers, or sound bank readers. 

## Related Documentation

 For more information on using Java Sound see: 

- [The Java Sound Tutorial](https://docs.oracle.com/javase/tutorial/sound/)

 Please note: In the `javax.sound.midi.spi` APIs, a `null` reference parameter to methods is incorrect unless explicitly documented on the method as having a meaningful interpretation. Usage to the contrary is incorrect coding and may result in a run time exception either immediately or at some later time. `NullPointerException` is an example of typical and acceptable run time exception for such cases.Since:1.3

- Related PackagesPackageDescription[javax.sound.midi](../package-summary.html)Provides interfaces and classes for I/O, sequencing, and synthesis of MIDI (Musical Instrument Digital Interface) data.
- ClassesClassDescription[MidiDeviceProvider](MidiDeviceProvider.html)A `MidiDeviceProvider` is a factory or provider for a particular type of MIDI device.[MidiFileReader](MidiFileReader.html)A `MidiFileReader` supplies MIDI file-reading services.[MidiFileWriter](MidiFileWriter.html)A `MidiFileWriter` supplies MIDI file-writing services.[SoundbankReader](SoundbankReader.html)A `SoundbankReader` supplies soundbank file-reading services.
