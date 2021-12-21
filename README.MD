# mikm.py
convert(VAL, "mi") approximates conversion VAL from miles to kilometers

convert(VAL, "km") approximates conversion VAL from kilometers to miles

Works by breaking down VAL into the sum of the largest component Fibonacci numbers and increments up or down as required.

---

Eg.

convert(10, "mi") --> 8 + 2 --> 13 + 3 --> 16km (10mi = 16.0934km)

convert(10, "km") --> 8 + 2 --> 5 + 1 --> 6mi (10km = 6.2137km)
