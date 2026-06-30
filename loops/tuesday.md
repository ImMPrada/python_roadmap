---
title: "🔁 Loops: enséñale a Python a repetir por ti"
date: 2026-06-30
thread_id: "1521519322713821189"
channel: "python"
---

¡Arrancamos semana de **loops**! 🚀

Un **loop** es una estructura que te deja ejecutar un bloque de código **muchas veces** sin tener que copiar y pegar lo mismo una y otra vez. Es de las herramientas más poderosas que vas a usar como programador, porque casi todo en la vida real es repetición: recorrer una **list**, procesar líneas de un archivo, sumar valores, etc.

En Python tienes dos tipos principales:

- **`for` loop** → cuando sabes *sobre qué* vas a iterar (una `list`, un `string`, un rango de números).
- **`while` loop** → cuando repites *mientras* una condición siga siendo verdadera.

Mira la diferencia con un ejemplo bobito: saludar 3 veces.

```python
# Sin loop (repetitivo y feo 😅)
print("Hola")
print("Hola")
print("Hola")

# Con un for loop (limpio y escalable ✨)
for i in range(3):
    print("Hola")
```

¿Y qué tal si fueran 1000 saludos? Con el loop solo cambias el número. Esa es la magia. 💡

Fíjate en la **indentation**: el código que se repite va **indentado** dentro del loop. En Python eso no es decoración, es obligatorio.

👉 Cuéntame en el thread: ¿alguna vez has copiado y pegado código casi idéntico varias veces? Eso casi siempre es un loop esperando a nacer. Esta semana le ponemos fin a eso. 💪
