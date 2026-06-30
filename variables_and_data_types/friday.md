---
title: "🔄 Convertir tipos: de string a int y de vuelta"
date: 2026-07-03
thread_id: ""
channel: "python"
---

El miércoles quedó una intriga: `23` es un **int** pero `"23"` es un **str**. Hoy aprendemos a **convertir** un tipo en otro, algo que se llama **type casting** o *casting*. 🔧

Las **functions** estrella para esto son `int()`, `float()`, `str()` y `bool()`:

```python
texto = "23"
numero = int(texto)      # ahora es un int de verdad
print(numero + 1)        # 24 ✅

precio = 19.99
print(str(precio))       # "19.99" -> ahora es texto
```

¿Por qué esto importa tanto en la vida real? Porque cuando le pides datos al usuario con `input()`, **siempre te llega un string**, aunque la persona escriba un número:

```python
edad = input("¿Cuántos años tienes? ")
print(type(edad))        # <class 'str'> 😮 ¡aunque escribas 30!

edad = int(edad)         # lo convertimos para poder hacer cuentas
print(f"En 10 años tendrás {edad + 10}")
```

Si intentas hacer `edad + 10` sin convertir, Python te lanza un `TypeError`. Es uno de los errores más comunes cuando arrancas. 🐛

📄 **Recurso del día:** "Python for Beginners: Data Types" — un repaso suave y claro de tipos y conversiones:
https://thenewstack.io/python-for-beginners-data-types/

👉 Mini-ejercicio: pide dos números con `input()`, conviértelos a **int** y muestra su suma con un f-string. Pega tu código en el hilo. 🙌
