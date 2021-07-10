#include <iostream>
#include <fstream>
#include <set>

using namespace std;

set<int> blast(set<int> hay_bales, int bale_shot, int blast_radius = 1) {
    set<int> exploded;
    for (auto hay_bale = hay_bales.begin(); hay_bale != hay_bales.end(); hay_bale++) {
        if (0 < abs(*hay_bale - bale_shot) && abs(*hay_bale - bale_shot) <= blast_radius) {
            exploded.insert(*hay_bale);
        }
    }
    for (auto hay_bale_exploded = exploded.begin(); hay_bale_exploded != exploded.end(); hay_bale_exploded++) {
        set<int> bale_chain_reaction;
        for (auto hay_bale2 = hay_bales.begin(); hay_bale2 != hay_bales.end(); hay_bale2++) {
            if (!(exploded.count(*hay_bale2)) || *hay_bale2 == bale_shot) {
                bale_chain_reaction.insert(*hay_bale2);
            }
        }
        set<int> reaction = blast(bale_chain_reaction, *hay_bale_exploded, blast_radius + 1);
        exploded.insert(reaction.begin(), reaction.end());
    }

    return exploded;
}

int main() {
    fstream input("angry.in", ios::in);
    int N;
    set<int> g1;

    string line;
    getline(input, line);

    for (string line; getline(input, line);) {
        g1.insert(stoi(line));
        cout << line << " ";
    }
    cout << endl;
    input.close();

    for (auto const &bale : g1) {
        cout << bale << " ";
    }
    cout << endl;

    set<int> output_of_cow_shot;

    for (auto it = g1.begin(); it != g1.end(); it++) {
        set<int> chain_reaction_output = blast(g1, *it);
        chain_reaction_output.insert(*it);
        output_of_cow_shot.insert(chain_reaction_output.size());
    }

    fstream MyFile("angry.out", ios::out);
    MyFile << *output_of_cow_shot.rbegin() << endl;
    MyFile.close();

    return 0;
}
