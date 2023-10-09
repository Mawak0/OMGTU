
using System;
class HelloWorld
{
    static void Main()
    {
        int dif1 = 9999999;
        int dif2 = 9999999;
        int summ = 0;
        int n = Convert.ToInt32(Console.ReadLine());
        for (int i = 0; i < n; i++)
        {
            int a = Convert.ToInt32(Console.ReadLine());
            int b = Convert.ToInt32(Console.ReadLine());
            summ += Math.Max(a, b);
            if (dif1 < 9999999)
            {
                if (Math.Abs(a - b) % 3 == 1) dif2 = Math.Min(dif2, Math.Abs(a - b) + dif1);
            }
            if (dif2 < 9999999)
            {
                if (Math.Abs(a - b) % 3 == 2) dif1 = Math.Min(dif1, Math.Abs(a - b) + dif2);
            }
            if (Math.Abs(a - b) % 3 == 1) dif1 = Math.Min(dif1, Math.Abs(a - b));

            if (Math.Abs(a - b) % 3 == 2) dif2 = Math.Min(dif2, Math.Abs(a - b));

        }


        if (summ % 3 == 0) Console.WriteLine(summ);
        if (summ % 3 == 1)
        {
            if (dif1 == 9999999) Console.WriteLine("NO");
            else Console.WriteLine(summ - dif1);
        }
        if (summ % 3 == 2)
        {
            if (dif2 == 9999999) Console.WriteLine("NO");
            else Console.WriteLine(summ - dif2);
        }
        Console.ReadLine();
    }
}