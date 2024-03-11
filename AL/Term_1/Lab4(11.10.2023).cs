/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
using System;
using System.Linq;
class HelloWorld {
  static bool contain_char(string s, char q){
      foreach (char c in s){
          if (c == Convert.ToChar(q)){ 
              return true;
          }
      }
      return false;
  }
  
  static int summa_cifr(int a){
      a = Math.Abs(a);
      int sum = 0;
      foreach (char c in Convert.ToString(a)){
          sum += Convert.ToInt32(Convert.ToString(c));
      }
      return sum;
  }
  static void Main() {
    int n = Convert.ToInt32(Console.ReadLine());
    int[] mass = new int[n];
    for (int i = 0; i < n; i++){
        mass[i] = Convert.ToInt32(Console.ReadLine());
    }
    int max_elem = mass[0];
    int max_elem_pos = 0;
    int min_elem = mass[0];
    int min_elem_pos = 0;
    for (int i = 0; i < n; i++){
        if (mass[i] > max_elem){
            max_elem = mass[i];
            max_elem_pos = i;
        }
        if (mass[i] < min_elem){
            min_elem = mass[i];
            min_elem_pos = i;
        }
        
    }
    int chet_mejdu = 0;
    if (Math.Abs(min_elem_pos - max_elem_pos) < 2){
        Console.WriteLine("Между максимальным и минимальным элементами пустое множество");
    }
    else{
        for (int i = Math.Min(min_elem_pos, max_elem_pos)+1; i < Math.Max(min_elem_pos, max_elem_pos); i++){
            if (mass[i] % 2 == 0) chet_mejdu++;
        }
        Console.WriteLine($"Количество четных элементов между максимальным и минимальным элементами = {chet_mejdu}");
    }
    int vse_na_chet_ime_5 = 1;
    for (int i = 0; i < n; i++){
        if (((i+1) %2 == 0) && (contain_char(Convert.ToString(mass[i]), '5') == false)){
            vse_na_chet_ime_5 = 0;
        }
    }
    if (vse_na_chet_ime_5 == 0) Console.WriteLine("Не все элементы стоящие на четных местах сожержат 5 в своей записи");
    else Console.WriteLine("Все элементы стоящие на четных местах сожержат 5 в своей записи");
    
    int[] new_mass = new int[n];
    for (int i = 0; i < n; i++){
        if (mass[i] % 2 ==0){
            new_mass[i] = mass[i];
        }
        else{
            new_mass[i] = summa_cifr(mass[i]);
        }
    }
    Console.WriteLine("Массив, после замены всех нечетных элементов на сумму их цифр");
    foreach (int a in new_mass){
        Console.Write($" {a} ");
    }
    int srednear_nechet = 0;
    int summa_nechet = 0;
    int count_nechet = 0;
    for (int i = 0; i < n; i++){
        if (mass[i] % 2 != 0){
            count_nechet++;
            summa_nechet += mass[i];
        }
    }
    srednear_nechet = summa_nechet / count_nechet;
    //Console.WriteLine($"\n {srednear_nechet}");
    int count_for_task_4 = 0;
    for (int i = 0; i < n; i++){
        if (mass[i] > srednear_nechet) count_for_task_4++;
    }
    Console.WriteLine($"\n Количество элементов массива, которые больше среднего арифметического нечетных элементов = {count_for_task_4}");
    
    int flag_task_5 = 0;
    for (int i =0; i < n; i++){
        if ((mass[i] < 0) && (Convert.ToString(mass[i]))[Convert.ToString(mass[i]).Length -1] == '3'){
            flag_task_5 = 1;
        }
    }
    if (flag_task_5 == 1) Console.WriteLine("В массиве имеется отрицательный элемент, оканчивающийся на тройку");
    else Console.WriteLine("В массиве нет отрицательного элемента, оканчивающегося на тройку");
  }
}
