#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;
#define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
#define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int max_v;
    max_v = max(a, b);
    max_v = max(max_v, c);
    int min_v;
    min_v = min(a, b);
    min_v = min(min_v, c);

    cout << max_v - min_v << endl;
}