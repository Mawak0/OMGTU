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
        Console.WriteLine("<номер> <дата> <время начала разговора> <длительность в минутах>");
        Queue<string> queue1 = new Queue<string>();
        Queue<string> queue2 = new Queue<string>();
        string s;
        for (int i = 0; i < str_count; i++) {
            s = Console.ReadLine();
            queue1.Enqueue(s);
            queue2.Enqueue(s);
        }
        
        Dictionary<string, int> d1 = new Dictionary<string, int>();
        Hashtable h1 = new Hashtable();
        string[] st;
        string number;
        string date;
        string begin_time;
        string talk_time;
        while (queue1.Count != 0)
        {
            st = queue1.Dequeue().Split(' ');
            number = st[0];
            date = st[1];
            begin_time = st[2];
            talk_time = st[3];


            if (d1.ContainsKey(number)) { d1[number] += Convert.ToInt32(talk_time); }

            else { d1.Add(number, Convert.ToInt32(talk_time));}


            if (h1.ContainsKey(number)) { h1[number] = Convert.ToInt32(h1[number]) + Convert.ToInt32(talk_time); }
            else { h1.Add(number, Convert.ToInt32(talk_time)); }
        }

        Console.WriteLine("Отчет: ");
        Console.WriteLine("Результат из хеш таблицы: ");
        foreach (DictionaryEntry e in h1) {
            Console.WriteLine($"{e.Key} - {e.Value} минут");
        }
        Console.WriteLine("\n\nРезультат из словаря: ");
        foreach (var e in d1) {
            Console.WriteLine($"{e.Key} - {e.Value} минут");
        }


        Dictionary<string, int> d2 = new Dictionary<string, int>();
        Hashtable h2 = new Hashtable();
        Console.WriteLine("Введите дату для получения информации о разговорах в этот день");
        string need_date = Console.ReadLine();
        while (queue2.Count != 0) {
            st = queue2.Dequeue().Split(' ');
            number = st[0];
            date = st[1];
            begin_time = st[2];
            talk_time = st[3];

            if (date == need_date)
            {
                if (d2.ContainsKey(number)) { d2[number] += Convert.ToInt32(talk_time); }
                else { d2.Add(number, Convert.ToInt32(talk_time)); }

                if (h2.ContainsKey(number)) { h2[number] = Convert.ToInt32(h2[number]) + Convert.ToInt32(talk_time); }
                else { h2.Add(number, Convert.ToInt32(talk_time)); }
            }
        }

        Console.WriteLine($"Отчет за {need_date}");
        Console.WriteLine("Результат из хеш таблицы: ");
        int sum = 0;
        foreach (DictionaryEntry e in h2)
        {
            sum += Convert.ToInt32(e.Value);
        }
        Console.WriteLine($"Суммарное время разговоров: {sum} минут");
        Console.WriteLine("\n\nРезультат из словаря: ");
        sum = 0;
        foreach (var e in d2)
        {
            sum += Convert.ToInt32(e.Value);
        }
        Console.WriteLine($"Суммарное время разговоров: {sum} минут");
    }
}
