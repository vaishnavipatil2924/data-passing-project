from django.shortcuts import render,HttpResponse

# Create your views here.


def addition_view(request,num1,num2):
    a =num1
    b=num2
    result = a + b
    return HttpResponse(f"<h2>Result of addition{a} + {b} is: {result}</h2>")
        
def area_of_circle(request,radius):

    r = radius
    area = 3.14 * r * r
    return HttpResponse(f"<h2>Area of circle with radius {r} is: {area}</h2>")

def area_of_rectangle(request,l,b):
    length = l
    breadth = b
    area = l * b
    return HttpResponse(f"<h2>Area of rectangle with length {length} and breadth {breadth} is: {area}</h2>")

def area_of_triangle(request,base,height):
    b = base
    h = height
    area = 0.5 * b * h
    return HttpResponse(f"<h2>Area of triangle with base {b} and height {h} is: {area}</h2>")

def area_of_square(request,side):
    s = side
    area = s * s
    return HttpResponse(f"<h2>Area of square with side {s} is: {area}</h2>")

def multiplication_view(request,num1,num2):
    a = num1
    b = num2
    result = a * b
    return HttpResponse(f"<h2>Result of multiplication {a} * {b} is: {result}</h2>")

def division_view(request,num1,num2):
    a = num1
    b = num2
    if b != 0:
        result = a / b
        return HttpResponse(f"<h2>Result of division {a} / {b} is: {result}</h2>")
    else:
        return HttpResponse("<h2>Error: Division by zero is not allowed.</h2>")

def subtraction_view(request,num1,num2):
    a = num1
    b = num2
    result = a - b
    return HttpResponse(f"<h2>Result of subtraction {a} - {b} is: {result}</h2>")

def area_of_cube(request,side):
    s = side
    area = 6 * s * s
    return HttpResponse(f"<h2>Area of cube with side {s} is: {area}</h2>")

