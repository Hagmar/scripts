import argparse
from PIL import Image, ImageDraw, ImageFont

CHARS = [chr(i) for i in range(32, 127)]


def main():
    args = parse_args()

    fnt = ImageFont.truetype('~/Library/Fonts/Hack Bold Nerd Font Complete.ttf', args.font_size)
    font_w, font_h = get_font_size(args.font_size, fnt)
    char_density = generate_char_density(fnt, (font_w, font_h))

    regions = get_regions(args.image, font_w, font_h)
    map_regions_to_chars(char_density, regions)


def map_regions_to_chars(char_density, regions):
    char_density_list = sorted(char_density.items(), key=lambda x: x[1])
    max_char_density = char_density_list[-1][1]

    max_region_density = 0
    for i in range(len(regions)):
        for j in range(len(regions[i])):
            regions[i][j] = sum(map(sum, regions[i][j].getdata()))
            max_region_density = max(max_region_density, regions[i][j])

    density_scale = max_char_density / max_region_density

    output = []
    for r_density in regions:
        for r_d in r_density:
            output.append(find_closest_char(char_density_list, r_d, density_scale))
        output.append('\n')

    print(''.join(output))


def find_closest_char(char_density_list, density, density_scale):
    target_density = density * density_scale
    char = min(char_density_list, key=lambda x: abs(x[1]-target_density))
    return char[0]


def get_regions(image, font_w, font_h):
    with Image.open(image) as im:
        im = im.convert('LA')
        img_w, img_h = im.size
        new_img = Image.new('RGB', im.size)
        h = 0
        w = 0
        regions = []
        while h <= img_w:
            region_list = []
            regions.append(region_list)
            while w <= img_w:
                region = im.crop((w, h, w+font_w, h+font_h))
                region_list.append(region)
                w += font_w
            w = 0
            h += font_h
    return regions


def generate_char_density(fnt, size):
    char_density = {}
    for c in CHARS:
        img = Image.new('RGB', size, color='white')
        d = ImageDraw.Draw(img)
        d.text((0, 0), c, font=fnt, fill='black')
        char_density[c] = sum(map(sum, img.getdata()))
    return char_density


def get_font_size(font_size, fnt):
    d = ImageDraw.Draw(Image.new('RGB', (font_size, font_size)))
    sizes = [d.textsize(c, font=fnt) for c in CHARS]
    max_w = max(sizes, key=lambda s: s[0])[0]
    max_h = max(sizes, key=lambda s: s[1])[1]

    return (max_w, max_h)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('image', help='Image file to turn into ASCII')
    parser.add_argument('--font-size', default=15, type=int, help='Font size')

    return parser.parse_args()


if __name__ == '__main__':
    main()
