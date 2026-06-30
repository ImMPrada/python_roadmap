---
title: "🧠 Recap + una curiosidad sobre strings inmutables"
date: 2026-07-05
thread_id: ""
channel: "python"
---

¡Cerramos la semana de **strings**! 🎉 Hagamos un recap rapidito de todo lo que ya tienes en tu caja de herramientas:

- 🧵 Creas **strings** con comillas simples, dobles o triples.
- 🔢 Sacas pedazos con **indexing** (`texto[0]`) y **slicing** (`texto[0:5]`), contando desde **0**.
- 🛠️ Los transformas con **methods**: `.upper()`, `.strip()`, `.replace()`, `.split()`...
- ✨ Los armas elegante con **f-strings**: `f"Hola {nombre}"`.

🤔 **Curiosidad para reflexionar — la inmutabilidad:**

Dijimos que los **strings** son **immutable**. Mira por qué esto importa de verdad:

```python
saludo = "hola"
saludo[0] = "H"   # 💥 TypeError: 'str' object does not support item assignment
```

¡No se puede! Para "cambiarlo" tienes que crear uno nuevo:

```python
saludo = "H" + saludo[1:]   # 'Hola'  -> nuevo string, no el mismo modificado
```

¿Por qué Python lo diseñó así? Porque la inmutabilidad hace los **strings** más **seguros** y **rápidos**: se pueden compartir en memoria sin miedo a que algo los cambie por sorpresa. Es una decisión de diseño, no un capricho. 🧩

📄 Y si te quedaste con ganas de los **multiline strings** (texto de varias líneas con `"""`), aquí hay una guía completa: https://roadmap.sh/python/multiline-strings

👉 **Para cerrar:** cuéntanos en el hilo cuál fue tu mayor "ajá" 💡 de la semana con **strings**. ¿El **slicing** al revés? ¿Los **f-strings**? ¿La inmutabilidad? La próxima semana seguimos. ¡Orgullo verte aprender! 🙌
