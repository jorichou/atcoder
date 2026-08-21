#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
using namespace std;
#define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
#define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int main() {
    string a, b;
    cin >> a >> b;
    if (a.size() < b.size()) {
        cout << b << endl;
    } else {
        cout << a << endl;
    }
}