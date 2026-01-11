
# CCSE-TestGen

Generador de tests tipo CCSE con CSV integrados. Incluye automatización de compilación a **EXE (Windows)** y **AppImage (Ubuntu 24.04)** mediante **GitHub Actions**.

## Parámetros por defecto
- PDF: **desactivado**
- Número de tests: **10**
- No repetir preguntas: **activado**

Estos valores pueden modificarse por CLI.

## Uso (CLI)
```bash
python -m src.main --csv-dir data/csv --n-tests 10 --no-repeat --no-pdf
```

## Estructura
```
CCSE-TestGen/
├── src/
│   ├── main.py
│   ├── generator.py
│   ├── ui.py
│   └── utils.py
├── data/
│   └── csv/
│       ├── tarea1.csv
│       ├── tarea2.csv
│       ├── tarea3.csv
│       ├── tarea4.csv
│       └── tarea5.csv
├── requirements.txt
├── README.md
├── LICENSE
└── .github/workflows/build.yml
```

## Compilación local
```bash
pip install -r requirements.txt
pyinstaller src/main.py --name CCSE-TestGen --onefile
```

El binario quedará en `dist/`.

## CI/CD (GitHub Actions)
Cada `push` a `main` creará artefactos:
- `CCSE-TestGen.exe` para Windows
- `CCSE-TestGen-x86_64.AppImage` para Ubuntu 24.04

## Sustituir CSV de ejemplo
Los CSV incluidos son de muestra. Sustituye los ficheros en `data/csv/` por tus oficiales. Deben tener al menos las columnas:
- `id` (único)
- `pregunta`
- `opciones` (separadas por `||`)
- `correcta` (índice o texto exacto)
- `tema` (opcional)

## Licencia
MIT.
