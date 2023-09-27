using System;
class HelloWorld
{
    static void Main()
    {
        Console.Write("n = ");
        int n = Convert.ToInt32(Console.ReadLine());
        int count_max = 0;
        int count = 0;
        int last = 99999;
        for (int i = 0; i < n; i++)
        {
            int a = Convert.ToInt32(Console.ReadLine());
            if (last != a)
            {
                if (count_max < count)
                {
                    count_max = count;
                }
                count = 1;
                last = a;
            }
            else
            {
                count++;
                last = a;
                if (count_max < count)
                {
                    count_max = count;
                }
            }
        }
        Console.WriteLine(count_max);
    }
}