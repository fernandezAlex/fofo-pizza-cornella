# Imágenes de la carta

## Estado actual

Las 20 pizzas muestran una miniatura circular y abren un modal circular accesible. Hasta disponer de fotografías propias de cada receta, todas utilizan provisionalmente:

- `assets/71452652.jpg`

La imagen se reutiliza desde la constante `PIZZA_PLACEHOLDER` de `index.html`, por lo que el navegador solo descarga una vez el archivo aunque aparezca en toda la carta.

## Interacción

- Hover o foco: la miniatura aumenta ligeramente y gira unos grados.
- Clic: se abre un `<dialog>` modal con la pizza ampliada.
- Apertura: la imagen circular escala y gira hasta quedar completamente estática.
- Cierre: botón circular, tecla Escape o clic fuera de la imagen.
- Al cerrar, el foco vuelve a la miniatura que abrió el modal.
- `prefers-reduced-motion` desactiva la animación.

## Sustitución futura

Cuando estén disponibles las fotografías definitivas:

1. Guardarlas optimizadas en `assets/menu/` con nombres estables, por ejemplo `margherita.jpg`, `diavola.jpg` y `fofo.jpg`.
2. Sustituir `PIZZA_PLACEHOLDER` por un mapa entre el nombre de cada pizza y su archivo.
3. Mantener el recorte circular mediante `object-fit: cover`.
4. Actualizar el texto alternativo y los hashes de preservación.
5. Ejecutar `python3 tests/validate.py` y revisar miniaturas y modal en escritorio y móvil.

No deben presentarse las imágenes provisionales como fotografías reales de cada receta.
