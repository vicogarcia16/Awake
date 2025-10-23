# Keep Awake Tool

Una sencilla utilidad para Windows que mantiene tu sistema "despierto", evitando que entre en modo de suspensión o se bloquee la sesión.

## Acerca de

Esta herramienta se ejecuta en la bandeja del sistema y simula la pulsación de la tecla "Scroll Lock" cada 60 segundos para mantener el sistema activo. Es ideal para situaciones en las que no tienes permisos para cambiar la configuración de energía del sistema o necesitas que una tarea larga se complete sin interrupciones.

## Características

- **Ligero y Discreto**: Se aloja en la bandeja del sistema sin interrumpir tu trabajo.
- **Configurable**: Pregunta cuántos minutos deseas mantener el sistema activo al iniciar.
- **Fácil de Usar**: Un menú simple para comprobar el estado o para detener y cerrar la aplicación.
- **Sin dependencias complejas**: Funciona con un conjunto mínimo de librerías de Python.

## Requisitos

- Python 3.13 (o compatible)
- `pipenv` para gestionar el entorno virtual y las dependencias.

## Instalación y Ejecución

Puedes ejecutar la herramienta directamente desde el código fuente o compilarla en un archivo `.exe` independiente.

### 1. Ejecutar desde el Código Fuente (para pruebas)

1.  **Clona el repositorio:**
    ```sh
    git clone <URL-del-repositorio>
    cd Awake
    ```

2.  **Instala las dependencias con `pipenv`:**
    Esto creará un entorno virtual e instalará `pystray` y `Pillow`.
    ```sh
    pipenv install
    ```

3.  **Ejecuta el script:**
    ```sh
    pipenv run python keep_awake_tray.py
    ```
    Aparecerá una ventana pidiéndote que introduzcas los minutos que deseas mantener activo el sistema.

### 2. Crear el archivo `.exe`

El `Pipfile` incluye un script para facilitar la compilación con PyInstaller.

1.  **Asegúrate de tener las dependencias instaladas:**
    ```sh
    pipenv install
    ```

2.  **Ejecuta el script de compilación definido en el `Pipfile`:**
    ```sh
    pipenv run ejecutar
    ```
    Este comando utiliza `PyInstaller` para empaquetar todo en un único archivo ejecutable.

3.  **Encuentra el resultado:**
    El archivo `KeepAwakeTool.exe` se encontrará en la carpeta `dist/`. Puedes mover este archivo a cualquier otra ubicación y se ejecutará sin necesidad de tener Python o las dependencias instaladas.

