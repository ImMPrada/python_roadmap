#!/usr/bin/env python3
"""Calendario de una semana (Lunes-Domingo) con festivos nacionales de Colombia.

Usa la API pública de https://calendariosnacionales.com (sin autenticación).
Dada una fecha de referencia, calcula la semana que la contiene (L-D) y marca
qué días son festivos nacionales.

Uso:
    python3 festivos_semana.py [YYYY-MM-DD]

Si no se pasa fecha, usa la fecha de hoy.
"""
import datetime
import json
import sys
import urllib.error
import urllib.request

API = "https://calendariosnacionales.com/co/v1/{year}/nacionales.json"
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


def fetch_year(year):
    """Descarga los festivos nacionales de un año. Devuelve {fecha_iso: nombre}."""
    url = API.format(year=year)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (festivos-cli)"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        raise SystemExit(f"Error {e.code} consultando {url} "
                         f"(¿año fuera de rango? La API cubre 2025-2027).")
    except urllib.error.URLError as e:
        raise SystemExit(f"No se pudo conectar a la API: {e.reason}")
    return {h["date"]: h["name"] for h in data.get("holidays", [])}


def week_range(ref):
    """Devuelve la lista de 7 fechas (Lunes a Domingo) que contienen ref."""
    monday = ref - datetime.timedelta(days=ref.weekday())  # weekday(): Lun=0
    return [monday + datetime.timedelta(days=i) for i in range(7)]


def holidays_for_week(week):
    """Mapa fecha_iso -> nombre festivo, cubriendo posible cruce de año."""
    years = {week[0].year, week[-1].year}
    hmap = {}
    for y in sorted(years):
        for iso, name in fetch_year(y).items():
            hmap.setdefault(iso, name)
    return hmap


def main():
    if len(sys.argv) > 1:
        try:
            ref = datetime.date.fromisoformat(sys.argv[1])
        except ValueError:
            raise SystemExit(f"Fecha inválida: {sys.argv[1]!r}. Formato esperado YYYY-MM-DD.")
    else:
        ref = datetime.date.today()

    week = week_range(ref)
    hmap = holidays_for_week(week)

    festivos = []
    print(f"Semana del {week[0].isoformat()} al {week[-1].isoformat()}\n")
    for i, d in enumerate(week):
        iso = d.isoformat()
        name = hmap.get(iso)
        marca = f"🎉 FESTIVO — {name}" if name else ""
        print(f"  {DIAS[i]:10} {iso}  {marca}")
        if name:
            festivos.append((iso, DIAS[i], name))

    print()
    if festivos:
        print(f"Festivos esta semana: {len(festivos)}")
        for iso, dia, name in festivos:
            print(f"  - {dia} {iso}: {name}")
    else:
        print("No hay festivos nacionales esta semana.")


if __name__ == "__main__":
    main()
