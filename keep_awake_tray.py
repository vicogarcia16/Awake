import ctypes
import sys
import threading
import multiprocessing
from PIL import Image, ImageDraw
from pystray import Icon, Menu, MenuItem
from tkinter import simpledialog, Tk, messagebox

# --- CONFIGURACIÓN DE TECLA Y CÓDIGOS DE WINDOWS ---
VK_SCROLL = 0x91
KEYEVENTF_KEYUP = 0x0002

# Bandera global para controlar el bucle de ejecución
stop_event = threading.Event()
# Variable para el icono de la bandeja del sistema
icon = None

def press_scroll_lock():
    """Simula la pulsación de Scroll Lock (Presionar y soltar)."""
    ctypes.windll.user32.keybd_event(VK_SCROLL, 0, 0, 0)
    ctypes.windll.user32.keybd_event(VK_SCROLL, 0, KEYEVENTF_KEYUP, 0)

def keep_awake_loop(minutes):
    """Bucle principal que se ejecuta en un hilo separado."""
    print(f"Iniciando ciclo por {minutes} minutos...")
    try:
        for i in range(1, minutes + 1):
            if stop_event.is_set():
                break
            
            stop_event.wait(60) 
            
            if stop_event.is_set():
                break
            
            press_scroll_lock()
            
        # Si el bucle terminó sin ser detenido (completó el tiempo)
        if not stop_event.is_set():
            messagebox.showinfo("Tarea Completada", "Tiempo forzado de actividad terminado. Volviendo a la normalidad.")
            if icon:
                icon.stop()

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error en el bucle: {e}")
        if icon:
            icon.stop()

def create_image(width, height, color1='white', color2='blue'):
    """Crea una imagen simple para usar como icono."""
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle((width // 4, height // 4, 3 * width // 4, 3 * height // 4), fill=color2)
    return image

def on_stop_click(icon, item):
    """Función llamada al hacer clic en 'Detener y Salir'."""
    stop_event.set()
    icon.stop()

def on_running_click(icon, item):
    """
    Función llamada al hacer clic en 'Estado'.
    Ejecuta la ventana de mensaje en un hilo separado para no bloquear el ícono.
    """
    
    def show_status():
        if not stop_event.is_set():
            messagebox.showinfo("Estado", "El sistema se está manteniendo activo.")
        else:
            messagebox.showinfo("Estado", "El proceso de activación está detenido.")

    # Esto evita que la ventana messagebox.showinfo bloquee el bucle del ícono.
    threading.Thread(target=show_status).start()

def setup_gui():
    """Paso 1: Solicita los minutos usando Tkinter."""
    global icon
    
    root = Tk()
    root.withdraw()
    
    minutes_str = simpledialog.askstring(
        "Awake Duration", 
        "¡xD! ¿Cuántos minutos quieres mantener activo tu sistema?\n\nIntroduce los minutos:", 
        parent=root
    )

    if minutes_str is None:
        root.destroy()
        sys.exit(0)

    try:
        minutes = int(minutes_str)
        if minutes <= 0:
            messagebox.showerror("Error", "Debes introducir un número mayor a cero.")
            root.destroy()
            sys.exit(0)
    except ValueError:
        messagebox.showerror("Error", "Entrada no válida. Debes introducir un número entero.")
        root.destroy()
        sys.exit(0)

    root.destroy()
    return minutes

def run_tray_icon(minutes):
    """Paso 2: Configura y corre el icono de la bandeja y el hilo de trabajo."""
    global icon
    
    worker_thread = threading.Thread(target=keep_awake_loop, args=(minutes,))
    worker_thread.daemon = True # Permite que el programa principal se cierre si este hilo sigue corriendo
    worker_thread.start()
    
    image = create_image(64, 64)

    menu = Menu(
        MenuItem('El Sistema está Activo', on_running_click),
        Menu.SEPARATOR,
        MenuItem('Detener y Salir', on_stop_click)
    )

    icon = Icon("KeepAwakeTool", image, "Sistema Activo (KeepAwake)", menu)
    icon.run() # Bloquea el hilo principal para mantener el icono

if __name__ == "__main__":
    multiprocessing.freeze_support()
    minutes = setup_gui()
    run_tray_icon(minutes)