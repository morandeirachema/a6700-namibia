# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Qué es este repo

Guía de fotografía en **español** de la **Sony a6700** para un viaje a Namibia: safari diurno, charcas nocturnas de Etosha y astrofotografía (el viaje coincide con luna nueva). Solo Markdown más los PDF generados de las hojas de campo: no hay build, lint ni tests. Publicar = commit y push a `main` (https://github.com/morandeirachema/a6700-namibia).

Equipo real del viaje (condiciona las recomendaciones; elegido en agosto de 2026, compra en curso): Sony a6700 + Rokinon/Samyang 12mm f/2.0 NCS CS propio (manual y sin contactos: la cámara marca F--) + Tamron 50-400mm f/4.5-6.3 Di III VC VXD (A067) en montura E + GoPro MISSION 1 con empuñadura-batería Volta 2, para vídeo, timelapses nocturnos y bici (ojo, la "Hero 14" no existe). El móvil del viaje es un Pixel 10 Pro. El Seestar S30 Pro que estuvo en evaluación fue **descartado** en agosto de 2026 (su rama `seestar` se borró; el material queda solo en el historial de git): no añadir contenido Seestar.

Historia del repo: la guía original era de una **Canon 5D Mark III prestada** (con Samyang 14mm EF y Sigma 150-600 C); en agosto de 2026 el autor la sustituyó por el kit Sony actual — la versión Canon completa queda en el historial de git (hasta el commit `6c2dce9`). Antes existió también una guía de la Sony A7 III, borrada a petición del autor (hasta `3975191`). **No reintroducir contenido de la 5D3, la 650D ni la A7 III.**

## Estructura

- `a6700/` — capítulos `00`–`05` (móvil→cámara, configuración, astro, safari diurno, charcas nocturnas, equipo) + dos hojas de campo imprimibles: `chuleta.md` y `verificacion-in-situ.md`. El capítulo 0 se llama `00-de-movil-a-la-a6700.md`.
- `comun/` — guías transversales: lista de tomas, mejores horas, el cielo del viaje (catálogo astro de la quincena, `cielo-del-viaje.md`), la guía de la GoPro por niveles (`gopro-mission-1.md`, con la lista de tomas del vídeo-recuerdo), su hoja de campo (`chuleta-gopro.md`), el plan de entrenamiento de las 11 semanas previas (`plan-de-entrenamiento.md`), apps del viaje, histograma, balance de blancos, edición básica, paisaje de Namibia, logística y limpieza en campo. El README ordena todo esto como ruta de aprendizaje en tres niveles.
- `mejora/` — el salto "de la foto correcta a la foto buena": `parte-1-principiante.md` (plan de charcas, comportamiento, el cielo real de noviembre), `parte-2-avanzado.md` (el seguimiento por IA a medida, plan de la noche hora a hora), `safari-a-fondo.md` (luz, velocidad, apertura, Kelvin y encuadre como decisiones creativas) y `estrellas-con-tierra.md` (cielo con primer plano desde cero, en tres noches: la base, la postal y los círculos).
- `pdf/` — versiones PDF maquetadas de las hojas de campo (chuleta a6700, verificación in situ, lista de tomas y chuleta GoPro), generadas desde el Markdown; al editar una hoja, regenerar su PDF.
- `README.md` — índice con fotos CC de Wikimedia Commons (mantener la atribución al editarlas).

## Contrato editorial (fijado por el autor)

- **Audiencia**: novato que viene sobre todo del móvil — **a todos los niveles**. Nada de teoría: recetas con valores concretos, pasos numerados y tablas de "si la foto sale mal, toca esto". Toda guía (también las de `mejora/`) debe ser **autocontenida desde lo básico**: la base imprescindible va resumida dentro, y los enlaces a otros capítulos son para ampliar, nunca requisito para empezar.
- **Esqueleto común de toda guía** (mantenerlo en contenido nuevo): qué resuelve (1 párrafo) → receta/tabla rápida → pasos numerados → tabla "si sale mal…" → Referencias con URLs. Excepciones deliberadas: las hojas de campo (chuletas, verificación, lista de tomas) son ultracompactas, e `histograma.md` es una chuleta visual. Los capítulos de escenario (2, 3 y 4) incluyen además una sección "Y la GoPro, mientras tanto" — el papel en paralelo de la segunda cámara.
- **Equipo**: siempre opciones **budget**, con precio orientativo y mención de segunda mano (mpb.com) cuando compense.
- **Enlaces externos**: toda referencia (apps, software, localizaciones, fabricantes) lleva su URL. No inventar URLs profundas; ante la duda, enlazar la página raíz del sitio.
- Los enlaces entre capítulos son relativos (`[capítulo 1](01-configuracion-basica.md)` dentro de `a6700/`, `../comun/...` entre carpetas); los del README llevan el prefijo de carpeta.
- **Datos técnicos: verificar antes de afirmar** (todo el contenido actual pasó un fact-check con fuentes en agosto de 2026). Peculiaridades ya verificadas y documentadas a propósito — no "corregirlas":
  - La a6700 **sí** permite compensación de exposición en M con ISO Auto (±5 EV) — al contrario que la Canon anterior; las recetas se apoyan en ello.
  - **Una sola ranura** SD (UHS-II): no hay copia automática en segunda tarjeta — el sistema de copias del repo gira alrededor del volcado nocturno.
  - La caja de la a6700 **no trae cargador**: carga por USB-C (PD) en cámara; el repo recomienda cargador doble USB aparte.
  - El aviso de quemados en vivo es el **Zebra 100+**; la a6700 no parpadea las altas luces en reproducción (no reintroducir el "aviso de altas luces" de Canon).
  - El Rokinon 12mm es manual y **sin contactos**: la cámara marca **F--** y exige `Disparo sin objetivo: Habilitar`; el IBIS necesita la focal a mano (`SteadyShot Adjust → Manual → 12 mm`).
  - El Tamron A067 en montura E **no tiene interruptor AF/MF**: lleva VC (1/2/OFF), botón Focus Set, interruptor Custom 1-2-3, bloqueo de zoom (solo a 50 mm) y puerto USB-C para Tamron Lens Utility (el limitador de enfoque se programa por software, no es un interruptor).
  - El obturador **electrónico** es totalmente silencioso (el arma de las charcas), pero con focos LED parpadeantes puede sacar **franjas**: el plan B documentado es el obturador mecánico.
  - El intervalómetro va **integrado** (`Interval Shoot Func.`): no recomendar intervalómetros de cable.
  - Focales siempre con su equivalencia APS-C (1.5x): 12 mm = 18 mm eq; 50–400 mm = 75–600 mm eq.
