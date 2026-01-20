import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class SpaceAnalyzer:
    def __init__(self, image_path):
        self.image_path = image_path
        self.img = cv2.imread(image_path)
        if self.img is None:
            raise ValueError(f"No se pudo leer la imagen en: {image_path}")
        self.img_rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

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
            
    # Se crea umbral adaptativo para detectar estrellas en condiciones de luz variables
    def get_star_count(self):

        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        
        # Un blur suave ayuda a eliminar ruido de un solo pixel
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Se pasan argumentos en orden: (imagen, max_valor, metodo_adaptativo, tipo_umbral, bloque, constante)
        thresh = cv2.adaptiveThreshold(
            blurred, 
            255, 
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 
            11, 
            2
        )
        
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Filtro de objetos demasiado pequeños (ruido)
        min_star_area = 3
        stars = [c for c in contours if cv2.contourArea(c) > min_star_area]
        
        return len(stars)
    
    
    # Calculo del histograma de color para R, G y B
    def get_color_histogram(self):
        colors = ('b', 'g', 'r') # OpenCV lee en BGR
        data = {}

        for i, color in enumerate(colors):
            # Calculo del histograma: imagen, canal, máscara, tamaño, rango
            hist = cv2.calcHist([self.img], [i], None, [256], [0, 256])
            col_name = 'Azul' if color == 'b' else 'Verde' if color == 'g' else 'Rojo'
            data[col_name] = hist.flatten()
        df = pd.DataFrame(data)
        return df
    
        
    # Genera un mapa de calor "térmico" basado en la luminosidad de los píxeles
    def get_thermal_heatmap(self):

        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        heatmap = ax.imshow(gray, cmap='inferno')
        
        plt.colorbar(heatmap, label='Intensidad de Luz (0-255)')
        ax.set_title("Mapa de Distribución de Energía Lumínica")
        ax.axis('off') 

        return fig