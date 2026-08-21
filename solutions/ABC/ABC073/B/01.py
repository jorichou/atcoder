#include <algorithm>
#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
using namespace std;
#define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
#define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int main() {
    int n;
    cin >> n;
    int l, r;
    int total = 0;

    for (int i = 0; i < n; i++) {
        cin >> l >> r;
        total += r - l + 1;
    }

    cout << total << endl;
}