using System;

class Calk<T>{
    public T Plus(T a, T b){
        dynamic q = a;
        dynamic w = b;
        return q+w;
    }
    
    public T Minus(T a, T b){
        dynamic q = a;
        dynamic w = b;
        return q-w;
    }
    
    public T Multiplication(T a, T b){
        dynamic q = a;
        dynamic w = b;
        return q*w;
    }
    
    public T Delenie(T a, T b){
        dynamic q = a;
        dynamic w = b;
        return q/w;
    }
}

class HelloWorld {
  static void Main() {
      


    //Console.WriteLine(c_double.Plus(1,2));
    
    Console.WriteLine("1) работа с целыми");
    Console.WriteLine("2) работа с вещественными");
    string h = Console.ReadLine();
    if (h == "1"){
        Console.WriteLine("Введите первое число");
        int a = int.Parse(Console.ReadLine());
        Console.WriteLine("Введите второе число");
        int b = int.Parse(Console.ReadLine());
        Calk<int> c = new Calk<int>();
        
        Console.WriteLine("1) Сложение");
        Console.WriteLine("2) Вычитание");
        Console.WriteLine("3) Умножение");
        Console.WriteLine("4) Деление");
        string p = Console.ReadLine();
        if (p == "1"){Console.WriteLine(c.Plus(a, b));}
        if (p == "2"){Console.WriteLine(c.Minus(a, b));}
        if (p == "3"){Console.WriteLine(c.Multiplication(a, b));}
        if (p == "4"){Console.WriteLine(c.Delenie(a, b));}
    }
    if (h == "2"){
        Console.WriteLine("Введите первое число");
        double a = double.Parse(Console.ReadLine());
        Console.WriteLine("Введите второе число");
        double b = double.Parse(Console.ReadLine());
        Calk<double> c = new Calk<double>();
        
        Console.WriteLine("1) Сложение");
        Console.WriteLine("2) Вычитание");
        Console.WriteLine("3) Умножение");
        Console.WriteLine("4) Деление");
        string p = Console.ReadLine();
        if (p == "1"){Console.WriteLine(c.Plus(a, b));}
        if (p == "2"){Console.WriteLine(c.Minus(a, b));}
        if (p == "3"){Console.WriteLine(c.Multiplication(a, b));}
        if (p == "4"){Console.WriteLine(c.Delenie(a, b));}
    }
    
  }
}
