# Todos los ajustes de la a6700 — el manual de tu cámara, con tus valores

> 🟢 **Iniciación** · Da por sabido: el [capítulo 0.5](../a6700/00b-menus-y-primer-dia.md) (cómo se navega el menú) · Te desbloquea: dejar de buscar ajustes y saber exactamente dónde está cada uno y qué valor lleva.

El resto del repo te da los valores repartidos por escenario. Esto es la
**referencia única** (y si quieres **el menú entero**, también lo que no
toca este viaje, está en [el menú completo](menu-completo.md)): cada ajuste que toca este viaje, con su **ruta exacta
de menú**, el valor para **fauna** y el valor para **noche**, y por qué. Para
consultar, no para leer de seguido.

**Cómo leer las rutas.** Se escriben así:

```
MENU → Toma → [Obturad./silenc.] → [Tipo de obturador]
  │      │            │                    │
  │      │            │                    └── el ajuste
  │      │            └── el grupo (sale abreviado en pantalla)
  │      └── la pestaña (los iconos de la izquierda)
  └── el botón MENU, arriba a la izquierda del respaldo
```

Las rutas salen de la **Guía de ayuda oficial de Sony** (consultada en agosto
de 2026) y cada ajuste enlaza abajo a su ficha: si dudas de un nombre, manda
la ficha. La mayoría están comprobadas una a una; en unos pocos el nombre del
grupo está deducido de la ficha de un ajuste vecino. Los
nombres salen **abreviados** en la pantalla de la cámara (`Calid. img/grab.`,
`Sens. Seguim. AF`): así están escritos aquí, tal cual los vas a leer.

---

## El mapa del menú, dibujado

Las ocho pestañas, y los grupos que vas a usar de verdad en este viaje:

```
┌──────────────────┬──────────────────────────────────────────────┐
│  PESTAÑA         │  GRUPOS QUE USARÁS                           │
├──────────────────┼──────────────────────────────────────────────┤
│ ▸ Principal      │  (lista rápida de ajustes de toma)           │
│ ▸ Toma           │  Calid. img/grab. · Modo de toma             │
│                  │  Modo de manejo (con Func. capt. interv.)    │
│                  │  Obturad./silenc. · Estabiliz. de img        │
│                  │  Soporte · Visualizac. toma                  │
│ ▸ Exposición/    │  Exposición · Visualizac. cebra              │
│    color         │  Balance blancos · Medición · Color/tono     │
│ ▸ Enfoque        │  AF/MF · Área de enfoque · Reconoc. motivo   │
│                  │  Asistencia enfoq. · Visualiz. resalte       │
│ ▸ Reproducc.     │  Aumento · Selección/nota                    │
│ ▸ Red            │  (emparejar con Creators' App)               │
│ ▸ Ajustes        │  Personal. operac. · Personalizar dial       │
│                  │  Área/fecha (con Idioma) · Rest/guard ajust  │
│ ▸ Mi Menú        │  el tuyo, vacío hasta que lo llenes          │
└──────────────────┴──────────────────────────────────────────────┘
```

> **El aviso que ahorra media hora**: el menú **cambia según el selector
> Foto / Vídeo / S&Q**. Si un ajuste "no existe", casi siempre estás en el
> modo equivocado. Comprueba el selector antes de buscar nada.

---

## Bloque A, lo que se pone una vez y no se toca más

Esto se hace en casa, antes de volar, y no se vuelve a mirar en todo el viaje.

