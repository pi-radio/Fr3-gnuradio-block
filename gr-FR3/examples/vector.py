from PIL import Image

img_path = 'Untitled.png'  
img = Image.open(img_path).convert('L').resize((64, 64))

width, height = img.size
complex_points = []


for y in range(height):
    for x in range(width):
        pixel_value = img.getpixel((x, y))
        if pixel_value < 128:
            i = (x / (width - 1)) * 2.0 - 1.0
            q = -((y / (height - 1)) * 2.0 - 1.0) 
            complex_points.append(complex(i, q))

print("Generated Vector for GNU Radio:")
print(repr(complex_points))
