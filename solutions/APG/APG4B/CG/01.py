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
   int pa;
   int ca;
   bool flag = false;
   for (int i = 0; i < 5; i++) {
       cin >> ca;
       if (i == 0) {
           pa = ca;
           continue;
       }

       if (pa == ca) {
           flag = true;
           break;
       }
       pa = ca;
   }

   if (flag) {
       cout << "YES" << endl;
   } else {
       cout << "NO" << endl;
   }
}