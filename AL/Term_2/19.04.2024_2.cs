/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
using System;
using System.IO;
using System.Text.RegularExpressions;
class HelloWorld {

  static void CreateFiles(){
    File.Create("input").Close();
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
    AppendLine("oooAAAAAAAAAppAAAAppqqq", "input");
    AppendLine("qweAAeqAAA", "input");
    AppendLine("oooAAAAAppppqqq", "input");
    AppendLine("qpwApwq", "input");
    
    int inp_l = FileLength("input");
    string s = "";
    bool stop = false;
    while (!stop){
        s = s+ "A";
        string pattern = @"([^A]|^)"+s+"([^A]|$)";
        for (int i = 0; i < inp_l; i++){
            string c_s = ReadLine("input", i);
                if (Regex.IsMatch(c_s, pattern)){
                    Console.WriteLine(c_s);
                    stop = true;
                    break;
                }
            }
        }
    }
    
}
