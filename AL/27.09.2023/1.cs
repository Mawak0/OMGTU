using System;
class HelloWorld
{
    static void Main()
    {
        Console.Write("n = ");
        int n = Convert.ToInt32(Console.ReadLine());
        int count = 0;
        int lastlast = 99999;
        int last = 99999;
        for (int i = 0; i != n; i++)
        {
            int a = Convert.ToInt32(Console.ReadLine());
            if (last == 99999)
            {
                last = a;
                continue;

            }
            else if (lastlast == 99999)
            {
                lastlast = last;
                last = a;
                continue;
            }
            else
            {
                if ((last < a) && (last < lastlast))
                {
                    count++;
                }
            }
            lastlast = last;
            last = a;

        }
        Console.WriteLine(count);
    }
}