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
    vector<int> check(n, false);
    bool flag = true;
    int counter = 0;
    vector<int> b(n);
    for (int i = 0; i < n; i++) {
        cin >> b.at(i);
    }

    int i = 0;
    while(true) {
        if (check.at(i) == true) {
            flag = false;
            break;
        } else {
            if (b.at(i) == 2) {
                counter++;
                break;
            } else {
                check.at(i) = true;
                i = b.at(i) - 1;
                counter++;
            }
            
        }
    }

    if (flag) {
        cout << counter << endl;
    } else {
        cout << -1 << endl;
    }
}