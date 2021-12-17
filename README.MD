# mikim.py
mikim(VAL, "mi") approximates conversion VAL from miles to kilometers

mikim(VAL, "km") approximates conversion VAL from kilometers to miles

Works by breaking down VAL into the sum of the largest component Fibonacci numbers and increments up or down as required.

Eg.
mikim(10, "mi") --> 8 + 2 --> 13 + 3 --> 16km (10mi = 16.0934km)
