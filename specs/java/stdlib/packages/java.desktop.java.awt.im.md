Module[java.desktop](../../../module-summary.html)

# Package java.awt.im

package java.awt.imProvides classes and interfaces for the input method framework. This package enables text editing components to receive text input through input methods. Input methods are software components that let the user enter text in ways other than simple typing on a keyboard. They are commonly used to enter Japanese, Chinese, or Korean - languages using thousands of different characters - on keyboards with far fewer keys. However, the framework also supports input methods for other languages and the use of entirely different input mechanisms, such as handwriting or speech recognition. 

## Related Documentation

 For overviews, tutorials, examples, guides, and tool documentation, please see [Input Method Framework Overview](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=imf_overview).Since:1.2

- Related PackagesPackageDescription[java.awt](../package-summary.html)Contains all of the classes for creating user interfaces and for painting graphics and images.[java.awt.im.spi](spi/package-summary.html)Provides interfaces that enable the development of input methods that can be used with any Java runtime environment.
- All Classes and InterfacesInterfacesClassesClassDescription[InputContext](InputContext.html)Provides methods to control text input facilities such as input methods and keyboard layouts.[InputMethodHighlight](InputMethodHighlight.html)An InputMethodHighlight is used to describe the highlight attributes of text being composed.[InputMethodRequests](InputMethodRequests.html)InputMethodRequests defines the requests that a text editing component has to handle in order to work with input methods.[InputSubset](InputSubset.html)Defines additional Unicode subsets for use by input methods.
