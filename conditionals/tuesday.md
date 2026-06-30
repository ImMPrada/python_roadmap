---
title: "🚦 Conditionals: enséñale a Python a tomar decisiones"
date: 2026-06-30
thread_id: "1521519316036620328"
channel: "python"
---

¡Arrancamos semana! 🚀 Esta semana le metemos el diente a los **conditionals**: la forma en que tu programa toma decisiones y hace cosas distintas según lo que esté pasando.

La idea es sencilla: *"SI se cumple esta condición, haz esto; SI NO, haz esto otro"*. En Python eso se escribe con **if**, **elif** y **else**:

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad ✅")
else:
    print("Eres menor de edad ⛔")
```

Tres claves para que no te enrede:

- La condición después de `if` se evalúa a un valor **booleano**: `True` o `False`.
- Fíjate en los dos puntos `:` al final de la línea del `if`.
- Lo que pasa "adentro" del `if` va con **indentation** (4 espacios). Esa sangría NO es decoración: es la que le dice a Python qué código pertenece a cada bloque.

Mira cómo cambia el resultado solo con cambiar la **variable** `edad`:

```python
edad = 15
if edad >= 18:
    print("Puedes entrar")
else:
    print("Todavía no 🙃")
# Imprime: Todavía no 🙃
```

Cuéntame en el hilo: ¿en qué situación de la vida real te imaginas usando un `if`? 💬 Mañana combinamos condiciones con **operators** para hacerlas más potentes. 💪
