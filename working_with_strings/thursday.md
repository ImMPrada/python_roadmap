---
title: "🛠️ String methods: tu caja de herramientas para texto"
date: 2026-07-02
thread_id: ""
channel: "python"
---

Python trae un montón de **methods** (métodos) ya listos para transformar **strings** sin que tú reinventes la rueda. 🧰 Estos son los que vas a usar TODOS los días:

```python
frase = "  Aprendiendo Python en Colombia  "

print(frase.upper())      # '  APRENDIENDO PYTHON EN COLOMBIA  '
print(frase.lower())      # '  aprendiendo python en colombia  '
print(frase.strip())      # 'Aprendiendo Python en Colombia' (quita espacios de los bordes)
print(frase.replace("Colombia", "Medellín"))
print("hola,mundo,python".split(","))  # ['hola', 'mundo', 'python']
```

Cositas para tener presente:

- 🔁 Como los **strings** son **immutable**, estos **methods** NO cambian el original: te **devuelven uno nuevo**. Por eso casi siempre haces `frase = frase.strip()`.
- 🧹 `.strip()` es oro puro para limpiar datos que vienen de un usuario o de un archivo.
- 🔎 Hay muchísimos más: `.startswith()`, `.endswith()`, `.find()`, `.count()`, `.title()`... no los memorices todos, solo conoce que existen.

🎥 **Recurso de hoy:** un video corto y muy claro sobre métodos de strings — "String methods in Python are easy": https://www.youtube.com/watch?v=tb6EYiHtcXU

👉 **Mini-ejercicio:** toma `nombre = "   juAN pErEz   "` y déjalo limpio y bien formateado como `"Juan Perez"` usando **methods** encadenados. Pista: mira `.strip()` y `.title()`. Pega tu resultado en el hilo. 💪
