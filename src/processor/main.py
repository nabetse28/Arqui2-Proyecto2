from PIL import Image
from clock import *


def main():

    # Can be many different formats.
    im = Image.open('../images/stormtropper.png', 'r')
    pix_val = list(im.getdata())
    # print(pix_val)
    print(pix_val[60][3])
    print(im.size)


main()
