def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)
  
def is_set(value, bit):
  return value & 1<<bit
