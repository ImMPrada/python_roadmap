---
title: "🏆 Reto del viernes: tu primera calculadora de IMC"
date: 2026-07-03
thread_id: ""
channel: "python"
---

¡Llegó el viernes de reto! 🎉 Hoy vamos a juntar todo lo de esta semana en un programita real: una **calculadora de IMC** (Índice de Masa Corporal).

La idea es practicar **variables**, conversión de tipos, operaciones y un **f-string** bien armado.

Empieza con esta base:

```python
# Pedimos datos al usuario con input()
peso = float(input("Tu peso en kg: "))      # convertimos el texto a float
estatura = float(input("Tu estatura en m: "))

imc = peso / (estatura ** 2)   # ** es elevar a una potencia

print(f"Tu IMC es {imc:.2f}")  # :.2f deja solo 2 decimales
```

Fíjate en dos detalles finos 👀:

- 🔄 `input()` siempre devuelve un **string**, por eso lo envolvemos en `float()` para poder hacer cuentas.
- 🎯 Dentro del **f-string**, `{imc:.2f}` formatea el número a 2 decimales. Limpiecito.

---

🎯 **El reto (nivel +1):**

Amplía el programa para que, además del número, imprima una categoría:

- IMC < 18.5 → "Bajo peso"
- 18.5 a 24.9 → "Peso normal"
- 25 o más → "Sobrepeso"

Pista: vas a necesitar un `if / elif / else` con su **indentation** bien puesta (acuérdate del miércoles 😉).

📨 Sube tu solución al hilo. El finde revisamos las mejores. ¡Dale que tú puedes! 💪
