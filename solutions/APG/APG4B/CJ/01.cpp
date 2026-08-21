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
    int avg;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a.at(i);
        avg += a.at(i);
    }

    avg /= n;
    for (int i = 0; i < n; i++) {
        if (a.at(i) > avg) {
            cout << a.at(i) - avg << endl; 
        } else {
            cout << avg - a.at(i) << endl;
        }
    }
    
}