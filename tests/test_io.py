
import os
import struct
import unittest
import xmlrunner
from unittest.case import TestCase

import zbin

class TestIo(TestCase):

    def test_read(self):
        # -------------------------Bit-width---------------------------------------------------

        # test bit-width=32, little-endian=True, singed=True, num_type='int'
        write_data = list(range(10))
        test_read_file = 'test_read.bin'
        with open(test_read_file, 'wb') as f:
            for i in range(0, len(write_data)):
                f.write(struct.pack('<i', write_data[i]))

        read_data = zbin.read(test_read_file, 32, big_endian=False, singed=True, num_type='int')
        self.assertListEqual(write_data, read_data)

        # test bit-width=16, little-endian=True, singed=True, num_type='int'
        write_data = list(range(10))
        test_read_file = 'test_read.bin'
        with open(test_read_file, 'wb') as f:
            for i in range(0, len(write_data)):
                f.write(struct.pack('<h', write_data[i]))

        read_data = zbin.read(test_read_file, 16, big_endian=False, singed=True, num_type='int')
        self.assertListEqual(write_data, read_data)

        # test bit-width=8, little-endian=True, singed=True, num_type='int'
        write_data = list(range(10))
        test_read_file = 'test_read.bin'
        with open(test_read_file, 'wb') as f:
            for i in range(0, len(write_data)):
                f.write(struct.pack('<b', write_data[i]))

        read_data = zbin.read(test_read_file, 8, big_endian=False, singed=True, num_type='int')
        self.assertListEqual(write_data, read_data)

        # -------------------------Bit-width--------endian--------------------------------------

        # test bit-width=32, big-endian=True, singed=True, num_type='int'
        write_data = list(range(10))
        test_read_file = 'test_read.bin'
        with open(test_read_file, 'wb') as f:
            for i in range(0, len(write_data)):
                f.write(struct.pack('>i', write_data[i]))

        read_data = zbin.read(test_read_file, 32, big_endian=True, singed=True, num_type='int')
        self.assertListEqual(write_data, read_data)

        # test bit-width=16, big-endian=True, singed=True, num_type='int'
        write_data = list(range(10))
        test_read_file = 'test_read.bin'
        with open(test_read_file, 'wb') as f:
            for i in range(0, len(write_data)):
                f.write(struct.pack('>h', write_data[i]))

        read_data = zbin.read(test_read_file, 16, big_endian=True, singed=True, num_type='int')
        self.assertListEqual(write_data, read_data)

        # test bit-width=8, big-endian=True, singed=True, num_type='int'
        write_data = list(range(10))
        test_read_file = 'test_read.bin'
        with open(test_read_file, 'wb') as f:
            for i in range(0, len(write_data)):
                f.write(struct.pack('>b', write_data[i]))

        read_data = zbin.read(test_read_file, 8, big_endian=True, singed=True, num_type='int')
        self.assertListEqual(write_data, read_data)

        # -------------------------Bit-width--------endian-------------singed-----------------

        # test bit-width=32, big-endian=True, singed=True, num_type='int'
        write_data = list(range(10))
        test_read_file = 'test_read.bin'
        with open(test_read_file, 'wb') as f:
            for i in range(0, len(write_data)):
                f.write(struct.pack('>I', write_data[i]))

        read_data = zbin.read(test_read_file, 32, big_endian=True, singed=False, num_type='int')
        self.assertListEqual(write_data, read_data)

        # test bit-width=16, big-endian=True, singed=True, num_type='int'
        write_data = list(range(10))
        test_read_file = 'test_read.bin'
        with open(test_read_file, 'wb') as f:
            for i in range(0, len(write_data)):
                f.write(struct.pack('>H', write_data[i]))

        read_data = zbin.read(test_read_file, 16, big_endian=True, singed=False, num_type='int')
        self.assertListEqual(write_data, read_data)

        # test bit-width=8, big-endian=True, singed=True, num_type='int'
        write_data = list(range(10))
        test_read_file = 'test_read.bin'
        with open(test_read_file, 'wb') as f:
            for i in range(0, len(write_data)):
                f.write(struct.pack('>B', write_data[i]))

        read_data = zbin.read(test_read_file, 8, big_endian=True, singed=False, num_type='int')
        self.assertListEqual(write_data, read_data)


        if os.path.isfile(test_read_file):
            os.remove(test_read_file)

        # -------------------------Bit-width--------endian-------------singed-------flaot---------

        # test bit-width=32, big-endian=True, singed=True, num_type='int'
        write_data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        test_read_file = 'test_read.bin'
        with open(test_read_file, 'wb') as f:
            for i in range(0, len(write_data)):
                f.write(struct.pack('>f', write_data[i]))

        read_data = zbin.read(test_read_file, 32, big_endian=True, singed=True, num_type='float')
        self.assertListEqual(write_data, read_data)


        if os.path.isfile(test_read_file):
            os.remove(test_read_file)

    def test_write(self):
        write_data = list(range(10))
        write_file = 'test_write.bin'

        zbin.write(write_file, write_data, 32, big_endian=True, singed=True, num_type='int')

        with open(write_file, 'rb') as f:
            read_data = f.read()

        res = b''
        for i in range(0, len(write_data)):
            res += struct.pack('>i', write_data[i])
        self.assertEqual(read_data, res)

        zbin.write(write_file, write_data, 16, big_endian=True, singed=True, num_type='int')

        with open(write_file, 'rb') as f:
            read_data = f.read()

        res = b''
        for i in range(0, len(write_data)):
            res += struct.pack('>h', write_data[i])
        self.assertEqual(read_data, res)

        zbin.write(write_file, write_data, 8, big_endian=True, singed=True, num_type='int')

        with open(write_file, 'rb') as f:
            read_data = f.read()

        res = b''
        for i in range(0, len(write_data)):
            res += struct.pack('>b', write_data[i])
        self.assertEqual(read_data, res)

        if os.path.isfile(write_file):
            os.remove(write_file) 






if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test_results'))
