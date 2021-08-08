#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main() {
    fstream input("water.in", ios::in);
    fstream output("water.out", ios::out);

    for (string line; getline(input, line);) {
        output << round(2.0/3 * 3.14 * pow(stoi(line, 0, 2), 3) / 1000) << endl;
    }

    output.close();
    input.close();

    return 0;
}
