---
title: "🤯 Curiosidad: las variables son etiquetas, no cajas"
date: 2026-07-02
thread_id: ""
channel: "python"
---

El martes te dije que una **variable** era como una cajita. Es una buena imagen para arrancar… pero hoy te cuento la verdad completa 😏

En Python, una **variable** en realidad es más como una **etiqueta** (un nombre) que apunta a un dato que vive en memoria. El dato no está "metido adentro" del nombre; el nombre solo lo señala. 🏷️➡️📦

Mira este detalle que confunde a medio mundo:

```python
a = 10
b = a      # b apunta al mismo valor que a
a = 99     # cambio a... ¿qué pasa con b?

print(a)   # 99
print(b)   # 10  👈 b NO cambió
```

`b` se quedó apuntando al `10` original. Reasignar `a` solo movió **esa etiqueta** a otro valor. Entender esto te evita bugs raros más adelante. 🐛

Otra curiosidad: como Python deduce el tipo solo (eso se llama **dynamic typing**), una misma variable puede cambiar de tipo en pleno vuelo:

```python
dato = 5        # ahora es int
dato = "cinco"  # ahora es str, ¡y Python ni se queja!
```

Cómodo, sí, pero también peligroso si te descuidas. 👀

📄 **Recurso del día:** "Variables in Python" de Real Python. Es de lo mejorcito para afianzar esto:
https://realpython.com/python-variables

👉 Para reflexionar en el hilo: en el primer ejemplo, ¿por qué crees que `b` siguió valiendo `10`? Explícalo con tus palabras. 💬
