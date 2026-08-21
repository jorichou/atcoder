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
    int total = 0;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (x < k - x) {
            total += x;
        } else {
            total += k - x;
        }
    }

    cout << total * 2 << endl;
}