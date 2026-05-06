from triangle import TriangleAnalyzer

def main():
    print("\n" + "="*50)
    print(" ПРОГРАММА ОПРЕДЕЛЕНИЯ ТРЕУГОЛЬНИКА")
    print("="*50)
    print("Введите длины трех сторон (для выхода введите 'exit'):")
    print()
    
    analyzer = TriangleAnalyzer(100)
    
    while True:
        print("-"*40)
        a = input("Сторона A: ")
        if a.lower() == 'exit':
            print("\nПрограмма завершена. Проверьте файл triangle.log")
            break
            
        b = input("Сторона B: ")
        if b.lower() == 'exit':
            print("\nПрограмма завершена. Проверьте файл triangle.log")
            break
            
        c = input("Сторона C: ")
        if c.lower() == 'exit':
            print("\nПрограмма завершена. Проверьте файл triangle.log")
            break
        
        print()
        result_type, coordinates = analyzer.process_request(a, b, c)
        
        if result_type:
            print(f"📐 Результат: {result_type}")
            print(f"📍 Координаты вершин (в поле 100x100):")
            print(f"   Вершина A: {coordinates[0]}")
            print(f"   Вершина B: {coordinates[1]}")
            print(f"   Вершина C: {coordinates[2]}")
        else:
            print("❌ Ошибка: невалидные входные данные")
            print("   (должны быть положительные числа)")
        print()

if __name__ == "__main__":
    main()
