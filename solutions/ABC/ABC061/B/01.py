#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;
#define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
#define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> c(n, 0);
    for (int i = 0; i < m; i++) {
        int city1, city2;
        cin >> city1;
        cin >> city2;
        c.at(city1 - 1)++;
        c.at(city2 - 1)++;
    }

    for (int i = 0; i < n; i++) {
        cout << c.at(i) << endl;
    }
}