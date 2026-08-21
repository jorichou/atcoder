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
   int n, s;
   cin >> n >> s;
   vector<int> a(n), p(n);
   for (int i = 0; i < n; i++) {
       cin >> a.at(i);
   }
   for (int i = 0; i < n; i++) {
       cin >> p.at(i);
   }

   int count = 0;
   for (int x : a) {
       for (int y : p) {
           if (x + y == s) {
               count++;
           }
       }
   }

   cout << count << endl;
}