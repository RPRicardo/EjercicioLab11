from abc import ABC, abstractmethod
import math

class Figura(ABC):
    
    @abstractmethod
    def get_color(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

class Triangulo(Figura):
    def __init__(self, color, lado1, lado2, lado3):
        self.color = color
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def get_color(self):
        return self.color
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def area(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

class Circulo(Figura):
    def __init__(self, color, radio):
        self.color = color
        self.radio = radio
    
    def get_color(self):
        return self.color
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def area(self):
        return math.pi * self.radio * self.radio

class Rectangulo(Figura):
    def __init__(self, color, altura, base):
        self.color = color
        self.altura = altura
        self.base = base
    
    def get_color(self):
        return self.color
    
    def perimetro(self):
        return 2 * (self.altura + self.base)
    
    def area(self):
        return self.altura * self.base

class Hexagono(Figura):
    def __init__(self, color, lado):
        self.color = color
        self.lado = lado
    
    def get_color(self):
        return self.color
    
    def perimetro(self):
        return 6 * self.lado
    
    def area(self):
        return (3 * math.sqrt(3) * self.lado * self.lado) / 2

def main():
    figuras = [
        Triangulo("rojo", 3, 4, 5),
        Circulo("azul", 7),
        Rectangulo("verde", 6, 8),
        Hexagono("amarillo", 5)
    ]
    
    for figura in figuras:
        print(f"Color: {figura.get_color()}")
        print(f"Perímetro: {figura.perimetro()}")
        print(f"Área: {figura.area()}")
        print()

if __name__ == "__main__":
    main()
