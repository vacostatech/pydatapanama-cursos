# 📦 Guía de Configuración

Bienvenido/a al archivo de configuración del entorno para este curso de Análisis de Datos con Python. Aquí aprenderás a crear un ambiente virtual con **Conda** o con **venv + pip**, instalar las dependencias necesarias y guardar estas dependencias en un archivo para reproducibilidad.

---

## ✅ Opcion 1: Usando Conda (recomendado)

### 1. Crear el ambiente virtual con Python 3.11

```bash
conda create -n pyda-py311 python=3.11
conda activate pyda-py311
```

### 2. Instalar las dependencias necesarias con conda

```bash
conda install pandas numpy matplotlib seaborn jupyterlab ipykernel ipywidgets openpyxl xlrd pathlib
```

### 3. Guardar las dependencias en un archivo `environment.yml`

```bash
conda env export --from-history > environment.yml
```

Esto generará un archivo `environment.yml` con el historial de paquetes instalados en ese entorno.

---

## ✅ Opcion 2: Usando venv + pip (alternativa sin Conda)

### 1. Crear el ambiente virtual

```bash
python3.11 -m venv .venv
source .venv/bin/activate   
# En Windows: .venv\Scripts\activate
```

### 2. Instalar las dependencias necesarias con pip

```bash
pip install pandas numpy matplotlib seaborn jupyterlab ipykernel ipywidgets openpyxl xlrd pathlib
```

### 3. Guardar las dependencias en un archivo `requirements.txt`

```bash
pip freeze > requirements.txt
```

---

## 🔍 Conda vs venv + pip

| Característica                    | Conda                   | venv + pip           |
| --------------------------------- | ----------------------- | -------------------- |
| Administra dependencias y entorno | ✅ Sí                    | ✅ Sí                 |
| Administra versiones de Python    | ✅ Sí                    | ❌ No                 |
| Velocidad de instalación          | ⏳ Ligeramente más lenta | ⚡ Más rápida con pip |
| Ideal para ciencia de datos       | ✅ Recomendado           | ✅ Alternativa ligera |

---

## 🔗 Documentación oficial

* Conda: [https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
* pip y venv: [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)
* pip: [https://pip.pypa.io/en/stable/](https://pip.pypa.io/en/stable/)

---

Recuerda que tener un entorno virtual limpio y bien configurado es el primer paso hacia un flujo de trabajo profesional en análisis de datos. ✨
