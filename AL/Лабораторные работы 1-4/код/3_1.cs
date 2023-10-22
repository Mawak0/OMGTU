using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OMGTU.AL.Лабораторные_работы_1_4
{
    internal class _3
    {
        static int Factorial(int n) { 
            int rez = 1;
            for (int i = 1; i <= n; i++)
            {
                rez = rez * i;
            }
            return rez;
        }
        static void Main() {
            Console.Write("n = ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine($"n! = {Factorial(n)}");
        }
    }
}
