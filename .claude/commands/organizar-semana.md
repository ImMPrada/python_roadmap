---
description: Organiza la semana de un tema — redacta los posts (planner) y corrige el voseo (corrector) en un solo paso
argument-hint: "<tema>  (ej: Basic syntax)"
---

Organiza la semana completa para el tema: **$ARGUMENTS**.

Ejecuta los agentes en orden y espera a que cada uno termine antes del siguiente:

1. Lanza `roadmap-week-planner` con:
   - topic: `$ARGUMENTS`
   - roadmap.sh link: `https://roadmap.sh/python`
   - discord channel: `python`

   Crea la carpeta `./<tema>/` con un `.md` por día hábil (salta festivos),
   `to_check.md`, y agrega el tema a `./to_do.md`.

2. Cuando el planner termine, lanza `tuteo-corrector` sobre el mismo tema
   (`$ARGUMENTS`) como red de seguridad para corregir cualquier voseo → tú.

3. Reporta el resultado combinado: archivos creados, días saltados por festivo,
   recursos destacados, y cuántas correcciones de voseo aplicó el corrector.

Nota: esto es DRAFT ONLY — no publica nada en Discord (el `thread_id` queda vacío).
