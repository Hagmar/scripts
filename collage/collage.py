from PIL import Image
import argparse
import os
import random
import sys


class Collage:
    def __init__(self, args):
        if not os.path.isfile(args.image):
            print('Please provide a path to an existing image')
            sys.exit(1)
        elif args.minscale > args.maxscale:
            print('Smallest scaling must be smaller than the largest scaling')
            sys.exit(2)

        self.image = Image.open(args.image)
        self.input_width, self.input_height = self.image.size
        self.width = args.width
        self.height = args.height
        self.minscale = args.minscale / 100
        self.maxscale = args.maxscale / 100

        self.output_image = Image.new('RGBA', (self.width, self.height))
        self.n = args.count

    def resize_and_rotate(self):
        scale = self.minscale + (random.random() * (self.maxscale - self.minscale))
        new_width = int(self.input_width * scale)
        new_height = int(self.input_height * scale)
        rotation = random.random() * 360

        resized = self.image.resize((new_width, new_height))
        rotated = resized.rotate(rotation, expand=1)
        #print('Minscale: {}\nMaxscale: {}\nScale: {}\nOriginal size: {}\nNew size: {}\nRotation: {}'.format(
        #    self.minscale, self.maxscale, scale, self.image.size, resized.size, rotation))
        return rotated
    
    def apply_image(self, new_image):
        new_x, new_y = new_image.size
        position_x = random.randint(0, self.width) - (new_x // 2)
        position_y = random.randint(0, self.height) - (new_y // 2)
        self.output_image.paste(new_image, (position_x, position_y), new_image)

    def apply_layer(self):
        transformed = self.resize_and_rotate()
        self.apply_image(transformed)

    def create(self):
        for _ in range(self.n):
            self.apply_layer()

    def show(self):
        self.output_image.show()


def main():
    args = parse_args()
    collage = Collage(args)
    collage.create()
    collage.show()
    

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('image', help='Image to use in collage')
    parser.add_argument('--width', type=int, default=1280, help='Collage width')
    parser.add_argument('--height', type=int, default=720, help='Collage height')
    parser.add_argument('--count', type=int, default=50, help='Number of instances of the image to include')
    parser.add_argument('--minscale', type=int, default=50, help='Smallest scaling of image (in percent)')
    parser.add_argument('--maxscale', type=int, default=150, help='Largest scaling of image (in percent)')

    return parser.parse_args()

if __name__ == '__main__':
    main()
