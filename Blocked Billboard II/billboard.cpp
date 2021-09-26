#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main() {
    ifstream input_file("billboard.in");

    int n = 0;
    int lawn_x1, lawn_y1, lawn_x2, lawn_y2, feed_x1, feed_y1, feed_x2, feed_y2;
    for (string line; getline(input_file, line);) {
        vector<int> tokens;
        string token;

        for (const char& c: line) {
            if (!isspace(c))
                token += c;
            else {
                if (token.length()) tokens.push_back(stoi(token));
                token.clear();
            }
        }

        if (token.length()) tokens.push_back(stoi(token));
        if (n == 0) {
            lawn_x1 = tokens[0];
            lawn_y1 = tokens[1];
            lawn_x2 = tokens[2];
            lawn_y2 = tokens[3];
            n++;
        } else {
            feed_x1 = tokens[0];
            feed_y1 = tokens[1];
            feed_x2 = tokens[2];
            feed_y2 = tokens[3];
        }
    }
    input_file.close();

    int tarp_size = (lawn_x2 - lawn_x1) * (lawn_y2 - lawn_y1);

    if (feed_x1 <= lawn_x1 && lawn_x2 <= feed_x2) {
        if (feed_y1 <= lawn_y1 && feed_y2 >= lawn_y2) {
            tarp_size = 0;
        }
        else if ((lawn_y1 <= feed_y2 && feed_y2 <= lawn_y2) && !(lawn_y1 <= feed_y1 && feed_y1 <= lawn_y2)) {
            tarp_size -= (feed_y2 - lawn_y1) * (lawn_x2 - lawn_x1);
        }
        else if ((lawn_y1 <= feed_y1 && feed_y1 <= lawn_y2) && !(lawn_y1 <= feed_y2 && feed_y2 <= lawn_y2)) {
            tarp_size -= (lawn_y2 - feed_y1) * (lawn_x2 - lawn_x1);
        }
    }

    else if (feed_y1 <= lawn_y1 && lawn_y2 <= feed_y2) {
        if ((lawn_x1 <= feed_x2 && feed_x2 <= lawn_x2) && !(lawn_x1 <= feed_x1 && feed_x1 <= lawn_x2)) {
            tarp_size -= (feed_x2 - lawn_x1) * (lawn_y2 - lawn_y1);
        }
        else if ((lawn_x1 <= feed_x1 && feed_x1 <= lawn_x2) && !(lawn_x1 <= feed_x2 && feed_x2 <= lawn_x2)) {
            tarp_size -= (lawn_x2 - feed_x1) * (lawn_y2 - lawn_y1);
        }
    }

    ofstream output_file("billboard.out");
    output_file << tarp_size << endl;
    output_file.close();

    return 0;
}
