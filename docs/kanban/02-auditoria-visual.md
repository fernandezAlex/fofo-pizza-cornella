# Exportación de Kanban — t_9f5fc295

```text
Task t_9f5fc295: Recopila y audita la identidad visual y las imágenes
  status:    done
  assignee:  default
  workspace: scratch @ /opt/data/kanban/workspaces/t_83cfbe87
  max-retries: 2 (default)
  created:   2026-07-26 23:45 by auto-decomposer
  started:   2026-07-26 23:45
  completed: 2026-07-26 23:52
  children:  t_2b2d22cd, t_83cfbe87, t_dc8e21da

Body:
Localiza los recursos visuales públicos de FOFO PIZZERIA Cornellà: logotipo, colores, tipografías aproximadas, fotografías del local, pizzas y otros productos, además del estilo de sus publicaciones. Registra para cada recurso su fuente, resolución y condiciones aparentes de uso. Prioriza archivos oficiales y descargables; no incorpores imágenes de terceros sin autorización o licencia compatible. Si faltan recursos utilizables, define alternativas seguras, como marcadores, fotografías con licencia o un tratamiento visual inspirado en la identidad sin copiar material protegido. Entrega un inventario organizado, una breve guía visual con paleta en códigos HEX y recomendaciones concretas para la web.

Latest summary:
Completé la auditoría visual en el comentario 10: inventario con fuente, resolución y riesgo de uso; guía de identidad con paleta HEX y tipografías aproximadas; alternativas seguras y checklist de materiales a pedir al propietario. La única foto inequívoca localizada es una fachada de 426×240 sin licencia reutilizable, por lo que se recomienda no publicar ningún recurso encontrado hasta obtener autorización u originales oficiales.

Comments (1):
  [2026-07-26 23:52] default: ## Auditoría visual — FOFO Pizza Cornellà

Fecha de consulta: 2026-07-26.

### Conclusión ejecutiva
No se ha localizado una web corporativa ni una cuenta social oficial verificable de FOFO Pizza Cornellà. El único recurso visual inequívocamente asociado al negocio que se pudo auditar es una fotografía exterior de baja resolución publicada por el directorio Bella Roma y aparentemente importada de una ficha de Google. Uber Eats confirma el nombre, dirección y carta, pero la extracción pública consultada no expone imágenes reutilizables ni licencia. Por tanto, **no debe publicarse ninguna de estas imágenes en la nueva web sin autorización escrita del restaurante o del fotógrafo**.

### Inventario de recursos

| ID | Recurso | Fuente | Resolución / tamaño | Autoría o carácter | Condición aparente de uso | Decisión |
|---|---|---|---|---|---|---|
| V-01 | Fachada del local: rótulo negro con “PIZZERIA” en blanco; escaparate con grafismo rojo/verde; persianas granate | Bella Roma, ficha FOFO: https://pizzeriabellaroma.es/pizzeria/fofo-pizza-cornella-de-llobregat/ ; archivo: https://pizzeriabellaroma.es/wp-content/uploads/AF1QipOKjZCZ-itD5hpaLGw7IR40EoacvXf6YwdcvJp1w426-h240-k-no.jpeg | 426×240 px, JPEG, 37.411 bytes (metadatos de WordPress, media 10944) | Tercero/directorio; el nombre de archivo tiene patrón de imagen de Google (`AF1Qip...`); sin crédito ni metadatos de copyright | No hay licencia compatible declarada. Publicación en directorio ≠ autorización de reutilización | **Solo referencia visual. No usar en producción** salvo cesión/permiso y original de mayor resolución |
| V-02 | Nombre comercial textual “Fofó Pizza” y catálogo de productos | Uber Eats: https://www.ubereats.com/es/store/fofo-pizza/2fvnPpSsWQOvI7jA-JmaVA | Texto; no se obtuvieron imágenes descargables auditables | Perfil de marketplace asociado a Salvador Allende 13, Cornellà | Términos de plataforma; el contenido no concede licencia para republicación | Usar solo como pista para validar carta con el propietario; no copiar fotos ni textos extensos |
| V-03 | Fotografías de pizzas/local presentes en resultados y directorios agregadores | Bella Roma, Google/Mapstr/Circolo y resultados indexados | Varias miniaturas entre 150×150, 300×169, 408×408, 426×240 y 408×543 | Terceros y, en varios casos, negocios distintos mostrados como recomendaciones | Sin licencia; riesgo alto de atribución errónea. Se comprobó que varias imágenes eran de La Tagliatella, LABEMPAÏDA, Telepizza u otros locales | **Descartadas**; no descargar ni incorporar |
| V-04 | Logotipo oficial en vector/PNG | No localizado | — | — | — | Solicitar al negocio SVG/PDF/AI y PNG transparente; no redibujar como “oficial” a partir de la foto |
| V-05 | Fotografías oficiales de pizzas, pizza frita, horno, equipo, interior y terraza | No localizadas con autoría/licencia verificable | — | — | — | Solicitar originales y autorización; si no existen, producir sesión propia |
| V-06 | Publicaciones sociales/estilo editorial oficial | No se encontró perfil oficial verificable por nombre, dirección ni teléfono | — | — | — | No atribuir cuentas homónimas ni copiar estilos ajenos |

### Identidad observada (nivel de confianza)

- **Marca visible:** el exterior prioriza un rótulo funcional y muy directo: fondo negro/antracita, palabra “PIZZERIA” en mayúsculas blancas, condensadas y pesadas. En el cristal aparece un grafismo manual/ilustrado con rojo y verde, pero la foto no tiene resolución suficiente para reconstruirlo con fidelidad.
- **Ambiente físico:** fachada sencilla de barrio; negro, crema, rojo oscuro/granate y pequeños acentos italianos rojo-verde. No hay evidencia suficiente para afirmar que exista un sistema gráfico corporativo completo.
- **Tipografía aproximada (no identificada):** para el carácter del rótulo, usar una alternativa libre condensada como **Oswald Bold** o **Barlow Condensed ExtraBold**. Para lectura y UI, **Inter** o **Manrope**. Ninguna debe presentarse como tipografía oficial hasta confirmarlo con el negocio.
- **Estilo social:** no auditable. Evitar inventar una estética “oficial”. Recomendación segura: fotografía gastronómica cálida y honesta, encuadres cercanos, proceso artesanal, pocas capas gráficas y mensajes breves.

### Paleta web propuesta (inspirada, no oficial)

| Rol | HEX | Uso recomendado |
|---|---|---|
| Carbón horno | `#1C1B19` | Cabecera, footer, fondos oscuros, texto principal |
| Crema masa | `#F4E8D2` | Fondo cálido principal |
| Tomate | `#C83A2D` | CTA primario, precios destacados, acentos |
| Vino/granate | `#7B2430` | Secciones oscuras secundarias, hover, detalles de fachada |
| Albahaca | `#347A4A` | Etiquetas vegetarianas, acento complementario |
| Mozzarella | `#FFF9EE` | Superficies/tarjetas |

