# Fofó Pizza Cornellà

Copia preservada del proyecto web conceptual de Fofó Pizza Cornellà, publicada sin rediseñar la versión original del VPS.

## Enlaces

- **Web en GitHub Pages:** https://fernandezalex.github.io/fofo-pizza-cornella/
- **Repositorio:** https://github.com/fernandezAlex/fofo-pizza-cornella
- **Previsualización del VPS:** https://fofo-pizza.31-97-153-148.nip.io/#inicio

## Qué contiene

La raíz del repositorio es directamente publicable en GitHub Pages:

- `index.html`: HTML, CSS y JavaScript de la web original.
- `assets/`: las siete fotografías utilizadas por el diseño original.
- `assets/logo-fofo.png`: logo corporativo con transparencia real, incorporado a la cabecera y el favicon.
- `docs/brand/`: fuente del logo, proceso de extracción y paleta corporativa.
- `docs/research/`: investigación inicial, investigación ampliada y fuentes/decisiones posteriores.
- `docs/kanban/`: exportación de las seis tareas del proyecto en el Kanban de Hermes, con cuerpos, comentarios, dependencias y resultados.
- `docs/project/`: documentación de preservación y README original.
- `docs/project/CARTA-IMAGENES.md`: funcionamiento de las miniaturas, el modal y la futura asignación de una foto propia a cada pizza.
- `artifacts/`: copia empaquetada de la web.
- `AGENTS.md`: reglas y contexto para Hermes, Codex, Claude Code y otros agentes.
- `tests/validate.py`: validación de estructura e integridad de las fotografías.

Consulta [`docs/README.md`](docs/README.md) para entender la clasificación y cronología de la documentación.

## Desarrollo local

No hay dependencias ni proceso de compilación:

```bash
python3 -m http.server 8080
```

Después abre `http://localhost:8080/#inicio`.

## Imágenes de la carta

Cada pizza incorpora una miniatura circular interactiva. Al pulsarla se abre una imagen circular grande con una animación de giro que termina en estado estático. De forma provisional, las 20 entradas reutilizan la misma fotografía; se sustituirán por sus imágenes correspondientes cuando estén disponibles.

## Validación

```bash
python3 tests/validate.py
```

## Preservación

La versión visual de referencia está formada por `index.html` y `assets/`. El 27/07/2026 se incorporó, por petición expresa de Alex, el logo corporativo y una ampliación de la paleta con verdes extraídos de la marca, manteniendo el rojo y todo el contenido anterior. Cualquier modificación posterior debe compararse con la web publicada y contar con una petición explícita del propietario del repositorio.

## Nota

Este repositorio conserva tanto la implementación como el contexto del proyecto. Algunos documentos representan fases diferentes de investigación y pueden incluir advertencias o propuestas posteriores que no se aplicaron a la versión visual publicada.
