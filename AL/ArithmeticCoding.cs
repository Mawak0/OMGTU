using System.Diagnostics.CodeAnalysis;
using System.IO;
using System.Net.NetworkInformation;
using System.Xml.Serialization;
using static System.Runtime.InteropServices.JavaScript.JSType;

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

    static Dictionary<char, decimal> FindProbability(char[] alphabet, string input) {
        Dictionary<char, decimal> probability = new Dictionary<char, decimal>();
        for (int i = 0; i < alphabet.Length; i++) {
            probability.Add(alphabet[i], Convert.ToDecimal(Count(input, alphabet[i])) / Convert.ToDecimal(input.Length));
        }
        return probability;
    }



    static decimal FindSumm(Dictionary<char, decimal> dynamic_prob, char c, char[] sorted_letters, decimal startpoint) {
        decimal sum = 0;
        foreach (char e in sorted_letters) {
            if (c == e) { return sum; }
            sum += dynamic_prob[e] - startpoint;
        }
        return sum;
    }


    static string Encode(string source) {
        // находим алфавит строки
        char[] alphabet = GetAlphabet(source);
        // находим распределение вероятностей
        Dictionary<char, decimal> probability = FindProbability(alphabet, source);

        // сортируем символы по вероятностям
        char[] sorted_letters = new char[alphabet.Length];
        for (int i = 0; i < alphabet.Length; i++) {
            decimal max_letter = 0;
            char letter = 'Q';
            foreach (var e in probability) {
                if (e.Value > max_letter) {
                    if (Contain(sorted_letters, e.Key) == false) { max_letter = e.Value; letter = e.Key; }
                }
            }
            sorted_letters[i] = letter;
        }

        // вычисляем отрезки
        Dictionary<char, decimal> dynamic_prob = new Dictionary<char, decimal>();
        foreach (var e in probability) {
            dynamic_prob.Add(e.Key, e.Value + FindSumm(probability, e.Key, sorted_letters, 0)); 
        }
        foreach (var e in dynamic_prob) {
            //Console.WriteLine($"{e.Key} - {e.Value}");
        }

        decimal oldstartpoint = 0;

        decimal endpoint = 0;
        decimal startpoint = 0;

        for (int i = 0; i < source.Length; i++) {
            endpoint = dynamic_prob[source[i]];
            int startpoint_elem_id = ElementIndex(sorted_letters, source[i]) - 1;
            if (startpoint_elem_id == -1) {startpoint = oldstartpoint; }
            else {
                startpoint = dynamic_prob[sorted_letters[startpoint_elem_id]];
            }

            //Console.WriteLine($"{startpoint}....{endpoint}");

            foreach (var e in dynamic_prob) {
                dynamic_prob[e.Key] = (endpoint - startpoint) * probability[e.Key] + startpoint;
            }
            Dictionary<char, decimal> old_dynamic = new Dictionary<char, decimal>();
            foreach (var e in dynamic_prob)
            {
                old_dynamic.Add(e.Key, e.Value);
            }
            dynamic_prob.Clear();
            foreach (var e in old_dynamic)
            {
                dynamic_prob.Add(e.Key, e.Value + FindSumm(old_dynamic, e.Key, sorted_letters, startpoint));
            }
            oldstartpoint = startpoint;
        }

        //Console.WriteLine(startpoint);
        //Console.WriteLine(endpoint);
        // находим наиболее короткую десятичную дробь между startpoint и endpoint
        string result = "";
        string sr_ar = Convert.ToString((startpoint + endpoint) / 2);
        for (int i = 2; i < sr_ar.Length; i++) {
            decimal sub = Convert.ToDecimal(sr_ar.Substring(0, i));
            if ((sub < endpoint) && (sub > startpoint)) {
                result = Convert.ToString(sub).Substring(2);
                break;
            }
        }

        return result;
    }




    static char[] Decode(Dictionary<char, decimal> probability, string code_str, int need_length)
    {
        char[] result = new char[need_length];

        char[] alphabet = new char[0];
        foreach (var e in probability) {
            Array.Resize(ref alphabet, alphabet.Length + 1);
            alphabet[alphabet.Length - 1] = e.Key;
        }

        // сортируем символы по вероятностям
        char[] sorted_letters = new char[alphabet.Length];
        for (int i = 0; i < alphabet.Length; i++)
        {
            decimal max_letter = 0;
            char letter = 'Q';
            foreach (var e in probability)
            {
                if (e.Value > max_letter)
                {
                    if (Contain(sorted_letters, e.Key) == false) { max_letter = e.Value; letter = e.Key; }
                }
            }
            sorted_letters[i] = letter;
        }

        // вычисляем отрезки
        Dictionary<char, decimal> dynamic_prob = new Dictionary<char, decimal>();
        foreach (var e in probability)
        {
            dynamic_prob.Add(e.Key, e.Value + FindSumm(probability, e.Key, sorted_letters, 0));
        }


        decimal oldstartpoint = 0;

        decimal endpoint = 0;
        decimal startpoint = 0;

        // представляем код в виде дроби
        decimal code = Convert.ToDecimal($"0,{code_str}");
        // расшифровка
        for (int i = 0; i < need_length; i++)
        {
            char current_letter = '0';
            for (int t = 0; t < sorted_letters.Length; t++) {
                //Console.WriteLine($"DEBUG1: {t}");
                if (t == 0)
                {
                    if (code < dynamic_prob[sorted_letters[t]]) { current_letter = sorted_letters[t]; break; }
                }
                else if (t == sorted_letters.Length - 1)
                {
                    if (dynamic_prob[sorted_letters[t]] < code) { current_letter = sorted_letters[t]; break; }
                }

                //Console.WriteLine(dynamic_prob[sorted_letters[t]]);
                //Console.WriteLine(dynamic_prob[sorted_letters[t+1]]);
                if ((dynamic_prob[sorted_letters[t]] < code) && (code < dynamic_prob[sorted_letters[t + 1]])) {
                    current_letter = sorted_letters[t + 1];
                    break;
                }
            }
            result[i] = current_letter;
            endpoint = dynamic_prob[current_letter];
            int startpoint_elem_id = ElementIndex(sorted_letters, current_letter) - 1;
            if (startpoint_elem_id == -1) { startpoint = oldstartpoint; }
            else
            {
                startpoint = dynamic_prob[sorted_letters[startpoint_elem_id]];
            }

            //Console.WriteLine($"{startpoint}....{endpoint}");

            foreach (var e in dynamic_prob)
            {
                dynamic_prob[e.Key] = (endpoint - startpoint) * probability[e.Key] + startpoint;
            }
            Dictionary<char, decimal> old_dynamic = new Dictionary<char, decimal>();
            foreach (var e in dynamic_prob)
            {
                old_dynamic.Add(e.Key, e.Value);
            }
            dynamic_prob.Clear();
            foreach (var e in old_dynamic)
            {
                dynamic_prob.Add(e.Key, e.Value + FindSumm(old_dynamic, e.Key, sorted_letters, startpoint));
            }

            oldstartpoint = startpoint;
        }



        return result;
    }






    static void WriteFile(Dictionary<char, decimal> probability, string code, int data_length, string file_path) {
        int alphabet_length = 0;
        foreach (var e in probability) { alphabet_length++; }
        using (BinaryWriter writer = new BinaryWriter(File.Open(file_path, FileMode.OpenOrCreate)))
        {
            writer.Write(alphabet_length);
            foreach (var e in probability) {
                writer.Write(e.Key);
                writer.Write(e.Value);
            }
            writer.Write(data_length);
            writer.Write(code);
        }
    }


    static Tuple<Dictionary<char, decimal>, string, int> ReadFile(string file_path)
    {
        Dictionary<char, decimal> probability = new Dictionary<char, decimal>();
        string code = "";
        int data_length = -1;
        using (BinaryReader reader = new BinaryReader(File.Open(file_path, FileMode.Open)))
        {
            int alphabet_length = reader.ReadInt32();
            for (int i = 0; i < alphabet_length; i++) {
                probability.Add(reader.ReadChar(), reader.ReadDecimal());
            }
            data_length = reader.ReadInt32();
            code = reader.ReadString();
        }
        Tuple<Dictionary<char, decimal>, string, int> result = Tuple.Create(probability, code, data_length);
        return result;
    }







    static void Main(){
        int ch = -1;
        Console.WriteLine("Выберите режим работы 1 - кодирование, 2 - декодирование");
        Console.Write("Режим: ");
        ch = Convert.ToInt32(Console.ReadLine());

        if (ch == 1) {
            Console.WriteLine("Выбран режим кодирования");
            Console.Write("Путь к исходному(txt) файлу(не более 15 символов в файле): ");
            string source_path = Console.ReadLine();
            string source_data;
            if (source_path.Contains(".txt") == false) {throw new Exception("Ошибка: не txt файл"); }
            using (StreamReader reader = new StreamReader(source_path)) {
                source_data = reader.ReadToEnd();
            }
            if (source_data.Length > 15) { throw new Exception("Ошибка: текст более 15 символов"); }
            Console.WriteLine("Начало кодирования");
            string code = Encode(source_data);
            char[] alphabet = GetAlphabet(source_data);
            Dictionary<char, decimal> probability = FindProbability(alphabet, source_data);
            string new_file_path = source_path.Replace(".txt", ".AC");
            WriteFile(probability, code, source_data.Length, new_file_path);
            Console.WriteLine("Кодирование завершено");
            Console.WriteLine(new_file_path);
            Console.ReadLine();
        }
        if (ch == 2) {
            Console.WriteLine("Выбран режим декодирования");
            Console.Write("Путь к закодированному(AC) файлу: ");
            string code_path = Console.ReadLine();
            if (code_path.Contains(".AC") == false) { throw new Exception("Ошибка: не AC файл"); }
            Tuple<Dictionary<char, decimal>, string, int> all_data = ReadFile(code_path);
            char[] text = Decode(all_data.Item1, all_data.Item2, all_data.Item3);
            string text_str = "";
            foreach (char q in text) {text_str = text_str + q; }
            string new_path = code_path.Replace(".AC", "-decoded.txt");
            using (StreamWriter writer = new StreamWriter(new_path))
            {
                writer.Write(text_str);
            }
            Console.WriteLine("Декодирование завершено");
            Console.WriteLine(new_path);
            Console.ReadLine();
        }
    }
}
