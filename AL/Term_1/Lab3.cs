/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
using System;
class HelloWorld {
  static void Main() {
    int n = Convert.ToInt32(Console.ReadLine());
    int[] elems = new int[n];
    for (int i = 0; i < n; i++){
        elems[i] = Convert.ToInt32(Console.ReadLine());
        
    }
    int vse_li_kratni_nomeru = 1;
    for (int i = 0; i < n; i++){
        if ((elems[i] % (i + 1)) != 0) vse_li_kratni_nomeru = 0;
    }
    if (vse_li_kratni_nomeru == 1) Console.WriteLine("Все кратны своему номеру");
    else Console.WriteLine("Не все кратны своему номеру");
    
    int bil_chet = 0;
    for (int i =0; i < n; i++){
        if ((bil_chet == 0) && (elems[i] % 2 == 0)){
            bil_chet = 1;
            Console.WriteLine($"Первый четный элемент под номером {i+1}");
        }
    }
    int last_zero_pos = -1;
    for (int i = 0; i < n; i++){
        if (elems[i] == 0){
            last_zero_pos = i;
        }
    }
    if (last_zero_pos == -1) Console.WriteLine("Нет нулевого элемента");
    else Console.WriteLine($"Последний нулевой элемент находится под номером {last_zero_pos+1}");
  
  int min_in_elem = 999999;
  foreach (int e in elems){
      if (e < min_in_elem) min_in_elem = e; 
  }
  if (min_in_elem != 0){
      int count_krat = 0;
      foreach (int e in elems){
          if (e % min_in_elem == 0) count_krat++;
      }
      Console.WriteLine($"Количество кратных минимальному =  {count_krat}");
    }
  int pos_min = -1;
  int pos_max = -1;
  int min = 999999;
  int max = -1;
  for (int i = 0; i < n; i++){
      if (elems[i] < min){
          pos_min = i;
          min = elems[i];
      }
      if (elems[i] > max){
          pos_max = i;
          max = elems[i];
      }
      
  }
  if (Math.Abs(pos_max - pos_min) == 0) Console.WriteLine("Количество элементов расположенных между максимальным и минимальным равно нолю");
  int is_low = 1;
    if (pos_max > pos_min){
    int last = elems[pos_min+1];
    for (int i = pos_min+2; i < pos_max; i++){
      if (elems[i] < last){
              last = elems[i];
          }
        else is_low = 0;
      }}
    else{
        int last = elems[pos_min-1];
    for (int i = pos_min-2; i > pos_max; i--){
      if (elems[i] < last){
              last = elems[i];
          }
        else is_low = 0;
      }
    }
    if (is_low == 1) Console.WriteLine("Элементы между максимальным и минимальным элементом составляют убывающую последовательность");
    else Console.WriteLine("Элементы между минимальным и максимальным элементом НЕ составляют убывающую последовательность");
}
}
