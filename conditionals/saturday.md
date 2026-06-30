---
title: "🔥 Reto del sábado: arma tu propio FizzBuzz"
date: 2026-07-04
thread_id: ""
channel: "python"
---

¡Sábado de reto! 🔥 Hoy juntamos todo lo de la semana en un clásico que cae hasta en entrevistas de trabajo: el **FizzBuzz**.

**Las reglas** para un número:

- Si es divisible por 3 **y** por 5 → imprime `"FizzBuzz"`
- Si solo es divisible por 3 → imprime `"Fizz"`
- Si solo es divisible por 5 → imprime `"Buzz"`
- Si no → imprime el número tal cual

La herramienta clave es el operator módulo `%`, que te da el residuo de una división. Si `n % 3 == 0`, entonces `n` es divisible por 3. 👇

```python
n = 15

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
# Imprime: FizzBuzz
```

⚠️ **Cuidado con el orden:** la condición de `"FizzBuzz"` (la más estricta) va **primero**. Si la pones de última, nunca se ejecuta, porque `n % 3 == 0` la atraparía antes. Acuérdate de lo que vimos el miércoles: Python se queda con el primer `True`.

🎯 **Tu reto:** prueba tu bloque de `if`/`elif`/`else` con estos valores y pega el resultado en el hilo 👇

```python
# Pruébalo con: 9, 10, 30, 7
```

¿Te atreves a hacerlo para los números del 1 al 20? (pista: vas a necesitar un `loop`, que es justo lo que viene pronto 😏). Mañana cerramos con una joya: **match-case**. 💪
