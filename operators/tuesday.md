---
title: "➕ Operators: los símbolos que hacen trabajar a Python"
date: 2026-06-30
thread_id: "1521519265004650570"
channel: "python"
---

¡Arrancamos semana! 🚀 Esta semana le vamos a meter el diente a los **operators**: esos símbolos y palabras clave que le dicen a Python qué hacer con tus valores y tus **variables**.

En Python hay varias familias:

- **Arithmetic**: `+ - * / // % **` para cálculos
- **Comparison**: `== != < > <= >=` para comparar
- **Logical**: `and or not` para combinar condiciones
- **Assignment**: `= += -=` para guardar y actualizar
- **Membership**: `in`, `not in` para buscar dentro de un `list` o un `string`

Empecemos por los aritméticos:

```python
print(7 + 2)   # 9
print(7 - 2)   # 5
print(7 * 2)   # 14
print(7 / 2)   # 3.5
```

👀 **Curiosidad colombiana de Python**: fíjate que `7 / 2` te da `3.5` y NO `3`. En Python 3, el operator `/` SIEMPRE devuelve un `float`, aunque la división sea exacta:

```python
print(10 / 2)   # 5.0  (¡no 5!)
print(type(10 / 2))  # <class 'float'>
```

Si lo que tú quieres es la división entera (sin decimales), existe el **floor division** `//`. Pero eso lo vemos más adelante esta semana. 😉

Cuéntame en el hilo: ¿qué te dio más curiosidad, que `/` devuelva `float`? Mañana seguimos con los **comparison operators**. 💪
