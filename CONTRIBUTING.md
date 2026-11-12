# Cómo agregar o corregir notas

Todo cambio entra a `main` por pull request. Nadie puede subir cambios directo a `main`: GitHub lo rechaza.

## Antes de empezar (una sola vez)

1. Pide acceso al repositorio `IUV-Universidad/base-conocimiento`.
2. Instala [Obsidian](https://obsidian.md) y [GitHub Desktop](https://desktop.github.com).
3. En GitHub Desktop: **File › Clone repository** y elige `IUV-Universidad/base-conocimiento`.
4. En Obsidian: **Abrir carpeta como bóveda** y elige la carpeta que clonaste.
5. En Obsidian: **Ajustes › Plugins principales** y activa **Plantillas**.

## Cada vez que hagas cambios

1. En GitHub Desktop, con la rama `main` seleccionada, da clic en **Fetch origin** y luego en **Pull origin** para traer lo último.
2. **Branch › New branch** y ponle un nombre que diga qué vas a hacer, por ejemplo `caja-nuevos-aranceles`.
3. Escribe o corrige las notas en Obsidian.
4. En GitHub Desktop, escribe un resumen del cambio y da clic en **Commit**.
5. Da clic en **Publish branch** y después en **Create Pull Request**.
6. Espera a que la revisión automática salga en verde y a que alguien apruebe el PR. Si la revisión falla, abre el detalle: dice qué nota y qué corregir.
7. Cuando el PR se mezcle, regresa a `main` en GitHub Desktop y repite desde el paso 1.

## Reglas de las notas

- **Nombre del archivo:** el título de la nota, sin `¿` ni `?`. Cambia `|` y `/` por ` - `. Ejemplo: la nota `# ¿Cuál es mi matrícula?` se guarda como `Cuál es mi matrícula.md`.
- **Primera línea:** el título completo con `# `, con signos de interrogación si es pregunta.
- **Ubicación:** en la carpeta de su área (`Caja/Preguntas frecuentes`, `Control escolar/Trámites`…).
- **Índice:** cada nota nueva se enlaza desde la nota índice de su carpeta (la que se llama igual que la carpeta, como `Trámites.md`). Una nota sin enlace no pasa la revisión.
- **Links:** escribe `[[` y elige la nota; Obsidian inserta el link en el formato correcto. No cambies el formato de links en los ajustes.
- **Plantillas:** para un trámite o una pregunta frecuente nueva, crea la nota y usa **Insertar plantilla** (`_plantillas/Trámite` o `_plantillas/Pregunta frecuente`).

## Revisión automática

Cada PR corre `scripts/check_vault.py`, que revisa nombres, títulos, links rotos y notas sin enlazar. Para correrla en tu equipo antes de subir:

```
python3 scripts/check_vault.py
```
