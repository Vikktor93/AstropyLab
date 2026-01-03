import cv2
import numpy as np
import matplotlib.pyplot as plt

class SpaceAnalyzer:
    def __init__(self, image_path):
        self.image_path = image_path
        # Se carga la imagen con OpenCV
        self.img = cv2.imread(image_path)
        # Se convierte de BGR (formato OpenCV) a RGB (formato estándar)
        self.img_rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

         
    # Calcula el color promedio de la imagen para inferir 'el tono' del universo en el día actual.  
    def analyze_colors(self):
        avg_color_per_row = np.average(self.img_rgb, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        
        print(f"Análisis de Color (RGB Promedio): {avg_color.astype(int)}")
        
        # Lógica simple de interpretación
        r, g, b = avg_color
        if r > b and r > g:
            print("   -> Dominancia ROJA: Posible nebulosa de emisión o superficie marciana")
        elif b > r and b > g:
            print("   -> Dominancia AZUL: Posible reflexión, estrellas jóvenes o atmósfera")
        else:
            print("   -> Equilibrio o escala de grises (Espacio profundo/Galaxia)")

    
    # Se usa umbralización para contar puntos brillantes (estrellas potenciales)
    def count_stars(self):
        # Conversión a escala de grises
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        # Se aplica un desenfoque suave para eliminar ruido (píxeles muertos)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Umbralización: Todo lo que brille más de 200 (en escala 0-255) es una estrella
        _, thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
        
        # Encontrar contornos (las 'islas' blancas)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        count = len(contours)
        print(f"Estrellas/Objetos brillantes detectados (aprox): {count}")
        return count