---
title: "🤯 Truthy y falsy: lo que Python considera 'verdadero'"
date: 2026-07-03
thread_id: ""
channel: "python"
---

Curiosidad del viernes que le vuela la cabeza a mucha gente 🤯: en Python **no necesitas comparar contra `True`**. Cualquier valor se puede usar directamente en un `if`, porque Python lo trata como **truthy** (cuenta como verdadero) o **falsy** (cuenta como falso).

Estos valores son **falsy** (es decir, el `if` NO entra):

- `0`, `0.0`
- `""` (un `string` vacío)
- `[]` (un `list` vacío)
- `None`
- `False`

Casi todo lo demás es **truthy**. Mira qué elegante queda:

```python
nombre = ""

if nombre:
    print(f"Hola, {nombre} 👋")
else:
    print("Aún no me has dicho tu nombre 🙈")
# Imprime: Aún no me has dicho tu nombre 🙈
```

Esto te evita escribir cosas como `if len(nombre) > 0:`. Más limpio y muy "pythonico". ✨

Y de ñapa, el **ternary operator**: un `if`/`else` en una sola línea, ideal para asignar valores:

```python
edad = 20
mensaje = "mayor" if edad >= 18 else "menor"
print(mensaje)   # mayor
```

📄 **Recurso recomendado** para afianzar todo lo de esta semana: *"Conditional Statements in Python"* de Real Python → https://realpython.com/python-conditional-statements/

🎯 **Reto rápido:** escribe un programa que reciba un `list` y, usando su valor truthy/falsy, imprima `"La lista está vacía"` o cuántos elementos tiene. Mañana viene el reto grande de la semana. 🔥
