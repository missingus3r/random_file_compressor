Segmentation and reconstruction method for lossless random binary file compression.

Abstract

The present script implements a data compression method that operates by removing and separating bytes in binary files. The process is divided into two main phases: compression and decompression. In the compression phase, the original file is split into two parts at a given position, and an initial sequence of bytes is removed. In the decompression phase, the original file is reconstructed by combining the separated parts and restoring the deleted initial byte sequence.
Introduction

Data compression is a fundamental technique for the efficient management of information storage and transmission. The presented algorithm focuses on the manipulation of binary files, where compression is achieved without the need for complex encoding, but through the removal and subsequent restoration of certain bytes from the file.

Methodology

Compression

1. Reading the Original File: The content of the original binary file_file.bin is read and converted into a list of integers, representing the bytes of the file.
2. Calculating the Size and Split Position: The total size of the integer array is calculated and a z-value is determined that indicates the position in which the file will be split. This value is obtained by adding the byte values from the beginning until the sum is less than the total size of the file.
3. Splitting the File: The integer array is split into two parts at position z. The first part contains the bytes from the beginning to z, and the second part contains the bytes from z to the end.
4. Writing Separate Files: Two new binary files are created, original_file.bin.1 and original_file.bin.2, containing the two split parts of the original file.

Decompression

1. Read First File Size: The size of the original_file.bin.1 file is read and converted to a sequence of bytes representing the initial bytes removed during compression.
2. Read Separate Files: The contents of the original_file.bin.1 and original_file.bin.2 files are read.
3. Reconstruction of the Original Content: The sequence of initial bytes is combined with the contents of the two separate files to reconstruct the original content of the file.
4. Write Decompressed File: The reconstructed contents are written to a new binary file original_file_decomp.bin.

Compression rate

The compression rate in this method depends directly on the size of the file and the number of bytes that can be removed in the compression phase. If the file has a size greater than or equal to 16,777,215 bytes (approximately 16 MB), the maximum number of bytes that can be removed is 3, since 3 bytes can represent a maximum number of 16,777,215 when encoded in an 8-bit binary representation (2^24 - 1).

To illustrate with a concrete example:

- Original file size: 16,777,215 bytes.
- Bytes removed during compression: 3 bytes
- Size after compression: 16,777,215 - 3 = 16,777,212 bytes

The compression rate (CT) can be calculated as:

TC = (Original size - Compressed size) / Original size.

Applying the values from the example:

TC = (16,777,215 - 16,777,212) / 16,777,215
TC = 3 / 16,777,215
TC ≈ 1.79e-7 (or approximately 0.000018%).

This example shows that the compression rate is extremely low for files of this size, indicating that the method is not efficient for large file compression if only 3 bytes are removed. The effectiveness of this method would be more noticeable in files where the ratio of bytes removed to the total file size is higher.

Conclusion

The script provides a simple but effective method for compression and decompression of binary files. Although it does not use traditional compression techniques such as Huffman or LZW encoding, it offers an alternative for file manipulation that may be useful in certain contexts where preservation of data structure is critical and conventional compression is not applicable.

Limitations and Future Improvements

The current method does not guarantee a significant reduction in file size and is highly dependent on the nature of the data contained in the original file. Future improvements could include the implementation of more sophisticated compression algorithms in combination with the byte stripping and splitting technique to improve the compression rate.
