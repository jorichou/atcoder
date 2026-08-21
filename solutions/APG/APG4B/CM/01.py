#include <algorithm>
#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
using namespace std;
#define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
#define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int main() {
    int a, b;
    cin >> a >> b;

    cout << "A:";
    while (a > 0) {
        cout << "]";
        a--;
    }
    cout << endl;
    
    cout << "B:";
    while (b > 0) {
        cout << "]";
        b--;
    }
    cout << endl;
}