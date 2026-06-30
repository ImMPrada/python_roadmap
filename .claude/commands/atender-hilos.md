---
description: Atiende los hilos de Discord con actividad nueva — el scanner detecta dudas/ejercicios sin responder y el tutor responde en cada hilo
---

Atiende los hilos abiertos de los temas activos. Orquesta el handoff entre dos agentes:

1. Lanza `thread-scanner`. Lee `./to_do.md` (temas sin chulear), encuentra los hilos
   publicados (`thread_id` no vacío) con **actividad de estudiantes sin responder**, y
   devuelve, por cada hilo que necesita atención, su transcript y metadatos
   (`topic`, `channel_id`, `thread_id`, `bot_id`, `last_bot_message_id`).

2. Para CADA hilo que el scanner reporte como "necesita atención", lanza un
   `discord-tutor` (uno por hilo) pasándole esos datos y el transcript. El tutor
   responde con UN mensaje consolidado en español colombiano (tuteo), basado en el
   contenido del tema en roadmap.sh.
   - Puedes lanzar varios `discord-tutor` en paralelo (uno por hilo) ya que son
     independientes.

3. Si el scanner no encuentra hilos con actividad nueva, no lances ningún tutor.

Al terminar, reporta: cuántos hilos tenían actividad, en cuáles respondió el tutor, y
si hubo alguna advertencia (p. ej. falta el MESSAGE CONTENT intent del bot).
