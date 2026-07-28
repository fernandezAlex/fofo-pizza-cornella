# Categorización provisional de la carta

Esta clasificación es editorial y provisional. No procede de una taxonomía oficial de Fofó Pizza; se creó para que los filtros de la web sean útiles hasta que la marca confirme sus categorías.

Las categorías pueden solaparse: una pizza clásica también puede ser vegetariana o picante.

## Todas — 20

Incluye la carta completa.

## Clásicas — 8

- Margherita
- Emy
- Diávola
- Cuatro quesos
- Capricciosa
- Calzone
- Marinara
- Focaccia

## De la casa — 12

- Parma e Búfala
- Fofó
- Atún
- Ortolana
- Parmigiana
- Evelin
- Luis
- Maria Elena
- Frankfurt
- Elena
- Fernando
- La Mortadella

## Vegetarianas — 5

- Margherita
- Cuatro quesos
- Ortolana
- Marinara
- Focaccia

## Picantes — 4

- Diávola
- Calzone
- Fofó
- Evelin

## Implementación

Cada `<article class="menu-item">` declara sus categorías en `data-tags`. Los botones comparan su `data-filter` con esas etiquetas. La regla CSS `.menu-item[hidden]{display:none}` es necesaria porque los artículos usan `display:grid`; sin esa regla, el estilo de autor prevalece sobre el comportamiento visual por defecto del atributo HTML `hidden`.

La validación automática comprueba los recuentos 8/12/5/4 para evitar cambios accidentales.
