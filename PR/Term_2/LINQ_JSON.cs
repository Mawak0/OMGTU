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
    public ResponseDataType3(string Discipline, string Group, double GPA){
        this.Discipline = Discipline;
        this.Group = Group;
        this.GPA = GPA;
    }
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
        var marks_by_discipline = from m_data in task.data group m_data by m_data.Discipline;
        var result = from data in marks_by_discipline select new {Discipline=data.Key, Groups_marks= (from d in data group d by d.Group into dd select new {Group=dd.Key, Average_mark=dd.Average(x => x.Mark)}).OrderByDescending(x => x.Average_mark).ToList()[0]};
        ResponseData<ResponseDataType3> r3 = new ResponseData<ResponseDataType3>();
        foreach (var r_data in result){
            r3.Response.Add(new ResponseDataType3(r_data.Discipline, r_data.Groups_marks.Group, r_data.Groups_marks.Average_mark));
        }
        WriteResponse<ResponseDataType3>(output_path, r3);
    }
}



DoTask("input3.json", "output3.json");

