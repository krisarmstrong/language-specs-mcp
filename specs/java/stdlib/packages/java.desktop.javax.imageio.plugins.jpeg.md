Module[java.desktop](../../../../module-summary.html)

# Package javax.imageio.plugins.jpeg

package javax.imageio.plugins.jpegClasses supporting the built-in JPEG plug-in. 

 This package contains some support classes for the built-in JPEG reader and writer plug-ins. Classes are provided for representing quantization and Huffman tables, and extensions of `ImageReadParam` and `ImageWriteParam` are provided to supply tables during the reading and writing process. For more information about the operation of the built-in JPEG plug-ins, see the [JPEG metadata format
 specification and usage notes](../../metadata/doc-files/jpeg_metadata.html).

Since:1.4

- ClassesClassDescription[JPEGHuffmanTable](JPEGHuffmanTable.html)A class encapsulating a single JPEG Huffman table.[JPEGImageReadParam](JPEGImageReadParam.html)This class adds the ability to set JPEG quantization and Huffman tables when using the built-in JPEG reader plug-in.[JPEGImageWriteParam](JPEGImageWriteParam.html)This class adds the ability to set JPEG quantization and Huffman tables when using the built-in JPEG writer plug-in, and to request that optimized Huffman tables be computed for an image.[JPEGQTable](JPEGQTable.html)A class encapsulating a single JPEG quantization table.
