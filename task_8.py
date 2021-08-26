# Task 8

# Please write a program to compress and decompress the string "Music industry hails passage of the Music Modernization Act".
#.......................................................................................................................

import gzip
import typing

#----------------------------------------

long_string: [str] = b'Music industry hails passage of the Music Modernization Act'
string_compress: [str] = gzip.compress(long_string)

print("\n Compressed String is :", gzip.compress(long_string))
print("\n Deompresseed String is :", gzip.decompress(string_compress))
