/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
// 0 = dead mouse
// 1 = black mouse
// 2 = white mouse
// mass = [state, number]
using System;
class HelloWorld
{

    static int one_alive_pos(int[][] mass)
    {
        int count = 0;
        int n = mass.Length;
        int last_alive = -1;
        for (int i = 0; i < n; i++)
        {
            if (mass[i][0] != 0)
            {
                count++;
                last_alive = i;
            }
        }
        if (count == 1) return last_alive;
        else return -1;
    }
    static void Main()
    {
        Console.WriteLine("Введите количество мышей");
        int n = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Съедать каждую k мышь, k = ");
        int k = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Номер белой мыши");
        int white_mouse_pos = Convert.ToInt32(Console.ReadLine()) - 1;
        int first_eat = 0;
        int[][] mass = new int[n][];
        for (int i = 0; i < n; i++) mass[i] = new int[2];
        for (int i = 0; i < n; i++)
        {
            if (i == white_mouse_pos)
            {
                mass[i][0] = 2;
                mass[i][1] = i;
            }
            else
            {
                mass[i][0] = 1;
                mass[i][1] = i;
            }
        }
        int delta = 0;
        int stay_alive = -1;
        mass[first_eat][0] = 0;
        for (int i = first_eat; stay_alive == -1; i++)
        {

            if (i >= n)
            {
                i = i - n;
            }

            stay_alive = one_alive_pos(mass);
            if ((mass[i][0] != 0) && (delta != k))
            {
                delta++;
            }
            if (delta == k)
            {
                if (stay_alive != -1) break;
                if (mass[i][0] != 0)
                {
                    mass[i][0] = 0;
                }
                delta = 0;
            }
        }
        int live_mouse_pos = -1;
        for (int i = 0; i < n; i++)
        {
            if (mass[i][0] != 0) live_mouse_pos = i;
        }
        int need_first_eat = 0;
        if (live_mouse_pos > white_mouse_pos) need_first_eat = -Math.Abs(live_mouse_pos - white_mouse_pos);
        if (live_mouse_pos < white_mouse_pos) need_first_eat = Math.Abs(live_mouse_pos - white_mouse_pos);
        if (need_first_eat < 0) need_first_eat = (n + 1) + need_first_eat;
        Console.WriteLine($"Первой должна быть съедена мышь под номером = {need_first_eat}");
    }
}
