using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OMGTU.AL.Лабораторные_работы_1_4
{
    internal class _1

    {
        static void Main() {
            int x = -1;
            double a = 0.5;
            int b = 2;
            double y = b * Math.Pow(x, 2) * Math.Exp(a * Math.Pow(x, 2)) + a * Math.Sqrt(x + 1.5);
            Console.WriteLine($"y(-1) = {y}");
            x = 1;
            y = b * Math.Pow(x, 2) * Math.Exp(a * Math.Pow(x, 2)) + a * Math.Sqrt(x + 1.5);
            Console.WriteLine($"y(1) = {y}");
        }
    }
}
