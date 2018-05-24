import hashlib
import random
import os

import argparse
from PIL import Image, ImageFilter


# Vars
im = None
load = None


def check_file_exists(file_):
    """
        Check if the original file exists
    """

    if not os.path.isfile(file_):
        raise RuntimeError('The file `%s` does not exist.' % file_)

    return True


def load_image(file_):
    """
        Open image
    """

    global im, load

    try:
        im = Image.open(file_)
        load = im.load()
    except Exception as e:
        raise RuntimeError('`%s` does not appear to be an image.' % file_)


def get_size(debug=False):
    """
        Return image size
    """

    global im

    width, height = im.size

    # Debug
    if debug:
        print('...debug -> canvas size: %d x %d' % (width, height))

    return width, height


def get_random_pixel_position(debug=False):
    """
        Returns the position of a random pixel in the image
    """

    # Get image size
    width, height = get_size(debug)

    # Get random pixel
    a, b = random.randint(0, width - 1), random.randint(0, height - 1)

    # Debug
    if debug:
        print('...debug -> random pixel: %d , %d' % (a, b))

    return a, b


def new_color(r, g, b):
    """
        Returns new pixel color
    """

    return new_value(r), new_value(g), new_value(b)


def new_value(code):
    """
        Returns a new color code
    """

    if code >= 200:
        code -= random.randint(1, 50)
    else:
        code += random.randint(1, 50)

    return code


def change_pixel(debug=False):
    """
        Get a random pixel and replace its r, g & b codes with a new value
    """

    global im, load

    # Get pixel position
    aPix, bPix = get_random_pixel_position(debug)

    # Get r, g & b for the pixel
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((aPix, bPix))

    # Get new color
    r2, g2, b2 = new_color(r, g, b)

    # Debug
    if debug:
        print('...debug -> current color: %d , %d, %d' % (r, g, b))
        print('...debug ->     new color: %d , %d, %d' % (r2, g2, b2))

    # Replace with a new value
    load[aPix, bPix] = r2, g2, b2

    return True


def save_image(file_, suffix='_2'):
    """
        Save new image
    """

    global im

    # Saving the filtered image to a new file
    im.save(get_new_filename(file_, suffix))

    return True


def get_new_filename(file_, suffix='_2'):
    """
        Returns the new file path
    """

    # Get name and extension of original file
    name, ext = get_filename_and_ext(file_)

    return name + suffix + ext


def get_filename_and_ext(file_):
    """
        Separate and returns the filename and extension of the original file
    """

    # Return format: filename, file_extension
    return os.path.splitext(file_)


def get_file_hash(filepath):
    """
        Calculate file sha1
    """

    sha1 = hashlib.sha1()
    f = open(filepath, 'rb')
    try:
        sha1.update(f.read())
    finally:
        f.close()
    return sha1.hexdigest()


def process_file(file_, suffix='_2', debug=False):
    """
        Process a file
    """

    # Check if file exists
    check_file_exists(file_)

    # Load image
    load_image(file_)

    # Replace a pixel
    change_pixel(debug)

    # Save new image
    save_image(file_, suffix)

    print('Current file signature: %s -> from     %s' %
          (get_file_hash(file_), file_))
    print('    New file signature: %s -> saved to %s' %
          (get_file_hash(get_new_filename(file_, suffix)), get_new_filename(file_, suffix)))

    return True


def main():
    """
        Main function
    """

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str,
                        help="Original file path", required=True)
    parser.add_argument("-s", "--suffix", type=str,
                        help="New file suffix", default='_2')
    parser.add_argument("-d", "--debug", action='store_true',
                        help="Show debug information")
    args = parser.parse_args()

    process_file(file_=args.file, suffix=args.suffix, debug=args.debug)


if __name__ == '__main__':
    main()
