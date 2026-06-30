---
title: "🔄 El while loop: repite mientras la condición aguante"
date: 2026-07-02
thread_id: ""
channel: "python"
---

Turno del **`while` loop**. ⏳

Mientras el `for` recorre algo que ya conoces, el `while` repite **mientras una condición sea `True`**. Es perfecto cuando *no sabes* cuántas vueltas vas a dar.

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1   # ⚠️ ¡súper importante!
```

Ese `contador += 1` es vital: si se te olvida actualizar la condición, el loop **nunca termina** → un **infinite loop** y tu programa se queda colgado. 😱

Dos palabras mágicas para controlar loops:

- **`break`** → rompe y sale del loop de una.
- **`continue`** → se salta el resto de la vuelta y pasa a la siguiente.

```python
while True:
    respuesta = input("Escribe 'salir': ")
    if respuesta == "salir":
        break          # 👋 chao loop
    print("Sigues adentro...")
```

🧠 **Curiosidad:** `while True:` parece un loop infinito a propósito, ¡y lo es! Pero combinado con `break` es un patrón clásico para menús y validaciones. No le tengas miedo.

🏋️ **Mini-ejercicio del día:**
Haz un `while` loop que cuente **de 10 hacia atrás hasta 1** y al final imprima `"¡Despegue! 🚀"`.

Compártelo en el thread. 👇

📄 Para dominar los `while`: https://realpython.com/python-while-loop/
