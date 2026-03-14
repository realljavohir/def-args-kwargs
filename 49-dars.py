# def -> define (yaratish, sozlash)

# 1) qiymat qaytarmaydigan funksiya
def salomlash():
    print("Assalomu aleykum, xush kelibsiz!")
salomlash()

# 2) qiymat qaytaradigan funksiya
def salomlash_2():
    return "Assalomu aleykum, xush kelibsiz!"
print(salomlash_2())

def biografika(ism):
    print(f"Assalomu aleykum, sizning ismingiz {ism}")
x = input("Izmingizni kiriting: ")
biografika(x)

def biografika(ism, yosh):
    print(f"Assalomu aleykum, sizning ismingiz {ism}")
    print(f"Sizning yoshingiz {yosh}")
x = input("Izmingizni kiriting: ")
y = input("Yoshingizni kiriting: ")
biografika(x, y)

#ARGS
def args(son, *args):
    print(f"Son -> ning qiymati: {son}")
    print(f"ARGS -> ning qiymati: {args}")

x, x1, x2, x3, x4, x5 = map(int, input("Sonlarni kiriting: ").split())
args(x, x2, x3, x4, x5)

# KWARGS
def args(son, **kwargs):
    print(f"Son -> ning qiymati: {son}")
    print(f"KWARGS -> ning qiymati: {kwargs}")

x, x1, x2, x3, x4, x5 = map(int, input("Sonlarni kiriting: ").split())
args(x, bir=x2, ikki=x3, uch=x4, tort=x5)