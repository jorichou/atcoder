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
    int max;

    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        int two = 0;
        while (a % 2 == 0) {
            a /= 2;
            two += 1;
        }
        if (i == 0) {
            max = two;
        } else {
            if (two < max) {
                max = two;
            }
        }
    }

    cout << max << endl;
}