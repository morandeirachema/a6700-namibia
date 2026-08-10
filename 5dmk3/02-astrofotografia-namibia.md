# 2. Astrofotografía en Namibia con la 5D Mark III — paso a paso

Namibia tiene algunos de los cielos más oscuros del planeta (la reserva
NamibRand es Dark Sky Sanctuary certificado). De mayo a septiembre —estación
seca— la Vía Láctea es visible gran parte de la noche.

## Receta rápida

| Parámetro | Valor de partida |
|---|---|
| Modo | M (o directamente **C2**, [capítulo 1](01-configuracion-basica.md)) |
| Apertura | La más baja del objetivo (f/2.8 típico en budget) |
| Obturación | 15–20 s con un 14 mm |
| ISO | 3200; sube a 6400 si queda oscura |
| Balance de blancos | Manual (K), 3900 K |
| Formato | RAW |
| Enfoque | Manual (interruptor AF/MF del objetivo en **MF**) |
| Estabilizador del objetivo | OFF (estás en trípode) |
| Disparo | Temporizador 2 s |
| Reducción ruido larga exposición | OFF |

## Antes de salir (checklist)

- [ ] Noche cercana a **luna nueva** (PhotoPills: <https://www.photopills.com/>).
- [ ] Batería llena + repuesto en el bolsillo (el frío las agota).
- [ ] Trípode, frontal de luz roja, cinta adhesiva.
- [ ] Dónde estará la Vía Láctea a qué hora: planificador de PhotoPills o
  Stellarium (<https://stellarium.org/>).
- [ ] Si quieres timelapse: **intervalómetro de cable** (la 5D3 no lo trae
  integrado, ver abajo).

## En el sitio, paso a paso

1. **Monta el trípode** bien asentado; cuelga la mochila del gancho central si
   hay viento.
2. Dial a **C2** (o pon la receta de arriba a mano).
3. **Componer a oscuras**: por el visor óptico no verás casi nada. Dos opciones:
   - Foto de reconocimiento "sucia": 5 s a ISO 25600. Sale horrible, pero te
     enseña el encuadre en 5 segundos. Ajusta y repite.
   - Live View con `Simulación de exposición` ON y la pantalla al máximo brillo.
4. **Enfoca a una estrella** (la parte más delicada, 2 minutos):
   1. Objetivo en **MF**, estabilizador OFF.
   2. Activa **Live View**, apunta el recuadro a la estrella más brillante.
   3. Botón **lupa (+)** hasta el aumento x10.
   4. Gira el anillo de enfoque despacio hasta que la estrella sea el punto
      **más pequeño y fino posible** (si se hincha, te has pasado).
   5. Fija el anillo con cinta. No lo toques más en toda la noche.
5. **Foto de prueba** con la receta rápida y temporizador de 2 s.
6. **Corrige mirando el histograma** (la pantalla engaña de noche: te parecerá
   más clara de lo que es). La montaña debe quedar despegada del borde
   izquierdo, hacia el primer tercio.
7. Cuando salga la buena: **haz 10 tomas idénticas seguidas** sin tocar nada.
   Se apilan luego en el ordenador y el ruido baja muchísimo (importante en la
   5D3, que a ISO alto es más ruidosa que las cámaras modernas).
8. ¿Timelapse? Necesitas un **intervalómetro de cable** (conector N3: el Canon
   TC-80N3 o un clon de ~25 €): 15 s de foto, intervalo 17 s, 300 tomas ≈ 10 s
   de vídeo.
9. Antes de recoger: revisa la última foto **ampliada al máximo** por si el
   enfoque se movió.

## Si la foto sale…

| Problema | Solución |
|---|---|
| Muy oscura | Sube ISO un paso (3200 → 6400). No alargues los segundos más allá del límite de trazas |
| Estrellas alargadas (trazas) | Baja los segundos: 20 → 15 → 13. Con un 14 mm aguantas ~20 s; con un 24 mm, ~13 s (calculadora "Spot Stars" de PhotoPills) |
| Estrellas gordas o borrosas | Enfoque mal: repite el paso 4. No es el ISO ni los segundos |
| Todo movido | Trípode vibrando: viento, correa colgando o tocaste la cámara — temporizador 2 s siempre; activa el **bloqueo de espejo** si hay dudas |
| Cielo naranja/verde raro | Balance de blancos a 3900 K (en RAW se corrige después sin pérdida) |
| Esquinas con estrellas "estiradas" | Coma del objetivo, no eres tú. Cierra de f/2.8 a f/3.2–3.5 si molesta mucho |
| Puntos rojos/calientes en exposiciones largas | Píxeles calientes, normales en un sensor de 2012. El apilado y el NR por IA los eliminan |

## Apilado en casa

Apila las 10 tomas del paso 7 con Sequator (Windows, gratis:
<https://sites.google.com/site/sequatorglobal/>) o Starry Landscape Stacker
(macOS: <https://sites.google.com/site/starrylandscapestacker/>). En la 5D3
es la diferencia entre un cielo ruidoso y uno limpio.

## Opcional avanzado: Magic Lantern

El firmware alternativo Magic Lantern (<https://www.magiclantern.fm/>) añade a
la 5D3 intervalómetro integrado y focus peaking. Funciona bien, pero es
software no oficial: instálalo solo si te sientes cómodo asumiendo el riesgo,
y nunca la semana antes del viaje.

## Localizaciones destacadas

- **NamibRand / zona de Sossusvlei**: cielo certificado Dark Sky.
  <https://darksky.org/places/namibrand-nature-reserve/>
- **Spitzkoppe**: arcos de granito como primer plano y acampada dentro.
- **Deadvlei/Sossusvlei**: acceso nocturno restringido; hay que alojarse en
  Sesriem (dentro de la primera puerta) o pedir permiso especial.
- **Bosque de árboles aljaba (Keetmanshoop)**: siluetas clásicas del cielo austral.

## Referencias

- Lonely Speck, práctica de astrofotografía: <https://www.lonelyspeck.com/>
- Guía práctica de Vía Láctea en español: <https://capturetheatlas.com/es/fotografiar-via-lactea/>
