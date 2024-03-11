/******************************************************************************

на вход подаются номера телефонов и количество минут разговоров, определить количество уникальных номеров

*******************************************************************************/
using System;
using System.Collections.Generic;
class HelloWorld {
  static void Main() {
    Console.WriteLine("Введите количество разговоров: ");
    int str_count = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Вводите данные в следующем формате: ");
    Console.WriteLine("88005553535 55");
    Console.WriteLine("<номер> <длительность разговора в минутах>");
    Queue<string> queue1 = new Queue<string>();
    string s;
    for (int i = 0; i < str_count; i++) {
        s = Console.ReadLine();
        queue1.Enqueue(s);
    }
    
    HashSet<string> set1 = new HashSet<string>();
    string[] st;
    string number;
    string talk_time;
    while (queue1.Count != 0)
    {
        st = queue1.Dequeue().Split(' ');
        number = st[0];
        talk_time = st[1];
        set1.Add(number);

  }
  Console.WriteLine($"Количество уникальных номеров: {set1.Count}");
}
}
