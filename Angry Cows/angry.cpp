#include <iostream>
#include <fstream>
#include <set>

using namespace std;

set<int> blast(set<int> &hay_bales, int bale_shot, int blast_radius = 1) {
    set<int> exploded;
    for (int hay_bale: hay_bales) {
        if (0 < abs(hay_bale - bale_shot) && abs(hay_bale - bale_shot) <= blast_radius) {
            exploded.insert(hay_bale);
        }
    }
    for (int hay_bale_exploded: exploded) {
        set<int> bale_chain_reaction;
        for (int hay_bale2: hay_bales) {
            if (!exploded.count(hay_bale2) && hay_bale2 != bale_shot) {
                bale_chain_reaction.insert(hay_bale2);
            }
        }
        set<int> reaction = blast(bale_chain_reaction, hay_bale_exploded, blast_radius + 1);
        exploded.insert(reaction.begin(), reaction.end());
    }

    return exploded;
}

int main() {
    ios_base::sync_with_stdio(false);
    
    fstream input("angry.in", ios::in);
    set<int> hay_bales;

    string line;
    getline(input, line);

    for (string line; getline(input, line);) {
        hay_bales.insert(stoi(line));
    }
    input.close();

    int max_size = 0;

    for (int bale_shot: hay_bales) {
        set<int> chain_reaction_output = blast(hay_bales, bale_shot);
        chain_reaction_output.insert(bale_shot);
        max_size = max(max_size, int(chain_reaction_output.size()));
    }

    fstream MyFile("angry.out", ios::out);
    MyFile << max_size << endl;
    MyFile.close();

    return 0;
}
