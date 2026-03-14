# Python *args va **kwargs Funksiyalari

Ushbu repository Python dasturlash tilida yozilgan funksiyalar orqali `*args` va `**kwargs` dan qanday foydalanishni ko‘rsatadi. Bu misollar funksiyalarga o‘zgaruvchan miqdordagi argumentlarni uzatish va ular bilan ishlashni tushunishga yordam beradi.

## 📌 Maqsad

* `*args` yordamida bir nechta positional argumentlarni qabul qilish
* `**kwargs` yordamida kalit-so‘z (keyword) argumentlar bilan ishlash
* Moslashuvchan va qayta foydalanish mumkin bo‘lgan funksiyalar yozishni o‘rganish

## 🧠 Misol

```python
# *args
def args(son, *args):
    print(f"Son -> ning qiymati: {son}")
    print(f"ARGS -> ning qiymati: {args}")

x, x1, x2, x3, x4, x5 = map(int, input("Sonlarni kiriting: ").split())
args(x, x2, x3, x4, x5)

# **kwargs
def args(son, **kwargs):
    print(f"Son -> ning qiymati: {son}")
    print(f"KWARGS -> ning qiymati: {kwargs}")

x, x1, x2, x3, x4, x5 = map(int, input("Sonlarni kiriting: ").split())
args(x, bir=x2, ikki=x3, uch=x4, tort=x5)
```

## 📚 Foydali mavzular

* `*args` – o‘zgaruvchan positional argumentlar
* `**kwargs` – o‘zgaruvchan keyword argumentlar

## 👨‍💻 Muallif

[realljavohir](https://github.com/realljavohir)
