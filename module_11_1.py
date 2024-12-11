from PIL import Image, ImageFilter

img = Image.open("52.jpg")
print(img.size)
# меняем размер картинки
new_size = (800, 500)
img.thumbnail(new_size)
# сохраняем
img.save("52-2.jpg")

img2 = Image.open("елка2.jpg")
img2.thumbnail(new_size)
img2.save("елка.jpg")

img1 = Image.open("52.jpg")
# фильтр
img = img1.filter(ImageFilter.EDGE_ENHANCE)
img.save("52-3.jpg")
# меняем формат на .png
img = Image.open("52-2.jpg")
new_name = "520.png"
img.save(new_name)
# меняем формат на .png
img = Image.open("елка.jpg")
new_name = "530.png"
img.save(new_name)


img1 = Image.open("520.png")
img2 = Image.open("530.png")
img = Image.blend(img1, img2, 0.5)
img.save("елка-33.png")
