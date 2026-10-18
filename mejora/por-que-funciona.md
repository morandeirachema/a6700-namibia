# Por qué funciona — el modelo que hay detrás de las recetas

> 🔴 **Avanzado** · Da por sabido: los capítulos 0 a 5 y haber disparado unas cuantas tardes · Te desbloquea: inventar **tu** receta cuando la escena no está en ninguna tabla.

Todo el repo hasta aquí te da recetas: números que funcionan, comprobados,
para las situaciones que vas a encontrar. Funcionan porque debajo hay un
modelo — y el día que la escena no encaje en ninguna tabla (y pasará), lo que
te salva es entender el modelo, no memorizar más tablas.

**La regla de esta guía**: ningún concepto se queda en teoría. Cada uno
termina en **la decisión** que te deja tomar, con los números de **tu**
equipo: una a6700 de 26 Mpx (sensor APS-C de 23,3 × 15,5 mm), un 11 mm f/1.8
y un 70-350 f/4.5-6.3.

---

## 1 · El paso: la única moneda del sistema

Un **paso** (o *stop*) es **el doble o la mitad de luz**. Es la única unidad
que necesitas, y los tres controles la manejan con escalas distintas:

| Control | Un paso más de luz es… | La escala |
|---|---|---|
| **Obturación** | El doble de tiempo | 1/1000 → 1/500 → 1/250 → 1/125… |
| **Apertura** | Un número f **dividido entre √2** | f/2 → 2.8 → 4 → 5.6 → 8 → 11 (cada salto ahí es un paso; el f/1.8 del 11 mm es un tercio más que f/2) |
| **ISO** | El doble de amplificación | 100 → 200 → 400 → 800 → 1600… |

De ahí sale lo único que hay que interiorizar: **tres exposiciones que dejan
entrar la misma luz** y dan tres fotos completamente distintas.

| Ajustes | Misma luz, pero… |
|---|---|
| 1/2000 · f/6.3 · ISO 6400 | El animal congelado, ruido alto |
| 1/500 · f/6.3 · ISO 1600 | Dos pasos menos de ruido, riesgo de movida |
| 1/500 · f/3.2 · ISO 400 | Aún más limpia — pero tu tele no abre a f/3.2 |

**La decisión**: cuando falte luz, decides **qué pagas**. Movimiento
(obturación), profundidad (apertura) o ruido (ISO). El orden que usa este
repo no es capricho: con trípode y animal quieto se paga con **tiempo**
primero, porque es lo único gratis; a pulso se paga con **ISO**, porque una
foto ruidosa se arregla y una movida no.

> **Ejercicio (20 minutos, en casa).** Un objeto quieto, luz constante. Haz
> la misma foto con cuatro combinaciones equivalentes, de 1/60 · f/8 · ISO 400
> a 1/500 · f/2.8 · ISO 400 compensando. Ábrelas juntas: la exposición es la
> misma y las cuatro fotos son distintas. Eso es el sistema entero.

---

## 2 · Exponer a la derecha, y por qué el histograma manda

Un RAW **no reparte la información a partes iguales**. La mitad de todos los
niveles de tu archivo viven en el paso más luminoso; el siguiente paso tiene
la mitad, el siguiente la mitad de eso… Traducción: **las sombras son pobres
en datos y las altas luces son ricas**. Por eso una foto subexpuesta que
levantas en revelado saca ruido y bandas, y una foto expuesta "hacia la
derecha" (ETTR) tiene margen de sobra.

Pero hay un límite duro: **lo quemado no vuelve**. No hay dato que
recuperar donde el sensor saturó.

**La decisión**: empuja el histograma a la derecha **sin que toque el
borde**. En la práctica de este viaje:

- Fondo de calcreta blanca o cielo → **+0.7 / +1** y vigila el **Zebra 100+**:
  si parpadea sobre algo que debe tener detalle, baja.
- Un animal oscuro sobre fondo claro no es un problema de exposición: es un
  problema de **medición** (medición puntual vinculada al punto de enfoque,
  [AF y exposición a fondo](af-y-exposicion-a-fondo.md)).
