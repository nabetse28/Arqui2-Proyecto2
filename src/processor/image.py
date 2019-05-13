from PIL import Image

f = open("image.txt", "r")
cadena = f.read()
# print(cadena)
image = cadena.split("\n")
# print(image)
# print(len(image))  # 16385
size = len(image)
size_1 = (size - 1) // 2
size_2 = size_1 + 1
print(size_1)
print(size_2)
image_list1 = []
image_list2 = []
for x in range(0, size_1):
    image_list1.append(int(image[x]))

for y in range(size_2, size - 1):
    image_list2.append(int(image[y]))


# print(image_list1)
im1 = Image.new('L', (128, 128))
im1.putdata(image_list1)
im1.save("encriptado2.jpg")

im2 = Image.new('L', (128, 128))
im2.putdata(image_list2)
im2.save("desencriptado2.jpg")
