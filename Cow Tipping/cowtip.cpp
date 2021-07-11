#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void cow_tipper(vector<int> pos1, vector<int> pos2, vector<vector<int>> &cows) {
    for (int index = pos1[0]; index < pos2[0] + 1; index++) {
        for (int index2 = pos1[1]; index2 < pos2[1] + 1; index2++) {
            if (cows[index][index2] == 1) {
                cows[index][index2] = 0;
            } else {
                cows[index][index2] = 1;
            }
        }
    }
}
    

int main() {
    fstream input("cowtip.in", ios::in);

    string line;
    getline(input, line);
    int cows_length = stoi(line) - 1;

    vector<vector<int>> cows;

    for (string line; getline(input, line);) {
        vector<int> current_line = {};
        for (char ch: line) {
            current_line.push_back((int)ch);
        }
    }
    
    input.close();

    int cow_tippers_used = 0;
    for (int index = cows_length; index < -1; index--) {
        int cows_sublist_length = cows[index].size() - 1;
        for (int index2 = cows_sublist_length; index2 < -1; index2--) {
            if (cows[index][index2] == 1) {
                cow_tipper({0, 0}, {index, index2}, cows);
                cow_tippers_used += 1;
            }
        }
    }

    fstream output("cowtip.out", ios::out);
    output << cow_tippers_used << endl;
    output.close();
}
