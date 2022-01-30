#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ifstream input("guess.in");
    string line;
    getline(input, line);

    vector<vector<string>> characteristics = {};

    for (string line; getline(input, line);) {
        vector<string> tokens;
        string token;

        int i = 0;

        for (const auto& c: line) {
            if (!isspace(c))
                token += c;
            else {
                if (i < 2) {
                    if (token.length()) tokens.push_back(token);
                    i++;
                }
                token.clear();
            }
        }

        if (token.length()) tokens.push_back(token);

        characteristics.push_back(tokens);
    }
    input.close();

    int most_shared = 0;
    for (int i = 0; i < characteristics.size(); i++) {
        for (int j = 0; j < characteristics.size(); j++) {
            if (i != j) {            
                // Sort the vector
                sort(characteristics[i].begin(), characteristics[i].end());
                sort(characteristics[j].begin(), characteristics[j].end());
                
                // Initialise a vector
                // to store the common values
                // and an iterator
                // to traverse this vector
                vector<int> v(characteristics[i].size() + characteristics[j].size());
                vector<int>::iterator it, st;
            
                it = set_intersection(characteristics[i].begin(),
                                          characteristics[i].end(),
                                          characteristics[j].begin(),
                                          characteristics[j].end(),
                                          v.begin());

                int z = 0;
                for (st = v.begin(); st != it; ++st)
                    z++;
                most_shared = max(z, most_shared);
            }
        }
    }

    ofstream output("guess.out");
    output << most_shared + 1 << endl;
    output.close();

    return 0;
}
