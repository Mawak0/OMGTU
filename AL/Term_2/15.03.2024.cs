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
        Dictionary<string, Dictionary<string, Dictionary<string, int>>> second_task_data = new Dictionary<string, Dictionary<string, Dictionary<string, int>>>();
        for (int i = 0; i < str_count; i++)
        {
            s = Console.ReadLine().Split(' ');
            string number_from = s[0];
            string number_to = s[1];
            string date = s[2];
            int talk_time = int.Parse(s[3]);



            if (!first_task_data.ContainsKey(date)) { first_task_data.Add(date, new Dictionary<string, Dictionary<string, int>>()); }
            if (!first_task_data[date].ContainsKey(number_from)) { first_task_data[date].Add(number_from, new Dictionary<string, int>()); }
            if (!first_task_data[date][number_from].ContainsKey(number_to)) { first_task_data[date][number_from].Add(number_to, 0); }
            first_task_data[date][number_from][number_to] = first_task_data[date][number_from][number_to] + 1;

            if (!second_task_data.ContainsKey(date)) { second_task_data.Add(date, new Dictionary<string, Dictionary<string, int>>()); }
            if (!second_task_data[date].ContainsKey(number_from)) { second_task_data[date].Add(number_from, new Dictionary<string, int>()); }
            if (!second_task_data[date][number_from].ContainsKey(number_to)) { second_task_data[date][number_from].Add(number_to, talk_time); }
            if (second_task_data[date][number_from][number_to] < talk_time) { second_task_data[date][number_from][number_to] = talk_time; }

        }


        Console.WriteLine("Введите номер абонента, для получения информации ");
        string need_number = Console.ReadLine();
        foreach (var e1 in first_task_data)
        {
            string data = e1.Key;
            foreach (var e2 in e1.Value)
            {
                string number_from = e2.Key;
                if (number_from == need_number)
                {
                    Console.WriteLine($"Статистика за {data}");
                    foreach (var e3 in e2.Value)
                    {
                        string number_to = e3.Key;
                        int calls_count = e3.Value;
                        Console.WriteLine($"{number_to} - {calls_count} звонков");
                    }
                }
            }
        }

        //int m = 0;
        foreach (var e1 in second_task_data)
        {
            string data = e1.Key;
            foreach (var e2 in e1.Value)
            {
                string number_from = e2.Key;
                int m = 0;
                string current_num = number_from;
                string favorite_num_to = "";

                foreach (var e3 in e2.Value)
                {
                    string number_to = e3.Key;
                    int talk_time = e3.Value;
                    if (m < talk_time)
                    {
                        m = talk_time;
                        favorite_num_to = number_to;
                    }
                }
                Console.WriteLine($"{data} Абонент с номером {current_num} разговаривал c {favorite_num_to} максимум {m} минут");

            }

        }



        Console.ReadKey();
    }
}
