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
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a.at(i);
    }
    vector<int> sorted_a(n);
    for (int i = 0; i < n; i++) {
        int max = 0;
        int index = 0;
        for (int j = 0; j < n; j++) {
            if (a.at(j) > max) {
                max = a.at(j);
                index = j;
            }
        }
        sorted_a.at(i) = max;
        a.at(index) = -1;
    }
    int allice = 0;
    int bob = 0;
    for (int i = 0; i < n; i++) {
        if (i % 2) {
            bob += sorted_a.at(i);
        } else {
            allice += sorted_a.at(i);
        }
    }

    cout << allice - bob << endl;
}