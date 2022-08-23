from argparse import ArgumentParser
from distutils.util import strtobool
import os
from pathlib import Path
from PIL import Image


parser = ArgumentParser(description='center cropping')
parser.add_argument('--input_dir', type=str)
parser.add_argument('--input_image', type=str)
parser.add_argument('--out_dir', type=str, default='result')
parser.add_argument('--is_resize', help='resize input image', type=strtobool, default='False')
parser.add_argument('--crop_size', type=int, help='cropped image size.', default=256)

args = parser.parse_args()

out_dir = args.out_dir

if not args.input_dir and not args.input_image:
    print("argument error.")
    exit()

if not os.path.exists(out_dir):
    os.mkdir(out_dir)

if args.input_image:
    image_path = [Path(args.input_image)]
else:
    in_dir = Path(args.input_dir)
    image_path = [f for f in in_dir.glob('*')]

is_resize = args.is_resize
crop_size = args.crop_size

if crop_size % 2 != 0:
    print("crop size must be even.")
    exit()

half_length = crop_size // 2

for image in image_path:
    im = Image.open(image)
    if im.height < crop_size or im.width < crop_size:
        print("size of " + os.path.basename(image) + " must be larger than" + str(crop_size) + "x" + str(crop_size) + ".")
        exit()
    
    if is_resize:
        h = im.height
        w = im.width
        short = min(h, w)
        # BICUBIC is deprecated and will be removed in Pillow 10 (2023-07-01). Use Resampling.BICUBIC instead.
        im = im.resize((int(w / short * crop_size), int(h / short * crop_size)), resample=Image.Resampling.BICUBIC)

    center = (im.width // 2, im.height // 2)
    out_im = Image.new(im.mode, (crop_size, crop_size))

    for i in range(-half_length, half_length):
        for j in range(-half_length, half_length):
            pix = im.getpixel((j + center[0], i + center[1]))
            out_im.putpixel((j + half_length, i + half_length), pix)
    
    out_im.save(out_dir + "/" + os.path.basename(image))
    print("crpped : " + os.path.basename(image))
