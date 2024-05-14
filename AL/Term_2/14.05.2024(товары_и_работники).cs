using System;
using System.Linq;
class data{
    public int number;
    public string FIO;
    public string education;
    public string speciality;
    public double salary;
    public int quantity_of_goods;
    public double pcs_price;
    public data(int number, string FIO, string education, string speciality, double salary, int quantity_of_goods, double pcs_price){
        this.number = number;
        this.FIO = FIO;
        this.education = education;
        this.speciality = speciality;
        this.salary = salary;
        this.quantity_of_goods = quantity_of_goods;
        this.pcs_price =pcs_price;
    }
}
class Program {
  static void Main() {
    data[] info = new data[5];
    info[0] = new data(1, "A A A", "v", "tr", 38, 15, 6);
    info[1] = new data(2, "A B A", "v", "tr", 400, 25, 7);
    info[2] = new data(3, "C C C", "v", "tr", 2000, 35, 10);
    info[3] = new data(4, "D D D", "sp", "pr", 50000, 78, 98);
    info[4] = new data(5, "D E F", "sp", "an", 20, 56, 2);
    
    var a = from person in info 
    where person.salary < person.quantity_of_goods*person.pcs_price
    select person;
    Console.WriteLine("Сотрудники, у которых зарплата меньше суммы создаваемой ими продукции:");
    foreach (var i in a){
        Console.WriteLine(i.FIO);
    }
    /*var tovar_po_price = from t in tov group t by t.category;
    var max_price_tovara = from t in tovar_po_price select new {a = t.Key, ib = t.Max(c => c.price)};*/
    //var b = from p in info group p by p.pcs_price;
    //var b1 = from p in b select new {e = p.Key, r = p.}
    var b = (from person in info 
    select person.quantity_of_goods).Sum();
    Console.WriteLine($"Количество единиц продукта по всем сотрудникам: {b}");

    var summ_price = (from p in info select p.quantity_of_goods*p.pcs_price).Sum();
    Console.WriteLine($"Суммарная стоимость всей производимой продукции: {summ_price}");
    
    var c = (from person in info 
    where person.salary >= (person.quantity_of_goods*person.pcs_price)*0.5
    select person).Count();
    Console.WriteLine($"Количество сотрудников, у которых зарплата не меньше 50% от суммы создаваемой ими продукции: {c}");

    
  }
}
