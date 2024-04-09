#include <iostream>
#include <string>

using namespace std;

int main(){

    string nome = "";
    string sobreNome = "";

    cin >> nome;
    cin >> sobreNome;

    int tamanho = nome.size();
    
    cout << sobreNome << "," << nome[0] << "," << nome[tamanho-1] << endl;

    return 0;



}