| Ajuste | Ruta | Valor | Por qué |
|---|---|---|---|
| **Formato archivo** | `Toma → [Calid. img/grab.] → [Formato archivo]` | **RAW** | Todo el revelado del repo asume RAW |
| **Tipo archivo RAW** | `Toma → [Calid. img/grab.] → [Tipo archivo RAW]` | **Comprimido sin pérdida** | Máxima calidad… y ojo: es el que deja el búfer en **23 fotos** (ver [equipo](../a6700/05-equipo-accesorios.md)) |
| **RR exposic. larga** | `Toma → [Calid. img/grab.] → [RR exposic. larga]` | **Desactivar** | Si no, tras cada foto de 20 s la cámara se pasa otros 20 s en negro: adiós star trails |
| **RR ISO Alta** | `Toma → [Calid. img/grab.] → [RR ISO Alta]` | **Bajo / Desactivar** | Solo afecta al JPEG; el ruido del RAW lo arreglas mucho mejor en casa |
| **Visualizac. cebra** | `Exposición/color → [Visualizac. cebra] → [Visualizac. cebra]` | **Activar** | Tu única alarma de quemados **en vivo** |
| **Nivel de cebra** | `Exposición/color → [Visualizac. cebra] → [Nivel de cebra]` | **100 IRE o +** | Raya solo lo que ya está perdido, no lo que está claro |
| **Idioma** | `Ajustes → [Área/fecha] → [Idioma]` | Español | — |
| **Área / fecha / hora** | `Ajustes → [Área/fecha] → [Aj. área/fecha/hora]` | Hora de **Namibia** al aterrizar | Ordenar 4.000 fotos por hora depende de esto |
| **Formatear** | `Toma → [Soporte] → [Formatear]` | Cada tarjeta nueva, **en la cámara** | Y **nunca más** durante el viaje: las tarjetas son tu segunda copia |
| **Liberar sin tarj. mem.** | `Toma → [Obturad./silenc.] → [Liberar sin tarj. mem.]` | **Inhabilitar** | De fábrica dispara sin tarjeta y **no guarda nada** |
| **Diales en M** | `Ajustes → [Personal. operac.] → [Ajuste t. pers./dial]` | **Dial frontal = `Velocidad obturador`**, **dial trasero = `Abertura`** | De fábrica es al revés; todo el repo cuenta con la velocidad en el delantero ([diales y botones](../a6700/00c-diales-y-botones.md)) |
| **Iluminador AF** | `Enfoque → [AF/MF] → [Iluminador AF]` | **Desactivar** | Su luz espanta a los animales de la charca |
| **AF c/obturador** | `Enfoque → [AF/MF] → [AF c/obturador]` | **Desactivar** | Es lo que separa enfoque (pulgar) y disparo (índice) |
| **Vis. lín. cuadrícul.** | `Toma → [Visualizac. toma] → [Vis. lín. cuadrícul.]` | **Activar** | La herramienta de encuadre: aire de la mirada y horizontes rectos |
| **Tipo lín. cuadríc.** | `Toma → [Visualizac. toma] → [Tipo lín. cuadríc.]` | **Regla de tres** | Es la que se corresponde con los encuadres del atlas |
| **Rev.automática** | `Ajustes → [Opción de visual.] → [Rev.automática]` | **Desactivar** | Te tapa el visor justo cuando la escena sigue pasando |
| **Aj. DISP (vis. pant.)** | `Ajustes → [Personal. operac.] → [Aj. DISP (vis. pant.)]` | Deja solo **toda info. · histograma · nivel** | Menos pulsaciones de DISP en el campo |
| **Valoración** | `Reproducc. → [Selección/nota] → [Valoración]` | A un botón, en reproducción | Marcar las 3 del día en cámara; Lightroom lee las estrellas al importar |

---

## Bloque B, fauna: la receta de MR1

Lo que va guardado en la memoria **1** del dial. Con esto puesto, en el coche
solo tocas la rueda delantera.

```
┌─ Enfoque ──────────────────────────────────────────┐
│  AF/MF                                             │
│    Modo de enfoque .................. AF-C   ◀     │
│    Sens. Seguim. AF ................. 3            │
│    AF c/obturador ................... Desactivar   │
│  Área de enfoque                                   │
│    Área de enfoque .................. Zona   ◀     │
│  Reconoc. motivo                                   │
│    Rec. motivo en AF ................ Activar ◀    │
│    Dest. reconocim. ................. Animal  ◀    │
└────────────────────────────────────────────────────┘
```