Combinaciones accesibles recomendadas: `#FFF9EE` sobre `#1C1B19`; `#1C1B19` sobre `#F4E8D2`; para botones usar texto blanco/crema sobre tomate solo tras validar contraste en el tamaño final. No usar rojo y verde como única codificación de estado.

### Dirección fotográfica recomendada

1. Hero horizontal propio, mínimo 2400×1350, mostrando una pizza completa recién salida del horno y manos/proceso; dejar espacio negativo para titular.
2. Serie vertical 4:5, mínimo 1600×2000: pizza Fofó, Margherita, Mortadella/burrata, pizza frita y postre.
3. Local: fachada diurna y nocturna, interior sin clientes identificables, horno y pizzero trabajando con consentimiento.
4. Luz cálida lateral (aprox. 3200–4500 K), textura real, contraste moderado; evitar filtros saturados, fondos falsos o imágenes genéricas que no representen el producto servido.
5. Preparar WebP/AVIF responsivos; conservar originales y exportar 320/640/960/1440/1920 px; objetivo aproximado de 150–300 KB por imagen web sin degradación visible.

### Alternativas seguras si faltan recursos

- Usar bloques tipográficos, formas abstractas inspiradas en horno/masa y marcadores neutros hasta disponer de fotos autorizadas.
- Comprar fotos con licencia comercial de Adobe Stock, Shutterstock o Envato y etiquetarlas internamente como **ambientales**, nunca como platos reales de FOFO.
- Usar bancos gratuitos solo verificando la licencia concreta y guardando URL, autor y captura/fecha de licencia; aun así, evitar sugerir que el plato genérico es el servido por el negocio.
- Mejor opción: micro-sesión propia de 2–3 horas con cesión de derechos web/redes y consentimientos de las personas reconocibles.

