---
title: "✨ f-strings: la mejor forma de armar texto"
date: 2026-07-03
thread_id: ""
channel: "python"
---

Hoy lo más útil de la semana: cómo **juntar texto con datos**. Hay varias formas, pero te voy a mostrar cuál usar y por qué. 🎁

La forma vieja era **concatenar** con `+`:

```python
nombre = "Sofía"
edad = 25
print("Hola, " + nombre + ", tienes " + str(edad) + " años")
```

Funciona, pero es incómodo: te toca poner espacios a mano y convertir todo a `str`. 😮‍💨

La forma moderna y limpia es el **f-string** (le pones una `f` antes de las comillas):

```python
nombre = "Sofía"
edad = 25
print(f"Hola, {nombre}, tienes {edad} años")
```

Y lo mejor: dentro de las llaves `{}` puedes meter **expresiones** y hasta formato:

```python
precio = 12000
print(f"Total: ${precio:,} COP")        # Total: $12,000 COP
print(f"La mitad de {edad} es {edad/2}")  # La mitad de 25 es 12.5
print(f"{nombre.upper()} está aprendiendo")
```

Por qué el **f-string** gana:

- ✅ Se lee clarísimo: ves el texto y los datos en su lugar.
- 🔢 Convierte los números por ti, no necesitas `str()`.
- 🎨 Permite formato: separador de miles, decimales, alineación.

¿Y si necesitas un salto de línea dentro del texto? Usas `\n`. 📄 Aquí hay una guía buenísima sobre eso: https://roadmap.sh/python/print-new-line

👉 **Mini-ejercicio:** crea variables `producto`, `cantidad` y `precio_unitario`, y con un solo **f-string** imprime algo como `"3 x Café = $9,000 COP"`. Pégalo en el hilo. 🚀
