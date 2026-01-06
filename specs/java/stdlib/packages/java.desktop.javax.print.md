Module[java.desktop](../../module-summary.html)

# Package javax.print

package javax.printProvides the principal classes and interfaces for the Java Print Service API. The Java Print Service API enables client and server applications to: 

- Discover and select print services based on their capabilities 
- Specify the format of print data 
- Submit print jobs to services that support the document type to be printed. 

## Print Service Discovery

 An application invokes the static methods of the abstract class [PrintServiceLookup](PrintServiceLookup.html) to locate print services that have the capabilities to satisfy the application's print request. For example, to print a double-sided document, the application first needs to find printers that have the double-sided printing capability. 

 The JDK includes `PrintServiceLookup` implementations that can locate the standard platform printers. To locate other types of printers, such as IPP printers or JINI printers, a print-service provider can write implementations of `PrintServiceLookup`. The print-service provider can dynamically install these `PrintServiceLookup` implementations using the [ServiceLoader](../../../java.base/java/util/ServiceLoader.html) facility. 

## Attribute Definitions

 The [javax.print.attribute](attribute/package-summary.html) and [javax.print.attribute.standard](attribute/standard/package-summary.html) packages define print attributes, which describe the capabilities of a print service, specify the requirements of a print job, and track the progress of a print job. 

 The `javax.print.attribute` package describes the types of attributes and how they can be collected into sets. The `javax.print.attribute.standard` package enumerates all of the standard attributes supported by the API, most of which are implementations of attributes specified in the IETF Specification, [RFC 2911 Internet Printing
 Protocol, 1.1: Model and Semantics](http://www.ietf.org/rfc/rfc2911.txt), dated September 2000. The attributes specified in `javax.print.attribute.standard` include common capabilities, such as: resolution, copies, media sizes, job priority, and page ranges. 

## Document Type Specification

 The [DocFlavor](DocFlavor.html) class represents the print data format, such as JPEG or PostScript. A `DocFlavor` object consists of a MIME type, which describes the format, and a document representation class name that indicates how the document is delivered to the printer or output stream. An application uses the `DocFlavor` and an attribute set to find printers that can print the document type specified by the `DocFlavor` and have the capabilities specified by the attribute set. 

## Using the API

 A typical application using the Java Print Service API performs these steps to process a print request: 

1. Chooses a `DocFlavor`. 
2. Creates a set of attributes. 
3. Locates a print service that can handle the print request as specified by the `DocFlavor` and the attribute set. 
4. Creates a [Doc](Doc.html) object encapsulating the `DocFlavor` and the actual print data, which can take many forms including: a Postscript file, a JPEG image, a `URL`, or plain text. 
5. Gets a print job, represented by [DocPrintJob](DocPrintJob.html), from the print service. 
6. Calls the print method of the print job. 

 The following code sample demonstrates a typical use of the Java Print Service API: locating printers that can print five double-sided copies of a Postscript document on size A4 paper, creating a print job from one of the returned print services, and calling print. 

```

 FileInputStream psStream;
 try {
     psStream = new FileInputStream("file.ps");
 } catch (FileNotFoundException ffne) {
 }
 if (psStream == null) {
     return;
 }
 DocFlavor psInFormat = DocFlavor.INPUT_STREAM.POSTSCRIPT;
 Doc myDoc = new SimpleDoc(psStream, psInFormat, null);
 PrintRequestAttributeSet aset = new HashPrintRequestAttributeSet();
 aset.add(new Copies(5));
 aset.add(MediaSizeName.ISO_A4);
 aset.add(Sides.DUPLEX);
 PrintService[] services =
 PrintServiceLookup.lookupPrintServices(psInFormat, aset);
 if (services.length > 0) {
     DocPrintJob job = services[0].createPrintJob();
     try {
         job.print(myDoc, aset);
     } catch (PrintException pe) {}
 }
 
```

 Please note: In the `javax.print` APIs, a `null` reference parameter to methods is incorrect unless explicitly documented on the method as having a meaningful interpretation. Usage to the contrary is incorrect coding and may result in a run time exception either immediately or at some later time. `IllegalArgumentException` and `NullPointerException` are examples of typical and acceptable run time exceptions for such cases.

Since:1.4

- Related PackagesPackageDescription[javax.print.attribute](attribute/package-summary.html)Provides classes and interfaces that describe the types of Java Print Service attributes and how they can be collected into attribute sets.[javax.print.event](event/package-summary.html)Package `javax.print.event` contains event classes and listener interfaces.
- All Classes and InterfacesInterfacesClassesException ClassesClassDescription[AttributeException](AttributeException.html)Interface `AttributeException` is a mixin interface which a subclass of [PrintException](PrintException.html) can implement to report an error condition involving one or more printing attributes that a particular Print Service instance does not support.[CancelablePrintJob](CancelablePrintJob.html)This interface is used by a printing application to cancel a print job.[Doc](Doc.html)Interface `Doc` specifies the interface for an object that supplies one piece of print data for a Print Job.[DocFlavor](DocFlavor.html)Class `DocFlavor` encapsulates an object that specifies the format in which print data is supplied to a [DocPrintJob](DocPrintJob.html).[DocFlavor.BYTE_ARRAY](DocFlavor.BYTE_ARRAY.html)Class `DocFlavor.BYTE_ARRAY` provides predefined static constant `DocFlavor` objects for example doc flavors using a byte array (`byte[]`) as the print data representation class.[DocFlavor.CHAR_ARRAY](DocFlavor.CHAR_ARRAY.html)Class `DocFlavor.CHAR_ARRAY` provides predefined static constant `DocFlavor` objects for example doc flavors using a character array (`char[]`) as the print data representation class.[DocFlavor.INPUT_STREAM](DocFlavor.INPUT_STREAM.html)Class `DocFlavor.INPUT_STREAM` provides predefined static constant `DocFlavor` objects for example doc flavors using a byte stream ([java.io.InputStream](../../../java.base/java/io/InputStream.html)) as the print data representation class.[DocFlavor.READER](DocFlavor.READER.html)Class `DocFlavor.READER` provides predefined static constant `DocFlavor` objects for example doc flavors using a character stream ([java.io.Reader](../../../java.base/java/io/Reader.html)) as the print data representation class.[DocFlavor.SERVICE_FORMATTED](DocFlavor.SERVICE_FORMATTED.html)Class `DocFlavor.SERVICE_FORMATTED` provides predefined static constant `DocFlavor` objects for example doc flavors for service formatted print data.[DocFlavor.STRING](DocFlavor.STRING.html)Class `DocFlavor.STRING` provides predefined static constant `DocFlavor` objects for example doc flavors using a string ([java.lang.String](../../../java.base/java/lang/String.html)) as the print data representation class.[DocFlavor.URL](DocFlavor.URL.html)Class `DocFlavor.URL` provides predefined static constant `DocFlavor` objects.[DocPrintJob](DocPrintJob.html)This interface represents a print job that can print a specified document with a set of job attributes.[FlavorException](FlavorException.html)Interface `FlavorException` is a mixin interface which a subclass of [PrintException](PrintException.html) can implement to report an error condition involving a doc flavor or flavors (class [DocFlavor](DocFlavor.html)).[MultiDoc](MultiDoc.html)Interface `MultiDoc` specifies the interface for an object that supplies more than one piece of print data for a Print Job.[MultiDocPrintJob](MultiDocPrintJob.html)Obtained from a `MultiDocPrintService`, a `MultiDocPrintJob` can print a specified collection of documents as a single print job with a set of job attributes.[MultiDocPrintService](MultiDocPrintService.html)Interface `MultiPrintService` is the factory for a `MultiDocPrintJob`.[PrintException](PrintException.html)Class `PrintException` encapsulates a printing-related error condition that occurred while using a Print Service instance.[PrintService](PrintService.html)Interface `PrintService` is the factory for a `DocPrintJob`.[PrintServiceLookup](PrintServiceLookup.html)Implementations of this class provide lookup services for print services (typically equivalent to printers) of a particular type.[ServiceUI](ServiceUI.html)This class is a collection of UI convenience methods which provide a graphical user dialog for browsing print services looked up through the Java Print Service API.[ServiceUIFactory](ServiceUIFactory.html)Services may optionally provide UIs which allow different styles of interaction in different roles.[SimpleDoc](SimpleDoc.html)This class is an implementation of interface `Doc` that can be used in many common printing requests.[StreamPrintService](StreamPrintService.html)This class extends [PrintService](PrintService.html) and represents a print service that prints data in different formats to a client-provided output stream.[StreamPrintServiceFactory](StreamPrintServiceFactory.html)A `StreamPrintServiceFactory` is the factory for [StreamPrintService](StreamPrintService.html) instances, which can print to an output stream in a particular document format described as a mime type.[URIException](URIException.html)Interface `URIException` is a mixin interface which a subclass of [PrintException](PrintException.html) can implement to report an error condition involving a `URI` address.
