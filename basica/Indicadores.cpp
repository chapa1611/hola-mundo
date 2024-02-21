#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

struct Alumno {
  string nombre;
  int codigo;
  string notas[3];
  float promedio;
};

int main() {
  Alumno *primerAlumno;
  primerAlumno = new Alumno[3];
  for (int i = 0; i < 3; i++) {
    cout << "Alumno " << i + 1 << endl;
    cout << "Nombre: ";
    cin >> (primerAlumno + i)->nombre;
    cout << "Código: ";
    cin >> (primerAlumno + i)->codigo;

    float sumaNotas = 0;
    for (int j = 0; j < 3; j++) {
      cout << "Nota " << j + 1 << ": ";
      cin >> (primerAlumno + i)->notas[j];
      sumaNotas += stof((primerAlumno + i)->notas[j]);
    }
    (primerAlumno + i)->promedio = sumaNotas / 3;
  }

  cout << endl << "Resultados:" << endl;
  for (int i = 0; i < 3; i++) {
    cout << endl << "Alumno " << i + 1 << endl;
    cout << "Nombre: " << (primerAlumno + i)->nombre << endl;
    cout << "Código: " << (primerAlumno + i)->codigo << endl;
    cout << "Promedio: " << fixed << setprecision(2) << (primerAlumno + i)->promedio << endl;

    for (int j = 0; j < 3; j++) {
      cout << "Nota " << j + 1 << ": " << (primerAlumno + i)->notas[j] << endl;
    }
  }
  delete[] primerAlumno;
  return 0;
}
