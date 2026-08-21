#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;
#define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
#define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int sum(vector<int> scores) {
    int total = 0;
    for (int i = 0; i < scores.size(); i++) {
        total += scores.at(i);
    }
    return total;
}

void output(int sum_a, int sum_b, int sum_c) {
    cout << sum_a * sum_b * sum_c << endl;
}

vector<int> input(int N) {
    vector<int> vec(N);
    for (int i = 0; i < N; i++) {
        cin >> vec.at(i);
    }
    return vec;
}

int main() {
   int n, m;
   cin >> n >> m;
   vector<vector<int>> p(m, vector<int>(2));

   for (int i = 0; i < m; i++) {
       for (int j = 0; j < 2; j++) {
           cin >> p.at(i).at(j);
       }
   }

   vector<vector<char>> r(n, vector<char>(n, '-'));

   for (vector<int> x : p) {
       int i = x.at(0);
       int j = x.at(1);
       r.at(i - 1).at(j - 1) = 'o';
       r.at(j - 1).at(i - 1) = 'x';
   }

   for (int i = 0; i < n; i++) {
       for (int j = 0; j < n; j++) {
           cout << r.at(i).at(j);
           if (j < n - 1) {
               cout << ' ';
           }
       }
       cout << endl;
   }
}