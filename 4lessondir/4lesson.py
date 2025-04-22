from PIL import Image

image = Image.open("monro.jpg")
rgb_image = image.convert("RGB")

red, green, blue = rgb_image.split()

a = 50
b = 25
c = 0

coord_1 = (a, c, red.width, red.height)
red_1 = red.crop(coord_1)

coord_2 = (b, c,red.width - b,red.height)
red_2 = red.crop(coord_2)


red_3 = Image.blend(red_1, red_2, 0.5)


coord_3 = (a, c, blue.width, blue.height)
blue_1 = blue.crop(coord_3)

coord_4 = (b, c, blue.width - b, blue.height)
blue_2 = blue.crop(coord_4)


blue_3 = Image.blend(blue_1, blue_2, 0.5)


coord_5 = (b, c, green.width - b, green.height)
green_2 = green.crop(coord_5)

new_image = Image.merge("RGB", (red_3, green_2, blue_3))
new_image.save("color_monro.jpg")

new_image.thumbnail((80, 80))
new_image.save("mini_monro.jpg")
