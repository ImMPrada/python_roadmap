---
title: "🔗 elif y operators lógicos: condiciones con más cerebro"
date: 2026-07-01
thread_id: ""
channel: "python"
---

Ayer vimos `if`/`else`. Hoy le sumamos dos cosas que vas a usar todos los días: **elif** y los **logical operators**. 🧠

Cuando tienes más de dos caminos, encadenas con `elif` (que es "else if"):

```python
nota = 4.2

if nota >= 4.5:
    print("Excelente 🌟")
elif nota >= 3.0:
    print("Aprobaste ✅")
else:
    print("Toca repetir 😅")
# Imprime: Aprobaste ✅
```

Python evalúa de arriba hacia abajo y se queda con el **primer** bloque cuya condición sea `True`. Por eso el orden importa.

Para combinar varias condiciones usas **and**, **or** y **not**:

```python
edad = 20
tiene_entrada = True

if edad >= 18 and tiene_entrada:
    print("¡Bienvenido al concierto! 🎶")
```

- `and` → se deben cumplir **todas** las condiciones.
- `or` → basta con que se cumpla **al menos una**.
- `not` → invierte el valor (`not True` es `False`).

🎯 **Mini-ejercicio de hoy:** escribe un `if` que reciba una **variable** `temperatura` y que imprima `"Hace calor 🥵"` si está por encima de 30, `"Rico clima 😎"` si está entre 20 y 30, y `"Hace frío 🥶"` si está por debajo de 20.

Pega tu solución en el hilo 👇 Mañana practicamos con **nested conditionals**.
