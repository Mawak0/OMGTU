using System;
using System.Linq;

class Tovar{
    public int number;
    public string name;
    public string category;
    public int count;
    public double price;
    public int storage_number;
    public Tovar(int number, string name, string category, int count, double price, int storage_number){
        this.number = number;
        this.name = name;
        this.category = category;
        this.count = count;
        this.price = price;
        this.storage_number = storage_number;
    }
}
class Program{
  static void Main() {
    Tovar[] tov = new Tovar[9];
    tov[0] = new Tovar(1, "kolbasa", "food", 99, 200, 1);
    tov[1] = new Tovar(2, "moloko", "food", 50, 45, 1);
    tov[2] = new Tovar(3, "hleb", "food", 26, 50, 2);
    tov[3] = new Tovar(4, "tovar bez kategory", "", 400, 250, 1076);
    tov[4] = new Tovar(5, "mouse","comp", 1, 1000, 3);
    tov[5] = new Tovar(6, "cat", "ne comp", 0, 999, 1);
    tov[6] = new Tovar(7, "kolbasa", "food", 189, 201, 2);
    tov[7] = new Tovar(8, "smetana", "food", 1, 30, 1);
    tov[8] = new Tovar(4, "tovar bez kategory 2", "", 800, 280, 1076);
    
    var tovarov_po_vsem_skladam = from t in tov group t by t.storage_number;
    var obem_tovarov_po_skladam = from t in tovarov_po_vsem_skladam select new {category = t.Key, count=t.Sum(x => x.count)};
    Console.WriteLine("Объем товаров по всем складам: ");
    foreach (var e in obem_tovarov_po_skladam){
        Console.WriteLine($"{e.category}: {e.count}");
    }
    var tovar_po_price = from t in tov group t by t.category;
    var max_price_tovara = from t in tovar_po_price select new {a = t.Key, ib = t.Max(c => c.price)};
    Console.WriteLine("Максимальная цена по каждой категории: ");
    foreach (var e in max_price_tovara){
        if (e.a == ""){ Console.WriteLine("Без категории:" + e.ib);}
        else{Console.WriteLine(e.a + ":" + e.ib);}
    }
    var sr_price_tovarov_bez_category = (from t in tov where t.category == "" select t).Average(x => x.price);
    Console.WriteLine($"Средняя цена товаров без категории: {sr_price_tovarov_bez_category}");
    var min_price = tov.Min(x => x.price);
    var min_price_tovar = (from t in tov where t.price == min_price select t).ToList();
    Console.WriteLine($"Самый дешевый товар со всех складов: {min_price_tovar[0].name} цена: {min_price}");
    var summ_price = tov.Sum(x => x.price);
  }
}
