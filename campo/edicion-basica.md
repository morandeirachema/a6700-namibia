# Edición básica — del RAW a la foto terminada

> 🔵 **Básico** · Da por sabido: haber disparado en RAW · Te desbloquea: del archivo en bruto a la foto terminada, en pasos.

Todo el tutorial te hace disparar en RAW; esta guía es el "después". Sin
teoría de color: un flujo que funciona, en orden.

## El programa

- **Adobe Lightroom** (~12 €/mes, incluye el Denoise por IA): la opción
  cómoda si el presupuesto lo permite. <https://www.adobe.com/products/photoshop-lightroom.html>
- **darktable** (gratis y libre, hace lo mismo con más curva de aprendizaje):
  <https://www.darktable.org/>

Los pasos de abajo valen para ambos; los nombres exactos cambian un poco.

> **En el viaje no hay ordenador** (decisión tomada: no va portátil). Durante
> las dos semanas solo pasan dos cosas: el **volcado nocturno** al SSD con el
> móvil ([logística](logistica-viaje.md)) y el **repaso de 10 minutos** de
> aquí abajo. Nada de cribar ni revelar sobre la marcha: se empieza al
> volver, y el orden está en [el archivo y la selección](archivo-y-seleccion.md).

## El repaso de cada noche (10 minutos, sin editar)

El hábito que hace que mejores *durante* el viaje, no al volver. Tras el
volcado de seguridad ([logística](logistica-viaje.md)), con las fotos del día.

**Y en este viaje se hace sin ordenador**: no va portátil, así que el repaso
es en la **pantalla de la cámara** (con ▶ y la rueda para ampliar sobre el
punto de enfoque, [capítulo 0.5](../a6700/00b-menus-y-primer-dia.md)) o en el
Pixel, que ya tienes conectado al SSD haciendo el volcado. Todo lo demás de
esta guía —revelar, ruido, apilar, montar— **espera a casa**.

1. Elige tus **3 mejores** del día. Solo eso — cría el ojo y la moral.
2. Busca el **error que se repite**: ¿movidas? → obturación corta la próxima
   vez. ¿Animales oscuros? → compensación. ¿Ojo blando? → punto AF. Las
   tablas de "si la foto sale…" de cada capítulo dan la corrección.
3. Decide **una sola cosa** que harás distinto mañana. Una, no cinco.
4. Marca en la [lista de tomas](../plan/lista-de-tomas.md) las conseguidas y elige
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
- **darktable**: módulo "reducción de ruido (perfilada)" — usa el perfil de
  tu cámara si tu versión lo incluye; si no, el modo genérico del módulo
  cumple igual.

Orden correcto: primero el denoise, después el revelado fino.

## Paso 4 — Las cinco operaciones que el resto de la guía da por hechas

El repo te manda hacer estas cinco cosas "en edición" una y otra vez. Aquí
está cómo, con los nombres de Lightroom y su equivalente libre.

### 1 · Recortar y enderezar

Es el paso 1 del revelado, pero merece detalle porque en fauna lo vas a usar
en la mitad de las fotos.

- **Tecla `R`** (Lightroom) abre el recorte. El **nivel automático** está en
  el botón de la reglita: `Auto` endereza solo casi siempre; si no, arrastra
  fuera del marco para girar a mano.
- Un horizonte torcido **1°** ya se nota en una duna o en el mar. Míralo
  siempre en las fotos de paisaje y de costa.
- **Cuánto puedes recortar**: los 26 Mpx aguantan un recorte al **50 %** de
  lado (queda un archivo de ~6,5 Mpx, de sobra para pantalla y para un A3).
  Si tienes que recortar más, no es una foto: es una anécdota.
- **Mantén la proporción** 3:2 por defecto; el cuadrado y el 16:9 son
  decisiones, no arreglos.
- En **darktable**: módulo `recortar` y `rotar y perspectiva`.

### 2 · Quitar el polvo del sensor