| Ajuste | Ruta | Valor | Por qué |
|---|---|---|---|
| **Modo de toma** | `Toma → [Modo de toma] → [Modo de toma]` | **M** | Con ISO Auto, y la compensación sigue funcionando (rareza buena de esta cámara) |
| **ISO** | `Exposición/color → [Exposición] → [ISO]` | **ISO AUTO**, y dentro: **ISO AUTO mínimo 100 · máximo 12800** | El techo de trabajo real del sensor |
| Obturación | Rueda delantera (tras intercambiar los diales) | **1/1000** de partida | Y la mueves por escena: [capítulo 3](../a6700/03-safari-diurno.md) |
| Apertura | Rueda trasera | **La mínima** del zoom | Cambia sola al zoomear; por debajo de 200 mm ganas luz |
| **Modo de enfoque** | `Enfoque → [AF/MF] → [Modo de enfoque]` | **AF-C** | Todo lo que se mueve |
| **Área de enfoque** | `Enfoque → [Área de enfoque] → [Área de enfoque]` | **Zona** (o *Ancho* si la escena está limpia) | Deja trabajar al reconocimiento sin perder el control |
| **Rec. motivo en AF** | `Enfoque → [Reconoc. motivo] → [Rec. motivo en AF]` | **Activar** | La cámara busca el ojo sola |
| **Dest. reconocim.** | `Enfoque → [Reconoc. motivo] → [Dest. reconocim.]` | **Animal** (→ *Ave* para aves) | Es el ajuste que más vas a cambiar: ponlo en el **Fn** |
| **Sens. Seguim. AF** | `Enfoque → [AF/MF] → [Sens. Seguim. AF]` | **3** (estándar) · **1** con hierba delante · **4–5** en persecución | 1 = tozudo, 5 = saltarín |
| **Modo manejo** | `Toma → [Modo de manejo] → [Modo manejo]` | **`Captura contin.`** en **Hi+** | 11 fps (~10 en RAW sin pérdida). En Hi+ el visor no va en vivo durante la ráfaga: si te cuesta seguir, baja a Hi |
| **SteadyShot** | `Toma → [Estabiliz. de img] → [SteadyShot]` | **Activar** (+ interruptor **OSS** del objetivo en ON) | A pulso y desde la ventanilla |
| **Modo medición** | `Exposición/color → [Medición] → [Modo medición]` | **Multi** de partida · **Puntual** vinculada al AF para el nivel avanzado (`[Medición] → [Punto med. punt.] → Vínc. punto enf.`) | El detalle, en [AF y exposición a fondo](../mejora/af-y-exposicion-a-fondo.md) |
| **Balance blanco** | `Exposición/color → [Balance blancos] → [Balance blanco]` | **Luz diurna** o K fijo | Es RAW: se cambia después sin coste |

**Guardarlo**: `Toma → [Modo de toma] → [Mem. ajustes cám]` → **1**.

---

## Bloque C, noche: las tres recetas

Las tres son distintas de verdad: no intentes cubrirlas con una sola memoria.

### C1, charca nocturna (Okaukuejo, Halali, Onguma)

```
┌─ Toma ─────────────────────────────────────────────┐
│  Obturad./silenc.                                  │
│    Tipo de obturador ....... Obturad. electr.  ◀   │
│         (¿franjas bajo los focos LED?              │
│          → Obturad. mecán.)                        │
└────────────────────────────────────────────────────┘
```

| Ajuste | Ruta | Valor |
|---|---|---|
| Modo | `Toma → [Modo de toma]` | **M** (ISO manual) |
| Obturación / apertura | Ruedas | **1/60** · la mínima (recoge bajo 200 mm y ganas un tercio de paso) |
| **ISO** | `Exposición/color → [Exposición] → [ISO]` | **6400**, techo 12800 (25600 solo rescate) |
| **Balance blanco** | `Exposición/color → [Balance blancos] → [Balance blanco]` | **K ≈ 3500**, ajustando con la revisión |
| **Modo de enfoque** | `Enfoque → [AF/MF] → [Modo de enfoque]` | **AF-S** |
| **Área de enfoque** | `Enfoque → [Área de enfoque]` | **Punto: S o M** sobre lo iluminado |
| **Tipo de obturador** | `Toma → [Obturad./silenc.] → [Tipo de obturador]` | **Obturad. electr.** — silencio absoluto |
| **SteadyShot** | `Toma → [Estabiliz. de img] → [SteadyShot]` | **Desactivar** (y el OSS del objetivo, también) |
| **Modo manejo** | `Toma → [Modo de manejo] → [Modo manejo]` | **`Captura contin.`**: ráfagas cortas de 3–4 en los momentos quietos; si sale todo movido, **`Autodisp.(senc)`** de 2 s |

