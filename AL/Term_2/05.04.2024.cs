/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
using System;

class Auto{
    public bool dirty;
    public Auto(){
        dirty = true;
    }
}

class Garage{
    public Auto[] cars;
    public Garage(){
        cars = new Auto[3];
    }
}

class Moika{
    public Auto MakeClean(Auto a){
        a.dirty = false;
        return a;
    }
}

class HelloWorld {
    delegate Auto dirtyless(Auto a);
  static void Main() {
    Garage g1 = new Garage();
    g1.cars[0] = new Auto();
    g1.cars[1] = new Auto();
    g1.cars[2] = new Auto();
    Moika m = new Moika();

    dirtyless cleaner1 = m.MakeClean;
    g1.cars[0] = cleaner1(g1.cars[0]);
    g1.cars[1] = cleaner1(g1.cars[1]);
    g1.cars[2] = cleaner1(g1.cars[2]);
    Console.WriteLine("Помыто!");
  }
}
