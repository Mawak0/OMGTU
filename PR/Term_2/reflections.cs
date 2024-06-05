using System.Reflection;
using System.Linq;
string assemblyFile = "C:/Users/user/Downloads/core.dll";
System.Reflection.Assembly assem = Assembly.LoadFrom(assemblyFile);
Type[] types = assem.GetTypes();
var interface_types = from t in types where t.IsInterface select new {name=t.FullName, attribute=(t.BaseType == typeof(System.Attribute)),  methods=from m in t.GetMethods() select new {m_name=m.Name, m_return=m.ReturnType, m_params=m.GetParameters()}};
var class_types = from t in types where t.IsClass select new {name=t.FullName, attribute=(t.BaseType == typeof(System.Attribute)), methods=from m in t.GetMethods() select new {m_name=m.Name, m_return=m.ReturnType, m_params=m.GetParameters()}};

Console.WriteLine("Интерфейсы: ");
foreach (var i in interface_types){
    Console.WriteLine("-------------------------------------");
    Console.WriteLine($"Имя интерфейса: {i.name}");
    if (i.attribute){Console.WriteLine("Является атрибутом");}
    Console.WriteLine("Список публичных методов: ");
    foreach (var m in i.methods){
        Console.WriteLine($"Имя: {m.m_name}, тип возвращаемого значения: {m.m_return}");
        Console.WriteLine("Формальные параметры: ");
        foreach (var p in m.m_params){
            Console.WriteLine($"{p.ParameterType} {p.Name}");
        }
    }
}


Console.WriteLine("Классы: ");
foreach (var i in class_types){
    Console.WriteLine("-------------------------------------");
    Console.WriteLine($"Имя класса: {i.name}");
    if (i.attribute){Console.WriteLine("Является атрибутом");}
    Console.WriteLine("Список публичных методов: ");
    foreach (var m in i.methods){
        Console.WriteLine($"Имя: {m.m_name}, тип возвращаемого значения: {m.m_return}");
        Console.WriteLine("Формальные параметры: ");
        foreach (var p in m.m_params){
            Console.WriteLine($"{p.ParameterType} {p.Name}");
        }
    }
}
