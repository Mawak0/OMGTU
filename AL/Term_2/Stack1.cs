using System;
using System.Collections.Generic;

    class Program
    {
        static void Main()
        {
            Console.WriteLine("Введите выражение: ");
            string phrase = Console.ReadLine();
            Stack<char> stack = new Stack<char>();
            bool good = true;
            foreach (char c in phrase) {
                if (c == '[' || c == '{' || c == '(') {
                    stack.Push(c);
                }
                if (c == ']') {
                    if (stack.Count == 0) { good = false; break; }
                    if (stack.Pop() != '[') { good = false; break;}
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
            if (good) { Console.WriteLine("Выражение составлено корректно"); }
            else { Console.WriteLine("Выражение составлено некорректно"); }
        }
    }
