using System;
using System.Collections.Generic;
using System.ComponentModel.Design;
using System.Linq.Expressions;

class Program
{
    static bool IsCorrectBracketSequence(string BracketSequence)
    {
        string phrase = BracketSequence;
        Stack<char> stack = new Stack<char>();
        bool good = true;
        foreach (char c in phrase)
        {
            if (c == '[' || c == '{' || c == '(')
            {
                stack.Push(c);
            }
            if (c == ']')
            {
                if (stack.Count == 0) { good = false; break; }
                if (stack.Pop() != '[') { good = false; break; }
            }
            if (c == '}')
            {
                if (stack.Count == 0) { good = false; break; }
                if (stack.Pop() != '{') { good = false; break; }
            }
            if (c == ')')
            {
                if (stack.Count == 0) { good = false; break; }
                if (stack.Pop() != '(') { good = false; break; }
            }
        }
        if (stack.Count != 0) { good = false; }
        if (good) { return true; }
        else { return false; }
    }
    static string ReversePolishNotation(string phrase)
    {
        Stack<string> stack = new Stack<string>();
        double result = 0;
        double a;
        double b;
        bool err = false;
        foreach (char c in phrase)
        {
            if (c == '+' || c == '-' || c == '*' || c == '/')
            {
                if (stack.Count < 2) { Console.WriteLine("Ошибка: Отсутствие элемента для произведения вычисления"); err = true; break; }
                if (stack.Count > 2) { Console.WriteLine("Ошибка: Неоднозначность результата"); err = true; break; }
                b = Convert.ToDouble(stack.Pop());
                a = Convert.ToDouble(stack.Pop());
                if (b == 0) { Console.WriteLine("Ошибка: Деление на ноль"); err = true; break; }
                if (c == '+') { result = a + b; }
                if (c == '-') { result = a - b; }
                if (c == '*') { result = a * b; }
                if (c == '/') { result = a / b; }
                stack.Push(Convert.ToString(result));
            }
            else
            {
                if (c != ' ')
                {
                    stack.Push(Convert.ToString(c));
                }
            }

        }
        if (err == false) { return stack.Pop(); }
        else { throw new Exception("Некорректное выражение"); }
    }
    static int Menu() {
        Console.WriteLine("0) Сведения об авторе");
        Console.WriteLine("1) Обратная польская запись");
        Console.WriteLine("2) Скобочная последовательность");
        Console.WriteLine("3) Выход из программы");
        return Convert.ToInt32(Console.ReadLine());
    }
    static void Main() {
        int c = -1;
        while (c != 3) {
            c = Menu();
            if (c == 0) { Console.WriteLine("Автор программы: Дрожжачих А.Д. ФИТ-231"); }
            else if (c == 1)
            {
                Console.WriteLine("Введите выражение в формате обратной польской записи: ");
                string phrase = Console.ReadLine();
                try { Console.WriteLine($"Значение выражения: {ReversePolishNotation(phrase)}"); }
                catch { Console.WriteLine("Ошибка: невозможно произвести вычисление"); }
            }
            else if (c == 2) {
                Console.WriteLine("Введите скобочную последовательность:");
                string phrase = Console.ReadLine();
                bool check = IsCorrectBracketSequence(phrase);
                if (check) { Console.WriteLine("Последовательность корректна"); }
                else { Console.WriteLine("Последовательность некорректна"); }
            }
        }
    }
}
