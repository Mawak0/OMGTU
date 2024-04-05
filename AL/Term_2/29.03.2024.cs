using System;
class Prog{

    interface ActionsTemplate{
        double Plus(float a, float b);
        double Minus(float a, float b);
        double Multiplication(float a, float b);
        double Division(float a, float b);
        double Sqrt(float a);
        double Sin(float a);
        float[] EnterValues();
        float EnterValue();
    }
    
    class Actions : ActionsTemplate{
        public double Plus(float a, float b) => (a+b);
        public double Minus(float a, float b) => (a-b);
        public double Multiplication(float a, float b) => (a*b);
        public double Division(float a, float b){
            if (b==0){
                throw new ArgumentException("a = 0");
            }
            return (a/b);
            
        }
        public double Sqrt(float a){
            if (a < 0){
                throw new ArgumentException("a < 0");
            }
            return Math.Sqrt(a);
            
        }
        public double Sin(float a) => (Math.Sin(a));
        public double Cos(float a) => (Math.Cos(a));
        public float[] EnterValues(){
                Console.WriteLine("Введите два числа через пробел");
                string s;
                s = Console.ReadLine();
                float a = float.Parse(s.Split(" ")[0]);
                float b = float.Parse(s.Split(" ")[1]);
                float[] f = new float[2];
                f[0] = a;
                f[1] = b;
                return f;
        }
        public float EnterValue(){
                Console.WriteLine("Введите число");
                string s;
                s = Console.ReadLine();
                float a = float.Parse(s);
                return a;
        }
    } 

    public static int Menu(){
        Console.WriteLine("Выберите математическую операцию: ");
        Console.WriteLine("1)Сложение");
        Console.WriteLine("2)Вычитание");
        Console.WriteLine("3)Умножение");
        Console.WriteLine("4)Деление");
        Console.WriteLine("5)Извлечение квадратного корня");
        Console.WriteLine("6)Нахождение синуса");
        Console.WriteLine("7)Нахождение косинуса");
        Console.WriteLine("8)Выход");
        return Convert.ToInt32(Console.ReadLine());
    }
    delegate double BinaryMathAction(float a, float b);
    delegate double UnaryMathAction(float a);
    public static void Main(){
        Actions Action = new Actions();
        BinaryMathAction plus = Action.Plus;
        BinaryMathAction minus = Action.Minus;
        BinaryMathAction multiplication = Action.Multiplication;
        BinaryMathAction division = Action.Division;
        UnaryMathAction sqrt = Action.Sqrt;
        UnaryMathAction sin = Action.Sin;
        UnaryMathAction cos = Action.Cos;
        int c = 0;
        float[] f;
        while (c != 8){
            c = Menu();
            if (c == 1){
                f = Action.EnterValues();
                Console.WriteLine(plus(f[0],f[1]));
                }
            if (c == 2){
                f = Action.EnterValues();
                Console.WriteLine(minus(f[0],f[1]));
            }
            if (c == 3){
                f = Action.EnterValues();
                Console.WriteLine(multiplication(f[0],f[1]));
            }
            if (c == 4){
                try{
                    f = Action.EnterValues();
                    Console.WriteLine(division(f[0],f[1]));
                }
                catch {
                    Console.WriteLine("Ошибка: Нельзя делить на ноль");
                }
            }
            if (c == 5){
                try{
                    Console.WriteLine(sqrt(Action.EnterValue()));
                }
                catch{
                    Console.WriteLine("Ошибка: Невозможно извлечь корень из отрицательного числа");
                }
            }
            if (c == 6){
                Console.WriteLine(sin(Action.EnterValue()));
            }
            if (c == 7){
                Console.WriteLine(cos(Action.EnterValue()));
            }
        } 
    }
}


