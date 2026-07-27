# Identidad visual de Fofó Pizza

## Archivos

- `../../assets/logo-fofo.png`: versión PNG con fondo transparente utilizada por la web.
- `logo-source-user.png`: imagen corporativa aportada por Alex el 27/07/2026; se conserva como fuente de referencia.

## Preparación del logo

La fuente aportada medía 234 × 282 px, estaba codificada como RGBA pero todos sus píxeles eran opacos y contenía un fondo oscuro. Se realizó una extracción del primer plano conservando:

- letras verdes y rojas;
- contornos y sombras negras;
- perfil blanco;
- bordes suavizados;
- transparencia alfa real.

La versión web se recortó al contenido y se exportó a 378 × 562 px para mejorar la definición al renderizarla en tamaños pequeños. No se encontró en la búsqueda pública una versión verificable del mismo logo con mayor resolución y transparencia real, por lo que se utilizó la imagen oficial facilitada por Alex.

## Paleta derivada

Los colores se extrajeron del archivo fuente y se adaptaron al contraste de la web:

| Token | Hex | Uso |
|---|---:|---|
| Verde corporativo | `#4FAA36` | Bordes, filtros y detalles de interfaz |
| Verde vivo del logo | `#74EC4A` | Acentos sobre fondos oscuros |
| Verde oscuro | `#245C32` | Texto y controles sobre fondos claros |
| Rojo principal existente | `#A52D25` | CTA y elementos principales |
| Rojo oscuro existente | `#702019` | Fondos y estados hover |

El rojo original de la web se mantiene; el verde se incorpora como color complementario de marca.
