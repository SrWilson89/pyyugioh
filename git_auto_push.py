import os
import time
import subprocess

def ejecutar_comando_git(comando):
    """
    Ejecuta un comando de Git y maneja los errores.
    """
    try:
        resultado = subprocess.run(
            comando,
            check=True,
            shell=True,
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        print(resultado.stdout)
        if resultado.stderr:
            print(f"Error (stderr): {resultado.stderr}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR: No se pudo ejecutar el comando '{' '.join(comando)}'")
        print(f"Código de retorno: {e.returncode}")
        print(f"Salida estándar: {e.stdout}")
        print(f"Salida de error: {e.stderr}")
        return False
    except FileNotFoundError:
        print("ERROR: Git no está instalado o no se encuentra en el PATH del sistema.")
        return False

def guardar_y_subir_a_git():
    """
    Añade, commitea y sube los cambios a Git.
    """
    print("\n--- Iniciando guardado y push automático a Git ---")
    
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"Auto-save: Proyecto actualizado - {timestamp}"
    
    # 1. Añadir todos los cambios
    if not ejecutar_comando_git(["git", "add", "."]):
        return
        
    # 2. Hacer el commit
    if not ejecutar_comando_git(["git", "commit", "-m", commit_message]):
        # Si el commit falla, podría ser porque no hay cambios.
        # Lo verificamos con 'git status'
        status_result = subprocess.run(
            ["git", "status", "--porcelain"], 
            capture_output=True, 
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        if status_result.stdout.strip() == "":
            print("No hay cambios para commitear. Saltando 'git commit'.")
        else:
            print("ERROR: No se pudo hacer el commit, revisa los mensajes de arriba.")
        return

    # 3. Hacer el push
    if not ejecutar_comando_git(["git", "push", "origin", "main"]):
        print("ERROR: No se pudo hacer el push. Asegúrate de que el branch 'main' exista y el remoto 'origin' esté configurado correctamente.")
        return

    print("--- Guardado y push a Git completado con éxito ---")

def iniciar_guardado_automatico():
    """
    Bucle principal para el guardado automático.
    """
    intervalo_minutos = 30
    intervalo_segundos = intervalo_minutos * 60
    
    print(f"Guardado automático iniciado. Se guardará y subirá a Git cada {intervalo_minutos} minutos.")
    print("Para detener, cierra esta ventana del terminal.")
    
    while True:
        guardar_y_subir_a_git()
        print(f"Esperando {intervalo_minutos} minutos para el siguiente guardado...")
        time.sleep(intervalo_segundos)

if __name__ == "__main__":
    iniciar_guardado_automatico()