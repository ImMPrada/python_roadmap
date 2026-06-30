---
title: "➡️ El for loop: recorre cualquier cosa sin sudar"
date: 2026-07-01
thread_id: ""
channel: "python"
---

Hoy nos metemos de lleno con el **`for` loop**, el más usado del día a día. 🧰

La idea es sencilla: tomas una secuencia (una `list`, un `string`, un `range`) y la recorres **elemento por elemento**.

```python
frutas = ["mango", "lulo", "guanábana"]

for fruta in frutas:
    print(f"Me encanta el {fruta}")
```

En cada vuelta, la **variable** `fruta` toma el valor del siguiente elemento. ¡Tú no manejas índices a mano, Python lo hace por ti! 🙌

¿Y si necesitas números? Para eso está **`range()`**:

```python
for i in range(1, 6):   # del 1 al 5 (el 6 NO entra)
    print(i)
```

Dato clave: `range(1, 6)` llega hasta **5**, no hasta 6. El límite superior es **exclusivo**. Es el error #1 de los que arrancan, así que tenlo presente. ⚠️

También puedes recorrer un **`string`** caracter por caracter:

```python
for letra in "Python":
    print(letra)
```

🏋️ **Mini-ejercicio del día:**
Escribe un `for` loop que imprima la **tabla de multiplicar del 7** (del 7x1 al 7x10), usando una **f-string** así: `7 x 1 = 7`.

Pega tu solución en el thread. 👇

📄 ¿Quieres profundizar? Échale ojo a este artículo de Real Python sobre `for` loops:
https://realpython.com/python-for-loop/
