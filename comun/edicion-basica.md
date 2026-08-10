# Edición básica — del RAW a la foto terminada

Todo el tutorial te hace disparar en RAW; esta guía es el "después". Sin
teoría de color: un flujo que funciona, en orden.

## El programa

- **Adobe Lightroom** (~12 €/mes, incluye el Denoise por IA): la opción
  cómoda si el presupuesto lo permite. <https://www.adobe.com/products/photoshop-lightroom.html>
- **darktable** (gratis y libre, hace lo mismo con más curva de aprendizaje):
  <https://www.darktable.org/>

Los pasos de abajo valen para ambos; los nombres exactos cambian un poco.

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
  perfil de ruido de ambas cámaras.

Orden correcto: primero el denoise, después el revelado fino.

## Astro: apilado con Sequator, paso a paso

Para las 10 tomas idénticas que hiciste siguiendo el capítulo 2 de tu cámara
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

## Exportar para compartir

- JPEG, lado largo **2048 px**, espacio de color **sRGB** (si no, los colores
  se ven lavados en el móvil de quien lo recibe).
- Para imprimir o archivar: JPEG a tamaño completo, calidad 90+.
