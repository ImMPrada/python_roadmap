---
title: "🪆 Nested conditionals: ifs dentro de ifs (sin enredarte)"
date: 2026-07-02
thread_id: ""
channel: "python"
---

A veces una decisión depende de otra. Ahí entran los **nested conditionals**: un `if` que vive adentro de otro `if`. 🪆

Imagínate un cajero: primero revisa si tu clave es correcta, y solo entonces revisa si tienes saldo:

```python
clave_ok = True
saldo = 50000
retiro = 80000

if clave_ok:
    if retiro <= saldo:
        print("Retiro exitoso 💸")
    else:
        print("Fondos insuficientes 🚫")
else:
    print("Clave incorrecta ❌")
# Imprime: Fondos insuficientes 🚫
```

Fíjate en la **indentation**: cada nivel suma 4 espacios más. El `if` interno está "más adentro" porque depende del externo.

💡 **Consejo:** anidar demasiado vuelve el código difícil de leer. Muchas veces puedes aplanarlo combinando condiciones con `and`:

```python
if clave_ok and retiro <= saldo:
    print("Retiro exitoso 💸")
```

🎯 **Mini-ejercicio de hoy:** simula el ingreso a un parque. Si la persona tiene un `ticket` válido, revisa adentro si es `vip` para mandarla a la fila preferencial o a la fila normal. Si no tiene `ticket`, no entra.

Compártelo en el hilo 👇 ¿Te quedó más claro anidar o aplanar con `and`?
