---
title: "🤯 Curiosidad: en Python los espacios SÍ importan"
date: 2026-07-01
thread_id: ""
channel: "python"
---

Dato curioso que vuela cabezas a quienes vienen de otros lenguajes: en Python la **indentation** (la sangría) no es solo por estética... ¡es parte de la sintaxis! 😮

En lenguajes como Java o C, los bloques de código van entre llaves `{ }`. En Python, el bloque se define por los **espacios** al inicio de la línea:

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")  # esta línea pertenece al if
    print("Puedes votar")        # esta también
print("Esto se imprime siempre")  # sin sangría, fuera del if
```

Si te equivocas en la indentation, Python te tira un `IndentationError` y no corre. Por eso la regla de oro:

- 📏 Usa **4 espacios** por nivel (es la convención oficial, el famoso PEP 8).
- 🚫 No mezcles `tabs` y espacios en el mismo archivo.

La idea detrás es preciosa: como el código BIEN escrito ya se indenta para que se lea fácil, Python decidió que esa misma indentation defina la estructura. Código legible = código que funciona. 🧘

💬 ¿Alguna vez te ha mordido un error de indentation? Cuenta tu historia en el hilo 👇
