# Edición básica — del RAW a la foto terminada

Todo el tutorial te hace disparar en RAW; esta guía es el "después". Sin
teoría de color: un flujo que funciona, en orden.

## El programa

- **Adobe Lightroom** (~12 €/mes, incluye el Denoise por IA): la opción
  cómoda si el presupuesto lo permite. <https://www.adobe.com/products/photoshop-lightroom.html>
- **darktable** (gratis y libre, hace lo mismo con más curva de aprendizaje):
  <https://www.darktable.org/>

Los pasos de abajo valen para ambos; los nombres exactos cambian un poco.

## El repaso de cada noche (10 minutos, sin editar)

El hábito que hace que mejores *durante* el viaje, no al volver. Tras el
volcado de seguridad ([logística](logistica-viaje.md)), con las fotos del día:

1. Elige tus **3 mejores** del día. Solo eso — cría el ojo y la moral.
2. Busca el **error que se repite**: ¿movidas? → obturación corta la próxima
   vez. ¿Animales oscuros? → compensación. ¿Ojo blando? → punto AF. Las
   tablas de "si la foto sale…" de cada capítulo dan la corrección.
3. Decide **una sola cosa** que harás distinto mañana. Una, no cinco.
4. Marca en la [lista de tomas](lista-de-tomas.md) las conseguidas y elige
   la que persigues mañana.
5. **No borres nada.**

## Paso 1 — Cribar (no edites lo que no vale)

De un safari salen 800 fotos y valen 30. Antes de editar nada:

1. Importa el día completo.
2. Pasa las fotos con dos teclas: **bandera** (P en Lightroom) a lo que
   promete, nada a lo demás. No lo pienses más de 2 segundos por foto.
3. Segunda pasada solo sobre las banderas: quédate con la mejor de cada
   ráfaga (el criterio: **ojo nítido** y gesto).
4. Edita solo las supervivientes. El resto no se borra, se ignora.

## Paso 2 — Revelado básico (en este orden, 2 minutos por foto)

1. **Recortar y nivelar** el horizonte.
2. **Exposición** general hasta que la foto respire.
3. **Altas luces** hacia abajo (recupera cielos), **sombras** hacia arriba
   (recupera el animal en sombra). En un RAW de estas cámaras puedes mover
   mucho ambos sin miedo.
4. **Blancos y negros**: sube blancos hasta justo antes de quemar (mira el
   histograma), baja negros hasta que haya negro de verdad.
5. **Balance de blancos** si el color está raro (la ventaja del RAW: se cambia
   ahora sin pérdida).
6. Pizca de **textura/claridad** (+10 a +20). Más que eso se nota y mal.

## Paso 3 — Ruido (las fotos de ISO alto de la charca)

- **Lightroom**: botón **Denoise** (IA), intensidad 30–50. Los resultados a
  ISO 12800 parecen de ISO 1600. <https://helpx.adobe.com/lightroom-cc/using/enhance-details.html>
- **DxO PureRAW** como alternativa/complemento (procesa el RAW antes de
  editar): <https://www.dxo.com/dxo-pureraw/>
- **darktable**: módulo "reducción de ruido (perfilada)", que ya conoce el
  perfil de ruido de la 5D3.

Orden correcto: primero el denoise, después el revelado fino.

## Astro: apilado con Sequator, paso a paso

