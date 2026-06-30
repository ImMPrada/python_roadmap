---
title: "🎁 match-case: el cierre elegante de la semana"
date: 2026-07-05
thread_id: ""
channel: "python"
---

Cerramos la semana con una herramienta más moderna (desde Python 3.10): el **match-case statement**. Es el primo ordenado de una cadena larga de `elif`. 🎁

Cuando comparas una misma **variable** contra muchos valores posibles, esto:

```python
comando = "guardar"

if comando == "abrir":
    print("Abriendo archivo 📂")
elif comando == "guardar":
    print("Guardando 💾")
elif comando == "salir":
    print("Cerrando 👋")
else:
    print("Comando desconocido 🤷")
```

...se puede escribir más limpio así:

```python
comando = "guardar"

match comando:
    case "abrir":
        print("Abriendo archivo 📂")
    case "guardar":
        print("Guardando 💾")
    case "salir":
        print("Cerrando 👋")
    case _:
        print("Comando desconocido 🤷")
# Imprime: Guardando 💾
```

El `case _:` es el comodín (equivale al `else`): atrapa todo lo que no coincidió. ✨

**Recap de la semana** 🧠:

- `if` / `elif` / `else` para decidir caminos.
- `and`, `or`, `not` para combinar condiciones.
- **Nested conditionals** y por qué a veces es mejor aplanarlos.
- Valores **truthy** / **falsy** y el **ternary operator**.
- **FizzBuzz** y el operator `%`.
- **match-case** para comparar contra muchos valores.

📄 **Para profundizar:** *"Python Switch Statement 101: Match-case and alternatives"* → https://roadmap.sh/python/switch

🎯 **Reflexión final:** ¿en qué momento usarías `match-case` en vez de `if`/`elif`? Déjamelo en el hilo 👇 ¡Excelente semana, tú puedes! 💪
