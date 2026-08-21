# include <bits/stdc++.h>
#include <cmath>
#include <iostream>
using namespace std;

int main() {
    int a, b;
    string op;
    
    cin >> a >> op >> b;
    int result;
    if (op == "+") {
        result = a + b;
        cout << result << endl;
    } else if (op == "-") {
        result = a - b;
        cout << result << endl;
    } else if (op == "*") {
        result = a * b;
        cout << result << endl;
    } else if (op == "/") {
        if (b == 0) {
            cout << "error" << endl;
        } else {
            cout << a / b << endl;
        }
    } else {
        cout << "error" << endl;
    }
}