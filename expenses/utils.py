from random import random, randrange

from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from cmapy import color

from .models import ExpenseType


def generate_color(user):
    old_colors = ExpenseType.objects.filter(user=user).values_list('color', flat=True)
    
    while True:
        # r = hex(int(random()*(1 << 24)))
        # new_color = "#"+("00000" + r)[-6:]
        # rgb = sRGBColor.new_from_rgb_hex(new_color)
        # print(new_color)

        # levels = range(32,256,32) 
        # colors = tuple(choice(levels) for _ in range(3))
        # rgb = sRGBColor(colors[0],colors[1], colors[2], is_upscaled=True)
        # print(colors,rgb)
        
        colors = color('gist_ncar_r', randrange(0, 256,1), rgb_order=True)
        rgb = sRGBColor(colors[0],colors[1], colors[2], is_upscaled=True)
        #return rgb.get_rgb_hex()
        print(rgb)
        new_color_lab = convert_color(rgb, LabColor)

        for old_color in old_colors:
            color_lab = convert_color(sRGBColor.new_from_rgb_hex(old_color), LabColor)
            delta= delta_e_cie2000(color_lab, new_color_lab)

            print(delta)
            if delta>50:
                return rgb.get_rgb_hex()

  #"#"+("00000" + ((Math.random() * (1 << 24)) | 0).toString(16)).slice(-6)
# number_of_colors = 8

# color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
#              for i in range(number_of_colors)]
# print(color)


  #https://docs.opencv.org/4.5.1/d3/d50/group__imgproc__colormap.html#ga9a805d8262bcbe273f16be9ea2055a65
  #https://stackoverflow.com/questions/28999287/generate-random-colors-rgb
  #https://dev.to/tejeshreddy/color-difference-between-2-colours-using-python-182b