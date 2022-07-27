import argparse
import os
from pathlib import Path
from rembg import remove
from PIL import Image

parser = argparse.ArgumentParser()

parser.add_argument('--input_image', type=str, help='File path to the input image')
parser.add_argument('--input_dir', type=str, help='Directory path to a batch of input images')
parser.add_argument('--out_dir', type=str, default='resrult', help='Directory path to save the output image(s)')

args = parser.parse_args()

out_dir = args.out_dir

if not args.input_image and not args.input_dir:
    print("No input image or input dir.")
    exit()

if args.input_image and args.input_dir:
    print("can't use both option input_image and input_dir.")
    exit()

if args.input_image:
    input_path = [Path(args.input_image)]
else:
    in_dir = Path(args.input_dir)
    input_path = [f for f in in_dir.glob('*')]

if not os.path.exists(out_dir) and out_dir != '.':
    os.mkdir(out_dir)


for f in input_path:
    input_image = Image.open(f)
    trans_image = remove(input_image)
    trans_pixel = trans_image.getpixel((0, 0))
    output_image = Image.new(input_image.mode, input_image.size)
    for i in range(input_image.height):
        for j in range(input_image.width):
            if trans_image.getpixel((j, i)) == trans_pixel:
                output_image.putpixel((j, i), (255, 255, 255))
            else:
                output_image.putpixel((j, i), input_image.getpixel((j, i)))
    out_name = "removedbg_" + os.path.basename(f)
    if out_dir != '.':
        output_image.save(out_dir + "/" + out_name)
    else:
        output_image.save(out_name)
    print("saved : " + out_name)
