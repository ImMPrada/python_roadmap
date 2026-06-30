---
title: "⚖️ Comparar valores: los comparison operators"
date: 2026-07-01
thread_id: ""
channel: "python"
---

Hoy le toca el turno a los **comparison operators**: los que comparan dos valores y siempre te devuelven un `bool` (`True` o `False`). 🤔

```python
print(5 == 5)   # True   (¿son iguales?)
print(5 != 3)   # True   (¿son diferentes?)
print(5 > 3)    # True
print(5 <= 4)   # False
```

⚠️ El error clásico de quien arranca: confundir `=` con `==`.

- `=` es **assignment**: guarda un valor en una **variable**.
- `==` es **comparison**: pregunta si dos cosas son iguales.

```python
edad = 18        # assignment: guardo 18
print(edad == 18)  # comparison: ¿es igual a 18? -> True
```

Y algo bonito de Python: puedes **encadenar** comparaciones de forma natural, casi como en matemáticas:

```python
nota = 4.2
print(3.0 <= nota <= 5.0)   # True  (¿está entre 3.0 y 5.0?)
```

🎯 **Mini-ejercicio**: crea una **variable** `temperatura` con cualquier número y escribe una comparación que diga si está entre `18` y `25` (un clima rico 😎). Pega tu código en el hilo y comparamos respuestas.

Mañana combinamos condiciones con `and`, `or` y `not`. ¡Te espero! 🙌