### C2, astro: la receta de MR2

```
┌─ Exposición/color ─────────────────────────────────┐
│  Exposición                                        │
│    ISO ............................ 1600     ◀     │
│    Aj. temporiz. BULB ............. (star trails)  │
└─ Enfoque ──────────────────────────────────────────┐
│  AF/MF → Modo de enfoque .......... MF       ◀     │
│  Visualiz. resalte → Visualizac. resalte → Activar │
└────────────────────────────────────────────────────┘
```

| Ajuste | Ruta | Valor |
|---|---|---|
| Modo · obturación · apertura | Dial y ruedas | **M · 20 s · f/1.8** (el 11 mm) |
| **ISO** | `Exposición/color → [Exposición] → [ISO]` | **1600**, subiendo a 3200 |
| **Balance blanco** | `Exposición/color → [Balance blancos] → [Balance blanco]` | **K 3900** |
| **Modo de enfoque** | `Enfoque → [AF/MF] → [Modo de enfoque]` | **MF** — el AF no ve estrellas |
| **Visualizac. resalte** | `Enfoque → [Visualiz. resalte] → [Visualizac. resalte]` | **Activar** — el peaking, para enfocar a mano |
| **RR exposic. larga** | `Toma → [Calid. img/grab.] → [RR exposic. larga]` | **Desactivar** (crítico en series) |
| **SteadyShot** | `Toma → [Estabiliz. de img] → [SteadyShot]` | **Desactivar** |
| **Modo manejo** | `Toma → [Modo de manejo] → [Modo manejo]` | **`Autodisp.(senc)`** de **2 s** |
| **Star trails** | `Toma → [Modo de manejo] → [Func. capt. interv.]` | 30 s de exposición · intervalo **31 s** · 90–180 tomas ([estrellas con la tierra dentro](../mejora/estrellas-con-tierra.md)) |
| **Timelapse del cielo** | `Toma → [Modo de manejo] → [Func. capt. interv.]` | 15 s de exposición · intervalo **17 s** · 300 tomas ([capítulo 2](../a6700/02-astrofotografia-namibia.md)) |

**Guardarlo**: `Toma → [Modo de toma] → [Mem. ajustes cám]` → **2**.

### C3, game drive nocturno con foco

Igual que la charca, con estos cambios: **ISO manual 6400–12800**,
**1/125–1/250** (vas a pulso en un vehículo abierto), **AF-C** con punto
único (o *Animal*) sobre lo iluminado, **SteadyShot Activar** (y el OSS),
sin temporizador, y medición **puntual vinculada al punto de enfoque** —
porque el fondo negro engaña al medidor al revés que de día.

---

## Bloque D, los ajustes que sí se tocan en el campo

Estos tres son los que vas a querer a mano. Mételos en el **menú Fn** y en
**Mi Menú**, y no volverás a entrar al menú con un león delante:

1. **Dest. reconocim.** (Animal ⇄ Ave)
2. **Área de enfoque** (Zona ⇄ Punto)
3. **Sens. Seguim. AF** (3 ⇄ 1)

- Cambiar las 12 casillas del Fn: `Ajustes → [Personal. operac.] → [Ajustes del menú Fn]`
- Añadir a Mi Menú: `Mi Menú → [Ajuste Mi Menú] → [Añadir elemento]`, y luego
  `[Mostrar de Mi Menú] → Activar` para que **MENU abra directamente ahí**.
- Asignar un botón (C1, C2, C3): `Ajustes → [Personal. operac.] → [Ajuste t. pers./dial]`.
  La botonera del viaje: **C1 = `Verificac. luminosa`** (*Bright Monitoring*:
  componer la Vía Láctea viéndola; solo en MF), **C2 = `Área de enfoque`**
  (de fábrica) y **C3 = `Amplific. enfoque`**. La **Guía en la cámara** no
  necesita botón: selecciona una línea del menú y pulsa C3.
