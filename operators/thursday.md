---
title: "🧠 and, or, not: pensando en lógica con Python"
date: 2026-07-02
thread_id: ""
channel: "python"
---

Llegaron los **logical operators**: `and`, `or` y `not`. Con ellos combinas varias condiciones en una sola decisión. 🔗

```python
edad = 20
tiene_documento = True

print(edad >= 18 and tiene_documento)   # True
print(edad < 18 or tiene_documento)     # True
print(not tiene_documento)              # False
```

La regla mental rápida:

- `and` → **todas** las condiciones deben ser `True`
- `or` → con que **una** sea `True`, basta
- `not` → le da la vuelta: `True` se vuelve `False`

⚡ **Curiosidad: short-circuit evaluation**. Python es perezoso (en el buen sentido 😏). En un `and`, si la primera parte ya es `False`, ni siquiera evalúa la segunda, porque el resultado ya no puede cambiar:

```python
def saluda():
    print("¡me ejecuté!")
    return True

False and saluda()   # NO imprime nada: se cortó antes
True or saluda()      # Tampoco imprime: con or ya bastaba el True
```

📘 Si quieres profundizar en `not`, roadmap.sh tiene una guía completa: **Python not Operator: The Complete Guide to Logical Negation** → https://roadmap.sh/python/not-operator

🎯 **Mini-ejercicio**: crea las **variables** `tiene_boleta` y `es_mayor_de_edad` (ambas `bool`) y arma una condición que sea `True` solo si la persona puede entrar a un concierto 🎶 (necesita las dos). Comparte tu solución en el hilo.

Mañana viene un reto más grande con `+=`, `in` y `//`. 🔥
