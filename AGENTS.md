# AGENTS.md — Contexto para agentes

## Objetivo del repositorio

Este repositorio conserva la versión original del proyecto web conceptual **Fofó Pizza Cornellà** tal como se mostraba en la URL de previsualización del VPS antes de su publicación en GitHub Pages.

## Regla principal de preservación

- No rediseñar, reinterpretar ni simplificar la web.
- No cambiar textos, fotografías, navegación, anclas, estilos, distribución o comportamiento salvo que Alex lo pida expresamente.
- `index.html`, las siete fotografías y `assets/logo-fofo.png` forman la versión visual canónica.
- Antes de publicar cualquier cambio, ejecutar `python3 tests/validate.py` y comparar visualmente con la referencia.

## Estructura

- `index.html`: sitio estático publicado mediante GitHub Pages.
- `assets/`: siete fotografías utilizadas por la versión original.
- `assets/logo-fofo.png`: logo oficial facilitado por Alex, procesado con transparencia alfa real.
- `docs/brand/`: fuente del logo, método de preparación y tokens de color corporativos.
- `docs/research/`: investigación inicial, ampliada y validaciones posteriores.
- `docs/kanban/`: exportación legible de las tareas, comentarios, decisiones y resultados del Kanban de Hermes.
- `docs/project/`: documentación original y notas de conservación.
- `docs/project/CARTA-IMAGENES.md`: estado provisional y procedimiento futuro para asignar una imagen distinta a cada pizza.
- `artifacts/`: paquete ZIP de preservación del sitio.
- `tests/validate.py`: comprobaciones de integridad y estructura.

## Cómo interpretar la documentación

La documentación recoge distintas fases y puede contener conclusiones contradictorias. La cronología es:

1. Investigación y construcción inicial de la web.
2. Auditoría visual y especificación de mejoras.
3. Investigación ampliada con advertencias sobre horarios, datos y licencia de fotografías.
4. Petición final de Alex: conservar y publicar la web original **tal cual**, incluyendo fotografías y todo el contexto documental.

La petición final de conservación prevalece para la versión publicada. Las advertencias posteriores se mantienen como contexto, no como instrucciones automáticas para modificar la interfaz.

El 27/07/2026 Alex autorizó una modificación concreta: añadir el logo corporativo y reforzar el verde de marca sin eliminar el rojo existente. Esta integración ya forma parte de la referencia visual canónica.

La carta incluye 20 miniaturas circulares que usan temporalmente una única fotografía. Deben conservarse el hover, el modal circular, el giro de apertura, el estado final estático, el cierre accesible y el retorno del foco. Las imágenes definitivas se asignarán por pizza cuando Alex las facilite.

## Publicación

GitHub Pages publica desde `main` y la raíz `/`. No requiere build, dependencias ni backend.
