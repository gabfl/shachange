import hashlib
import random
import os

import argparse
from PIL import Image, ImageFilter


# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str, help="Original file path", required=True)
parser.add_argument("-s", "--suffix", type=str, help="New file suffix", default='_2')
parser.add_argument("-d", "--debug", action='store_true', help="Show debug information")
args = parser.parse_args()

# Vars
im = None
load = None


def checkFileExists():
    """
        Check if the original file exists
    """

    if not os.path.isfile(args.file):
        raise RuntimeError('The file `%s` does not exist.' % args.file)


def loadImage():
    """
        Open image
    """

    global im, load

    try:
        im = Image.open(args.file)
        load = im.load()
    except Exception as e:
        raise RuntimeError('`%s` does not appear to be an image.' % args.file)


def getSize():
    """
        Return image size
    """

    global im

    width, height = im.size

    # Debug
    if args.debug:
        print('...debug -> canvas size: %d x %d' % (width, height))

    return width, height


def getRandomPixePositionl():
    """
        Returns the position of a random pixel in the image
    """

    # Get image size
    width, height = getSize()

    # Get random pixel
    a, b = random.randint(0, width - 1), random.randint(0, height - 1)

    # Debug
    if args.debug:
        print('...debug -> random pixel: %d , %d' % (a, b))

    return a, b


def newColor(r, g, b):
    """
        Returns new pixel color
    """

    return newValue(r), newValue(g), newValue(b)


def newValue(code):
    """
        Returns a new color code
    """

    if code >= 200:
        code -= random.randint(1, 50)
    else:
        code += random.randint(1, 50)

    return code


def changePixel():
    """
        Get a random pixel and replace its r, g & b codes with a new value
    """

    global im, load

    # Get pixel position
    a, b = getRandomPixePositionl()

    # Get r, g & b for the pixel
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((a, b))

    # Get new color
    r2, g2, b2 = newColor(r, g, b)

    # Debug
    if args.debug:
        print('...debug -> current color: %d , %d, %d' % (r, g, b))
        print('...debug ->     new color: %d , %d, %d' % (r2, g2, b2))

    # Replace with a new value
    load[a, b] = r2, g2, b2


def saveImage():
    """
        Save new image
    """

    global im

    # Saving the filtered image to a new file
    im.save(getNewFileName(), 'JPEG')


def getNewFileName():
    """
        Returns the new file path
    """

    # Get name and extension of original file
    name, ext = GetFileNameAndExt()

    return name + args.suffix + ext


def GetFileNameAndExt():
    """
        Separate and returns the filename and extension of the original file
    """

    # Return format: filename, file_extension
    return os.path.splitext(args.file)


def getFileHash(filepath):
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


def main():
    """
        Main function
    """

    # Check if file exists
    checkFileExists()

    # Load iage
    loadImage()

    # Replace a pixel
    changePixel()

    # Save new image
    saveImage()

    print('Current file signature: %s -> from     %s' % (getFileHash(args.file), args.file))
    print('    New file signature: %s -> saved to %s' % (getFileHash(getNewFileName()), getNewFileName()))


if __name__ == '__main__':
    main()