Con el polvo de Etosha y un solo cambio de objetivo, vas a tener manchas. Se
ven como puntos grises borrosos, **siempre en el mismo sitio**, y solo se
notan en zonas lisas y claras: cielos, dunas al sol, el pan blanco. A f/8 y
más cerrado, peor.

1. Lightroom: **tecla `Q`** (herramienta de eliminación).
2. Marca **`Visualizar puntos`** abajo del panel: la foto se vuelve un
   negativo raro donde las manchas saltan a la vista. Sube el deslizador
   hasta que las veas y **antes** de que aparezca ruido de más.
3. Pincel un poco **mayor que la mancha**, un clic encima, y el programa
   busca de dónde copiar. Si elige mal, arrastra el círculo de origen.
4. **El truco que ahorra una tarde**: cuando termines una foto, cópiale los
   ajustes (`Ctrl+Shift+C`) y **pégalos en todas las del mismo día**
   (`Ctrl+Shift+V`). El polvo está en el mismo sitio en todas: se limpian
   las 300 de golpe.
5. En **darktable**: módulo `retoque`, herramienta de clonar o curar.

### 3 · Blanco y negro (la carta del mediodía)

La guía te hace disparar **pensando en B/N** en tres sitios: la clave alta de
la calcreta a mediodía, las rayas de la cebra y los *badlands* del Kuiseb. El
RAW guarda el color, así que la decisión se toma aquí y es reversible.

1. **Tecla `V`** en Lightroom convierte a B/N. Eso solo es el punto de
   partida: una conversión "de fábrica" siempre sale gris y sosa.
2. La foto se hace en el panel **`Mezcla B/N`**: cada deslizador controla
   **qué gris le toca a cada color original**. Los dos que importan en
   Namibia:
   - **Bajar el azul** oscurece el cielo y hace que las nubes revienten.
   - **Subir el naranja y el amarillo** aclara la arena, la calcreta y la
     piel del elefante rebozado en polvo.
3. Luego, **contraste y negros**: en B/N hay que ser más bruto que en color.
   Que haya un negro de verdad y un blanco de verdad, o la foto se queda en
   barro gris.
4. **Cuándo tiene sentido**: luz dura sin color interesante (mediodía),
   escenas de puro patrón (cebras, dunas, la colonia de Cape Cross), niebla
   de la costa. **Cuándo no**: cualquier cosa a la hora dorada — ahí el color
   *es* el tema.
5. En **darktable**: módulo `monocromo` o, mejor, `mezclador de canales de
   color` en modo gris.

### 4 · Fusionar el horquillado (cuando la escena no cabía)

Si seguiste la instrucción de horquillar ±2 EV en Deadvlei o en un
contraluz, tienes tres archivos de la misma escena.

1. Selecciona las tres (clic + `Ctrl`).
2. `Foto → Combinar fotos → HDR`, o **`Ctrl+H`**.
3. Marca **`Alineación automática`** (por si el trípode se movió) y deja
   `Cantidad de desfantasma` en *Ninguno* salvo que se moviera algo en la
   escena (ramas, agua, un animal): entonces, *Medio*.
4. Sale un **DNG nuevo** con todo el rango dentro, que se revela como
   cualquier RAW — y ahora sí puedes bajar altas luces y subir sombras a lo
   bestia sin que se rompa.
5. El aviso de siempre: un HDR bien hecho **no se nota**. Si parece un
   cuadro, has subido demasiado las sombras.
6. En **darktable**: `crear HDR` desde la mesa de luz.

### 5 · Fundir cielo y suelo (las dos tomas de la noche)

El "nivel extra" de tu segunda noche de estrellas: una toma para el cielo
(20 s) y otra para el suelo (60–120 s), sin mover el trípode. Fundirlas pide
**capas**, así que aquí Lightroom se queda corto:

