#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;
#define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
#define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int main() {
    int n;
    cin >> n;
    vector<int> d(n);
    for (int i = 0; i < n; i++) {
        cin >> d.at(i);
    }

    sort(d.begin(), d.end());

    int count = 1;
    for (int i = 1; i < n; i++) {
        if (d.at(i - 1) == d.at(i)) continue;
        count++;
    }
    cout << count << endl;
}