# 🤝 Guía para contribuir creando cursos

Gracias por tu interés en contribuir al repositorio de cursos de **PyDataPanama**. Este espacio está abierto para que cualquier persona pueda proponer, desarrollar y mantener cursos de forma colaborativa.

Este documento está enfocado en contribuciones al **repositorio general**, como la creación de nuevos cursos, mejoras de documentación o estructura general.

---

## 🚀 1. Haz un fork del repositorio

1. Ve al repositorio principal: [https://github.com/PyData-Panama/pydatapanama-cursos](https://github.com/PyData-Panama/pydatapanama-cursos)
2. Haz clic en [**"Fork"**](https://github.com/PyData-Panama/pydatapanama-cursos/fork)
3. Clona tu fork en local:

```bash
git clone https://github.com/tu-usuario/pydatapanama-cursos.git
cd pydatapanama-cursos
```

---

## 🧱 2. Cómo crear un nuevo curso

Sigue estos pasos para agregar un nuevo curso al repositorio:

1. Dirígete a la carpeta `cursos/` y crea un nuevo directorio con formato:

```bash
cursos/0X-nombre-del-curso/
```

Ejemplo:

```bash
cursos/02-visualizacion-avanzada/
```

2. Dentro de la carpeta del curso, incluye al menos:

* `README.md` del curso (explicando objetivos y estructura)
* Carpeta `notebooks/` con notebooks de clase o ejercicios
* Carpeta `data/` si usarás datos
* Carpeta `references/` con recursos, slides o instrucciones
* Cualquier archivo adicional necesario (`requirements.txt`, `setup.md`, etc.)

3. Sigue el estilo y organización del curso 01 como referencia.

---

## ✅ Buenas prácticas

* Usa nombres de carpetas y archivos **en minúsculas y con guiones**
* Incluye documentación clara para facilitar el uso del curso
* Los notebooks deben tener celdas bien documentadas
* Revisa ortografía, claridad y formato antes de subir

---

## 🔁 3. Pull Requests

1. Crea una nueva branch:

```bash
git checkout -b {tu-usuario-github}/nuevo-curso
```

2. Agrega tus archivos, haz commit y push:

```bash
git add .
git commit -m "Agrego curso de visualización avanzada"
git push origin {tu-usuario-github}/nuevo-curso
```

3. Abre un Pull Request en GitHub desde tu repositorio fork al `main` del repositorio original.

---

## 🌐 Participación en comunidad

* Puedes sugerir ideas de cursos abriendo un **issue**
* Participa en nuestras sesiones comunitarias o eventos
* Comparte recursos o mejora cursos existentes

---

Gracias por ser parte de esta iniciativa educativa abierta. ¡Esperamos tus contribuciones! 🙌

**#ConstruyamosJuntos #PyDataPanama**
