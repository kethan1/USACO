#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    fstream input("hps.in", ios::in);
    
    vector<vector<int>> input_data;
    vector<vector<string>> permutations = {
        {"R", "P", "S"}, 
        {"R", "S", "P"},
        {"P", "R", "S"},
        {"P", "S", "R"},
        {"S", "R", "P"},
        {"S", "P", "R"}
    };
    input.ignore(numeric_limits<streamsize>::max(), '\n');

    for (string line; getline(input, line);) {
        vector<int> tokens;
        string token;

        for (const auto& c: line) {
            if (!isspace(c))
                token += c;
            else {
                if (token.length()) tokens.push_back(stoi(token));
                token.clear();
            }
        }

        if (token.length()) tokens.push_back(stoi(token));

        input_data.push_back(tokens);
    }
        
    vector<int> possibilites;
    for(const vector<string>& permutation: permutations) {
        int games_won = 0;
        for (const vector<int>& move: input_data) {
            string move1L = permutation[move[0] - 1];
            string move2L = permutation[move[1] - 1];
            if ((move1L == "R" && move2L == "S") || (move1L == "S" && move2L == "P") || (move1L == "P" && move2L == "R")) {
                games_won += 1;
            }
        }
        possibilites.push_back(games_won);
    }

    fstream MyFile("hps.out", ios::out);
    MyFile << *max_element(possibilites.begin(), possibilites.end()) << endl;
    MyFile.close();

    return 0;
}
