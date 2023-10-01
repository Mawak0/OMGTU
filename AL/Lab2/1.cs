
using System;
class HelloWorld
{
    static void Main()
    {
        int dif1 = 0;
        int dif2 = 0;
        int summ = 0;
        int n = Convert.ToInt32(Console.ReadLine());
        for (int i = 0; i < n; i++)
        {
            int a = Convert.ToInt32(Console.ReadLine());
            int b = Convert.ToInt32(Console.ReadLine());
            summ += Math.Max(a, b);
            if (Math.Abs(a - b) % 3 == 1) dif1 = Math.Min(dif1, Math.Abs(a - b));
            if (Math.Abs(a - b) % 3 == 2) dif2 = Math.Min(dif2, Math.Abs(a - b));
        }
        if (summ % 3 == 0) Console.WriteLine(summ);
        if (summ % 3 == 1)
        {
            if (dif1 == 0) Console.WriteLine("NO");
            else Console.WriteLine(summ - dif1);
        }
        if (summ % 3 == 2)
        {
            if (dif2 == 0) Console.WriteLine("NO");
            else Console.WriteLine(summ - dif2);
        }
    }
}