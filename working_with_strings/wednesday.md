---
title: "🔢 Indexing y slicing: agarra el pedazo que necesitas"
date: 2026-07-01
thread_id: ""
channel: "python"
---

Hoy aprendes a **sacar partes** de un **string**. Esto se llama **indexing** (un solo carácter) y **slicing** (un pedazo). 🎯

En Python cada carácter tiene una posición, y se cuenta **desde cero**:

```python
palabra = "Python"
#          0123456
print(palabra[0])   # 'P'  -> primer carácter
print(palabra[-1])  # 'n'  -> el último (índices negativos cuentan desde el final)
```

Para **slicing** usas `[inicio:fin]`, donde `fin` NO se incluye:

```python
texto = "Programando en Colombia"
print(texto[0:11])   # 'Programando'
print(texto[15:])    # 'Colombia'  -> sin fin = hasta el final
print(texto[:11])    # 'Programando' -> sin inicio = desde el principio
print(texto[::-1])   # 'aibmoloC ne odnamargorP' -> ¡al revés! 🤯
```

Tres claves:

- 0️⃣ Se empieza a contar en **0**, no en 1. Esto confunde al principio, pero te acostumbras rápido.
- ➖ Los índices **negativos** son tu amigo para llegar al final sin contar.
- ✂️ En `[a:b]`, el carácter `b` queda por fuera. Piénsalo como "hasta antes de b".

👉 **Mini-ejercicio:** toma `correo = "ana@gmail.com"` y usa **slicing** para imprimir solo `"ana"`. Pega tu solución en el hilo y cuéntanos qué índices usaste. 💬
