# Python *args va **kwargs Funksiyalari

Ushbu repository Python dasturlash tilida yozilgan funksiyalar orqali `*args` va `**kwargs` dan qanday foydalanishni ko‘rsatadi. Bu misollar funksiyalarga o‘zgaruvchan miqdordagi argumentlarni uzatish va ular bilan ishlashni tushunishga yordam beradi.

## 📌 Maqsad

* `*args` yordamida bir nechta positional argumentlarni qabul qilish
* `**kwargs` yordamida kalit-so‘z (keyword) argumentlar bilan ishlash
* Moslashuvchan va qayta foydalanish mumkin bo‘lgan funksiyalar yozishni o‘rganish

## 🧠 Misol

```python
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(add_numbers(1, 2, 3, 4))
print_info(name="Ali", age=21, city="Tashkent")
```

## 📚 Foydali mavzular

* `*args` – o‘zgaruvchan positional argumentlar
* `**kwargs` – o‘zgaruvchan keyword argumentlar

## 👨‍💻 Muallif

[realljavohir](https://github.com/realljavohir)
