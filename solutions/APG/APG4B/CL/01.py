#include <algorithm>
#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
using namespace std;
#define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
#define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int main() {
    int n, a;
    cin >> n >> a;
    for (int i = 0; i < n; i++) {
        string op;
        int b;
        cin >> op >> b;
        if (op == "+") {
            a += b;
        } else if (op == "-") {
            a -= b;
        } else if (op == "*") {
            a *= b;
        } else if (op == "/") {
            if (b == 0) {
                cout << "error" << endl;
                break;
            } else {
                a /= b;
            }
        }
        cout << i + 1 << ":" << a << endl;
    }
}