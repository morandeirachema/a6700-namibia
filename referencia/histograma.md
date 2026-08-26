# El histograma por escenario — chuleta visual

> 🟢 **Iniciación** · Da por sabido: nada · Te desbloquea: juzgar si una foto está bien expuesta sin fiarte de la pantalla.

El histograma es la única medición fiable (la pantalla engaña al sol y de
noche). Regla universal: **el borde derecho es sagrado** — lo que lo toca es
blanco quemado irrecuperable; el izquierdo perdona más, porque el RAW levanta
sombras. A partir de ahí, cada escenario tiene su forma "buena".

## Safari diurno

```
│      ▄▄█████▄▄        │
│   ▄▄█████████████▄    │
└┴──────────────────┴──┘
 negro              blanco
```

- Montaña ancha por el centro, **sin tocar ningún borde**.
- Caso típico de Etosha: animal oscuro sobre calcreta clara → **dos jorobas**
  (animal a la izquierda, fondo a la derecha). Expón para que la joroba
  derecha se acerque al borde **sin tocarlo** (compensación +0.7/+1): el
  animal quedará levantable en edición.
- Destellos del sol en agua o cromados pueden tocar la derecha: ignóralos, son
  puntuales.

## Paisaje

```
│  ▄▄███▄▄▄▄▄▄▄███▄▄    │
│ ██████████████████▄   │
└┴──────────────────┴──┘
```

- Montaña que **usa casi todo el ancho** sin tocar bordes: la escena tiene
  negros, medios y blancos. Es el histograma "de libro".
- Amanecer en Deadvlei o interior de Kolmanskop: si para no quemar la derecha
  tienes que empotrar la izquierda (no cabe todo), la escena supera al sensor
  → **horquillado ±2 EV** ([guía de paisaje](../tecnica/paisaje-namibia.md)).
- **Excepción deliberada — siluetas al atardecer**: pico pegado al borde
  izquierdo (las siluetas negras) + joroba a la derecha (el cielo). Aquí el
  amontonamiento a la izquierda no es un error, es la foto.

## Safari nocturno en charca

```
│█▄                     │
│███▄        ▄█▄        │
└┴──────────────────┴──┘
      animal iluminado ↑
```

- Gran masa **pegada a la izquierda** (la noche alrededor: es negro real,
  déjalo negro) + una **joroba pequeña hacia el centro-derecha**: el animal
  bajo el foco. Esa joroba es lo único que importa.
- Error típico: subir la exposición "porque el histograma está muy a la
  izquierda" → el animal se quema. La masa izquierda **debe** estar ahí.
- Vigila solo que la joroba del animal no toque el borde derecho (la piel
  mojada bajo el foco quema rápido: −0.3/−0.7 si hace falta).

## Astrofotografía

```
│   ▄██▄                │
│  ██████▄              │
└┴──────────────────┴──┘
   ↑ primer tercio
```

- **Una sola montaña estrecha en el primer tercio izquierdo, despegada del
  borde**. Esa es toda la regla del astro.
- Pegada al borde izquierdo → foto subexpuesta: sube ISO un paso (no los
  segundos, que hacen trazas).
- Montaña en el centro o más allá → cielo sobreexpuesto: hay luna, resplandor
  de campamento… o te has pasado de ISO.
- Las estrellas son picos minúsculos a la derecha: normal, ignóralos.

## Cómo verlo en la a6700

En revisión (▶), botón DISP hasta la vista con histograma. Y la ventaja de
esta cámara: el **histograma en vivo** — pulsa DISP mientras encuadras y la
gráfica aparece en el visor o la pantalla **antes** de disparar, con la
exposición real que va a salir (salvo de noche con exposiciones largas: ahí
no acumula los segundos — fíate del de la revisión). Para lo quemado, activa
el **Zebra 100+** (en el menú de exposición/color): rayas en vivo sobre lo
que se quema — aquí la alarma no espera a la revisión.

## Ejercicio (15 minutos, una vez)

Cinco fotos de la **misma pared blanca** con compensación −2, −1, 0, +1, +2.
Míralas con el histograma en pantalla y quédate con la imagen mental: la
misma pared, la misma luz, y la montaña recorriendo el gráfico de izquierda a
derecha. A partir de ahí el histograma deja de ser un adorno.

Repítelo con algo **negro** (una chaqueta oscura): verás lo contrario — la
cámara intenta hacerla gris, y hay que compensar **en negativo**.

## Referencias

- El porqué de todo esto (rango dinámico y ETTR): [por qué funciona](../mejora/por-que-funciona.md)
- Guía de ayuda de la a6700 (histograma y Zebra): <https://helpguide.sony.net/ilc/2320/v1/es/>
