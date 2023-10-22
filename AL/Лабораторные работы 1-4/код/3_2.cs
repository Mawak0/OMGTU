using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OMGTU.AL.Лабораторные_работы_1_4
{
    internal class _3_2
    {
        static void Main() {
            double step = Math.PI / 16;
            for (int i = 1; i <= 16; i++) {
                double x = step * i;
                double F1 = 2 * Math.Sin(2 * x) + 1;
                double F2 = Math.Pow(x + 5, 3) * (1 + Math.Pow(Math.Sin(x), 2));
                Console.WriteLine($"F1({x}) = {F1}");
                Console.WriteLine($"F2({x}) = {F2}");
            }
        }
    }
}
