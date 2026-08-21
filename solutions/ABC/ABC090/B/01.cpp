#include <algorithm>
#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
using namespace std;
#define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
#define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int main() {
    int a, b;
    int i;
    cin >> a >> b;
    int total = 0;

    for (i = a; i <= b; i++) {
        int n = i;
        int n1 = n / 10000;
        n -= n1 * 10000;
        int n2 = n / 1000;
        n -= n2 * 1000;
        int n3 = n / 100;
        n -= n3 * 100;
        int n4 = n / 10;
        n -= n4 * 10;

        if ((n1 == n) && (n2 == n4)) {
            total++;
        }
    }

    cout << total << endl;
}