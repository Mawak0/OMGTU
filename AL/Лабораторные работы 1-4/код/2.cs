using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OMGTU.AL.Лабораторные_работы_1_4
{
    internal class _2
    {
        static void Main() {
            Console.Write("x = ");
            double x = Convert.ToDouble(Console.ReadLine());
            double y = 0;
            double a = 1.5;
            if ((0.9 <= x) & (x <= 5))
            {
                if (x < 1.3) y = Math.PI * Math.Pow(x, 2) - (7 / Math.Pow(x, 2));
                else if ((1.3 <= x) & (x < 3)) y = a * Math.Pow(x, 3) + 7 * Math.Sqrt(x);
                else if (x >= 3) y = Math.Log(x + 7 * Math.Sqrt(x), 10);
                Console.WriteLine($"y = {y}");
            }
            else Console.WriteLine("Функция не определена для этого x");
        }
    }
}
