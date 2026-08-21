#include <bits/stdc++.h>
// #include <cmath>
// #include <iostream>
// #include <vector>
using namespace std;
// #define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
// #define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int count_report_num(vector<vector<int>> &children, int x) {
    if (children.at(x).size() == 0) {
        return 1;
    }

    int sum = 0;
    for (int c : children.at(x)) {
        sum += count_report_num(children, c);
    }
    sum += 1;
    return sum;
}

int main() {
    int n;
    cin >> n;

    vector<int> p(n);
    p.at(0) = -1;
    for (int i = 1; i < n; i++) {
        cin >> p.at(i);
    }

    vector<vector<int>> children(n);
    for (int i = 1; i < n; i++) {
        int parent = p.at(i);
        children.at(parent).push_back(i);
    } 

    for (int i = 0; i < n; i++) {
        cout << count_report_num(children, i) << endl;
    }
}