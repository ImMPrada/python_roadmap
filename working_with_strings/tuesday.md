---
title: "🧵 Strings: cómo Python guarda el texto"
date: 2026-06-30
thread_id: "1521519311582269623"
channel: "python"
---

¡Buenas, parceros! 🙌 Esta semana le metemos el diente a una de las cosas que más vas a usar en tu vida programando: los **strings**, o sea el **texto**.

Un **string** es simplemente una secuencia de caracteres: letras, números, espacios, emojis... lo que sea. En Python los creas encerrando el texto entre comillas. Y aquí viene lo bonito: tienes tres formas de hacerlo 👇

```python
sencillas = 'Hola, mundo'
dobles    = "Hola, mundo"
triples   = """Esto puede
ocupar varias
líneas"""
```

Tres ideas clave para arrancar:

- 💬 Comillas **simples** y **dobles** funcionan igual. Usa las dobles cuando tu texto lleva un apóstrofe: `"It's Python"` te evita dolores de cabeza.
- 📜 Las comillas **triples** sirven para un **multiline string** (texto de varias líneas) sin tener que hacer malabares.
- 🔒 Ojo con esto: los **strings** son **immutable**. Una vez creado, no puedes cambiar un carácter por dentro. Si quieres "modificarlo", en realidad creas uno nuevo. Lo veremos en detalle esta semana.

¿Por qué importa? Porque casi todo lo que tu programa le muestra a un usuario es **texto**: nombres, mensajes, datos de un archivo, respuestas de una API. Dominar **strings** es dominar la comunicación de tu código. 🚀

👉 Para calentar: crea una **variable** con tu frase favorita usando comillas dobles y haz un `print` de ella. Pégala en el hilo. ¡Vamos con toda! 💪