- **Dónde NO se aplica**: en astro no hay derecha a la que exponer — el cielo
  es oscuro de verdad. Ahí la montaña del histograma va en el **primer
  tercio**, separada del borde izquierdo, y punto.

---

## 3 · Profundidad de campo: tres palancas, y una pesa más

Lo que sale nítido delante y detrás del punto de enfoque depende de tres
cosas, y conviene saber **cuál manda**:

1. **La distancia al sujeto** — la palanca fuerte. Va al cuadrado: al doble
   de distancia, cuatro veces más profundidad.
2. **La focal** — también al cuadrado, en sentido contrario: más milímetros,
   menos profundidad.
3. **La apertura** — la palanca suave, lineal.

Con **tu 11 mm** esto se traduce en una tabla que puedes usar tal cual. La
**hiperfocal** es la distancia a la que enfocar para que todo salga nítido
desde su mitad hasta el infinito:

| Apertura | Enfoca a… | Y sale nítido desde… |
|---|---|---|
| f/2.8 | 2,2 m | ~1,1 m hasta ∞ |
| f/4 | 1,5 m | ~0,75 m hasta ∞ |
| f/5.6 | 1,1 m | ~0,55 m hasta ∞ |
| **f/8** | **0,8 m** | **~0,40 m hasta ∞** |
| f/11 | 0,6 m | ~0,30 m hasta ∞ |

Por eso la receta de paisaje del repo dice "f/8, enfoca a ~1 m y pasa a MF":
no es magia, es esa fila. Y por eso puedes poner una piedra a medio metro de
la lente sin perder las dunas del fondo.

Con **el 70-350** la misma cuenta da un susto sano, a 30 m del animal:

| Focal y apertura | Profundidad nítida total |
|---|---|
| 70 mm · f/4.5 | ~48 metros |
| 200 mm · f/6.3 | ~5,7 metros |
| 350 mm · f/6.3 | **~1,9 metros** |
| 350 mm · f/6.3, pero a 15 m | **~0,5 metros** |

**La decisión**: a 350 mm y con el animal cerca **no tienes profundidad para
fallar**: medio metro es la diferencia entre el ojo y la oreja. De ahí que
todo el repo insista en el ojo y en verificar al 100 %. Y al revés: a 70 mm
tienes cuarenta y ocho metros de margen — encuadrar más ancho no solo da luz,
también perdona.

---

## 4 · Difracción: por qué f/16 no es "más nítido"

Al cerrar el diafragma, la luz que pasa por un agujero pequeño se **difracta**
y cada punto de la imagen se emborrona un poco. Es física, no calidad del
objetivo: le pasa a todos por igual.

Cuándo empieza a notarse depende del tamaño del píxel. El tuyo mide unas
**3,8 micras** (26 Mpx en 23,3 mm de ancho), así que:

- **f/5.6 – f/8**: el punto dulce. Máxima nitidez real de tus dos objetivos.
- **f/11**: ya se nota si amplías al 100 %. Aceptable cuando de verdad
  necesitas la profundidad.
- **f/16 y más allá**: pérdida clara. Ganas profundidad y pierdes detalle en
  **toda** la foto.

**La decisión**: el "f/16 de paisaje" que has leído mil veces es herencia del
formato completo y de cámaras de menos megapíxeles. En tu equipo, paisaje es
**f/8 con la hiperfocal puesta**, no f/16. Y si aun así no llega la
profundidad, la solución no es cerrar más: es **alejar el primer plano** —
que es la palanca fuerte del punto 3.

---

## 5 · La compresión no la hace el tele: la hace la distancia

"El teleobjetivo comprime los planos" es una verdad a medias que se repite en
todas partes. Lo que comprime es **estar lejos**: si haces la foto desde el
mismo sitio con 70 mm y recortas hasta el encuadre de 350 mm, la relación
entre el sujeto y el fondo es **exactamente la misma**. El tele no comprime:
te permite estar lejos y aun así llenar el encuadre.

**Las decisiones que salen de esto**:

