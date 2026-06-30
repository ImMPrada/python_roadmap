---
title: "🔢 Los data types básicos que vas a usar todos los días"
date: 2026-07-01
thread_id: ""
channel: "python"
---

Ayer guardamos datos en variables. Pero, ¿qué *tipo* de dato estamos guardando? Hoy conocemos los **data types** básicos de Python 👇

```python
edad = 23           # int     -> números enteros
precio = 19.99      # float   -> números con decimales
nombre = "Camilo"   # str     -> texto (string)
activo = True       # bool    -> verdadero o falso
```

Los cuatro grandes para empezar:

- 🔢 **int**: números enteros, sin decimales (`7`, `-3`, `1000`).
- 🌊 **float**: números con punto decimal (`3.14`, `0.5`).
- 🔤 **str** (*string*): cualquier texto, va entre comillas (`"hola"`).
- ✅ **bool**: solo dos valores posibles, `True` o `False`.

¿No sabes qué tipo tiene una variable? Pregúntale a Python con la **function** `type()`:

```python
print(type(edad))     # <class 'int'>
print(type(precio))   # <class 'float'>
print(type(nombre))   # <class 'str'>
```

Ojo con un detalle clásico: `23` es un **int**, pero `"23"` (entre comillas) es un **str**. Se ven igual pero NO son lo mismo. De eso hablamos el viernes 👀

👉 Mini-ejercicio: crea una variable de cada tipo (un **int**, un **float**, un **str** y un **bool**) y usa `type()` para confirmarlo. Comparte tu resultado en el hilo. 🙌
