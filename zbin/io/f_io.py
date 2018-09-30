
import struct

FORMAT_DICT = {
  '1_S_B': '>b',
  '1_U_B': '>B',
  '1_S_L': '<b',
  '1_U_L': '<B',
  '2_S_B': '>h',
  '2_U_B': '>H',
  '2_S_L': '<h',
  '2_U_L': '<H',
  '4_S_B': '>i',
  '4_U_B': '>I',
  '4_S_L': '<i',
  '4_U_L': '<I',
  '8_S_B': '>q',
  '8_U_B': '>Q',
  '8_S_L': '<q',
  '8_U_L': '<Q',
  '4_F_B': '>f',
  '4_F_L': '<f',
  '8_F_B': '>d',
  '8_F_L': '<d'
}

def struct_format(num_bit, big_endian=False, singed=True, num_type='int'):
  """Format Characters

  Args:
    num_bit: int, Number of digits.
    big_endian: bool, The size end of the data, default big-endian.
    singed: bool, Data symbol, default signed.

  Returns:
    A str.
  """
  if num_type == 'float' and num_bit not in (4, 8):
    raise ValueError('Floating point numbers only support 32-bit and 64-bit data.')

  s = 'S' if singed else 'U'
  b = 'B' if big_endian else 'L'
  if num_type == 'float':
    s = 'F'

  key = '%d_%s_%s' % (num_bit, s, b)

  return FORMAT_DICT[key]


def read(file_path, bit_width, big_endian=False, singed=True, num_type='int'):
  """Read binary

  Args:
    file_path: str, Binary file path.
    bit_width: int, Bit width of data.
    big_endian: bool, The size end of the data, default big-endian.
    singed: bool, Data symbol, default signed.
    num_type: str, Data type, 'int' or 'float'.

  Returns:
    A list object.
  """

  # Number of digits
  if not isinstance(bit_width, int):
    raise ValueError('bit_width should be a int object, not %s.' % type(bit_width))

  if bit_width not in (8, 16, 32):
    raise ValueError('Only 8, 16, 32-bit data reading is supported.')

  num_bit = bit_width // 8
  str_format = struct_format(num_bit, big_endian, singed, num_type)

  with open(file_path, 'rb') as f:
    pre_data = f.read()

  unpack_data = []
  add = unpack_data.append

  for i in range(0, len(pre_data) // num_bit):
    p = i * num_bit
    add(struct.unpack(str_format, pre_data[p:p+num_bit])[0])

  return unpack_data


def write(file_path, buffer_data, bit_width, 
          big_endian=False, singed=True, num_type='int'):
  """write binary to file.

  Args:
    file_path: str, file path.
    buffer_data: list, Data to be written.
    bit_width: int, Bit width of data.
    big_endian: bool, The size end of the data, default big-endian.
    singed: bool, Data symbol, default signed.
    num_type: str, Data type, 'int' or 'float'.

  """
  # Number of digits
  if not isinstance(bit_width, int):
    raise ValueError('bit_width should be a int object, not %s.' % type(bit_width))

  if bit_width not in (8, 16, 32):
    raise ValueError('Only 8, 16, 32-bit data writeing is supported.')

  num_bit = bit_width // 8
  str_format = struct_format(num_bit, big_endian, singed, num_type)

  with open(file_path, 'wb') as f:
    for i in range(0, len(buffer_data)):
      f.write(struct.pack(str_format, buffer_data[i]))