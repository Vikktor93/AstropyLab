import cv2
import numpy as np

class SpaceAnalyzer:
    def __init__(self, image_path):
        self.image_path = image_path
        self.img = cv2.imread(image_path)
        self.img_rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

    # Retorna el color promedio (R, G, B) y una etiqueta de texto
    def get_dominant_color(self):
        avg_row = np.average(self.img_rgb, axis=0)
        avg_color = np.average(avg_row, axis=0).astype(int)
        
        r, g, b = avg_color
        label = "Espacio Profundo / Neutro"
        if r > b and r > g:
            label = "Dominancia ROJA (Posible Nebulosa/Marte)"
        elif b > r and b > g:
            label = "Dominancia AZUL (Estrellas Jóvenes/Oxígeno)"
            
        return avg_color, label

    # Retorna el número aproximado de estrellas
    def get_star_count(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return len(contours)