- **El órix diminuto en la duna enorme**: eso no es "poner el tele", es
  **alejarte** todo lo que puedas y luego encuadrar con el zoom. Desde cerca,
  esa foto no existe con ninguna focal.
- **El retrato de fauna que no deforma**: no te acerques más — **aléjate y
  zoomea**. Cerca y con angular, la nariz del animal se hincha.
- **Las capas azuladas de Spreetshoogte**: la compresión de sierras que hace
  bonito el mirador es distancia pura; el 70-350 solo la recorta.

---

## 6 · Ruido, ISO y el punto en que deja de importar

El ISO **no añade ruido**: amplifica. El ruido ya estaba, y es sobre todo
falta de fotones — poca luz. Por eso la frase correcta no es "no subas el
ISO", sino **"recoge toda la luz que puedas, y luego amplifica lo que haga
falta"**.

Tu cámara tiene ISO base **100** (máxima calidad y rango dinámico) y, como
casi todos los sensores modernos, un **segundo escalón de ganancia** en la
parte baja-media del rango. Y algo más útil todavía: **a partir de ISO ~800
la a6700 es prácticamente ISO-invariante** — subir el ISO en cámara o
levantar la exposición después en el revelado dan casi el mismo resultado.

**Las decisiones**:

- **Por debajo de ISO 800, expón bien en cámara.** Ahí la cámara **no** es
  invariante y subexponer "para levantarlo luego" te cuesta calidad real.
- **Por encima de 800, protege las altas luces.** En la charca, si dudas
  entre quemar la orilla iluminada o dejar la foto un poco oscura: **déjala
  oscura y levántala en revelado**. Lo quemado no vuelve; el ruido que añades
  al levantar es pequeño y la reducción por IA se lo come.
- Y antes de cruzar ningún techo de ISO, el orden del [capítulo 4](../a6700/04-safari-nocturno-charcas.md)
  sigue mandando: con trípode y animal quieto, **baja la obturación primero**.
  Eso es luz gratis; el ISO nunca lo es.

---

## 7 · El autofoco por dentro (y por qué muere en la charca)

La a6700 combina **detección de fase** (rápida, predictiva, la que persigue
al animal) y **detección de contraste** (fina, la que remata). Ambas
necesitan lo mismo: **un borde con contraste**. Sobre una panza lisa o un
cielo uniforme no hay nada que medir, y el objetivo "caza" recorriendo todo
el rango.

Y hay un número que lo explica casi todo: la ficha de Sony da sensibilidad de
AF **de −3 EV a +20 EV**, medida **a f/2.0**. Tu 70-350 abre a **f/6.3**: son
algo más de **tres pasos** (3,3) menos de luz llegando al sensor. El AF que
en el papel ve a −3 EV, con tu tele puesto se queda alrededor de **+0,3 EV** — que
es, exactamente, la penumbra de la charca de Okaukuejo.

**Las decisiones**:

- En la charca, no es que el AF "falle": es que está fuera de su rango.
  **Punto único sobre una zona iluminada y con borde**, o enfoque manual
  prefijado a la orilla. Las dos cosas que dice el capítulo 4, ahora con el
  porqué.
- Con el 11 mm (f/1.8) el AF ve muchísimo mejor, pero en astro tampoco hay
  contraste: por eso ahí siempre es **manual con lupa y peaking**.
- La **sensibilidad de seguimiento** no cambia la potencia del AF: solo
  decide **cuánto tarda en soltar** el sujeto cuando algo se cruza. Por eso 1
  con hierba delante y 4–5 en una persecución.

---

## 8 · Tus dos objetivos, sin marketing

**Sony E 11mm F1.8** — angular luminoso, sin estabilizador propio (lo pone el
IBIS), rosca de 55 mm.

- A f/1.8 entra toda la luz del mundo, pero **las esquinas son lo primero que
  sufre** en astro: las estrellas del borde pueden salir con "alitas" (coma).
  Si te pasa, cierra a **f/2.2–f/2.8** y sube el ISO un paso: pierdes menos
  que ganas. Compruébalo en casa con la prueba de punto de luz de la
  [hoja de verificación](../a6700/verificacion-in-situ.md), no en Namibia.
