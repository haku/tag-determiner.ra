from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AboutRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AboutReply(_message.Message):
    __slots__ = ("name", "tag_cls")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_CLS_FIELD_NUMBER: _ClassVar[int]
    name: str
    tag_cls: str
    def __init__(self, name: _Optional[str] = ..., tag_cls: _Optional[str] = ...) -> None: ...

class DetermineTagsRequest(_message.Message):
    __slots__ = ("mimetype", "content")
    MIMETYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    mimetype: str
    content: bytes
    def __init__(self, mimetype: _Optional[str] = ..., content: _Optional[bytes] = ...) -> None: ...

class DetermineTagsReply(_message.Message):
    __slots__ = ("tag",)
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tag: _Optional[_Iterable[str]] = ...) -> None: ...
