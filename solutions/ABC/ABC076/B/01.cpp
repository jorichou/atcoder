#include <algorithm>
#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
using namespace std;
#define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
#define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int main() {
    int n, k;
    cin >> n >> k;
    int bord = 1;

    for (int i = 0; i < n; i++) {
        if (bord * 2 < bord + k) {
            bord *= 2;
        } else {
            bord += k;
        }
    }

    cout << bord << endl;
}