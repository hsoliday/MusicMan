import pyaudio

FORMAT_LQ = pyaudio.paInt8
FORMAT_MQ = pyaudio.paInt16
FORMAT_MHQ= pyaudio.paInt24
FORMAT_HQ = pyaudio.paInt32
FORMAT_FLOAT = pyaudio.paFloat32

SINGLE_CHANNEL = 1
DUAL_CHANNELS = 2
QUAD_CHANNEL = 4
OCTO_CHANNEL = 8

RATE_NORMAL = 44100
RATE_HALF = 22050
RATE_DOUBLE = 88200

CHUNK_HALF = 512
CHUNK = 1024
CHUNK_DOUBLE = 2048

DEFAULT_RECORD_TIME = 5

DEFAULT_OUTPUT_FILENAME = "default.wav"
