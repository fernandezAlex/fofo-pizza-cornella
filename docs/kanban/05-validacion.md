# Exportación de Kanban — t_dc8e21da

```text
Task t_dc8e21da: Valida el contenido y la calidad de la web
  status:    done
  assignee:  default
  workspace: scratch @ /opt/data/kanban/workspaces/t_83cfbe87
  max-retries: 2 (default)
  created:   2026-07-26 23:45 by auto-decomposer
  completed: 2026-07-27 00:19
  parents:   t_8ea390e1, t_9f5fc295, t_e8d9d1f5
  children:  t_83cfbe87

Body:
Revisa la implementación final contra la investigación y el inventario de recursos. Comprueba que dirección, teléfono, horarios, carta, precios, enlaces y llamadas a la acción coincidan con las fuentes documentadas y que no haya datos inventados ni imágenes sin procedencia aceptable. Ejecuta las pruebas, lint y build disponibles; corrige fallos funcionales, enlaces rotos, errores de consola y problemas evidentes de accesibilidad, SEO o rendimiento. Verifica visualmente los principales anchos de móvil, tableta y escritorio, incluyendo navegación, legibilidad de la carta y carga de imágenes. Deja el proyecto en estado desplegable y documenta cualquier limitación o dato que requiera confirmación del negocio.

Result:
Validación final superada: contenido contrastado, 29 productos, HTML/JSON-LD/enlaces comprobados y navegador sin errores.

Events (6):
  [2026-07-26 23:45] created {'by': 'auto-decomposer', 'from_decompose_of': 't_83cfbe87'}
  [2026-07-26 23:45] linked {'parent': 't_8ea390e1', 'child': 't_dc8e21da'}
  [2026-07-26 23:45] linked {'parent': 't_9f5fc295', 'child': 't_dc8e21da'}
  [2026-07-26 23:45] linked {'parent': 't_e8d9d1f5', 'child': 't_dc8e21da'}
  [2026-07-27 00:19] promoted
  [2026-07-27 00:19] [run 14] completed {'result_len': 121, 'summary': 'HTTP 200, 0 errores de consola, filtros funcionales, sin imágenes no autorizadas ni contenido prohibido.'}

Runs (1):
  #14  completed    @default  0s  2026-07-27 00:19
        → HTTP 200, 0 errores de consola, filtros funcionales, sin imágenes no autorizadas ni contenido prohibido.
```
