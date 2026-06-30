---
description: Publica en Discord los posts del día (temas activos en to_do.md) creando los hilos y guardando el thread_id
---

Lanza el agente `daily-discord-publisher` para publicar el contenido de **hoy**
(hora Colombia).

El agente debe:
1. Leer `./to_do.md` y tomar solo los temas **sin chulear** `[ ]`.
2. En cada carpeta de tema, encontrar el `.md` con `date` = hoy y `thread_id` vacío.
3. Crear el hilo en Discord (nombre = `title`), postear el cuerpo dentro, y escribir
   el `thread_id` de vuelta en el archivo.
4. Ser idempotente (no re-publicar lo que ya tiene `thread_id`).

Úsalo a través del agente `daily-discord-publisher` (no repliques su lógica aquí).
Al terminar, reporta qué se publicó o si no había nada para hoy.
