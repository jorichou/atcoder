#include <algorithm>
#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
using namespace std;
#define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
#define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int main() {
    int n;
    string s;
    bool f = false;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> s;
        if (s == "Y") {
            f = true;
            break;
        }
    }

    if (f) {
        cout << "Four" << endl;
    } else {
        cout << "Three" << endl;
    }
}