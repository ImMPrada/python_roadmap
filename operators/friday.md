---
title: "🛠️ Reto del viernes: assignment, membership y floor division"
date: 2026-07-03
thread_id: ""
channel: "python"
---

¡Viernes de reto! 🎉 Hoy juntamos tres herramientas nuevas en un solo ejercicio.

**1) Assignment operators** — actualizar una **variable** usando su valor actual:

```python
puntos = 10
puntos += 5    # equivale a: puntos = puntos + 5  -> 15
puntos -= 3    # 12
puntos *= 2    # 24
```

**2) Membership operators** — `in` y `not in` para buscar dentro de un `list` o un `string`:

```python
frutas = ["mango", "lulo", "guanábana"]
print("lulo" in frutas)        # True
print("pera" not in frutas)    # True
print("man" in "mango")        # True  (¡también sirve en strings!)
```

**3) Floor division** `//` y **modulo** `%` — lo prometido el martes:

```python
print(17 // 5)   # 3  (división entera, sin decimales)
print(17 % 5)    # 2  (el residuo)
```

📄 Para reforzar: **Python Division: Operators, Floor Division and Examples** → https://roadmap.sh/python/division

---

🏆 **Reto del día — el repartidor justo**

Tienes `73` arepas 🫓 y quieres repartirlas en partes iguales entre `8` amigos. Escribe un programa que, usando `//` y `%`, imprima:

1. Cuántas arepas le tocan a cada uno (parte entera).
2. Cuántas sobran (el residuo).
3. Un mensaje usando un membership operator que diga si `"sobran"` aplica, es decir, si el residuo es distinto de `0`.

Pega tu solución en el hilo 👇 y mañana comparamos enfoques. ¡Tú puedes! 💪
