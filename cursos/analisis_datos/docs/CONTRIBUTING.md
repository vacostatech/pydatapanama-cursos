# 🤝 Guía para contribuir

Gracias por tu interés en contribuir a este proyecto de cursos de la comunidad PyDataPanama. Las contribuciones están abiertas a cualquier persona interesada en compartir conocimientos o mejorar el contenido. Sigue los pasos y buenas prácticas que se describen a continuación.

---

## 🚀 1. Haz un fork del repositorio

1. Ve al repositorio principal: [https://github.com/pydata-panama/pydatapanama-cursos](https://github.com/pydata-panama/pydatapanama-cursos)
2. Haz clic en el botón [**"Fork"**](https://github.com/PyData-Panama/pydatapanama-cursos/fork)
3. Clona tu fork localmente:

```bash
git clone https://github.com/tu-usuario/pydatapanama-cursos.git
cd pydatapanama-cursos/cursos/01-analisis-de-datos
```

---

## 🗂 2. Estructura del proyecto del curso

```markdown
analisis_datos/
├── data/
│   ├── raw/             # Datos originales sin procesar
│   └── processed/       # Datos limpios o transformados
├── notebooks/           # Aportes de los estudiantes y ejercicios
├── references/          # Material de clases (enunciados, presentaciones, ejemplos base)
├── utils/               # Funciones auxiliares en Python
├── docs/                # Archivos de documentación Markdown
├── pyproject.toml       # Configuración opcional del proyecto
└── README.md            # Descripción del curso
```

---

## 🧑‍🏫 3. Estructura de clases

* Cada sesión del curso tiene material de apoyo dentro de la carpeta `references/`.
* El material se entrega en formato `.ipynb` o `.md`.

---

## 🧩 4. Reglas para contribuir ejercicios

Si quieres enviar tus ejercicios o soluciones:

* Crea un archivo en formato `.ipynb`
* Sigue esta convención de nombres:

```bash
pyda-modulo01-{tu_usuario_de_github}.ipynb
```

* Guarda el archivo dentro de la carpeta:

```bash
notebooks/
```

📌 Ejemplo:

```bash
notebooks/pyda-modulo01-janedoe.ipynb
```

Puedes enviar tantas contribuciones como desees, separadas por sesión.

---

## ✅ Buenas prácticas

* Mantén tu branch actualizado con el repositorio original:

```bash
git remote add upstream https://github.com/pydata-panama/pydatapanama-cursos.git
git pull upstream main
```

* Usa `markdown` claro y legible si vas a escribir notas o documentación.
* Si creas nuevos datasets o scripts, documenta su uso.
* Evita subir archivos innecesarios o muy pesados (>50MB).

---

## 🔁 5. Pull Request

1. Crea una nueva branch desde `main`:

```bash
git checkout -b pyda/{tu-usuario-githib}
```

2. Haz tus cambios y haz commit:

```bash
git add .
git commit -m "Mi aporte a la sesión 01"
```

3. Haz push:

```bash
git push origin pyda/{tu-usuario-githib}
```

4. Ve a tu repositorio en GitHub y abre un **Pull Request** hacia `main` del repositorio original.

---

## 📬 Contacto

Si tienes dudas, puedes abrir un issue o contactarnos a través de [GitHub Discussions](https://github.com/pydata-panama/pydatapanama-cursos/discussions) o el grupo de WhatsApp de la comunidad.

---

Gracias por ser parte de la comunidad PyDataPanama 🙌