- **Gratis**: [GIMP](https://www.gimp.org/). **De pago, una vez**:
  [Affinity Photo](https://affinity.serif.com/es/photo/) (~70 €). También
  vale Photoshop si ya lo tienes.
- El método, en cuatro pasos:
  1. Revela las dos tomas por separado (cada una para lo suyo) y expórtalas
     a TIFF de 16 bits.
  2. Ábrelas **una encima de otra** como dos capas. Al no haber movido el
     trípode, encajan solas.
  3. A la capa de arriba, **máscara de capa**, y con un **degradado negro a
     blanco** sobre la línea del horizonte tapas la mitad que no quieres.
  4. Pincel negro suave, al 20 % de opacidad, para repasar la silueta (un
     árbol, una roca) donde el degradado recto no llega.
- **El atajo, si esto te supera**: haz UNA sola toma con la receta del
  cielo y sube las sombras del suelo en el revelado. Sale con más ruido
  abajo, pero es una foto, y funciona.
- Y para el **apilado** de astro, Sequator tiene su propia solución: la
  casilla `Freeze ground`, ya explicada más abajo.

## Astro: apilado con Sequator, paso a paso

Para las 10 tomas idénticas que hiciste siguiendo el
[capítulo 2](../a6700/02-astrofotografia-namibia.md)
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

(Los del Pixel salen ya montados del móvil — esto es para las series del
intervalómetro integrado de la a6700, que es la versión de máxima calidad.)

Para la serie de intervalos del capítulo 2 (300 tomas ≈ 12 s de clip a 25
fotogramas por segundo, los del vídeo del viaje):

1. Revela **una** foto de la serie y sincroniza/pega el ajuste a todas
   (misma exposición fija en cámara = mismo revelado para todas).
2. Exporta la serie a JPEG, lado largo 1920 px (o 3840 para 4K), a una
   carpeta vacía y con numeración ordenada.
3. Móntalo gratis con **ffmpeg** (<https://ffmpeg.org/>), un solo comando
   desde esa carpeta:
   `ffmpeg -framerate 25 -pattern_type glob -i '*.jpg' -c:v libx264 -pix_fmt yuv420p timelapse.mp4`
   (en Windows, cambia el patrón: `-i img%04d.jpg`).
   Alternativa con interfaz: **DaVinci Resolve** gratis
   (<https://www.blackmagicdesign.com/products/davinciresolve>) importa la
   carpeta como "image sequence".
4. ¿Parpadeo entre fotogramas (*flicker*)? Con todo en manual (exposición,
   ISO, WB fijos — como manda la receta) apenas habrá; si molesta, la
   herramienta especializada es **LRTimelapse** (de pago:
   <https://lrtimelapse.com/>).

## Montar el vídeo del viaje (DaVinci para novatos)

El cierre del viaje: **un solo vídeo de unos 3 minutos y sin voz** — imágenes,
sonido ambiente y una canción — con los dos materiales: los planos de la
a6700, que son el esqueleto, y los timelapses y el recurso del Pixel. El
guion ya lo rodaste: es la estructura en siete bloques de
[el vídeo del viaje](../tecnica/video-del-viaje.md) (gancho → el viaje empieza →
desierto → costa → safari → noche → cierre). El montaje, paso a paso en
**DaVinci Resolve** (gratis:
<https://www.blackmagicdesign.com/products/davinciresolve>):

1. Proyecto nuevo → importa la carpeta de clips del viaje (ya volcados por
   días al SSD). Los de la Sony y los del móvil van juntos: distinta cámara,
   misma línea de tiempo (si el color no casa, iguala el del móvil al de la
   Sony con la rueda de temperatura, no al revés). La frecuencia de la línea
   de tiempo, a **25 fps** —la de la Sony—, fijada en los ajustes del
   proyecto **antes** de crear la línea de tiempo; los clips del Pixel, que
   graba a 24/30/60, entran igual y DaVinci los adapta.
2. **Primero la música**: elige la canción antes de montar — sin voz, es
   ella la que marca el ritmo. Luego coloca los planos por bloques, cortando
   en los golpes que te pida la música. Nunca en el orden de grabación: la
   historia manda.
3. Recorta cada clip a sus **3–6 segundos buenos** (herramienta de corte;
   los 3 s quietos que dejaste al grabar son el margen). Fuera todo lo que
   dude: mejor 3 minutos redondos que 8 regulares.
4. Los timelapses del Pixel ya vienen montados: entran como un clip más. Los
   de la a6700, como los exportaste
   ([arriba](#montar-un-timelapse-en-vídeo)).
5. **Música y ambiente**: una sola canción sin copyright (la biblioteca de
   audio de YouTube Studio, por ejemplo) de fondo, y **el sonido ambiente de
   los clips por debajo, no apagado** — es lo que hace que el vídeo se sienta
   real. Y en dos o tres momentos, baja la música y deja **solo el ambiente**:
   las focas, la tormenta, el elefante bebiendo. Ese contraste es todo el
   "montaje avanzado" que necesitas.
6. Exporta con el preajuste **YouTube 1080p** de la pestaña Deliver y
   listo: ese archivo es el recuerdo.

La alternativa exprés: **Google Fotos** monta solo, desde el móvil, un
resumen con música en cinco minutos — vale como tráiler para mandar al grupo
mientras te animas con el montaje bueno.

## Exportar para compartir

- JPEG, lado largo **2048 px**, espacio de color **sRGB** (si no, los colores
  se ven lavados en el móvil de quien lo recibe).
- Para imprimir o archivar: JPEG a tamaño completo, calidad 90+.

## Si te atascas…

| Problema | Solución |
|---|---|
| 800 fotos y no sabes por dónde empezar | No edites: **criba** primero (paso 1). Editar sin cribar es el atasco número 1 |
| El Denoise tarda una eternidad | Es normal (es IA): pásalo solo a las supervivientes de la criba, nunca al día entero |
| Sequator no traga los archivos | Dale los RAW (.ARW) directamente; si protesta, convierte antes a TIFF y repite |
| El apilado sale con el suelo emborronado | Falta `Freeze ground` en Composition |
| El comando de ffmpeg falla en Windows | El patrón `*.jpg` no funciona ahí: usa `-i img%04d.jpg` con los archivos numerados |
| El timelapse parpadea (flicker) | ¿Algo quedó en auto (ISO, WB)? Con todo fijo apenas ocurre; si molesta, LRTimelapse |
| Los colores del vídeo/foto se ven lavados al compartir | Exportaste fuera de sRGB (foto) o el móvil del receptor hace lo suyo: exporta sRGB y preajuste YouTube 1080p |

## La regla final

De cada sesión de edición deben salir **pocas fotos rematadas**, no muchas a
medias: tres redondas por día de viaje son un reportaje espectacular de
cuarenta y cinco.

## Ejercicio antes de volar (una tarde)

Coge **veinte RAW** de cualquier salida tuya y haz el flujo entero de esta
guía, cronometrado: criba en dos pasadas, revelado de las cinco marcadas en
el orden de la tabla, ruido por IA en la más oscura y exportación a sRGB.
Objetivo: **menos de una hora en total**. A la vuelta tendrás miles de
fotos, no veinte: si estas te llevan tres horas, aquellas no las harás.

## Referencias

- Lightroom: <https://www.adobe.com/products/photoshop-lightroom.html> · darktable: <https://www.darktable.org/>
- Sequator: <https://sites.google.com/view/sequator/> · StarStaX: <https://markus-enzweiler.de/software/starstax/>
- DxO PureRAW: <https://www.dxo.com/dxo-pureraw/>
- ffmpeg: <https://ffmpeg.org/> · DaVinci Resolve: <https://www.blackmagicdesign.com/products/davinciresolve> · LRTimelapse: <https://lrtimelapse.com/>
