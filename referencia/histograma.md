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

## Silueta y contraluz

```
│█                    ▄█│
│██▄                 ███│
└┴──────────────────┴──┘
 ↑ el animal          ↑ el cielo
```

- **Dos picos separados y el centro vacío**: el animal empotrado a la
  izquierda (negro de verdad) y el cielo cerca de la derecha. El valle del
  medio no es un fallo: **es la foto**.
- Expón para que el pico derecho se acerque al borde **sin tocarlo** — el
  color del cielo es lo único que hay que salvar. Compensación **−1/−1.7**.
- Si intentas rescatar el animal, pierdes el cielo y te quedas con una foto
  gris a medio camino ([fotos desmontadas](../mejora/fotos-desmontadas.md), nº 5).
- **Con polvo a contraluz** el pico izquierdo se ensancha y sube hacia el
  centro: es la luz atravesando las partículas. Perfecto.

## Clave alta: mediodía sobre la calcreta

```
│              ▄▄███████│
│           ▄██████████▓│
└┴──────────────────┴──┘
        ↑ casi todo a la derecha
```

- **Casi todo amontonado a la derecha, sin llegar a tocar el borde.** Es el
  histograma que parece "mal expuesto" y no lo es: el pan de Etosha **es**
  blanco.
- El medidor querrá oscurecerlo hasta gris: compensa **+2/3 a +1** y
  comprueba con el **Zebra 100+** que la calcreta raya solo en los brillos
  puntuales, no en toda la superficie.
- Es la receta de la foto en clave alta que luego se convierte a blanco y
  negro ([edición](../campo/edicion-basica.md)).

## Aves contra el cielo

```
│    ▄▄               ██│
│   ████             ███│
└┴──────────────────┴──┘
```

- Parecido a la silueta, pero **el pico del cielo manda**: un cielo blanco
  quemado deja el ave recortada sobre nada.
- Con cielo claro, **+1** para que el ave no salga en negro; con cielo azul
  intenso, **0 o −0.3**.
- Comprueba en revisión que el borde derecho no está tocado: en cielo blanco
  se quema sin avisar.

## Retrato de personas

```
│      ▄▄███▄▄▄         │
│   ▄████████████▄      │
└┴──────────────────┴──┘
      ↑ la cara, aquí
```

- Lo único que importa es **dónde cae la piel**: en el centro-derecha, nunca
  en el tercio izquierdo.
- Con arena o cielo detrás, la cara se va a la izquierda sola: **+0.7/+1**.
- A contraluz, **+1 a +1.7** — y da igual que el fondo se queme: la foto es
  la cara ([retrato de viaje](../tecnica/retrato-de-viaje.md)).

## De un vistazo

| Tipo de foto | Dónde va la masa | Compensación de partida |
|---|---|---|
| Safari, luz normal | Centro ancho, sin tocar bordes | 0 |
| Animal oscuro sobre calcreta | Dos jorobas; la derecha cerca del borde | **+0.7 / +1** |
| Mediodía en el pan (clave alta) | Casi todo a la derecha | **+2/3 a +1** |
| Silueta y contraluz | Dos picos, valle en medio | **−1 / −1.7** |
| Ave contra cielo claro | Pico del cielo a la derecha | **+1** |
| Retrato de persona | La piel en el centro-derecha | **+0.7 / +1** |
| Paisaje "de libro" | Usa todo el ancho | 0 |
| Paisaje que no cabe | Empotrado en **ambos** bordes → horquilla | ±2 EV |
| Charca de noche | Masa pegada a la izquierda + joroba pequeña | Ninguna: **no la toques** |
| Astro | Una montaña en el primer tercio, despegada | Subir ISO, no segundos |

## Cómo verlo en la a6700

En revisión (▶), botón DISP hasta la vista con histograma. Ahí, además,
**las zonas quemadas o empastadas parpadean** sobre la foto (la advertencia
de sobrexposición/subexposición de Sony): si parpadea algo que debía tener
detalle, la siguiente con −0,3. Y la ventaja de
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
