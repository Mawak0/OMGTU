using Newtonsoft.Json;
using System;
using System.IO;

class MarkData{
    public string Name;
    public string Group;
    public string Discipline;
    public int Mark;
}

class Task{
    public string taskName;
    public MarkData[] data;
}

class ResponseDataType1{
    public string Cadet;
    public double GPA;
    public ResponseDataType1(string Cadet, double GPA){
        this.Cadet = Cadet;
        this.GPA = GPA;
    }
}

class ResponseDataType3{
    public string Discipline;
    public string Group;
    public double GPA;
}

class ResponseData<T>{
    public List<T> Response = new List<T>();
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

static void DoTask(string input_path, string output_path){
    Task task = ReadTask(input_path);
    if (task.taskName == "GetStudentsWithHighestGPA"){
        var marks_by_student = from m_data in task.data group m_data by m_data.Name;
        var students_GPA = from student_marks in marks_by_student select new {Name = student_marks.Key, GPA = (student_marks.Sum(x => (double)x.Mark))/student_marks.Count()};
        var max_GPA = students_GPA.Max(x => x.GPA);
        var students_with_max_GPA = from student_GPA in students_GPA where (student_GPA.GPA == max_GPA) select student_GPA;
        ResponseData<ResponseDataType1> r1 = new ResponseData<ResponseDataType1>();
        foreach (var e in students_with_max_GPA){
            r1.Response.Add(new ResponseDataType1(e.Name, e.GPA));
        }
        WriteResponse<ResponseDataType1>(output_path, r1);
    }
    else if (task.taskName == "CalculateGPAByDiscipline"){
        var marks_by_discipline = from m_data in task.data group m_data by m_data.Discipline;
        var disciplines_GPA = from discipline in marks_by_discipline select new {Discipline=discipline.Key, GPA=(discipline.Sum(x => (double)x.Mark)/discipline.Count())};
        ResponseData<Dictionary<string, double>> r2 = new ResponseData<Dictionary<string, double>>();
        foreach (var discipline in disciplines_GPA){
            r2.Response.Add(new Dictionary<string, double>() {{discipline.Discipline, discipline.GPA}});
        }

        WriteResponse<Dictionary<string, double>>(output_path, r2);
    }
    else if (task.taskName == "GetBestGroupsByDiscipline"){
        
    }
}



DoTask("input1.json", "output1.json");









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