- Todos los botones y diales, uno a uno: [diales y botones](../a6700/00c-diales-y-botones.md).
- Todo el menú, no solo lo del viaje: [el menú completo](menu-completo.md).

---

## Bloque E, vídeo: con el selector en Vídeo

El selector **Foto / Vídeo / S&Q** separa el vídeo de la foto **si se lo
pides**: primero `Ajustes → [Personal. operac.] → [Ajust dif imgs fij/víd]`
con las ocho casillas marcadas (fila de abajo). Luego esto se pone una vez,
en casa, y no toca a MR1 ni a MR2. El porqué de cada valor, en
el [capítulo 1](../a6700/01-configuracion-basica.md) y en
[el vídeo del viaje](../tecnica/video-del-viaje.md).

| Ajuste | Ruta | Valor |
|---|---|---|
| **Ajust dif imgs fij/víd** | `Ajustes → [Personal. operac.] → [Ajust dif imgs fij/víd]` | **Las ocho casillas marcadas**, antes de tocar nada de vídeo. Sin eso, abertura, velocidad, ISO, compensación, medición, balance, perfil y modo de enfoque son comunes a foto y vídeo |
| **Selector NTSC/PAL** | `Ajustes → [Área/fecha] → [Selector NTSC/PAL]` | **PAL** — con una tarjeta formateada en el otro sistema puede pedir **reformatearla**: en casa, nunca en el viaje |
| **Formato archivo** (película) | `Toma → [Calid. img/grab.] → [Formato archivo]` | **XAVC S 4K**, a **25p · 100 Mbps** |
| Modo · obturación | Dial y ruedas | **M con ISO AUTO**, **1/50** |
| **Perfil de imagen** | `Exposición/color → [Color/tono] → [Perfil de imagen]` | **OFF** (sin perfil: nada de S-Log3) |
| **SteadyShot** (película) | `Toma → [Estabiliz. de img] → [SteadyShot]` | **Activo** andando (recorta 1,1x) · **Estándar** parado · **Desactivar** en trípode |
| **Temp. APAGA auto** | `Ajustes → [Opc. ajuste enrg.] → [Temp. APAGA auto]` | **Estándar** a pulso; **Alto** solo en trípode (Sony avisa de quemaduras si la sujetas) |

---

## Las tres memorias del dial

| Memoria | Para qué | Se guarda con |
|---|---|---|
| **1** | Safari diurno (bloque B) | `Toma → [Modo de toma] → [Mem. ajustes cám] → 1` |
| **2** | Astro (bloque C2) | Ídem → 2 |
| **3** | Aves en vuelo: como MR1, pero **1/2500**, *Dest. reconocim.* **Ave**, área **Zona**, Sens. Seguim. **3** y Continuo Hi+ | Ídem → 3 |

**Cómo funcionan**: al girar el dial recuperan **lo guardado**, no lo que
tenías puesto. Es una ventaja — nunca heredas los ajustes raros de anoche —
pero significa que para hacer fijo un cambio hay que **volver a guardar**.
Caben 3 en la cámara y 4 más (M1–M4) en la tarjeta… que se borran al
formatearla.

---

## Si un ajuste no aparece

| Síntoma | Causa | Solución |
|---|---|---|
| "Este ajuste no existe" | El selector **Foto / Vídeo / S&Q** está en otro modo | Ponlo en Foto y vuelve a buscar |
| Aparece en gris, no se puede tocar | Lo bloquea otro ajuste (p. ej. RR exposic. larga con obturador electrónico) | Mira la nota de la propia pantalla |
| No sé qué hace lo que estoy mirando | — | **Guía en la cámara**: selecciona la línea y pulsa **C3** |
| No encuentro nada nunca | No has hecho tu **Mi Menú** | Diez minutos, bloque D |
| Lo he desajustado todo | — | `Ajustes → [Rest/guard ajust] → [Restablecer ajuste] → Reponer ajustes de cámara`. No borra fotos |

---

## Sobre las capturas de pantalla

