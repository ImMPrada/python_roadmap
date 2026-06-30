---
title: "🧩 Recap dominguero: todo lo que aprendiste de operators"
date: 2026-07-05
thread_id: ""
channel: "python"
---

¡Lo lograste! 🎉 Cerramos la semana de **operators**. Hagamos un repaso rápido para que te quede grabado:

- ➕ **Arithmetic**: `+ - * / // % **` — y acuérdate: `/` siempre da `float`, `//` es **floor division**.
- ⚖️ **Comparison**: `== != < > <= >=` — devuelven `bool` y se pueden encadenar (`0 <= x <= 10`).
- 🧠 **Logical**: `and`, `or`, `not` — con **short-circuit** para no evaluar de más.
- 🛠️ **Assignment**: `= += -= *=` — actualizan una **variable** usando su valor previo.
- 🔍 **Membership**: `in`, `not in` — buscan dentro de un `list` o un `string`.
- 🔢 **Bitwise**: `& | ^ << >>` — para trabajar con bits.

📘 Si quieres una referencia para tener a la mano, esta tabla de W3Schools resume todos los operators con ejemplos: **Python Operators** → https://www.w3schools.com/python/python_operators.asp

---

🤔 **Reto integrador de cierre — el validador de claves**

Pide (o define) un `string` `clave` y valida que cumpla **todo** esto a la vez, usando `and` y `len()`:

1. Tenga más de `8` caracteres (`len(clave) > 8`).
2. Contenga al menos un número del 0 al 9 (pista: un `loop` + membership `in`).
3. No contenga espacios (`" " not in clave`).

Imprime `True` o `False` según si es una clave válida. 🔐

Pega tu solución en el hilo 👇. ¿Qué operator se te hizo más útil esta semana? Cuéntame. ¡Nos vemos la próxima! 🚀
