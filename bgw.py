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

WHITE = (255, 255, 255)

for f in input_path:
    input_image = Image.open(f)
    trans_image = remove(input_image, alpha_matting=True,
                alpha_matting_foreground_threshold=240,
                alpha_matting_background_threshold=10,
                alpha_matting_erode_size=6)

    trans_image.load()
    save_image = Image.new("RGB", trans_image.size, WHITE)
    save_image.paste(trans_image, mask=trans_image.split()[3])

    out_name = "removedbg_" + os.path.splitext(os.path.basename(f))[0] + ".jpg"
    
    if out_dir != '.':
        save_image.save(out_dir + "/" + out_name)
    else:
        save_image.save(out_name)

    print("saved : " + out_name)
