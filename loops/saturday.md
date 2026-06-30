---
title: "✨ Trucos de loops que te hacen ver pro"
date: 2026-07-04
thread_id: ""
channel: "python"
---

Sábado relajado, pero con joyitas que separan a un principiante de alguien que ya escribe Python bonito. 😎

**1. `enumerate()` — índice y valor al tiempo**

¿Necesitas el número de posición *y* el elemento? No uses un contador manual:

```python
equipos = ["Nacional", "Millonarios", "Junior"]

for i, equipo in enumerate(equipos, start=1):
    print(f"{i}. {equipo}")
```

**2. `zip()` — recorre dos listas en paralelo**

```python
nombres = ["Ana", "Luis"]
edades = [25, 30]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
```

**3. Nested loops — un loop dentro de otro**

Útiles para grillas o combinaciones. Ojo: cuidado con el rendimiento si las listas son enormes.

```python
for fila in range(1, 4):
    for col in range(1, 4):
        print(f"({fila},{col})", end=" ")
    print()
```

🧠 **Curiosidad:** Python tiene un `for ... else` (¡sí, un `else` pegado al loop!). El bloque `else` se ejecuta **solo si el loop terminó sin `break`**. Es raro al principio, pero muy útil para búsquedas:

```python
for n in [2, 4, 6]:
    if n % 2 != 0:
        print("Encontré un impar")
        break
else:
    print("Todos eran pares ✅")
```

👉 Reto corto: usa `enumerate()` para imprimir tu **list** favorita de canciones numerada. Pégala en el thread. 🎶
