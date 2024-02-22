import pyautogui
import time

input("Appuyez sur Entrée pour commencer le test...")

time.sleep(2)

current_position = pyautogui.position()
print(f"Coordonnées actuelles du curseur : {current_position}")

input("Appuyez sur Entrée pour fermer la fenêtre...")