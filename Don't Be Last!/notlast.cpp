#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    fstream input("notlast.in", ios::in);
    int N;

    std::map<string, int> input_data = {
        {"Bessie", 0},
        {"Elsie", 0},
        {"Daisy", 0},
        {"Gertie", 0},
        {"Annabelle", 0},
        {"Maggie", 0},
        {"Henrietta", 0}
    };

    string line;
    getline(input, line);

    for (string line; getline(input, line);) {
        vector<string> tokens;
        string token;

        for (const auto& c: line) {
            if (!isspace(c))
                token += c;
            else {
                if (token.length()) tokens.push_back(token);
                token.clear();
            }
        }

        if (token.length()) tokens.push_back(token);
        input_data[tokens[0]] += stoi(token);
    }
    input.close();

    set<int> input_dct_values;
    for (auto const& data: input_data)
        input_dct_values.insert(data.second);

    vector<int> input_dct_values_repeat;
    for (auto const& data: input_data)
        input_dct_values_repeat.push_back(data.second);

    fstream output_file("notlast.out", ios::out);
    if (input_dct_values.size() > 1) {
        string cow_name;
        int min_value = *next(input_dct_values.begin(), 1);
        if (count(input_dct_values_repeat.begin(), input_dct_values_repeat.end(), min_value) > 1) {
            output_file << "Tie" << endl;
        } else {
            for (auto const& i: input_data) {
                if (i.second == min_value) {
                    cow_name = i.first;
                }
            }
            output_file << cow_name << endl;
        }
    } else {
        output_file << "Tie" << endl;
    }
    output_file.close();

    return 0;
}