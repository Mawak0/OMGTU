using System.Diagnostics.CodeAnalysis;

class ArithmeticCoding {

    static bool Contain(char[] mass, char c) {
        for (int j = 0; j < mass.Length; j++) {
            if (mass[j] == c) {
                return true;
            }
        }
        return false;
    }

    static int ElementIndex(char[] mass, char c) {
        for (int i = 0; i < mass.Length; i++) {
            if (mass[i] == c) { return i; }
        }
        return -1;
    }

    static int Count(string input, char c) {
        int count = 0;
        for (int i = 0; i < input.Length; i++) {
            if (input[i] == c) { count++; }
        }
        return count;
    }

    static char[] GetAlphabet(string input)
    {
        char[] alphabet = new char[0];
        for (int i = 0; i < input.Length; i++) {
            if ((Contain(alphabet, input[i])) == false) {
                Array.Resize(ref alphabet, alphabet.Length + 1);
                alphabet[alphabet.Length - 1] = input[i];
            }
        }
        return alphabet;
    }

    static Dictionary<char, double> FindProbability(char[] alphabet, string input) {
        Dictionary<char, double> probability = new Dictionary<char, double>();
        for (int i = 0; i < alphabet.Length; i++) {
            probability.Add(alphabet[i], Convert.ToDouble(Count(input, alphabet[i])) / Convert.ToDouble(input.Length));
        }
        return probability;
    }



    static double FindSumm(Dictionary<char, double> dynamic_prob, char c, char[] sorted_letters, double startpoint) {
        double sum = 0;
        foreach (char e in sorted_letters) {
            if (c == e) { return sum; }
            sum += dynamic_prob[e] - startpoint;
        }
        return sum;
    }


    static decimal Encode(string source) {
        // добавляем символ конца строки ^
        source = source + "^";
        // находим алфавит строки
        char[] alphabet = GetAlphabet(source);
        // находим распределение вероятностей
        Dictionary<char, double> probability = FindProbability(alphabet, source);

        // сортируем символы по вероятностям
        char[] sorted_letters = new char[alphabet.Length];
        for (int i = 0; i < alphabet.Length; i++) {
            double max_letter = 0;
            char letter = 'Q';
            foreach (var e in probability) {
                if (e.Value > max_letter) {
                    if (Contain(sorted_letters, e.Key) == false) { max_letter = e.Value; letter = e.Key; }
                }
            }
            sorted_letters[i] = letter;
        }

        // вычисляем отрезки
        Dictionary<char, double> dynamic_prob = new Dictionary<char, double>();
        foreach (var e in probability) {
            dynamic_prob.Add(e.Key, e.Value + FindSumm(probability, e.Key, sorted_letters, 0)); 
        }
        foreach (var e in dynamic_prob) {
            Console.WriteLine($"{e.Key} - {e.Value}");
        }

        double oldstartpoint = 0;

        for (int i = 0; i < source.Length; i++) {
            double endpoint = dynamic_prob[source[i]];
            int startpoint_elem_id = ElementIndex(sorted_letters, source[i]) - 1;
            double startpoint;
            if (startpoint_elem_id == -1) {startpoint = oldstartpoint; }
            else {
                startpoint = dynamic_prob[sorted_letters[startpoint_elem_id]];
            }

            Console.WriteLine($"{startpoint}....{endpoint}");

            foreach (var e in dynamic_prob) {
                dynamic_prob[e.Key] = (endpoint - startpoint) * probability[e.Key] + startpoint;
            }
            Dictionary<char, double> old_dynamic = new Dictionary<char, double>();
            foreach (var e in dynamic_prob)
            {
                old_dynamic.Add(e.Key, e.Value);
            }
            dynamic_prob.Clear();
            foreach (var e in old_dynamic)
            {
                dynamic_prob.Add(e.Key, e.Value + FindSumm(old_dynamic, e.Key, sorted_letters, startpoint));
            }
            foreach (var e in dynamic_prob)
            {
                Console.WriteLine($"{e.Key} - {e.Value}");
            }
            oldstartpoint = startpoint;

        }

        return 0;
    }
    static void Main(){
        Console.WriteLine("Hello world");
        string h = "abaabaaca";
        Encode(h);
    }
}
