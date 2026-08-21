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

void saiten(vector<vector<int>> &a, int &correct_count, int &wrong_count) {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (a.at(i).at(j) == (i + 1) * (j + 1)) {
                correct_count++;
            } else {
                wrong_count++;
                a.at(i).at(j) = (i + 1) * (j + 1);
            }
        }
    }
}


int main() {
    vector<vector<int>> a(9, vector<int>(9));
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cin >> a.at(i).at(j);
        }
    }

    int correct_count = 0;
    int wrong_count = 0;

    saiten(a, correct_count, wrong_count);

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cout << a.at(i).at(j);
            if (j < 8) cout << " ";
            else cout << endl;
        }
    }

    cout << correct_count << endl;
    cout << wrong_count << endl;
}