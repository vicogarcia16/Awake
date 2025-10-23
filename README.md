# Keep Awake Tool ☕

Una sencilla utilidad para Windows que mantiene tu sistema "despierto", evitando que entre en modo de suspensión o se bloquee la sesión.

## 💡 Acerca de

Esta herramienta se ejecuta en la bandeja del sistema y simula la pulsación de la tecla "Scroll Lock" cada 60 segundos para mantener el sistema activo. Es ideal para situaciones en las que no tienes permisos para cambiar la configuración de energía del sistema o necesitas que una tarea larga se complete sin interrupciones.

## ✨ Características

-   **🤫 Ligero y Discreto**: Se aloja en la bandeja del sistema sin interrumpir tu trabajo.
-   **⏱️ Configurable**: Pregunta cuántos minutos deseas mantener el sistema activo al iniciar.
-   **✅ Fácil de Usar**: Un menú simple para comprobar el estado o para detener y cerrar la aplicación.

## ⚙️ Tecnologías Utilizadas

-   **🐍 Python 3.13**: El lenguaje principal de la aplicación.
-   **🖼️ Pystray**: Para crear y gestionar el ícono en la bandeja del sistema de Windows.
-   **🎨 Pillow (PIL)**: Utilizada para generar la imagen del ícono dinámicamente.
-   **🪟 Tkinter**: Para mostrar la ventana de diálogo simple que solicita los minutos al usuario.
-   **🔗 Ctypes**: Para interactuar directamente con la API de Windows y simular la pulsación de teclas (`keybd_event`).
-   **📦 PyInstaller**: Para empaquetar la aplicación en un único archivo `.exe` que no requiere instalación de Python.
-   **🌐 Pipenv**: Para la gestión del entorno virtual y las dependencias del proyecto.

## 📋 Requisitos

-   Python 3.13 (o compatible)
-   `pipenv` para gestionar el entorno virtual.

## 🚀 Instalación y Ejecución

Puedes ejecutar la herramienta directamente desde el código fuente o compilarla en un archivo `.exe` independiente.

### 1. Ejecutar desde el Código Fuente (para pruebas)

1.  **Clona el repositorio:**
    ```sh
    git clone <URL-del-repositorio>
    cd Awake
    ```

2.  **Instala las dependencias con `pipenv`:**
    ```sh
    pipenv install
    ```

3.  **Ejecuta el script:**
    ```sh
    pipenv run python keep_awake_tray.py
    ```
    Aparecerá una ventana pidiéndote que introduzcas los minutos.

### 2. Crear el archivo `.exe`

El `Pipfile` incluye un script para facilitar la compilación.

1.  **Asegúrate de tener las dependencias instaladas:**
    ```sh
    pipenv install
    ```

2.  **Ejecuta el script de compilación:**
    ```sh
    pipenv run ejecutar
    ```

3.  **Encuentra el resultado:**
    El archivo `KeepAwakeTool.exe` se encontrará en la carpeta `dist/`. ¡Listo para usar!

