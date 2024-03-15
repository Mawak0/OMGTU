using System;
using System.Collections.Generic;
using System.Collections;

class Program
{
    static void Main()
    {
        Console.WriteLine("Введите количество разговоров: ");
        int str_count = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Вводите данные в следующем формате: ");
        Console.WriteLine("88005553535 8800111111 15.03.2024 55");
        Console.WriteLine("<номер с которого звонили> <номер на который звонили> <дата> <длительность в минутах>");
        string[] s;

        Dictionary<string, Dictionary<string, Dictionary<string, int>>> first_task_data = new Dictionary<string, Dictionary<string, Dictionary<string, int>>>(); // {date: {number_from: {number_to: count}}}
        for (int i = 0; i < str_count; i++)
        {
            s = Console.ReadLine().Split(' ');
            string number_from = s[0];
            string number_to = s[1];
            string date = s[2];
            string talk_time = s[3];



            if (!first_task_data.ContainsKey(date)) { first_task_data.Add(date, new Dictionary<string, Dictionary<string, int>>()); }
            if (!first_task_data[date].ContainsKey(number_from)) { first_task_data[date].Add(number_from, new Dictionary<string, int>()); }
            if (!first_task_data[date][number_from].ContainsKey(number_to)) { first_task_data[date][number_from].Add(number_to, 0); }
            first_task_data[date][number_from][number_to] = first_task_data[date][number_from][number_to] + 1;

        }


        Console.WriteLine("Введите номер абонента, для получения информации ");
        string need_number = Console.ReadLine();
        foreach (var e1 in first_task_data) {
            string data = e1.Key;
            foreach (var e2 in e1.Value) {
                string number_from = e2.Key;
                if (number_from == need_number) {
                    Console.WriteLine($"Статистика за {data}");
                    foreach (var e3 in e2.Value) {
                        string number_to = e3.Key;
                        int calls_count = e3.Value;
                        Console.WriteLine($"{number_to} - {calls_count} звонков");
                    }
                }
            }
        }
        
    }
}
