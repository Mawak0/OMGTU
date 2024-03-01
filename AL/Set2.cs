/******************************************************************************

на вход подаются три множества, необходимо выполнить операцию пересечения, объединения и дополнения

*******************************************************************************/
using System;
using System.Collections.Generic;
class HelloWorld {
    
  static void ShowSet(HashSet<string> set){
      Console.Write("\n");
      foreach (string s in set){
          Console.Write($"{s} ");
      }
      Console.Write("\n");
  }
  static void Main() {
    Console.WriteLine("Вводите элементы множеств в следующем формате: ");
    Console.WriteLine("A B C D E");
    Console.WriteLine("Введите первое множество: ");
    string s;
    s = Console.ReadLine();
    HashSet<string> set1 = new HashSet<string>();
    HashSet<string> set11 = new HashSet<string>();
    foreach (string e in s.Split(" ")){
        set1.Add(e);
        set11.Add(e);
    }
    Console.WriteLine("Введите второе множество: ");
    s = Console.ReadLine();
    HashSet<string> set2 = new HashSet<string>();
    foreach (string e in s.Split(" ")){
        set2.Add(e);
    }
    Console.WriteLine("Введите третье множество: ");
    s = Console.ReadLine();
    HashSet<string> set3 = new HashSet<string>();
    foreach (string e in s.Split(" ")){
        set3.Add(e);
    }
    HashSet<string> union = new HashSet<string>();
    union.UnionWith(set1);
    union.UnionWith(set2);
    union.UnionWith(set3);
    Console.WriteLine("Объединение множеств: ");
    ShowSet(union);
    set11.IntersectWith(set2);
    set11.IntersectWith(set3);
    Console.WriteLine("Пересечение множеств: ");
    ShowSet(set11);
    Console.WriteLine("Дополнение первого множества: ");
    union.ExceptWith(set1);
    ShowSet(union);
    union.UnionWith(set1);
    union.UnionWith(set2);
    union.UnionWith(set3);
    Console.WriteLine("Дополнение второго множества: ");
    union.ExceptWith(set2);
    ShowSet(union);
    union.UnionWith(set1);
    union.UnionWith(set2);
    union.UnionWith(set3);
    Console.WriteLine("Дополнение третьего множества: ");
    union.ExceptWith(set3);
    ShowSet(union);
    
    
    
    
    
}
}
