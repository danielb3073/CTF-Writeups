## XOR Starter ##

# key = "label"
# result = ""

# for c in key:
#     x = (ord(c)^13)
#     result += (chr(x))

# print("crypto{" + result + "}")

## XOR Properties ##

# Commutative: A ⊕ B = B ⊕ A
# Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# Identity: A ⊕ 0 = A
# Self-Inverse: A ⊕ A = 0

## You either know, XOR you don't ##

# key = "myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkey"
# xor_str = bytearray.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104").decode()

# a_list = [chr(ord(a) ^ ord(b)) for a,b in zip(key, xor_str)]
# print(a_list)
# s3 = "".join(a_list)
# print(s3)

# from PIL import Image, ImageChops

# im1 = Image.open("flag.png")
# im2 = Image.open("lemur.png")

# result = ImageChops.add(ImageChops.subtract(im2, im1), ImageChops.subtract(im1, im2))

# result.save('result.png')

