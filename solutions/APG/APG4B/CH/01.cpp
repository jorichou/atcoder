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
   int N;
   cin >> N;

   vector<int> A = input(N);
   vector<int> B = input(N);
   vector<int> C = input(N);

   int sum_A = sum(A);
   int sum_B = sum(B);
   int sum_C = sum(C);

   output(sum_A, sum_B, sum_C);
}