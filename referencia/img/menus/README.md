# Capturas de los menús — el guion, para el día que llegue la cámara

La a6700 no tiene función de captura de pantalla, y las imágenes del manual
de Sony tienen derechos: no se copian aquí. Así que estas capturas las haces
**tú**, con el móvil, y salen mejor que cualquier alternativa — en tu idioma,
con tus valores ya puestos y con tu firmware.

**Media hora, una vez.** Y luego `python3 referencia/img/menus/insertar.py`
las pega solas en [la referencia de ajustes](../../ajustes-a6700.md).

## Cómo se hacen

1. **Apaga la luz de arriba.** El reflejo en la pantalla es el único enemigo.
   Luz lateral suave o luz de ventana.
2. **Deja el ajuste ya puesto en su valor**, el del repo. La captura vale
   doble si además documenta tu configuración.
3. Móvil **en 1x** (no 0.5x, que deforma), de frente y perpendicular a la
   pantalla, a unos 25 cm.
4. **Recorta a la pantalla** y guarda en JPEG, lado largo ~1200 px.
5. Nombre exacto de la tabla de abajo, en esta carpeta.

Las **★** son las catorce imprescindibles. Si solo vas a hacer catorce, haz esas.

## El guion, en orden de navegación

### Pestaña Toma

| ☐ | Pantalla | Ruta | Nombre del archivo |
|---|---|---|---|
| ☐ ★ | Formato archivo = RAW | `Toma → [Calid. img/grab.]` | `formato-archivo.jpg` |
| ☐ | Tipo archivo RAW | `Toma → [Calid. img/grab.]` | `tipo-archivo-raw.jpg` |
| ☐ ★ | RR exposic. larga = Desactivar | `Toma → [Calid. img/grab.]` | `rr-exposic-larga.jpg` |
| ☐ | RR ISO Alta | `Toma → [Calid. img/grab.]` | `rr-iso-alta.jpg` |
| ☐ ★ | Mem. ajustes cám | `Toma → [Modo de toma]` | `mem-ajustes-cam.jpg` |
| ☐ ★ | Modo manejo = Continuo Hi+ | `Toma → [Modo de manejo]` | `modo-manejo.jpg` |
| ☐ ★ | Tipo de obturador | `Toma → [Obturad./silenc.]` | `tipo-de-obturador.jpg` |
| ☐ ★ | Func. capt. interv. | `Toma` | `func-capt-interv.jpg` |
| ☐ | SteadyShot | `Toma → [Estabiliz. de img]` | `steadyshot.jpg` |
| ☐ | Formatear | `Toma → [Soporte]` | `formatear.jpg` |

### Pestaña Exposición/color

| ☐ | Pantalla | Ruta | Nombre del archivo |
|---|---|---|---|
| ☐ ★ | ISO, con ISO AUTO máximo/mínimo | `Exposición/color → [Exposición]` | `iso-auto-limites.jpg` |
| ☐ ★ | Nivel de cebra = 100 IRE o + | `Exposición/color → [Visualizac. cebra]` | `nivel-de-cebra.jpg` |
| ☐ | Visualizac. cebra = Activar | `Exposición/color → [Visualizac. cebra]` | `visualizac-cebra.jpg` |
| ☐ | Modo medición | `Exposición/color → [Medición]` | `modo-medicion.jpg` |
| ☐ | Balance blanco en K | `Exposición/color` | `balance-blanco.jpg` |

### Pestaña Enfoque

| ☐ | Pantalla | Ruta | Nombre del archivo |
|---|---|---|---|
| ☐ ★ | Modo de enfoque = AF-C | `Enfoque → [AF/MF]` | `modo-de-enfoque.jpg` |
| ☐ ★ | AF con disparador = Desactivar | `Enfoque → [AF/MF]` | `af-con-disparador.jpg` |
| ☐ ★ | Sens. Seguim. AF | `Enfoque → [AF/MF]` | `sens-seguim-af.jpg` |
| ☐ ★ | Área de enfoque | `Enfoque → [Área de enfoque]` | `area-de-enfoque.jpg` |
| ☐ ★ | Dest. reconocim. = Animal | `Enfoque → [Reconoc. motivo]` | `dest-reconocim.jpg` |
| ☐ | Rec. motivo en AF = Activar | `Enfoque → [Reconoc. motivo]` | `rec-motivo-af.jpg` |
| ☐ | Visualiz. resalte (peaking) | `Enfoque` | `visualiz-resalte.jpg` |

### Ajustes, Mi Menú y Reproducción

| ☐ | Pantalla | Ruta | Nombre del archivo |
|---|---|---|---|
| ☐ | Ajuste t. pers./dial | `Ajustes → [Personal. operac.]` | `ajuste-t-pers-dial.jpg` |
| ☐ | Ajustes del menú Fn | `Ajustes → [Personal. operac.]` | `ajustes-menu-fn.jpg` |
| ☐ | Ajuste Mi Menú | `Mi Menú` | `mi-menu.jpg` |
| ☐ | Aumento (reproducción) | `Reproducc. → [Aumento]` | `ampliacion.jpg` |
| ☐ | Restablecer ajuste | `Ajustes → [Rest/guard ajust]` | `restablecer-ajuste.jpg` |

### Y tres que no son de menú, pero valen más que muchas

| ☐ | Pantalla | Cómo | Nombre del archivo |
|---|---|---|---|
| ☐ ★ | **El menú Fn**, con tus 12 casillas | Pulsa Fn en modo de toma | `menu-fn.jpg` |
| ☐ | **Tu Mi Menú** ya relleno | MENU, con `Mostrar de Mi Menú` en Activar | `mi-menu-relleno.jpg` |
| ☐ | **La pantalla de toma** con histograma y Zebra | DISP hasta verlos, apuntando a algo claro | `pantalla-de-toma.jpg` |

## Cuando las tengas

```bash
python3 referencia/img/menus/insertar.py
```

Recorre esta carpeta, ve qué archivos existen y **reconstruye la galería** al
final de `referencia/ajustes-a6700.md`, en el orden de este guion. Se puede
ejecutar tantas veces como quieras: si añades capturas después, vuelve a
correrlo y se actualiza.
