# CV digital de Luis Enrique Aviles Lucas

Portafolio profesional en español para presentar mi experiencia contable y administrativa, habilidades tecnológicas y proyecto de registro de entradas y salidas con Python y SQL.

Incluye contacto directo por WhatsApp, correo electrónico, fotografía, currículum descargable de una página y diseño adaptable a celulares y computadoras.

## Publicación en GitHub y Vercel

### 1. Extraer y subir a GitHub

1. Descomprime el ZIP y abre la carpeta `cv-luis-aviles`.
2. Crea un repositorio en GitHub, por ejemplo `cv-luis-aviles`.
3. Utiliza **Add file → Upload files**. Si el repositorio está vacío, utiliza **uploading an existing file**.
4. Arrastra el contenido de la carpeta: `dist`, `scripts`, `vercel.json`, `README.md` y `TEXTO_PARA_LINKEDIN.txt`.
5. Guarda con **Commit changes**.

El archivo `vercel.json` debe verse en la raíz del repositorio, junto a la carpeta `dist`. Sube los archivos extraídos; GitHub no descomprime el ZIP como parte del sitio.

### 2. Publicar en Vercel

1. En Vercel, crea un proyecto e importa el repositorio de GitHub.
2. Conserva la raíz del repositorio como **Root Directory**.
3. Comprueba estos valores:

| Opción | Valor |
| --- | --- |
| Framework Preset | `Other` |
| Root Directory | Raíz del repositorio (`./`) |
| Build Command | Vacío |
| Install Command | Vacío |
| Output Directory | `dist` |

`vercel.json` incluye la configuración. Este sitio se publica como archivos estáticos y no necesita instalar paquetes para funcionar.

4. Pulsa **Deploy** y espera a que Vercel entregue el enlace.
5. Abre el enlace y comprueba la fotografía, la descarga del PDF y el botón de WhatsApp.
6. Copia tu enlace en `TEXTO_PARA_LINKEDIN.txt` antes de usar ese borrador.

## Archivos principales

| Archivo | Función |
| --- | --- |
| `dist/index.html` | Textos, experiencia, proyecto, habilidades y contacto |
| `dist/assets/styles.css` | Diseño principal y adaptación a pantallas |
| `dist/assets/profile-updates.css` | Presentación del proyecto y habilidades ampliadas |
| `dist/assets/main.js` | Copiar enlace y navegación activa |
| `dist/assets/CV_Luis_Aviles.pdf` | Currículum listo para descargar |
| `dist/assets/luis-aviles.jpg` | Fotografía del perfil |
| `vercel.json` | Configuración para publicar en Vercel |
| `scripts/create_cv.py` | Generador opcional del PDF |
| `TEXTO_PARA_LINKEDIN.txt` | Borrador para anunciar el perfil |

El sitio está construido con HTML, CSS y JavaScript. La sección del proyecto describe el sistema de asistencia desarrollado con Python y SQL.

## Revisar y editar en tu computadora

Puedes abrir `dist/index.html` directamente. Para revisar mediante un servidor local, si tienes Python instalado, ejecuta desde la carpeta del proyecto:

```bash
python -m http.server 8000 --directory dist
```

Después abre `http://localhost:8000` en el navegador. En Windows, puedes utilizar `py` si el comando `python` no está disponible.

Edita `dist/index.html` para cambiar los textos y los archivos CSS para modificar el diseño. La descarga del PDF es un archivo independiente: actualízala también cuando cambies la información del perfil.

El número de WhatsApp configurado es `593969951379` (equivalente a `0969951379` en Ecuador). Cada enlace abre la conversación y prepara un mensaje que el visitante puede enviar.

## Regenerar el PDF (opcional)

El PDF actualizado ya está incluido. Solo necesitas los siguientes pasos si posteriormente deseas cambiar su contenido usando el generador:

1. Instala Python y abre una terminal en la carpeta del proyecto.
2. Instala la dependencia:

```bash
python -m pip install -r scripts/requirements-pdf.txt
```

3. Edita los textos de `scripts/create_cv.py`.
4. Ejecuta:

```bash
python scripts/create_cv.py
```

El resultado reemplaza `dist/assets/CV_Luis_Aviles.pdf`. Las fuentes necesarias vienen incluidas en `scripts/fonts`, con su licencia. El generador fue verificado con ReportLab 4.4.9.

## Fuentes de las instrucciones de publicación

- [GitHub: añadir archivos a un repositorio](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)
- [Vercel: configurar la publicación](https://vercel.com/docs/builds/configure-a-build)
- [Vercel: configuración con vercel.json](https://vercel.com/docs/project-configuration/vercel-json)

Preparado el 6 de octubre de 2026.
