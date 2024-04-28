using Newtonsoft.Json;
using System;
using System.IO;

class Student{
    public string Name;
    public string Group;
    public string Discipline;
    public int mark;
}

class Task{
    public string taskName;
    public Student[] data;
}

class ResponseDataType1{
    public string Cadet;
    public int GPA;
    public ResponseDataType1(string Cadet, int GPA){
        this.Cadet = Cadet;
        this.GPA = GPA;
    }
}

class ResponseDataType2{
    public Dictionary<string, double> data;
    public ResponseDataType2(Dictionary<string, double> data){
        this.data = data;
    }
}

class ResponseDataType3{
    public string Discipline;
    public string Group;
    public double GPA;
}

class ResponseData<T>{
    public T[] Response;
    public ResponseData(int len){
        Response = new T[len];
    }
}

static void WriteResponse<ResponseType>(string path, ResponseData<ResponseType> Response){
    StreamWriter writer = new StreamWriter(path);
    string json = JsonConvert.SerializeObject(Response);
    writer.Write(json);
    writer.Close();
}

static Task ReadTask(string path){
    StreamReader reader = new StreamReader(path);
    string json = reader.ReadToEnd();
    reader.Close();
    Task task = JsonConvert.DeserializeObject<Task>(json);
    return task;
}







//Task task = ReadTask("input1.json");
//Console.WriteLine(task.data[0].Name);

//ResponseData<ResponseDataType1> r1 = new ResponseData<ResponseDataType1>(1);
//r1.Response[0] = new ResponseDataType1("User1", 5);
//WriteResponse<ResponseDataType1>("output1.json", r1)

ResponseData<Dictionary<string, int>> r2 = new ResponseData<Dictionary<string, int>>(2);
Dictionary<string, int> d1 = new Dictionary<string, int>(1);
d1.Add("Math", 5);
r2.Response[0] = d1;
Dictionary<string, int> d2 = new Dictionary<string, int>(1);
d2.Add("SomeLesson", 3);
r2.Response[1] = d2;
WriteResponse<Dictionary<string, int>>("output1.json", r2)

