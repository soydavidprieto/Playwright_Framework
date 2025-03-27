
# 🎭 Playwright QA Automation Framework (Python + Pytest + Screenplay)

Este framework está diseñado para automatización de pruebas E2E modernas, modulares y mantenibles. Combina Playwright con Pytest, el patrón Screenplay, BDD, ejecución paralela, mocking y reporting visual.

---

## 📦 Estructura del Proyecto

```
qa_framework/
├── abilities/            # Abilities como BrowseTheWeb
├── config/               # Carga de variables desde .env
├── hooks/                # Hooks personalizados (tracing, etc.)
├── pages/                # Page Object Models
├── questions/            # Validaciones (elementos visibles, etc.)
├── resources/data/       # Datos dinámicos (YAML/JSON)
├── tasks/                # Tasks como Login(username, password)
├── tests/
│   ├── e2e/              # Pruebas automatizadas E2E
│   ├── features/         # Archivos Gherkin
│   └── step_definitions/ # Implementaciones BDD
├── utils/                # Logger, excepciones personalizadas
├── reports/              # Reportes Allure y HTML
├── conftest.py           # Fixtures centralizados
├── .env                  # Variables de entorno
└── requirements.txt
```

---

## 🚀 Instalación y uso

```bash
# 1. Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate  # o .venv\Scripts\activate en Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Instalar navegadores de Playwright
python -m playwright install

# 4. Ejecutar pruebas
pytest tests/ --html=reports/report.html --self-contained-html
```

---

## 🧪 Ejecución paralela

```bash
pytest tests/ -n auto
```

---

## 📊 Allure Reporting

```bash
# Ejecutar y guardar resultados
pytest tests/ --alluredir=reports/allure-results

# Generar y abrir reporte
allure generate reports/allure-results --clean -o reports/allure-report
allure open reports/allure-report
```

---

## 🧬 GitHub Actions (CI/CD)

Ubica este archivo en `.github/workflows/ci.yml`:

```yaml
name: Playwright QA Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: |
          pip install -r requirements.txt
          python -m playwright install --with-deps
          pytest tests/ --html=reports/report.html --self-contained-html
      - uses: actions/upload-artifact@v3
        with:
          name: html-report
          path: reports/report.html
```

---

## 🔍 Visual Testing & Mocking

```python
page.screenshot(path="screenshots/login.png")

page.route("**/auth", lambda route: route.fulfill(
    status=200, content_type="application/json", body='{"token": "fake"}'
))
```
