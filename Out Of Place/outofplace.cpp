#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ifstream input_file("outofplace.in");

    string first_line;
    getline(input_file, first_line);

    vector<int> cows = {};

    for (string line; getline(input_file, line);) {
        cows.push_back(stoi(line));
    }
    input_file.close();

    int swaps = -1;
    vector<int> cows_sorted(cows);

    sort(cows_sorted.begin(), cows_sorted.end());

    for (auto it(cows_sorted.begin()); it != cows_sorted.end(); it++) {
        if (*it != cows[distance(cows_sorted.begin(), it)]) {
            swaps++;
        }
    }

    ofstream output_file("outofplace.out");
    output_file << swaps << endl;
    output_file.close();

    return 0;
}
