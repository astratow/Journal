import colorgram

rgb_colors =[]
colors = colorgram.extract('img/image.jpeg', 50)

print(colors)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

print(rgb_colors)