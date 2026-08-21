#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
using namespace std;
#define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
#define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int main() {
    string s;
    cin >> s;
    int l = s.size();
    if (s[l - 1] == 'T') {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}