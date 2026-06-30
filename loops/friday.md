---
title: "🏆 Reto del viernes: el cajero automático en Python"
date: 2026-07-03
thread_id: ""
channel: "python"
---

¡Viernes de **reto fuerte**! Hoy juntamos todo lo de la semana: `while`, `break`, `continue` y condicionales. 💪

🎯 **El reto: un mini cajero automático**

Tu programa debe:

1. Guardar un **saldo** inicial, por ejemplo `saldo = 100000`.
2. Usar un **`while` loop** que muestre un menú una y otra vez:
   - `1` → Consultar saldo
   - `2` → Retirar dinero
   - `3` → Salir
3. Si el usuario retira **más de lo que tiene**, le avisas y **no** modificas el saldo (usa `continue` o un `if`).
4. Cuando elija `3`, sales con `break` y te despides.

Una base para arrancar:

```python
saldo = 100000

while True:
    print("\n--- Cajero ---")
    print("1. Consultar saldo")
    print("2. Retirar")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(f"Tu saldo es ${saldo}")
    elif opcion == "2":
        monto = int(input("¿Cuánto quieres retirar? "))
        # 👉 completa tú: valida que haya saldo suficiente
        ...
    elif opcion == "3":
        print("¡Gracias por usar el cajero! 👋")
        break
    else:
        print("Opción inválida 🤔")
```

🧩 **Bonus (opcional):** lleva un **contador** de cuántos retiros se hicieron y muéstralo al salir.

No hay una sola respuesta correcta. Sube tu versión al thread y comparamos enfoques. ¡Tú puedes! 🔥
