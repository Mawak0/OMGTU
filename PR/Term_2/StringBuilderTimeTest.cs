using System;
using System.Text;
using System.Diagnostics;
class HelloWorld {
  static void SbTest(){
    StringBuilder sb = new StringBuilder("0123456789", 10);
    Random rnd = new Random();
    for (int i = 0; i <= 1000000; i++){
        sb[i % 10] = Convert.ToString(rnd.Next(0, 9))[0];
    }
    //Console.WriteLine(sb.ToString());
  }
  
  static void StrTest(){
    string str = "0123456789";
    Random rnd = new Random();
    int index;
    for (int i = 0; i <= 1000000; i++){
        index = i % 10;
        str = str.Remove(index, 1).Insert(index, Convert.ToString(rnd.Next(0, 9)));
    }
    //Console.WriteLine(str);
  }
  static void Main() {
    Stopwatch v1 = new Stopwatch();
    v1.Start();
    
    StrTest();
    
    v1.Stop();
    Console.WriteLine($"String test = {v1.Elapsed}");
    
    
    Stopwatch v2 = new Stopwatch();
    v2.Start();
    
    SbTest();
    
    v2.Stop();
    Console.WriteLine($"StringBuilder test = {v2.Elapsed}");

  }
}