### Checklist de entrega a solicitar al propietario

- Logo maestro SVG/PDF/AI y PNG transparente a 2000 px o más.
- Confirmación escrita de colores y tipografías, si existen.
- 10–20 fotos originales (sin descargar de Google/Instagram/marketplaces), autor y permiso de uso web/publicitario.
- Autorizaciones de imagen de personal/clientes reconocibles.
- Carta y precios vigentes en documento propio; Uber Eats debe servir solo para contraste.
- Enlaces oficiales de Instagram/Facebook/TikTok y acceso o autorización para embeber publicaciones.
- Documento simple de procedencia/licencias por archivo.

### Fuentes contrastadas

- Bella Roma / WordPress API del post y medio: https://pizzeriabellaroma.es/wp-json/wp/v2/pizzeria/10943?_embed=1
- Uber Eats (nombre, dirección y carta): https://www.ubereats.com/es/store/fofo-pizza/2fvnPpSsWQOvI7jA-JmaVA
- Circolo Pizza (directorio secundario): https://www.circolopizza.es/pizzeria/fofo-pizza/
- Mapstr (directorio secundario): https://mapstr.com/place/uKh4gu7pTF

**Regla de producción:** no incorporar ningún archivo visual de estas fuentes al repositorio. Mantener V-01 únicamente como referencia privada hasta recibir material oficial o autorización verificable.

Events (13):
  [2026-07-26 23:45] created {'by': 'auto-decomposer', 'from_decompose_of': 't_83cfbe87'}
  [2026-07-26 23:45] promoted
  [2026-07-26 23:45] [run 9] claimed {'lock': 'ac0cb58b64bc:4952', 'expires': 1785103240, 'run_id': 9}
  [2026-07-26 23:45] [run 9] spawned {'pid': 12925}
  [2026-07-26 23:45] [run 9] heartbeat
  [2026-07-26 23:46] [run 9] heartbeat
  [2026-07-26 23:47] [run 9] heartbeat
  [2026-07-26 23:49] [run 9] heartbeat
  [2026-07-26 23:50] [run 9] heartbeat
  [2026-07-26 23:51] [run 9] heartbeat
  [2026-07-26 23:52] [run 9] heartbeat
  [2026-07-26 23:52] commented {'author': 'default', 'len': 7641}
  [2026-07-26 23:52] [run 9] completed {'result_len': 0, 'summary': 'Completé la auditoría visual en el comentario 10: inventario con fuente, resolución y riesgo de uso; guía de identidad con paleta HEX y tipografías aproximadas; alternativas seguras y checklist de materiales a pedir al propietario. La única foto inequívoca localizada es una fachada de 426×240 sin licencia reutilizable, por lo que se recomienda no publicar ningún recurso encontrado hasta obtener au'}

Runs (1):
  #9   completed    @default  394s  2026-07-26 23:45
        → Completé la auditoría visual en el comentario 10: inventario con fuente, resolución y riesgo de uso; guía de identidad con paleta HEX y tipografías aproximadas;
```
