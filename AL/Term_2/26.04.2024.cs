using System;
using System.Linq;
using System.Collections.Generic;
class HelloWorld {
  static void Main() {
    List<string> str = new List<string>() {"s", "jth", "98", "rtrt", "rtyu"};
    var sel = from e in str where e.Length % 2 == 0 select e;
    foreach (string s in sel){
        Console.WriteLine(s);
    }
    Console.WriteLine("Введите количество строк, которые нужно добавить");
    int a = int.Parse(Console.ReadLine());
    for(int i = 0; i < a; i++)
    {
        str.Add(Console.ReadLine());
    }

    List<string> del = (from e in str where str.IndexOf(e)%2 != 0 select e).ToList();
    str = del;
    sel = from e in str where e.Length % 2 == 0 select e;
    Console.WriteLine("--------------");
    foreach (string s in sel){
        Console.WriteLine(s);
    }
  }
}
