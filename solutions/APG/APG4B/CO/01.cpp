#include <algorithm>
# include <bits/stdc++.h>
#include <cmath>
#include <iostream>
using namespace std;

int main() {
    int patern;
    int price;
    int n;
    cin >> patern;

    if (patern == 2) {
        string text;
        cin >> text;
        cout << text << "!" << endl;
    }

    cin >> price >> n;
    cout << price * n << endl;
    
}