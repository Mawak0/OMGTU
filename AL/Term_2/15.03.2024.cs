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
        Console.WriteLine("88005553535 27.02.1990 17:30 55");
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

            if (first_task_data.ContainsKey(date))
            {
                if (first_task_data[date].ContainsKey(number_from))
                {
                    if (first_task_data[date][number_from].ContainsKey(number_to))
                    {
                        first_task_data[date][number_from][number_to] += 1;
                    }
                    else { first_task_data[date][number_from].Add(number_to, 1); }
                }
                else { first_task_data[date].Add(number_from, new Dictionary<string, int>()); }
            }
            else { first_task_data.Add(date, new Dictionary<string, Dictionary<string, int>>()); }

        }

        Console.WriteLine()

        Console.WriteLine("Введите номер абонента, для получения информации ");
        
    }
}
