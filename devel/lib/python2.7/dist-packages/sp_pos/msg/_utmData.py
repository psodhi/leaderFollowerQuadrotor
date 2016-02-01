"""autogenerated by genpy from sp_pos/utmData.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class utmData(genpy.Message):
  _md5sum = "49b19eb1db7e204c2b9962b01694fa27"
  _type = "sp_pos/utmData"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 utmNorthing
float64 utmEasting
string utmZone

"""
  __slots__ = ['utmNorthing','utmEasting','utmZone']
  _slot_types = ['float64','float64','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       utmNorthing,utmEasting,utmZone

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(utmData, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.utmNorthing is None:
        self.utmNorthing = 0.
      if self.utmEasting is None:
        self.utmEasting = 0.
      if self.utmZone is None:
        self.utmZone = ''
    else:
      self.utmNorthing = 0.
      self.utmEasting = 0.
      self.utmZone = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_2d.pack(_x.utmNorthing, _x.utmEasting))
      _x = self.utmZone
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.utmNorthing, _x.utmEasting,) = _struct_2d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.utmZone = str[start:end].decode('utf-8')
      else:
        self.utmZone = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_2d.pack(_x.utmNorthing, _x.utmEasting))
      _x = self.utmZone
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.utmNorthing, _x.utmEasting,) = _struct_2d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.utmZone = str[start:end].decode('utf-8')
      else:
        self.utmZone = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2d = struct.Struct("<2d")
