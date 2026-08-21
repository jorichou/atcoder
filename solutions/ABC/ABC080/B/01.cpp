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
    int x = n;
    int fx = 0;

    while (n != 0) {
        fx += n % 10;
        n /= 10;
    }
    
    if (x % fx == 0) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}