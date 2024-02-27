using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.WriteLine("Введите выражение: ");
        string phrase = Console.ReadLine();
        Stack<string> stack = new Stack<string>();
        double result = 0;
        double a;
        double b;
        bool err = false;
        foreach (char c in phrase) {
            if (c == '+' || c == '-' || c == '*' || c == '/')
            {
                if (stack.Count < 2) { Console.WriteLine("Ошибка: Отсутствие элемента для произведения вычисления"); err = true; break; }
                if (stack.Count > 2) { Console.WriteLine("Ошибка: Неоднозначность результата"); err = true; break; }
                b = Convert.ToDouble(stack.Pop());
                a = Convert.ToDouble(stack.Pop());
                if (b == 0) { Console.WriteLine("Ошибка: Деление на ноль"); err = true; break; }
                if (c == '+') { result = a+b; }
                if (c == '-') { result = a - b; }
                if (c == '*') { result = a * b; }
                if (c == '/') { result = a / b; }
                stack.Push(Convert.ToString(result));
            }
            else {
                if (c != ' ')
                {
                    stack.Push(Convert.ToString(c));
                }
            }
            //Console.Write($"\n_{c}_");
            //foreach (string e in stack) { Console.Write($"{e} "); }
        }
        if (err == false) { Console.WriteLine($"Результат вычисления: {stack.Pop()}"); }
    }
}
