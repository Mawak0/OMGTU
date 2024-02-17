using System;
using System.Linq;
using System.Linq.Expressions;
using System.Reflection;
using System.Collections;



class MainMenu {
    public int ShowMenu() {
        Console.WriteLine("\n\n0) Выход\n1) Меню Array\n2) Меню ArrayList\n3) Меню SortedList");
        return Convert.ToInt32(Console.ReadLine());
    }
}

class ArrayMenu
{
    public int ShowMenu(bool array_created)
    {
        if (array_created)
        {
            Console.WriteLine("\n\n\n\n0) Назад \n1) Создать массив\n2) Узнать количество элементов в массиве (Length)\n3) Выполнить бинарный поиск элемента (BinarySearch)\n4) Скопировать коллекцию(Copy)\n5) Выполнить поиск вхождения подстроки(Find)\n6) Выполнить поиск вхождения подстроки с конца(FindLast)\n7) Нахождение индекса элемента (IndexOf)\n8) Перевернуть массив (Reverse)\n9) Изменить размер массива (Resize)\n10) Сортировать массив (Sort)");
        }
        else {
            Console.WriteLine("\n\n\n\n0) Назад \n1) Создать массив\n");
        }
        return Convert.ToInt32(Console.ReadLine());
    }

    public string[] CreateArray()
    {
        Console.WriteLine("Создан массив вида {'AA', 'AB', 'AC', 'BD', 'WE', 'DF'}");
        string[] a = {"RT", "AA", "AB", "AC", "BD", "WE", "DF" };
        return a;
    }

    public void GetCount(string[] arr)
    {
        Console.WriteLine($"Количество элементов в коллекции {arr.Length}");
    }

    public void MakeBinSearch(string[] arr)
    {
        Console.Write("Введите элемент, который требуется найти: ");
        string needStr = Console.ReadLine();
        string[] array2 = new string[arr.Length];
        Array.Copy(arr, array2, arr.Length);
        Array.Sort(array2);
        int index = Array.BinarySearch(array2, needStr);
        if (index < 0)
        {
            Console.WriteLine("Элемент не найден");
        }
        else
        {
            Console.WriteLine($"Индекс элемента: {index}");
        }
    }

    public void ShowArray(string[] array)
    {
        foreach (var e in array)
        {
            Console.Write($" {e}");
        }
        Console.WriteLine();
    }

    public void MakeCopy(string[] array)
    {
        string[] array2 = new string[array.Length];
        Array.Copy(array, array2, array.Length);
        Console.WriteLine("Коллекция скопирована, копия: ");
        ShowArray(array2);
    }

    public void MakeFind(string[] array)
    {
        Console.Write("Введите подстроку, для нахожения первого элемента массива, который ее содержит: ");
        string needStr = Console.ReadLine();
        try
        {
            string elem = Array.Find(array, x => x.Contains(needStr));
            Console.WriteLine($"Найденая строка: {elem}");
        }
        catch (ArgumentNullException)
        {
            Console.WriteLine("Элемент не найден");
        }
    }

    public void MakeFindLast(string[] array)
    {
        Console.Write("Введите подстроку, для нахожения последнего элемента массива, который ее содержит: ");
        string needStr = Console.ReadLine();
        try
        {
            string elem = Array.FindLast(array, x => x.Contains(needStr));
            Console.WriteLine($"Найденая строка: {elem}");
        }
        catch (ArgumentNullException)
        {
            Console.WriteLine("Элемент не найден");
        }
    }

    public void MakeIndexOf(string[] array) {
        Console.Write("Введите элемент, который требуется найти: ");
        string needStr = Console.ReadLine();
        int index = Array.IndexOf(array, needStr);
        if (index < 0)
        {
            Console.WriteLine("Элемент не найден");
        }
        else
        {
            Console.WriteLine($"Индекс элемента: {index}");
        }
    }
    public void MakeReverse(string[] array) {
        string[] array2 = new string[array.Length];
        Array.Copy(array, array2, array.Length);
        Array.Reverse(array2);
        Console.WriteLine("Перевернутый массив выглядит так: ");
        ShowArray(array);
    }

    public void MakeResize(string[] array) {
        Console.WriteLine("Новый размер массива: ");
        int new_size = Convert.ToInt32(Console.ReadLine());
        string[] array2 = new string[array.Length];
        Array.Copy(array, array2, array.Length);
        Array.Resize(ref array2, new_size);
        Console.WriteLine($"Массив длинны {new_size} выглядит так: ");
        ShowArray(array2);
    }

    public void MakeSort(string[] array) {
        string[] array2 = new string[array.Length];
        Array.Copy(array, array2, array.Length);
        Array.Sort(array2);
        Console.WriteLine($"Сортированный массив выглядит так: ");
        ShowArray(array2);
    }
}

