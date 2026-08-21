#include <algorithm>
#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
using namespace std;
#define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
#define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int main() {
    string s;
    cin >> s;
    int ans = 1;
    for (int i = 1; i < s.size(); i += 2) {
        if (s.at(i) == '+') {
            ans++;
        } else if (s.at(i) == '-') {
            ans--;
        }
    }

    cout << ans << endl;
}