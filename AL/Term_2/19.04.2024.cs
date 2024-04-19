/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
using System;
using System.IO;
class HelloWorld {

  static void CreateFiles(){
    File.Create("input_1").Close();
    File.Create("input_2").Close();
    File.Create("output").Close();
  }

  static void AppendLine(string line, string path){
        StreamWriter writer = new StreamWriter(path, true);
        writer.WriteLine(line);
        writer.Close();
  }
  static string ReadLine(string path, int pos){
        StreamReader reader = new StreamReader(path);
        for (int c = 0; c < pos; c++){reader.ReadLine();}
        string str = reader.ReadLine();
        reader.Close();
        return str;
  }
 
 static int FileLength(string path){
        StreamReader reader = new StreamReader(path);
        for (int c = 0; c != -1; c++){
            if (reader.ReadLine() == null){
                reader.Close();
                return c; 
            }
        }
        return 0;
 }
 
  static void Main() {
    CreateFiles();
    AppendLine("1", "input_1");
    AppendLine("2", "input_1");
    AppendLine("5", "input_1");
    AppendLine("1", "input_2");
    AppendLine("10", "input_2");
    AppendLine("70", "input_2");
    //Console.WriteLine(ReadLine("input_2", 100));
    //Console.WriteLine(FileLength("input_2"));
    
    int r = FileLength("input_2");
    for (int i = 0; i < r; i++)
    {
        AppendLine(ReadLine("input_2", i),"input_1");
    }
    
    int low_border = 0;
    int i1l = FileLength("input_1");
    while (FileLength("output")!=FileLength("input_1"))
    {
        int min = 9999999;
        for (int i = 0; i < i1l; i++){
            int current_number = Convert.ToInt32(ReadLine("input_1", i));
            if ((min > current_number) && (current_number > low_border)){
                min = current_number;
                Console.WriteLine(min);
            }
            low_border = min;
            Console.WriteLine(min);
            Console.WriteLine(low_border);
            Console.ReadLine();
            
        }
        for (int i = 0; i < i1l; i++){
            if (min == Convert.ToInt32(ReadLine("input_1", i))){
                AppendLine(Convert.ToString(min), "output");
            }
        }
    }
  }
}
