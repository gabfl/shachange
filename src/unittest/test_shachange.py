
import unittest

from PIL import Image, ImageFilter

from .. import shachange


class Test(unittest.TestCase):

    test_images = {
        'jpg': {
            'path': 'src/unittest/utils/img/raspberry.jpg',
            'size': (473, 640),
            'hash': '3a5f4bc896880886b32509a67c9efc925fa17f8c',
        },
        'jpeg': {
            'path': 'src/unittest/utils/img/raspberry.jpeg',
            'size': (473, 640),
            'hash': '9acab45b5c51593fb9fb0bf044b08b481e9148a5',
        },
        'jp2': {
            'path': 'src/unittest/utils/img/raspberry.jp2',
            'size': (473, 640),
            'hash': '72a0bb18c1aa47c6c991733cf3dfe5bd61ad98d2',
        },
        # 'gif': {
        #     'path': 'src/unittest/utils/img/raspberry.gif',
        #     'size': (473, 640),
        #     'hash': 'aac71c9f631e2ef834dd81f6981d3591d19302ac',
        # },
        'png': {
            'path': 'src/unittest/utils/img/raspberry.png',
            'size': (473, 640),
            'hash': 'b9e397bce9265387212d9bbf2d0348588a3dbb6c',
        },
        'tiff': {
            'path': 'src/unittest/utils/img/raspberry.tiff',
            'size': (473, 640),
            'hash': 'c5cdea4f281bfb9cbb797c9e00356e0bd29c608e',
        },
    }

    def test_check_file_exists(self):
        for _, image in self.test_images.items():
            self.assertTrue(shachange.check_file_exists(image['path']))

    def test_load_image(self):
        for type_, image in self.test_images.items():
            shachange.load_image(image['path'])

            if type_ == 'jpg':
                self.assertIsInstance(
                    shachange.im, PIL.JpegImagePlugin.JpegImageFile)
            elif type_ == 'jpeg':
                self.assertIsInstance(
                    shachange.im, PIL.JpegImagePlugin.JpegImageFile)
            elif type_ == 'jp2':
                self.assertIsInstance(
                    shachange.im, PIL.Jpeg2KImagePlugin.Jpeg2KImageFile)
            elif type_ == 'gif':
                self.assertIsInstance(
                    shachange.im, PIL.GifImagePlugin.GifImageFile)
            elif type_ == 'png':
                self.assertIsInstance(
                    shachange.im, PIL.PngImagePlugin.PngImageFile)
            elif type_ == 'tiff':
                self.assertIsInstance(
                    shachange.im, PIL.TiffImagePlugin.TiffImageFile)
            # self.assertIsInstance(shachange.load, PixelAccess)

            shachange.im.close()

    def test_get_size(self):
        for type_, image in self.test_images.items():
            shachange.load_image(image['path'])

            w, h = shachange.get_size()
            ew, eh = image['size']

            self.assertEqual(w, ew)
            self.assertEqual(h, eh)

    def test_get_random_pixel_position(self):
        for type_, image in self.test_images.items():
            shachange.load_image(image['path'])

            a, b = shachange.get_random_pixel_position()

            self.assertIsInstance(a, int)
            self.assertIsInstance(b, int)

    def test_new_color(self):
        a, b, c = shachange.new_color(1, 2, 3)

        self.assertIsInstance(a, int)
        self.assertIsInstance(b, int)
        self.assertIsInstance(c, int)

    def test_new_value(self):
        self.assertTrue(shachange.new_value(220) in range(220 - 51, 220))
        self.assertTrue(shachange.new_value(120) in range(120, 120 + 51))

    def test_change_pixel(self):
        for type_, image in self.test_images.items():
            shachange.load_image(image['path'])

            self.assertTrue(shachange.change_pixel())

    def test_save_image(self):
        for type_, image in self.test_images.items():
            shachange.load_image(image['path'])

            self.assertTrue(shachange.save_image('/tmp/tmp.png'))

    def test_get_new_filename(self):
        for type_, image in self.test_images.items():
            file_, ext = image['path'].split('.')
            newname = file_ + '_2.' + ext

            self.assertEqual(shachange.get_new_filename(
                image['path']), newname)

    def test_get_filename_and_ext(self):
        for type_, image in self.test_images.items():
            file_, ext = shachange.get_filename_and_ext(image['path'])
            efile_, eext = image['path'].split('.')

            self.assertEqual(file_, efile_)
            self.assertEqual(ext, '.' + eext)

    def test_get_file_hash(self):
        for type_, image in self.test_images.items():
            self.assertEqual(shachange.get_file_hash(
                image['path']), image['hash'])

    def test_process_file(self):
        for type_, image in self.test_images.items():
            self.assertTrue(shachange.process_file(image['path']))