Para las 10 tomas idénticas que hiciste siguiendo el
[capítulo 2](../5dmk3/02-astrofotografia-namibia.md)
(Windows; en macOS, Starry Landscape Stacker funciona parecido:
<https://sites.google.com/site/starrylandscapestacker/>).

1. Descarga Sequator: <https://sites.google.com/view/sequator/>
2. `Star images` → añade las 10 tomas (los RAW directamente).
3. `Base image` → elige una del medio de la serie.
4. `Output` → nombre del archivo final (TIFF).
5. `Composition` → **Align stars** + `Freeze ground` (alinea las estrellas sin
   emborronar el suelo).
6. Marca `Reduce distor. effects` y `Reduce light pollution` si el horizonte
   tiene resplandor.
7. `Start`. El TIFF resultante se edita después en Lightroom/darktable como
   cualquier RAW: baja altas luces, ajusta el balance hacia 3900 K, contraste
   al gusto.

Revelado típico de astro sobre el resultado: exposición +0.3/+0.7, contraste
+15, claridad +10 **solo en el cielo** (pincel/máscara), y resiste la
tentación de saturar la Vía Láctea hasta el neón.

## Star trails: apilar con StarStaX

Para la serie de circumpolares del capítulo 2: exporta las fotos a JPEG y
apílalas en **StarStaX** (gratis, modo *Lighten* — también tiene *Gap
filling* si hay microhuecos entre tomas):
<https://markus-enzweiler.de/software/starstax/>

## Montar un timelapse en vídeo

(Los de la GoPro salen ya montados de cámara — esto es para las series de
la 5D3; los clips y archivos de la GoPro tienen su apartado en
[su guía](gopro-mission-1.md).)

Para la serie de intervalos del capítulo 2 (300 tomas ≈ 10 s de clip a 24
fotogramas por segundo):

1. Revela **una** foto de la serie y sincroniza/pega el ajuste a todas
   (misma exposición fija en cámara = mismo revelado para todas).
2. Exporta la serie a JPEG, lado largo 1920 px (o 3840 para 4K), a una
   carpeta vacía y con numeración ordenada.
3. Móntalo gratis con **ffmpeg** (<https://ffmpeg.org/>), un solo comando
   desde esa carpeta:
   `ffmpeg -framerate 24 -pattern_type glob -i '*.jpg' -c:v libx264 -pix_fmt yuv420p timelapse.mp4`
   (en Windows, cambia el patrón: `-i img%04d.jpg`).
   Alternativa con interfaz: **DaVinci Resolve** gratis
   (<https://www.blackmagicdesign.com/products/davinciresolve>) importa la
   carpeta como "image sequence".
4. ¿Parpadeo entre fotogramas (*flicker*)? Con todo en manual (exposición,
   ISO, WB fijos — como manda la receta) apenas habrá; si molesta, la
   herramienta especializada es **LRTimelapse** (de pago:
   <https://lrtimelapse.com/>).

## Montar el vídeo-recuerdo (DaVinci para novatos)

El cierre del viaje: los clips de la GoPro convertidos en un vídeo de 3–5
minutos. El guion ya lo rodaste — los capítulos de la
[lista de tomas del vídeo](gopro-mission-1.md): ida, carretera, desierto,
costa, safari, noche, campamento, vuelta. El montaje, paso a paso en
**DaVinci Resolve** (gratis:
<https://www.blackmagicdesign.com/products/davinciresolve>):

1. Proyecto nuevo → importa la carpeta de clips del viaje (ya volcados por
   días al SSD).
2. Arrastra a la línea de tiempo **en el orden del guion**, no en el orden
   de grabación: la historia manda.
3. Recorta cada clip a sus **3–6 segundos buenos** (herramienta de corte;
   los 5 s quietos que dejaste al grabar son el margen). Fuera todo lo que
   dude: mejor 3 minutos redondos que 8 regulares.
4. Los timelapses y star trails de la GoPro ya vienen montados: entran como
   un clip más. Los de la 5D3, como los exportaste
   ([arriba](#montar-un-timelapse-en-vídeo)).
5. **Música**: una sola canción sin copyright (la biblioteca de audio de
   YouTube Studio, por ejemplo) marca el ritmo de los cortes. Baja el sonido
   ambiente de los clips — salvo donde ES la escena: las focas, la tormenta,
   el león de noche.
6. Exporta con el preajuste **YouTube 1080p** de la pestaña Deliver y
   listo: ese archivo es el recuerdo.

La alternativa exprés: la app **Quik** de GoPro monta un borrador
automático con música en 5 minutos — vale como tráiler mientras te animas
con el montaje bueno.

## Exportar para compartir

- JPEG, lado largo **2048 px**, espacio de color **sRGB** (si no, los colores
  se ven lavados en el móvil de quien lo recibe).
- Para imprimir o archivar: JPEG a tamaño completo, calidad 90+.

## Si te atascas…

| Problema | Solución |
|---|---|
| 800 fotos y no sabes por dónde empezar | No edites: **criba** primero (paso 1). Editar sin cribar es el atasco número 1 |
| El Denoise tarda una eternidad | Es normal (es IA): pásalo solo a las supervivientes de la criba, nunca al día entero |
| Sequator no traga los archivos | Dale los RAW (.CR2) directamente; si protesta, convierte antes a TIFF y repite |
| El apilado sale con el suelo emborronado | Falta `Freeze ground` en Composition |
| El comando de ffmpeg falla en Windows | El patrón `*.jpg` no funciona ahí: usa `-i img%04d.jpg` con los archivos numerados |
| El timelapse parpadea (flicker) | ¿Algo quedó en auto (ISO, WB)? Con todo fijo apenas ocurre; si molesta, LRTimelapse |
| Los colores del vídeo/foto se ven lavados al compartir | Exportaste fuera de sRGB (foto) o el móvil del receptor hace lo suyo: exporta sRGB y preajuste YouTube 1080p |

## La regla final

De cada sesión de edición deben salir **pocas fotos rematadas**, no muchas a
medias: tres redondas por día de viaje son un reportaje espectacular de
cuarenta y cinco.
