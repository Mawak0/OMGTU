using System;
using System.Linq;

class TrapezoidalRule
{
    public static double Solve(Func<double, double> f, double a, double b, double dx)
    {
        double epsilon = 10E-7;
        if (!double.IsNormal(a)) { throw new ArgumentException("a is not a number"); }
        if (!double.IsNormal(b)) { throw new ArgumentException("b is not a number"); }
        if (dx < epsilon) { throw new ArgumentException("dx меньше epsilon"); }

        int distCount = Convert.ToInt32(Math.Ceiling((b - a) / dx)); // Number of segments
        double[] xValues = Enumerable.Range(0, distCount + 1).Select(i => a + dx * i).ToArray();

        return xValues.Sum(x => Math.Abs(((f(x) + f(x + dx)) * dx) / 2));
    }
}
Func<double, double> f = (double x) => -x*x + 9;
double a = 1;
double b = 4;
double dx = 0.1;
Console.WriteLine(TrapezoidalRule.Solve(f,a,b,dx));
