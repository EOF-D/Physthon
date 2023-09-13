from __future__ import annotations

from typing import cast
from codecs import BufferedIncrementalDecoder, CodecInfo, register, utf_8_encode
from traceback import print_exc


class _IncrDecoder(BufferedIncrementalDecoder):
    def _buffer_decode(self, data: bytes, *_: tuple[str, bool]) -> tuple[str, int]:
        if data != b"":
            return decode(data)

        return str(), 0

def decode(input: bytes | memoryview, errors: str = "strict") -> tuple[str, int]:
    parse: bytes = cast(bytes, input)

    if isinstance(input, memoryview):
        parse = input.tobytes()

    try:
        return parse.decode(), len(parse)
    except Exception:
        print_exc()
        print(errors)
        raise

ENCODINGS: dict[str, CodecInfo] = {
    encoding: CodecInfo(
        decode=decode,
        encode=utf_8_encode, # type: ignore
        name=encoding,
        incrementaldecoder=_IncrDecoder,
    )

    for encoding in {"Physthon", "physthon"}
}


register(ENCODINGS.get)
