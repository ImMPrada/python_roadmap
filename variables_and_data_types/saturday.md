---
title: "🏆 Reto del sábado: arma una mini ficha de usuario"
date: 2026-07-04
thread_id: ""
channel: "python"
---

¡Llegó el reto fuerte de la semana! 💪 Hoy vas a juntar TODO lo que vimos: **variables**, **data types** y **casting**.

Pero antes, un tipo nuevo que te va a servir: **None**. Es un valor especial que significa "aquí todavía no hay nada". Su tipo se llama **NoneType** y se usa muchísimo para representar datos que aún no existen o que faltan. 🕳️

```python
telefono = None          # todavía no lo sabemos
print(type(telefono))    # <class 'NoneType'>
print(telefono is None)  # True
```

### 🎯 El reto

Arma una **ficha de usuario** usando variables de distintos tipos:

```python
nombre = "Daniela"       # str
edad = 27                # int
estatura = 1.65          # float
es_estudiante = True     # bool
apodo = None             # NoneType (aún no tiene)

print(f"Nombre: {nombre}")
print(f"Edad: {edad} | Estatura: {estatura} m")
print(f"¿Estudia?: {es_estudiante}")
print(f"Apodo: {apodo}")
```

Para subir el nivel 🚀:

- 📥 Pide al menos un dato con `input()` y recuerda hacer el **casting** (acuérdate que `input()` siempre devuelve **str**).
- 🧮 Calcula algo derivado, por ejemplo el año aproximado de nacimiento: `2026 - edad`.
- 🏷️ Usa nombres de variable descriptivos.

📘 **Recurso del día:** guía oficial sobre **None** y los valores faltantes en Python:
https://roadmap.sh/python/null

👉 Comparte tu ficha completa en el hilo. ¡Muéstranos de qué eres capaz! 🔥
