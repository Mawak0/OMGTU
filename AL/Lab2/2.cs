using System;
class HelloWorld
{
    static void Main()
    {
        Console.Write("n = ");
        int n = Convert.ToInt32(Console.ReadLine());
        int count = 0;
        int last = 0;
        for (int i = 0; i != n; i++)
        {
            int a = Convert.ToInt32(Console.ReadLine());
            if (last == 0)
            {
                if (a < 0)
                {
                    last = -1;
                }
                if (a > 0)
                {
                    last = 1;
                }
                continue;

            }
            else
            {
                if ((a > 0) && (last < 0))
                {
                    count++;
                }
                if ((a < 0) && (last > 0))
                {
                    count++;
                }
                if (a < 0)
                {
                    last = -1;
                }
                if (a > 0)
                {
                    last = 1;
                }
            }


        }
        Console.WriteLine(count);
    }
}