- Para paisaje, f/8 con la hiperfocal de la tabla del punto 3.

**Sony E 70-350mm F4.5-6.3 G OSS** — 105–525 mm equivalentes, y el objetivo
que más vas a usar.

- **Su apertura escalona**: f/4.5 (70–81 mm) · f/5 (82–113) · f/5.6 (114–199)
  · f/6.3 (200–350). Recoger el zoom por debajo de 200 mm **es luz gratis**, y
  por debajo de 114 mm, más todavía.
- Como todo superzoom, **su punto más blando es 350 mm a f/6.3**. Cuando el
  animal lo permita, encuadrar a ~300 mm y recortar los 26 Mpx en edición a
  menudo da un resultado igual o mejor.
- **0,23x de ampliación máxima** a 350 mm desde 1,5 m: da para texturas y
  flores grandes. No es macro, y no lo va a ser.

---

## Todo el modelo, en una tabla de decisiones

| Cuando… | El modelo dice… | Y tú haces… |
|---|---|---|
| Falta luz | Solo hay tres monedas y todas cuestan algo | Con apoyo, paga con tiempo; a pulso, con ISO |
| Fondo blanco o cielo | El medidor busca el gris medio | +0.7/+1 y vigila el Zebra 100+ |
| Dudas si quemar o subexponer (ISO alto) | Por encima de 800 la cámara es casi invariante | Salva las altas luces, levanta después |
| A 350 mm y el animal cerca | Menos de un metro de profundidad | El ojo, y verificación al 100 % |
| Quieres todo nítido en paisaje | La difracción castiga a partir de f/11 | f/8 e hiperfocal; si no llega, aleja el primer plano |
| Quieres el sujeto pequeño en un fondo enorme | La compresión es distancia, no focal | Aléjate y zoomea |
| El AF caza y no fija de noche | Con f/6.3 pierdes algo más de 3 pasos de sensibilidad | Punto único a un borde iluminado, o MF prefijado |

## Ejercicios (tres tardes, antes de volar)

1. **La tarde del paso** (ejercicio del punto 1): cuatro exposiciones
   equivalentes de la misma escena. Aprendes a pensar en pasos, no en números
   sueltos.
2. **La tarde de la profundidad**: pon tres objetos a 2, 4 y 10 metros
   (a 350 mm el tele no enfoca a menos de 1,5 m). Fotografía la fila a 70 mm
   y a 350 mm, y luego a f/6.3 (lo más abierto a 350 mm) y a f/11. Cuatro
   fotos que enseñan la tabla del punto 3 mejor que la tabla.
3. **La tarde de la difracción**: un cartel con texto pequeño, trípode, misma
   escena a f/4, f/8, f/11 y f/16. Amplía al 100 %. Verás con tus ojos dónde
   deja de mejorar y empieza a empeorar — y no volverás a cerrar por inercia.

## Referencias

- Especificaciones oficiales de la a6700 (sensor, rango de AF): <https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_specifications_ilc2320.html>
- Guía de ayuda completa de la a6700: <https://helpguide.sony.net/ilc/2320/v1/es/>
- Difracción y límite del sensor, con calculadora: <https://www.cambridgeincolour.com/tutorials/diffraction-photography.htm>
- Profundidad de campo e hiperfocal, con calculadora: <https://www.dofmaster.com/dofjs.html>
- Curvas de ruido de lectura y rango dinámico medidos, cámara a cámara (Photons to Photos): <https://www.photonstophotos.net/>
- Prueba de invarianza ISO de la a6700 hecha por usuarios (foro DPReview): <https://www.dpreview.com/forums/threads/a6700-iso-invariance-test.4740029/>
- Review de referencia del Sony E 70-350mm G OSS (Dustin Abbott): <https://dustinabbott.net/2022/05/sony-e-70-350mm-f4-5-6-3-g-oss-review/>
- Ficha oficial del Sony E 11mm F1.8: <https://www.sony.es/lenses/products/sel11f18>
