for s in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
    print(s*8, end='')

import struct
print(struct.pack("<I", 0x83e58955))
