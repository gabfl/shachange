# shachange: Change an image sha signature

`shachange` is a very simple Python program designed to change the signature of an image (sha1, sha256, md5...) in order to fool computer programs designed to identify unique images based on their signatures.

The modification in the image is virtually impossible to see for a human but computers programs will see the image as a different one.

## How does it work?

 - A single pixel is slightly modified: it will change the image signature and will be virtually indistinctible for a human
 - For improved security, meta data are removed

## Demo

![Demo](https://github.com/gabfl/shachange/blob/master/img/demo.gif?raw=true)

## Installation

```
pip3 install shachange
```

## Usage

```
shachange --file 'image.jpg'
Current file signature: f482afa0a6d9fa0023df7c35c978b5ccd59e3904 -> from image.jpg
    New file signature: a53d273986cb08f5135835744397f2c05e61bc37 -> saved to image_2.jpg
```
