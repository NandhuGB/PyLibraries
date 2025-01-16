from enum import Enum

# product class
class Color(Enum):
    Red = 1
    Green = 2
    Blue = 3

class Size(Enum):
    Small = 1
    Medium = 2
    Large = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# Product Filter - anti design
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p


# Enterprise design patterns - Specification
from abc import ABC, abstractmethod 
# abstract class
class Specification:

    def is_satified(self, item):
        pass
# abstract class
class Filter():

    def filter(self, items, spec:Specification):
        pass

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color
    def is_satified(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size: Size) -> None:
        self.size = size
    def is_satified(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1= spec1
        self.spec2 = spec2
    def is_satisfied(self, item):
        return self.spec1.is_satified(item) and self.spec2.is_satified(item)
    
class BetterFilter(Filter):
    def filter(self, items, spec:Specification):
        for item in items:
            if spec.is_satified(item):
                yield item

apple = Product("Apple", Color.Green, Size.Small)
tree = Product("Tree", Color.Green, Size.Large)
house = Product("House", Color.Blue, Size.Medium)
products = [apple, tree, house]


### Anti design
#-----------------------------------------
pf = ProductFilter()

print("Green color products: Anti-design")
for p in pf.filter_by_color(products = products, color = Color.Green):
    print(f"{p.name} is green")


print("Large sized products - Anti-design")
for p in pf.filter_by_size(products = products, size = Size.Large):
    print(f"{p.name} is large")

# combinator
print("Medium sized blue colored item -  Anti-design")
for p in pf.filter_by_size_and_color(products= products, size = Size.Medium, color = Color.Blue):
    print(f"{p.name} is medium blue")


### Better Filter
#---------------------------------------------

bpf = BetterFilter() 

print("Green colored Products: Better way")
green  =ColorSpecification(Color.Green)
for p in bpf.filter(items = products, spec = green):
    print(f" - {p.name} is green")


print("Large sized products - Better way")
large = SizeSpecification(Size.Large)
for p in bpf.filter(items = products, spec = large):
    print(f" - {p.name} is large")

print("Medium Sized Blue colored Items: Better way")
medium =  SizeSpecification(Size.Medium)
blue = ColorSpecification(Color.Blue)
large_green =  AndSpecification(large, green)
for p in bpf.filter(items= products, spec = large_green):
    print(f" - {p.name} is medium blue")
