#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void cow_tipper(int pos2_x, int pos2_y, vector<vector<int>> &cows) {
    for (int index = 0; index < pos2_x + 1; index++) {
        for (int index2 = 0; index2 < pos2_y + 1; index2++) {
            cows[index][index2] = 1 - cows[index][index2];  // flips the cow (converts 1 to 0 and 0 to 1)
        }
    }
}


int main() {
    ifstream input("cowtip.in");

    string first_line;
    getline(input, first_line);

    vector<vector<int>> cows;

    for (string line; getline(input, line);) {
        vector<int> current_line = {};
        for (char &ch: line) {
            current_line.push_back(ch - '0');  // converts char to int and pushes it to the vector
        }
        cows.push_back(current_line);
    }
    input.close();

    int cow_tippers_used = 0;
    for (int index = stoi(first_line) - 1; index > -1; index--) {
        for (int index2 = cows[index].size() - 1; index2 > -1; index2--) {
            if (cows[index][index2] == 1) {
                cow_tipper(index, index2, cows);
                cow_tippers_used += 1;
            }
        }
    }

    ofstream output("cowtip.out");
    output << cow_tippers_used << endl;
    output.close();
}
