using System.IO;
using System;
using System.Text;

struct Dano{
    public string FIO;
    public string Number;
    public string City;
    
    public Dano(string FIO, string Number, string City){
        this.FIO = FIO;
        this.Number = Number;
        this.City = City;
    }
    
}

class HelloWorld {
    
  static void WriteData(Dano[] data, string path){
        BinaryWriter writer = new BinaryWriter(File.Open(path, FileMode.OpenOrCreate));
        foreach (var e in data){
            string FIO = e.FIO;
            string Number = e.Number;
            string City = e.City;
            writer.Write(FIO);
            writer.Write(Number);
            writer.Write(City);
        }
        writer.Close();
  }
  static Dano[] ReadData(string path){
      BinaryReader reader = new BinaryReader(File.Open(path, FileMode.OpenOrCreate));
      Dano[] data = new Dano[0];
      while (true){
          try{
            string FIO = reader.ReadString();
            string Number = reader.ReadString();
            string City = reader.ReadString();
            Array.Resize(ref data, data.Length+1);
            data[data.Length-1] = new Dano(FIO, Number, City);
          }
          catch{break;}
        }
        reader.Close();
        return data;
  }
  static void Main() {
    Dano[] data = new Dano[3];
    data[0] = new Dano("A A A", "1", "g");
    data[1] = new Dano("A A B", "2", "l");
    data[2] = new Dano("T T T", "3", "g");
    WriteData(data, "data");
    Dano[] r_data = ReadData("data");
    Console.WriteLine("Введите город");
    string city = Console.ReadLine();
    Dano[] city_data = new Dano[0];
    foreach (Dano i in r_data)
    {
        if (i.City == city){
            Array.Resize(ref city_data, city_data.Length+1);
            city_data[city_data.Length-1] = i;
        }
    }
    WriteData(city_data, "city_data");    
    foreach (var e in ReadData("city_data")){
        Console.WriteLine($"{e.FIO} {e.Number} {e.City}");
    }
    Console.WriteLine("Введите фамилию");
    string surname = Console.ReadLine();
    Dano[] surname_data = new Dano[0];
    foreach (Dano i in r_data)
    {
        if (i.FIO.Split(" ")[0] == surname){
            Array.Resize(ref surname_data, surname_data.Length+1);
            surname_data[surname_data.Length-1] = i;
        }
    }
    WriteData(surname_data, "surname_data");    
    foreach (var e in ReadData("surname_data")){
        Console.WriteLine($"{e.FIO} {e.Number} {e.City}");
    }
    
    Console.WriteLine("Введите город и фамилию (через пробел)");
    string inp = Console.ReadLine();
    city = inp.Split(" ")[0];
    surname = inp.Split(" ")[1];
    Dano[] cf_data = new Dano[0];
    foreach (Dano i in r_data)
    {
        if ((i.City == city) && (i.FIO.Split(" ")[0] == surname)){
            Array.Resize(ref cf_data, cf_data.Length+1);
            cf_data[cf_data.Length-1] = i;
        }
    }
    WriteData(cf_data, "cf_data");    
    foreach (var e in ReadData("cf_data")){
        Console.WriteLine($"{e.FIO} {e.Number} {e.City}");
    }

  }
}
