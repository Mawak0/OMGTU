using System;
using System.Linq;
class data{
    public int Number_check;
    public string FIO;
    public string Number;
    public double Income;
    public double Expenses;
    public double Tax;
    public double Balance;
    
    public data(int Number_check, string FIO, string Number, double Income, double Expenses){
        this.Number_check = Number_check;
        this.FIO = FIO;
        this.Number = Number;
        this.Income = Income;
        this.Expenses = Expenses;
        this.Tax = Income* 5 /100;
        this.Balance = Income - Expenses;
        
    }
}

class HelloWorld {
  static void Main() {
    data[] mass = new data[5];
    mass[0] = new data(1, "A A A", "88005553535", 130, 73);
    mass[1] = new data(2, "B B V", "88005553532", 1450, 453);
    mass[2] = new data(3, "p A A", "880059993535", 100000, 899983);
    mass[3] = new data(4, "pfrjkt,fkb", "666", 13202020, 9699969);
    mass[4] = new data(9, "AAAAAAAAAAAAAA", "78005553535", 2, 8973);
    
    var negative_balance_count = (from p in mass
    where p.Balance < 0
    select p).Count();
    Console.WriteLine("Количество клиентов с отрицательным балансом: "+Convert.ToString(negative_balance_count));
    var max_balance = mass.Max(x => x.Balance);
    var user_with_max_balance = from user in mass where user.Balance == max_balance select user;
    Console.WriteLine("Номер счета клиента с наибольшим балансом: "+Convert.ToString(user_with_max_balance.ToList()[0].Number_check));
    var sr = mass.Sum(x => x.Income)/mass.Length;
    Console.WriteLine("Средний доход по счетам: " + sr);
    var sum_tax = mass.Sum(x => x.Tax);
    Console.WriteLine("Суммарная сумма налогов: "+Convert.ToString(sum_tax));
}
}
