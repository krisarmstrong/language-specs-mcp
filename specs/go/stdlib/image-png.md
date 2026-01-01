package png // import "image/png"

Package png implements a PNG image decoder and encoder.

The PNG specification is at https://www.w3.org/TR/PNG/.

FUNCTIONS

func Decode(r io.Reader) (image.Image, error)
    Decode reads a PNG image from r and returns it as an image.Image. The type
    of Image returned depends on the PNG contents.

func DecodeConfig(r io.Reader) (image.Config, error)
    DecodeConfig returns the color model and dimensions of a PNG image without
    decoding the entire image.

func Encode(w io.Writer, m image.Image) error
    Encode writes the Image m to w in PNG format. Any Image may be encoded,
    but images that are not image.NRGBA might be encoded lossily.


TYPES

type CompressionLevel int
    CompressionLevel indicates the compression level.

const (
	DefaultCompression CompressionLevel = 0
	NoCompression      CompressionLevel = -1
	BestSpeed          CompressionLevel = -2
	BestCompression    CompressionLevel = -3
)
type Encoder struct {
	CompressionLevel CompressionLevel

	// BufferPool optionally specifies a buffer pool to get temporary
	// EncoderBuffers when encoding an image.
	BufferPool EncoderBufferPool
}
    Encoder configures encoding PNG images.

func (enc *Encoder) Encode(w io.Writer, m image.Image) error
    Encode writes the Image m to w in PNG format.

type EncoderBuffer encoder
    EncoderBuffer holds the buffers used for encoding PNG images.

type EncoderBufferPool interface {
	Get() *EncoderBuffer
	Put(*EncoderBuffer)
}
    EncoderBufferPool is an interface for getting and returning temporary
    instances of the EncoderBuffer struct. This can be used to reuse buffers
    when encoding multiple images.

type FormatError string
    A FormatError reports that the input is not a valid PNG.

func (e FormatError) Error() string

type UnsupportedError string
    An UnsupportedError reports that the input uses a valid but unimplemented
    PNG feature.

func (e UnsupportedError) Error() string

