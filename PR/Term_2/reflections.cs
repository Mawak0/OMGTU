using System.Reflection;
string assemblyFile = "C:/Users/user/Downloads/core.dll";
System.Reflection.Assembly assem = Assembly.LoadFrom(assemblyFile);
Type[] types = assem.GetTypes();
foreach (Type t in types){
    Console.WriteLine("--------------------------------------");
    if (t.IsClass){Console.WriteLine($"Класс: {t.FullName}");}
    else if (t.IsInterface) {Console.WriteLine($"Интерфейс: {t.FullName}");}
    if (t.BaseType == typeof(System.Attribute)){Console.WriteLine("Является атрибутом");}
    if (t.IsInterface || t.IsClass){
        System.Reflection.MethodInfo[] methods = t.GetMethods();
        Console.WriteLine("Список публичных методов: ");
        foreach (System.Reflection.MethodInfo m in methods){
            System.Reflection.ParameterInfo[] parametres = m.GetParameters();
            Console.WriteLine($"Имя: {m.Name}, тип возвращаемого значения: {m.ReturnType}");
            Console.WriteLine("Формальные параметры: ");
            foreach (System.Reflection.ParameterInfo p in parametres){
                Console.WriteLine($"{p.ParameterType} {p.Name}");
            }
        }
    }
}