class ArrayListMenu {
    public int ShowMenu(bool array_list_created) {
        if (array_list_created)
        {
            Console.WriteLine("\n\n0) Назад\n1) Создать коллекцию\n2) Бинарный поиск (BinarySearch)\n3) Копирование(CopyTo)\n4) Нахождение индекса элемента (IndexOf)\n5) Вставить элемент (Insert)\n6) Перевернуть коллекцию (Reverse)\n7) Отсортировать коллекцию (Sort)\n8) Добавить строку в конец коллекции");
        }
        else {
            Console.WriteLine("\n\n0) Назад\n1) Создать коллекцию");
        }
        return Convert.ToInt32(Console.ReadLine());
    }
    public void ShowArrayList(ArrayList arr_list)
    {
        foreach (var e in arr_list)
        {
            Console.Write($" {e}");
        }
        Console.WriteLine();
    }

    public ArrayList CreateArrayList() {
        Console.WriteLine("Создана коллекция вида { \"AD\", 123, 0, 567, \"AE\" }");
        return new ArrayList() { "AD", "123", "0", "567", "AE" };
    }

    public void MakeBinSearch(ArrayList arr_list) {
        Console.Write("Введите элемент, который требуется найти: ");
        string needStr = Console.ReadLine();
        arr_list.Sort();
        Console.WriteLine("Коллекция отсортирована, теперь она выглядит так:");
        ShowArrayList(arr_list);
        int index = arr_list.BinarySearch(needStr);
        if (index < 0)
        {
            Console.WriteLine("Элемент не найден");
        }
        else
        {
            Console.WriteLine($"Индекс элемента: {index}");
        }
    }

    public void MakeCopyTo(ArrayList arr_list) {
        string[] arr = new string[arr_list.Count];
        arr_list.CopyTo(arr);
        Console.WriteLine("Коллекция скопирована в одномерный строковый массив, копия: ");
        foreach (var e in arr) { Console.Write($" {e}"); }
    }
    public void MakeIndexOf(ArrayList arr_list)
    {
        Console.Write("Введите элемент, который требуется найти: ");
        string needStr = Console.ReadLine();
        int index = arr_list.IndexOf(needStr);
        if (index < 0)
        {
            Console.WriteLine("Элемент не найден");
        }
        else
        {
            Console.WriteLine($"Индекс элемента: {index}");
        }
    }
    public ArrayList MakeInsert(ArrayList arr_list) {
        Console.WriteLine("Введите строку,которую требуется вставить: ");
        string need_str = Console.ReadLine();
        Console.Write("Индекс, на который нужно вставить строку: ");
        int need_index = Convert.ToInt32(Console.ReadLine());
        arr_list.Insert(need_index, need_str);
        Console.WriteLine("Обьект добавлен, теперь коллекция выглядит так: ");
        ShowArrayList(arr_list);
        return arr_list;
    }

    public ArrayList MakeReverse(ArrayList arr_list) {
        arr_list.Reverse();
        Console.WriteLine("Коллекция перевернута, теперь она выглядит так: ");
        ShowArrayList(arr_list);
        return arr_list;
    }

    public ArrayList MakeSort(ArrayList arr_list) {
        arr_list.Sort();
        Console.WriteLine("Коллекция отсортирована, теперь она выглядит так: ");
        ShowArrayList(arr_list);
        return arr_list;
    }

    public ArrayList MakeAdd(ArrayList arr_list)
    {
        Console.WriteLine("Введите строку,которую требуется вставить: ");
        string need_str = Console.ReadLine();
        arr_list.Add(need_str);
        Console.WriteLine("Обьект добавлен, теперь коллекция выглядит так: ");
        ShowArrayList(arr_list);
        return arr_list;
    }


}

class SortedListMenu {
    public int ShowMenu(bool sorted_list_created) {
        if (sorted_list_created)
        {
            Console.WriteLine("\n\n0) Назад\n1) Создать SortedList\n2) Добавить элемент (Add)\n3) Найти индекс ключа (IndexOfKey)\n4) Найти индекс значения (IndexOfValue)\n5) Вывод ключа по индексу\n6) Вывод значения по индексу");
        }
        else {
            Console.WriteLine("\n\n0) Назад\n1) Создать SortedList");
        }
        return Convert.ToInt32(Console.ReadLine());
    }

    public SortedList CreateSortedList() {
        Console.WriteLine("Создан SortedList вида: {'key1': 'AA', 'key2': 'BA', 'key3': 'WA'}");
        SortedList sort_list = new SortedList();
        sort_list.Add("key1", "AA");
        sort_list.Add("key2", "BA");
        sort_list.Add("key3", "WA");
        return sort_list;
    }

    public void ShowSortedList(SortedList sort_list) {
        foreach (var e in sort_list.GetKeyList()) {
            Console.WriteLine($"{e}: {sort_list[e]}");
        }
    }

    public SortedList MakeAdd(SortedList sort_list) {
        Console.WriteLine("Введите ключ элемента: ");
        string need_key = Console.ReadLine();
        Console.WriteLine("Введите значение элемента ");
        string need_value = Console.ReadLine();
        sort_list.Add(need_key, need_value);
        Console.WriteLine("Элемент добавлен, теперь SortedList выглядит так: ");
        ShowSortedList(sort_list);
        return sort_list;
    }

