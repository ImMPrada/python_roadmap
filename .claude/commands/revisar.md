---
description: Revisa los to_check.md de los temas activos y chulea los días vencidos; cierra el tema en to_do.md cuando ya no queda nada por revisar
---

Lanza el agente `to-check-reviewer` para actualizar las listas de revisión de **hoy**
(hora Colombia).

El agente debe:
1. Leer `./to_do.md` y tomar solo los temas **sin chulear** `[ ]`.
2. En cada `./<tema>/to_check.md`, chulear `[x]` los días cuya fecha `revisar antes de`
   ya llegó o pasó (`hoy >= deadline`).
3. Cuando **todos** los días de un tema queden chuleados, chulear ese tema en
   `./to_do.md`.

Úsalo a través del agente `to-check-reviewer` (no repliques su lógica aquí).
Al terminar, reporta qué chuleó y qué temas cerró, o si no había nada que hacer.
