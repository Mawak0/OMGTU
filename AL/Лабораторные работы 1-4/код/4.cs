using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OMGTU.AL.Лабораторные_работы_1_4
{
    internal class _4
    {
        static double Z(double x, double a)
        {
            if ((0 <= x) & (x <= 2)) return x * x * Math.Pow(Math.E, -(x * x) / 2);
            if ((2 < x) & (x <= 3.6)) return Math.Pow(Math.E, (x * x) / a) - 1;
            return double.NaN;
        }
        static void Main()
        {
            for (double a = 0.5; a <= 0.75; a += 0.25)
            {
                for (double x = 0; x <= 3.6; x = x + a / 2)
                {
                    Console.WriteLine($"a = {a}, x = {x}, Z = {Z(x, a)}");
                }
            }

        }
    }
}