Los dibujos de esta página son **reproducciones esquemáticas**, no capturas:
la a6700 no tiene función de captura de pantalla y las imágenes del manual de
Sony tienen derechos, así que no se copian aquí. Dos formas de tener la
pantalla real delante:

- **La oficial**: cada ajuste de esta página enlaza abajo a su ficha en la
  Guía de ayuda de Sony, donde sale la pantalla real.
- **La tuya, que es mejor**: fotografía tus propias pantallas con el móvil.
  Ya está todo preparado — hay un **guion de captura** con las 30 pantallas
  en orden de navegación, el nombre de archivo de cada una y las doce
  imprescindibles marcadas: [`referencia/img/menus/`](img/menus/). Media hora
  el día que llegue la cámara.

Cuando las tengas, un comando las pega solas aquí abajo:

```bash
python3 referencia/img/menus/insertar.py
```

## Las pantallas, una a una

<!-- CAPTURAS:INICIO -->

*(Aún vacío: haz las capturas siguiendo el [guion](img/menus/) y ejecuta
`insertar.py`. Aparecerán aquí, en orden, con su ruta de menú debajo.)*

<!-- CAPTURAS:FIN -->

---

## Referencias — la ficha oficial de cada ajuste

- El menú y cómo se navega: <https://helpguide.sony.net/ilc/2320/v1/es/contents/0201B_using_menu.html>
- Rec. motivo en AF y Dest. reconocim.: <https://helpguide.sony.net/ilc/2320/v1/es/contents/211h_subject_recognition_af.html>
- Área de enfoque: <https://helpguide.sony.net/ilc/2320/v1/es/contents/0405C_autofocus_area.html>
- Sens. Seguim. AF: <https://helpguide.sony.net/ilc/2320/v1/es/contents/0405D_af_tracking_sensitivity.html>
- Visualiz. resalte (peaking): <https://helpguide.sony.net/ilc/2320/v1/es/contents/0405M_peaking_display.html>
- ISO y límites de ISO AUTO: <https://helpguide.sony.net/ilc/2320/v1/es/contents/0408C_iso.html>
- Modo medición: <https://helpguide.sony.net/ilc/2320/v1/es/contents/0406_metering_mode.html>
- Balance blanco: <https://helpguide.sony.net/ilc/2320/v1/es/contents/0410C_white_balance.html>
- Visualizac. cebra: <https://helpguide.sony.net/ilc/2320/v1/es/contents/0406M_zebra_display.html>
- Formato archivo: <https://helpguide.sony.net/ilc/2320/v1/es/contents/0404M_file_format.html>
- RR exposic. larga: <https://helpguide.sony.net/ilc/2320/v1/es/contents/0414_long_exposure_nr.html>
- RR ISO Alta: <https://helpguide.sony.net/ilc/2320/v1/es/contents/0414C_high_iso_nr.html>
- Tipo de obturador: <https://helpguide.sony.net/ilc/2320/v1/es/contents/0414H_shutter_type.html>
- Modo manejo: <https://helpguide.sony.net/ilc/2320/v1/es/contents/0407C_drive_mode.html>
- SteadyShot: <https://helpguide.sony.net/ilc/2320/v1/es/contents/0414_still_image_steadyshot.html>
- Func. capt. interv. (intervalómetro): <https://helpguide.sony.net/ilc/2320/v1/es/contents/0407P_interval_shoot_setting.html>
- Var.exp. enfoque (horquillado de enfoque, por si algún día lo necesitas): <https://helpguide.sony.net/ilc/2320/v1/es/contents/211h_focus_bracket.html>
- Ajuste t. pers./dial: <https://helpguide.sony.net/ilc/2320/v1/es/contents/0413M_custom_key.html>
- Ajustes del menú Fn: <https://helpguide.sony.net/ilc/2320/v1/es/contents/201h_fn_menu_setting.html>
- Formatear: <https://helpguide.sony.net/ilc/2320/v1/es/contents/0601_memory_format.html>
- Restablecer ajuste: <https://helpguide.sony.net/ilc/2320/v1/es/contents/0601_setting_reset.html>
- Guía de ayuda completa: <https://helpguide.sony.net/ilc/2320/v1/es/>
