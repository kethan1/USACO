#include <map>
#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>

std::map<int, int> shells = {
    {1, 0},
    {2, 0},
    {3, 0}
};

std::vector<int> correct_guesses = {0, 0, 0};

int main() {
    std::ifstream input("shell.in");
    
    std::string line;
    std::getline(input, line);

    std::vector<std::vector<int>> switches_and_guesses = {};

    for (std::string line; getline(input, line);) {
        std::vector<int> tokens;
        std::string token;

        for (const auto& c: line) {
            if (!isspace(c))
                token += c;
            else {
                if (token.length()) tokens.push_back(stoi(token));
                token.clear();
            }
        }

        if (token.length()) tokens.push_back(stoi(token));

        switches_and_guesses.push_back(tokens);
    }

    for (int shell_start = 1; shell_start < 4; shell_start++) {
        shells[shell_start] = 1;

        for (std::vector<int> &move: switches_and_guesses) {
            std::swap(shells.at(move[0]), shells.at(move[1]));
            correct_guesses[shell_start - 1] += shells[move[2]];
        }

        shells = {
            {1, 0},
            {2, 0},
            {3, 0}
        };
    }

    input.close();
    std::ofstream output("shell.out");
    output << *std::max_element(correct_guesses.begin(), correct_guesses.end()) << std::endl;
    output.close();

    return 0;
}