    public void MakeIndexOfKey(SortedList sort_list) {
        Console.WriteLine("Введите ключ, индекс которого нужно найти: ");
        string need_key = Console.ReadLine();
        int index = sort_list.IndexOfKey(need_key);
        if (index < 0) { Console.WriteLine("Ключ не найден"); }
        else { Console.WriteLine($"Индекс ключа: {index}"); }
    }
    public void MakeIndexOfValue(SortedList sort_list)
    {
        Console.WriteLine("Введите значение, индекс которого нужно найти: ");
        string need_value = Console.ReadLine();
        int index = sort_list.IndexOfValue(need_value);
        if (index < 0) { Console.WriteLine("Значение не найдено"); }
        else { Console.WriteLine($"Индекс значения: {index}"); }
    }

    public void GetKeyByIndex(SortedList sort_list) {
        Console.WriteLine("Индекс ключа: ");
        int index = Convert.ToInt32(Console.ReadLine());
        try
        {
            string key = Convert.ToString(sort_list.GetKeyList()[index]);
            Console.WriteLine($"Найден ключ: {key}");
        }
        catch (ArgumentOutOfRangeException) {
            Console.WriteLine("Неверный индекс");
        }
    }

    public void GetValueByIndex(SortedList sort_list)
    {
        Console.WriteLine("Индекс значения: ");
        int index = Convert.ToInt32(Console.ReadLine());
        try
        {
            string value = Convert.ToString(sort_list.GetValueList()[index]);
            Console.WriteLine($"Найдено значение: {value}");
        }
        catch (ArgumentOutOfRangeException)
        {
            Console.WriteLine("Неверный индекс");
        }
    }

}

class Program
{
    static void Main()
    {
        MainMenu main_menu = new MainMenu();
        ArrayMenu array_menu = new ArrayMenu();
        ArrayListMenu arrlist_menu = new ArrayListMenu();
        SortedListMenu sortlist_menu = new SortedListMenu();
        int c = -1;
        int main_c = -1;
        string[] array = new string[0];
        ArrayList arr_list = new ArrayList();
        SortedList sort_list = new SortedList();
        bool array_created = false;
        bool array_list_created = false;
        bool sorted_list_created = false;
        while (main_c != 0)
        {
            main_c = main_menu.ShowMenu();
            c = -1;
            if (main_c == 1)
            {
                //run ArrayMenu
                while (c != 0)
                {
                    c = array_menu.ShowMenu(array_created);
                    if (c == 1)
                    {
                        array = array_menu.CreateArray();
                        array_created = true;
                    }
                    if (c == 2)
                    {
                        array_menu.GetCount(array);
                    }
                    if (c == 3)
                    {
                        array_menu.MakeBinSearch(array);
                    }
                    if (c == 4)
                    {
                        array_menu.MakeCopy(array);
                    }
                    if (c == 5)
                    {
                        array_menu.MakeFind(array);
                    }
                    if (c == 6)
                    {
                        array_menu.MakeFindLast(array);
                    }
                    if (c == 7)
                    {
                        array_menu.MakeIndexOf(array);
                    }
                    if (c == 8)
                    {
                        array_menu.MakeReverse(array);
                    }
                    if (c == 9)
                    {
                        array_menu.MakeResize(array);
                    }
                    if (c == 10)
                    {
                        array_menu.MakeSort(array);
                    }

                }
            }
            if (main_c == 2) {
                //run ArrayListMenu
                while (c != 0) {
                    c = arrlist_menu.ShowMenu(array_list_created);
                    if (c == 1) {
                        arr_list = arrlist_menu.CreateArrayList();
                        array_list_created = true;
                    }
                    if (c == 2) {
                        arrlist_menu.MakeBinSearch(arr_list);
                    }
                    if (c == 3) {
                        arrlist_menu.MakeCopyTo(arr_list);
                    }
                    if (c == 4) {
                        arrlist_menu.MakeIndexOf(arr_list);
                    }
                    if (c == 5) {
                        arr_list = arrlist_menu.MakeInsert(arr_list);
                    }
                    if (c == 6)
                    {
                        arr_list = arrlist_menu.MakeReverse(arr_list);
                    }
                    if (c == 7) {
                        arr_list = arrlist_menu.MakeSort(arr_list);
                    }
                    if (c == 8) {
                        arr_list = arrlist_menu.MakeAdd(arr_list);
                    }

                }
            }
            if (main_c == 3) {
                //run SortedListMenu
                while (c != 0) {
                    c = sortlist_menu.ShowMenu(sorted_list_created);

                    if (c == 1) {
                        sort_list = sortlist_menu.CreateSortedList();
                        sorted_list_created = true;
                    }

                    if (c == 2) {
                        sort_list = sortlist_menu.MakeAdd(sort_list);
                    }
                    if (c == 3) {
                        sortlist_menu.MakeIndexOfKey(sort_list);
                    }
                    if (c == 4) {
                        sortlist_menu.MakeIndexOfValue(sort_list);
                    }
                    if (c == 5) {
                        sortlist_menu.GetKeyByIndex(sort_list);
                    }
                    if (c == 6) {
                        sortlist_menu.GetValueByIndex(sort_list);
                    }

                }
            }

        }
    }
}
