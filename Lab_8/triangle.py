import math
import logging
from datetime import datetime
from typing import List, Tuple, Union

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('triangle.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

class TriangleAnalyzer:
    """Класс для анализа треугольника и вычисления координат вершин"""
    
    def __init__(self, canvas_size: int = 100):
        self.canvas_size = canvas_size
        
    def validate_input(self, side_a: str, side_b: str, side_c: str) -> Union[Tuple[float, float, float], None]:
        """Проверка валидности входных данных"""
        try:
            a = float(side_a)
            b = float(side_b)
            c = float(side_c)
            
            # Проверка на положительные числа
            if a <= 0 or b <= 0 or c <= 0:
                logging.warning(f"Отрицательное или нулевое значение: a={a}, b={b}, c={c}")
                return None
                
            return (a, b, c)
        except ValueError as e:
            logging.error(f"Ошибка преобразования: {e}, данные: {side_a}, {side_b}, {side_c}")
            return None
    
    def get_triangle_type(self, a: float, b: float, c: float) -> str:
        """Определение типа треугольника"""
        # Проверка неравенства треугольника
        if a + b <= c or a + c <= b or b + c <= a:
            return "не треугольник"
        
        # Проверка на равносторонний
        if abs(a - b) < 1e-6 and abs(b - c) < 1e-6:
            return "равносторонний"
        
        # Проверка на равнобедренный
        if abs(a - b) < 1e-6 or abs(b - c) < 1e-6 or abs(a - c) < 1e-6:
            return "равнобедренный"
        
        return "разносторонний"
    
    def calculate_coordinates(self, a: float, b: float, c: float) -> List[Tuple[int, int]]:
        """Вычисление координат вершин треугольника"""
        # Проверка, существует ли треугольник
        if a + b <= c or a + c <= b or b + c <= a:
            return [(-1, -1), (-1, -1), (-1, -1)]
        
        # Размещаем первую вершину в начале координат
        A = (0, 0)
        
        # Вторую вершину на оси X
        B = (self.canvas_size, 0)
        
        # Вычисляем координаты третьей вершины по формулам
        max_side = max(a, b, c)
        scale = self.canvas_size / max_side
        
        # Масштабируем стороны
        a_scaled = a * scale
        b_scaled = b * scale
        c_scaled = c * scale
        
        # Вычисляем координаты вершины C
        x_C = (a_scaled**2 - b_scaled**2 + c_scaled**2) / (2 * c_scaled)
        y_C = math.sqrt(max(0, a_scaled**2 - x_C**2))
        
        C = (int(round(x_C)), int(round(y_C)))
        
        return [A, B, C]
    
    def process_request(self, side_a: str, side_b: str, side_c: str) -> Tuple[str, List[Tuple[int, int]]]:
        """Обработка запроса: определение типа и координат"""
        # Логируем запрос
        logging.info(f"Запрос: стороны [{side_a}, {side_b}, {side_c}]")
        
        # Валидация входных данных
        sides = self.validate_input(side_a, side_b, side_c)
        
        if sides is None:
            # Нечисловые или невалидные данные
            logging.warning("Невалидные входные данные")
            return "", [(-2, -2), (-2, -2), (-2, -2)]
        
        a, b, c = sides
        
        # Определяем тип треугольника
        triangle_type = self.get_triangle_type(a, b, c)
        
        # Вычисляем координаты
        if triangle_type == "не треугольник":
            coordinates = [(-1, -1), (-1, -1), (-1, -1)]
        else:
            coordinates = self.calculate_coordinates(a, b, c)
        
        # Логируем результат
        if triangle_type in ["равносторонний", "равнобедренный", "разносторонний"]:
            logging.info(f"Успех: {triangle_type}, координаты: {coordinates}")
        else:
            logging.warning(f"Неуспех: {triangle_type}, координаты: {coordinates}")
        
        return triangle_type, coordinates


# Пример использования
if __name__ == "__main__":
    analyzer = TriangleAnalyzer(100)
    
    # Тестовые примеры
    test_cases = [
        ("5", "5", "5"),      # Равносторонний
        ("5", "5", "3"),      # Равнобедренный
        ("3", "4", "5"),      # Прямоугольный (разносторонний)
        ("1", "1", "3"),      # Не треугольник
        ("a", "5", "5"),      # Нечисловые данные
        ("-5", "5", "5"),     # Отрицательные числа
    ]
    
    print("="*60)
    print("ТЕСТИРОВАНИЕ ПРОГРАММЫ ОПРЕДЕЛЕНИЯ ТРЕУГОЛЬНИКА")
    print("="*60)
    
    for sides in test_cases:
        print("\n" + "-"*40)
        print(f"Входные данные: {sides}")
        result_type, coords = analyzer.process_request(*sides)
        if result_type:
            print(f"✓ Тип: {result_type}")
        else:
            print("✗ Ошибка: невалидные входные данные")
        print(f"  Координаты вершин:")
        print(f"    Вершина A: {coords[0]}")
        print(f"    Вершина B: {coords[1]}")
        print(f"    Вершина C: {coords[2]}")
    
    print("\n" + "="*60)
    print("Тестирование завершено. Проверьте файл triangle.log")
    print("="*60)
