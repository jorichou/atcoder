#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;
#define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
#define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int main() {
    int h, w;
    cin >> h >> w;
    vector<string> p(h);
    for (int i = 0; i < h; i++) {
        cin >> p.at(i);
    }

    for (int i = 0; i < w + 2; i++) {
        cout << '#';
    }

    cout << endl;

    for (int i = 0; i < h; i++) {
        cout << '#' << p.at(i) << '#' << endl;
    }

    for (int i = 0; i < w + 2; i++) {
        cout << '#';
    }

    cout << endl;
}