Module[java.desktop](../../../../module-summary.html)

# Package javax.sound.sampled.spi

package javax.sound.sampled.spiSupplies abstract classes for service providers to subclass when offering new audio devices, sound file readers and writers, or audio format converters. 

## Related Documentation

 For more information on using Java Sound see: 

- [The Java Sound Tutorial](https://docs.oracle.com/javase/tutorial/sound/)

 Please note: In the `javax.sound.sampled.spi` APIs, a `null` reference parameter to methods is incorrect unless explicitly documented on the method as having a meaningful interpretation. Usage to the contrary is incorrect coding and may result in a run time exception either immediately or at some later time. `NullPointerException` is an example of typical and acceptable run time exception for such cases.Since:1.3

- Related PackagesPackageDescription[javax.sound.sampled](../package-summary.html)Provides interfaces and classes for capture, processing, and playback of sampled audio data.
- ClassesClassDescription[AudioFileReader](AudioFileReader.html)Provider for audio file reading services.[AudioFileWriter](AudioFileWriter.html)Provider for audio file writing services.[FormatConversionProvider](FormatConversionProvider.html)A format conversion provider provides format conversion services from one or more input formats to one or more output formats.[MixerProvider](MixerProvider.html)A provider or factory for a particular mixer type.
