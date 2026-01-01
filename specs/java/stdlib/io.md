# Java I/O (java.io and java.nio)

## Files (java.nio.file)

### Reading Files

```java
// Read entire file
String content = Files.readString(Path.of("file.txt"));
byte[] bytes = Files.readAllBytes(Path.of("file.bin"));
List<String> lines = Files.readAllLines(Path.of("file.txt"));
List<String> lines = Files.readAllLines(Path.of("file.txt"), StandardCharsets.UTF_8);

// Stream lines (lazy, for large files)
try (Stream<String> lines = Files.lines(Path.of("file.txt"))) {
    lines.filter(line -> line.contains("error"))
         .forEach(System.out::println);
}

// BufferedReader
try (BufferedReader reader = Files.newBufferedReader(Path.of("file.txt"))) {
    String line;
    while ((line = reader.readLine()) != null) {
        process(line);
    }
}

// InputStream
try (InputStream in = Files.newInputStream(Path.of("file.bin"))) {
    byte[] buffer = new byte[8192];
    int bytesRead;
    while ((bytesRead = in.read(buffer)) != -1) {
        process(buffer, bytesRead);
    }
}
```

### Writing Files

```java
// Write entire file
Files.writeString(Path.of("file.txt"), content);
Files.write(Path.of("file.bin"), bytes);
Files.write(Path.of("file.txt"), lines);

// With options
Files.writeString(Path.of("file.txt"), content,
    StandardOpenOption.CREATE,
    StandardOpenOption.TRUNCATE_EXISTING);

// Append
Files.writeString(Path.of("file.txt"), content, StandardOpenOption.APPEND);

// BufferedWriter
try (BufferedWriter writer = Files.newBufferedWriter(Path.of("file.txt"))) {
    writer.write("Line 1");
    writer.newLine();
    writer.write("Line 2");
}

// OutputStream
try (OutputStream out = Files.newOutputStream(Path.of("file.bin"))) {
    out.write(bytes);
}

// PrintWriter
try (PrintWriter writer = new PrintWriter(Files.newBufferedWriter(path))) {
    writer.println("Line 1");
    writer.printf("Value: %d%n", 42);
}
```

### File Operations

```java
Path path = Path.of("dir", "subdir", "file.txt");
Path path = Path.of("/absolute/path/file.txt");
Path path = Paths.get("file.txt");

// Path operations
path.getFileName();         // file.txt
path.getParent();          // dir/subdir
path.getRoot();            // / (or null on relative)
path.toAbsolutePath();
path.normalize();          // resolve . and ..
path.resolve("other.txt"); // dir/subdir/other.txt
path.resolveSibling("sibling.txt");
path.relativize(otherPath);

// File operations
Files.exists(path);
Files.notExists(path);
Files.isDirectory(path);
Files.isRegularFile(path);
Files.isReadable(path);
Files.isWritable(path);
Files.isExecutable(path);
Files.size(path);

// Create
Files.createFile(path);
Files.createDirectory(path);
Files.createDirectories(path);  // creates parents
Files.createTempFile("prefix", ".tmp");
Files.createTempDirectory("prefix");

// Copy/Move/Delete
Files.copy(source, target);
Files.copy(source, target, StandardCopyOption.REPLACE_EXISTING);
Files.move(source, target);
Files.move(source, target, StandardCopyOption.ATOMIC_MOVE);
Files.delete(path);
Files.deleteIfExists(path);

// Attributes
Files.getLastModifiedTime(path);
Files.setLastModifiedTime(path, FileTime.fromMillis(millis));
Files.getOwner(path);
Files.getAttribute(path, "unix:uid");
```

### Directory Operations

```java
// List directory
try (DirectoryStream<Path> stream = Files.newDirectoryStream(dir)) {
    for (Path entry : stream) {
        System.out.println(entry);
    }
}

// With filter
try (DirectoryStream<Path> stream = Files.newDirectoryStream(dir, "*.java")) {
    // only .java files
}

// Walk directory tree
try (Stream<Path> paths = Files.walk(dir)) {
    paths.filter(Files::isRegularFile)
         .filter(p -> p.toString().endsWith(".java"))
         .forEach(System.out::println);
}

// Walk with depth limit
try (Stream<Path> paths = Files.walk(dir, 2)) {
    // max depth 2
}

// Find files
try (Stream<Path> paths = Files.find(dir, Integer.MAX_VALUE,
        (path, attrs) -> attrs.isRegularFile() && path.toString().endsWith(".java"))) {
    paths.forEach(System.out::println);
}
```

## Streams (java.io)

### Byte Streams

```java
// FileInputStream/FileOutputStream
try (FileInputStream fis = new FileInputStream("file.bin");
     FileOutputStream fos = new FileOutputStream("output.bin")) {
    byte[] buffer = new byte[8192];
    int bytesRead;
    while ((bytesRead = fis.read(buffer)) != -1) {
        fos.write(buffer, 0, bytesRead);
    }
}

// ByteArrayInputStream/ByteArrayOutputStream
byte[] data = "Hello".getBytes();
try (ByteArrayInputStream bais = new ByteArrayInputStream(data)) {
    // read from byte array
}

ByteArrayOutputStream baos = new ByteArrayOutputStream();
baos.write(data);
byte[] result = baos.toByteArray();

// BufferedInputStream/BufferedOutputStream
try (BufferedInputStream bis = new BufferedInputStream(new FileInputStream("file"));
     BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream("out"))) {
    // buffered I/O
}

// DataInputStream/DataOutputStream (primitive types)
try (DataOutputStream dos = new DataOutputStream(new FileOutputStream("data.bin"))) {
    dos.writeInt(42);
    dos.writeDouble(3.14);
    dos.writeUTF("Hello");
}

try (DataInputStream dis = new DataInputStream(new FileInputStream("data.bin"))) {
    int i = dis.readInt();
    double d = dis.readDouble();
    String s = dis.readUTF();
}
```

