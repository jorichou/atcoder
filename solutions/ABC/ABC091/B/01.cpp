#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;
#define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
#define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int main() {
    int n, m;
    cin >> n;
    vector<string> brue(n);

    for (int i = 0; i < n; i++) {
        cin >> brue.at(i);
    }

    cin >> m;
    vector<string> red(m);
    for (int i = 0; i < m; i++) {
        cin >> red.at(i);
    }

    
    int max = 0;
    for (int i = 0; i < n; i++) {
        string t = brue.at(i);
        int count = 0;
        // 青カード
        for (int j = 0; j < n; j++) {
            if (brue.at(j) == t) {
                count++;
            }
        }
        for (int j = 0; j < m; j++) {
            if (red.at(j) == t) {
                count--;
            }
        }
        if (count > max) {
            max = count;
        }
        
    }

    if (max > 0) {
        cout << max << endl;
    } else {
        cout << 0 << endl;
    }
}