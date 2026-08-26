#!/usr/bin/env python3
"""Pega las capturas de menú que existan en la galería de ajustes-a6700.md.

Uso:  python3 referencia/img/menus/insertar.py

Recorre esta carpeta, mira qué archivos del guion (README.md) están ya
hechos y reconstruye la sección "Las pantallas, una a una" al final de
referencia/ajustes-a6700.md. Es idempotente: ejecútalo las veces que quieras.
"""
import pathlib
import sys

AQUI = pathlib.Path(__file__).resolve().parent
GUIA = AQUI.parent.parent / "ajustes-a6700.md"

INICIO = "<!-- CAPTURAS:INICIO -->"
FIN = "<!-- CAPTURAS:FIN -->"

# (archivo, pie de foto) en el orden del guion
PANTALLAS = [
    ("formato-archivo.jpg",    "`Toma → [Calid. img/grab.] → [Formato archivo]` — RAW"),
    ("tipo-archivo-raw.jpg",   "`Toma → [Calid. img/grab.] → [Tipo archivo RAW]` — comprimido sin pérdida"),
    ("rr-exposic-larga.jpg",   "`Toma → [Calid. img/grab.] → [RR exposic. larga]` — Desactivar"),
    ("rr-iso-alta.jpg",        "`Toma → [Calid. img/grab.] → [RR ISO Alta]`"),
    ("mem-ajustes-cam.jpg",    "`Toma → [Modo de toma] → [Mem. ajustes cám]` — guardar MR1/MR2/MR3"),
    ("modo-manejo.jpg",        "`Toma → [Modo de manejo] → [Modo manejo]` — Continuo Hi+"),
    ("tipo-de-obturador.jpg",  "`Toma → [Obturad./silenc.] → [Tipo de obturador]` — electrónico en la charca"),
    ("func-capt-interv.jpg",   "`Toma → [Func. capt. interv.]` — el intervalómetro integrado"),
    ("steadyshot.jpg",         "`Toma → [Estabiliz. de img] → [SteadyShot]`"),
    ("formatear.jpg",          "`Toma → [Soporte] → [Formatear]`"),
    ("iso-auto-limites.jpg",   "`Exposición/color → [Exposición] → [ISO]` — con ISO AUTO máximo y mínimo"),
    ("nivel-de-cebra.jpg",     "`Exposición/color → [Visualizac. cebra] → [Nivel de cebra]` — 100 IRE o +"),
    ("visualizac-cebra.jpg",   "`Exposición/color → [Visualizac. cebra]` — Activar"),
    ("modo-medicion.jpg",      "`Exposición/color → [Modo medición]`"),
    ("balance-blanco.jpg",     "`Exposición/color → [Balance blanco]` — en Kelvin"),
    ("modo-de-enfoque.jpg",    "`Enfoque → [AF/MF] → [Modo de enfoque]` — AF-C"),
    ("af-con-disparador.jpg",  "`Enfoque → [AF/MF] → [AF con disparador]` — Desactivar (enfoque al pulgar)"),
    ("sens-seguim-af.jpg",     "`Enfoque → [AF/MF] → [Sens. Seguim. AF]`"),
    ("area-de-enfoque.jpg",    "`Enfoque → [Área de enfoque] → [Área de enfoque]`"),
    ("dest-reconocim.jpg",     "`Enfoque → [Reconoc. motivo] → [Dest. reconocim.]` — Animal"),
    ("rec-motivo-af.jpg",      "`Enfoque → [Reconoc. motivo] → [Rec. motivo en AF]` — Activar"),
    ("visualiz-resalte.jpg",   "`Enfoque → [Visualiz. resalte]` — el peaking del enfoque manual"),
    ("ajuste-t-pers-dial.jpg", "`Ajustes → [Personal. operac.] → [Ajuste t. pers./dial]`"),
    ("ajustes-menu-fn.jpg",    "`Ajustes → [Personal. operac.] → [Ajustes del menú Fn]`"),
    ("mi-menu.jpg",            "`Mi Menú → [Ajuste Mi Menú]`"),
    ("ampliacion.jpg",         "`Reproducción → [Ampliación]`"),
    ("restablecer-ajuste.jpg", "`Ajustes → [Rest/guard ajust] → [Restablecer ajuste]`"),
    ("menu-fn.jpg",            "**El menú Fn**, con las 12 casillas del día a día"),
    ("mi-menu-relleno.jpg",    "**Mi Menú** ya relleno, que es como debería quedar"),
    ("pantalla-de-toma.jpg",   "**La pantalla de toma** con histograma y Zebra"),
]


def main() -> int:
    hechas = [(f, pie) for f, pie in PANTALLAS if (AQUI / f).exists()]
    if not hechas:
        print("Todavía no hay ninguna captura en", AQUI)
        print("El guion está en", AQUI / "README.md")
        return 0

    lineas = [INICIO, ""]
    for archivo, pie in hechas:
        lineas += [f'<img src="img/menus/{archivo}" alt="{pie}" width="46%">', "",
                   f"<sub>{pie}</sub>", ""]
    lineas.append(FIN)
    bloque = "\n".join(lineas)

    texto = GUIA.read_text()
    if INICIO in texto and FIN in texto:
        antes = texto[:texto.index(INICIO)]
        despues = texto[texto.index(FIN) + len(FIN):]
        GUIA.write_text(antes + bloque + despues)
    else:
        print("No encuentro los marcadores de la galería en", GUIA)
        return 1

    faltan = len(PANTALLAS) - len(hechas)
    print(f"{len(hechas)} capturas insertadas en {GUIA.name}"
          + (f" · faltan {faltan}" if faltan else " · guion completo"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