### Character Streams

```java
// FileReader/FileWriter
try (FileReader reader = new FileReader("file.txt");
     FileWriter writer = new FileWriter("output.txt")) {
    int ch;
    while ((ch = reader.read()) != -1) {
        writer.write(ch);
    }
}

// BufferedReader/BufferedWriter
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
    String line;
    while ((line = reader.readLine()) != null) {
        process(line);
    }
}

// InputStreamReader/OutputStreamWriter (with encoding)
try (Reader reader = new InputStreamReader(inputStream, StandardCharsets.UTF_8);
     Writer writer = new OutputStreamWriter(outputStream, StandardCharsets.UTF_8)) {
    // character I/O with specific encoding
}

// StringReader/StringWriter
try (StringReader reader = new StringReader("Hello World")) {
    // read from string
}

StringWriter sw = new StringWriter();
sw.write("Hello");
String result = sw.toString();

// PrintWriter
try (PrintWriter pw = new PrintWriter(new FileWriter("output.txt"))) {
    pw.println("Line 1");
    pw.printf("Value: %d%n", 42);
    pw.print("No newline");
}
```

## NIO Channels and Buffers

### ByteBuffer

```java
// Allocate
ByteBuffer buffer = ByteBuffer.allocate(1024);
ByteBuffer direct = ByteBuffer.allocateDirect(1024);  // off-heap
ByteBuffer wrapped = ByteBuffer.wrap(byteArray);

// Write to buffer
buffer.put((byte) 42);
buffer.putInt(1234);
buffer.putDouble(3.14);
buffer.put(byteArray);

// Prepare for reading
buffer.flip();

// Read from buffer
byte b = buffer.get();
int i = buffer.getInt();
double d = buffer.getDouble();
buffer.get(byteArray);

// Reset for reuse
buffer.clear();     // reset position, keep data
buffer.rewind();    // reset position to 0
buffer.compact();   // move unread data to beginning

// Properties
buffer.position();
buffer.limit();
buffer.capacity();
buffer.remaining();
buffer.hasRemaining();
```

### FileChannel

```java
// Read
try (FileChannel channel = FileChannel.open(path, StandardOpenOption.READ)) {
    ByteBuffer buffer = ByteBuffer.allocate(1024);
    while (channel.read(buffer) > 0) {
        buffer.flip();
        // process buffer
        buffer.clear();
    }
}

// Write
try (FileChannel channel = FileChannel.open(path,
        StandardOpenOption.WRITE, StandardOpenOption.CREATE)) {
    ByteBuffer buffer = ByteBuffer.wrap("Hello".getBytes());
    channel.write(buffer);
}

// Memory-mapped file
try (FileChannel channel = FileChannel.open(path, StandardOpenOption.READ)) {
    MappedByteBuffer mmap = channel.map(
        FileChannel.MapMode.READ_ONLY, 0, channel.size());
    // access file as memory
}

// Transfer
try (FileChannel source = FileChannel.open(sourcePath);
     FileChannel dest = FileChannel.open(destPath, StandardOpenOption.WRITE)) {
    source.transferTo(0, source.size(), dest);
}
```

## Serialization

```java
// Serialize
try (ObjectOutputStream oos = new ObjectOutputStream(
        new FileOutputStream("object.ser"))) {
    oos.writeObject(myObject);
}

// Deserialize
try (ObjectInputStream ois = new ObjectInputStream(
        new FileInputStream("object.ser"))) {
    MyClass obj = (MyClass) ois.readObject();
}

// Custom serialization
public class MyClass implements Serializable {
    private static final long serialVersionUID = 1L;
    
    private transient String cached;  // not serialized
    
    private void writeObject(ObjectOutputStream out) throws IOException {
        out.defaultWriteObject();
        // custom serialization
    }
    
    private void readObject(ObjectInputStream in) 
            throws IOException, ClassNotFoundException {
        in.defaultReadObject();
        // custom deserialization
    }
}
```

## Compression

```java
// GZIP
try (GZIPOutputStream gzip = new GZIPOutputStream(
        new FileOutputStream("file.gz"))) {
    gzip.write(data);
}

try (GZIPInputStream gzip = new GZIPInputStream(
        new FileInputStream("file.gz"))) {
    byte[] data = gzip.readAllBytes();
}

// ZIP
try (ZipOutputStream zos = new ZipOutputStream(
        new FileOutputStream("archive.zip"))) {
    ZipEntry entry = new ZipEntry("file.txt");
    zos.putNextEntry(entry);
    zos.write(content);
    zos.closeEntry();
}

try (ZipInputStream zis = new ZipInputStream(
        new FileInputStream("archive.zip"))) {
    ZipEntry entry;
    while ((entry = zis.getNextEntry()) != null) {
        String name = entry.getName();
        byte[] content = zis.readAllBytes();
        zis.closeEntry();
    }
}

// ZipFile (random access)
try (ZipFile zip = new ZipFile("archive.zip")) {
    ZipEntry entry = zip.getEntry("file.txt");
    try (InputStream is = zip.getInputStream(entry)) {
        // read entry
    }
}
```
