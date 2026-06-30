---
title: "🏆 Reto del sábado: un validador de contraseñas"
date: 2026-07-04
thread_id: ""
channel: "python"
---

¡Llegó el reto fuerte de la semana! 💪 Hoy vas a juntar TODO lo que aprendiste de **strings**: **indexing**, **slicing**, **methods** y **f-strings**.

🎯 **El reto:** escribe un programa que reciba un **string** con una contraseña y te diga si es **segura** o no. Una contraseña segura debe cumplir:

- Tener al menos **8 caracteres** (pista: `len(password)`).
- Tener al menos **una mayúscula** y **una minúscula**.
- Tener al menos **un número**.

Para esto te van a servir métodos como `.isupper()`, `.islower()`, `.isdigit()` recorriendo cada carácter. Aquí va un esqueleto para que arranques:

```python
password = "Python2026"

tiene_mayus = any(c.isupper() for c in password)
tiene_minus = any(c.islower() for c in password)
tiene_num   = any(c.isdigit() for c in password)
larga       = len(password) >= 8

if larga and tiene_mayus and tiene_minus and tiene_num:
    print(f"✅ '{password}' es una contraseña segura")
else:
    print(f"❌ '{password}' es débil, mejórala")
```

🔥 **Para subir el nivel** (opcional): que tu programa imprima EXACTAMENTE qué regla falló, por ejemplo "te falta un número" o "es muy corta".

📘 Si quieres ver la lista completa de operaciones sobre strings, la documentación oficial es tu mejor aliada: https://docs.python.org/3/library/string.html

👉 Pega tu solución en el hilo y prueba las contraseñas de tus compañeros para ver si tu validador las "rompe". ¡A darle! 🚀
