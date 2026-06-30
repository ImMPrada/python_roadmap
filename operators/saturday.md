---
title: "🔢 Sábado de curiosidades: el modulo y los bitwise operators"
date: 2026-07-04
thread_id: ""
channel: "python"
---

Sábado relajado, pero con dos joyitas de los operators. ✨

**El operator `%` (modulo) es más útil de lo que parece.** Te da el residuo de una división, y eso sirve para un montón de cosas del día a día:

```python
# ¿Un número es par o impar?
numero = 7
print(numero % 2 == 0)   # False -> es impar

# ¿El año es bisiesto? (versión simplificada)
anio = 2024
print(anio % 4 == 0)     # True
```

📄 Guía completa: **Python Modulo Operator (%): Complete Guide with Examples** → https://roadmap.sh/python/modulo

---

**Curiosidad: los bitwise operators** 🤯

Estos trabajan con los números en su forma **binaria** (bits). No los vas a usar todos los días, pero es bueno saber que existen:

```python
print(5 & 3)   # 1   AND bit a bit
print(5 | 3)   # 7   OR  bit a bit
print(5 ^ 3)   # 6   XOR bit a bit
print(5 << 1)  # 10  corre los bits a la izquierda (¡multiplica por 2!)
```

Fíjate que `5 << 1` da `10`: correr un bit a la izquierda es como multiplicar por 2. Por eso a veces se usan en código de bajo nivel y optimizaciones. 😎

🎯 **Ejercicio cortico**: usando `%`, escribe una línea que diga si el número `100` es múltiplo de `5`. Pega tu respuesta en el hilo.

Mañana cerramos la semana con un recap. 🧩
