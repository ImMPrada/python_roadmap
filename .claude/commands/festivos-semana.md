---
description: Muestra el calendario de una semana (Lunes-Domingo) e indica qué días son festivos nacionales en Colombia
argument-hint: "[YYYY-MM-DD]  (opcional; por defecto la semana actual)"
allowed-tools: Bash(python3 scripts/festivos_semana.py:*)
---

Ejecuta el script `scripts/festivos_semana.py` para obtener el calendario de la
semana (Lunes a Domingo) que contiene la fecha dada y saber qué días son
festivos nacionales en Colombia.

Datos desde la API pública de https://calendariosnacionales.com (cobertura 2025-2027).

Argumento: `$ARGUMENTS` — una fecha `YYYY-MM-DD` opcional. Si está vacío, usa la semana actual.

Pasos:
1. Ejecuta: `python3 scripts/festivos_semana.py $ARGUMENTS`
2. Presenta al usuario la semana con cada día y resalta claramente los festivos.
3. Si hubo un error (fecha inválida o año fuera del rango 2025-2027), explícalo brevemente.
