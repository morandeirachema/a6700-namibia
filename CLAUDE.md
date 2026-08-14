# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Qué es este repo

Guía de fotografía en **español** de la **Canon 5D Mark III** para un viaje a Namibia: safari diurno, charcas nocturnas de Etosha y astrofotografía (el viaje coincide con luna nueva). Solo Markdown más los PDF generados de las hojas de campo: no hay build, lint ni tests. Publicar = commit y push a `main` (https://github.com/morandeirachema/5dmk3-namibia).

Equipo real del viaje (condiciona las recomendaciones): cuerpo prestado + Samyang 14mm f/2.8 EF propio (sin contactos: la cámara marca f/00) + Sigma 150-600 Contemporary EF + GoPro MISSION 1 con empuñadura-batería Volta 2, para vídeo, timelapses nocturnos y bici (ojo, la "Hero 14" no existe) + Canon 650D como posible respaldo. El móvil del viaje es un Pixel 10 Pro. El autor valoró y **descartó** un Seestar S30 Pro — no reintroducir contenido de telescopios inteligentes.

## Estructura

- `5dmk3/` — capítulos `00`–`05` (móvil→cámara, configuración, astro, safari diurno, charcas nocturnas, equipo), el anexo de la 650D de respaldo (`anexo-650d.md`) + dos hojas de campo imprimibles: `chuleta.md` y `verificacion-in-situ.md`.
- `comun/` — guías transversales: lista de tomas, mejores horas, el cielo del viaje (catálogo astro de la quincena, `cielo-del-viaje.md`), la guía de la GoPro por niveles (`gopro-mission-1.md`, con la lista de tomas del vídeo-recuerdo), apps del viaje, histograma, balance de blancos, edición básica, paisaje de Namibia, logística y limpieza en campo. El README ordena todo esto como ruta de aprendizaje en tres niveles.
- `mejora/` — el salto "de la foto correcta a la foto buena": `parte-1-principiante.md` (plan de charcas, comportamiento, el cielo real de noviembre), `parte-2-avanzado.md` (AF a medida, plan de la noche hora a hora) y `safari-a-fondo.md` (luz, velocidad, apertura, Kelvin y encuadre como decisiones creativas).
- `pdf/` — versiones PDF maquetadas de las hojas de campo (chuleta, verificación in situ, lista de tomas), generadas desde el Markdown; al editar una hoja, regenerar su PDF.
- `README.md` — índice con fotos CC de Wikimedia Commons (mantener la atribución al editarlas).

Existió una guía paralela de la Sony A7 III y una comparativa: fueron **borradas a petición del autor** (quedan solo en el historial de git, hasta el commit `3975191`). No reintroducir contenido de la A7 III.

## Contrato editorial (fijado por el autor)

- **Audiencia**: novato que viene sobre todo del móvil. Nada de teoría: recetas con valores concretos, pasos numerados y tablas de "si la foto sale mal, toca esto". Cada capítulo sigue ese patrón — mantenerlo en contenido nuevo.
- **Equipo**: siempre opciones **budget**, con precio orientativo y mención de segunda mano (mpb.com) cuando compense.
- **Enlaces externos**: toda referencia (apps, software, localizaciones, fabricantes) lleva su URL. No inventar URLs profundas; ante la duda, enlazar la página raíz del sitio.
- Los enlaces entre capítulos son relativos (`[capítulo 1](01-configuracion-basica.md)` dentro de `5dmk3/`, `../comun/...` entre carpetas); los del README llevan el prefijo de carpeta.
- **Datos técnicos: verificar antes de afirmar** (todo el contenido actual pasó un fact-check con fuentes en agosto de 2026). Peculiaridades ya verificadas y documentadas a propósito — no "corregirlas": sin compensación de exposición en M+ISO Auto en la 5D3; ranura SD sin soporte UHS (lenta, el RAW va a la CF); el Samyang marca f/00 (sin contactos, apertura en su anillo); selector del Sigma con tres posiciones AF/MO/MF y limitador FULL/10m–∞/2,8–10m; el obturador mecánico reduce pero no elimina los artefactos de focos LED parpadeantes.
