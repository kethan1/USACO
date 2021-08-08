#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>

using namespace std;

set<int> blast(set<int> hay_bales, int bale_shot, int blast_radius = 1) {
    set<int> exploded;
    for (int hay_bale: hay_bales) {
        if (0 < abs(hay_bale - bale_shot) && abs(hay_bale - bale_shot) <= blast_radius) {
            exploded.insert(hay_bale);
        }
    }
    for (int hay_bale_exploded: exploded) {
        set<int> bale_chain_reaction;
        for (int hay_bale2: hay_bales) {
            if (exploded.count(hay_bale2) == 0 && hay_bale2 != bale_shot) {
                bale_chain_reaction.insert(hay_bale2);
            }
        }
        set<int> reaction = blast(bale_chain_reaction, hay_bale_exploded, blast_radius + 1);
        exploded.insert(reaction.begin(), reaction.end());
    }

    return exploded;
}

int main() {
    fstream input("angry.in", ios::in);
    set<int> g1;

    string line;
    getline(input, line);

    for (string line; getline(input, line);) {
        g1.insert(stoi(line));
    }
    input.close();

    int max_size = 0;

    for (int cow: g1) {
        set<int> chain_reaction_output = blast(g1, cow);
        chain_reaction_output.insert(cow);
        max_size = max(max_size, int(chain_reaction_output.size()));
    }

    fstream MyFile("angry.out", ios::out);
    MyFile << max_size << endl;
    MyFile.close();

    return 0;
}
