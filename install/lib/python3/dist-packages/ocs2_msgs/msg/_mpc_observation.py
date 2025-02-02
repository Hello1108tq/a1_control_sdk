# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ocs2_msgs/mpc_observation.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ocs2_msgs.msg

class mpc_observation(genpy.Message):
  _md5sum = "c4075a25799f2a89c6d62b26e93cb66f"
  _type = "ocs2_msgs/mpc_observation"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# MPC observation
float64        time        # Current time
mpc_state      state       # Current state
mpc_input      input       # Current input
int8           mode        # Current mode

================================================================================
MSG: ocs2_msgs/mpc_state
# MPC internal model state vector
float32[] value

================================================================================
MSG: ocs2_msgs/mpc_input
# MPC internal model input vector 

float32[] value"""
  __slots__ = ['time','state','input','mode']
  _slot_types = ['float64','ocs2_msgs/mpc_state','ocs2_msgs/mpc_input','int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       time,state,input,mode

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(mpc_observation, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.time is None:
        self.time = 0.
      if self.state is None:
        self.state = ocs2_msgs.msg.mpc_state()
      if self.input is None:
        self.input = ocs2_msgs.msg.mpc_input()
      if self.mode is None:
        self.mode = 0
    else:
      self.time = 0.
      self.state = ocs2_msgs.msg.mpc_state()
      self.input = ocs2_msgs.msg.mpc_input()
      self.mode = 0

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
      _x = self.time
      buff.write(_get_struct_d().pack(_x))
      length = len(self.state.value)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.state.value))
      length = len(self.input.value)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.input.value))
      _x = self.mode
      buff.write(_get_struct_b().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.state is None:
        self.state = ocs2_msgs.msg.mpc_state()
      if self.input is None:
        self.input = ocs2_msgs.msg.mpc_input()
      end = 0
      start = end
      end += 8
      (self.time,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.state.value = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.input.value = s.unpack(str[start:end])
      start = end
      end += 1
      (self.mode,) = _get_struct_b().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.time
      buff.write(_get_struct_d().pack(_x))
      length = len(self.state.value)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.state.value.tostring())
      length = len(self.input.value)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.input.value.tostring())
      _x = self.mode
      buff.write(_get_struct_b().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.state is None:
        self.state = ocs2_msgs.msg.mpc_state()
      if self.input is None:
        self.input = ocs2_msgs.msg.mpc_input()
      end = 0
      start = end
      end += 8
      (self.time,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.state.value = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.input.value = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 1
      (self.mode,) = _get_struct_b().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_b = None
def _get_struct_b():
    global _struct_b
    if _struct_b is None:
        _struct_b = struct.Struct("<b")
    return _struct_b
_struct_d = None
def _get_struct_d():
    global _struct_d
    if _struct_d is None:
        _struct_d = struct.Struct("<d")
    return _struct_d
