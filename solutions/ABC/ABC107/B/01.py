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
    int h, w;
    cin >> h >> w;
    vector<vector<char>> a(h, vector<char>(w));
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            cin >> a.at(i).at(j);
        }
    }

    // 横の走査
    for (int i = 0; i < h; i++) {
        int count = 0;
        for (int j = 0; j < w; j++) {
            if (a.at(i).at(j) == '.') {
                count++;
            }
        }
        if (count == w) {
            for (int k = 0; k < w; k++) {
                a.at(i).at(k) = 'x';
            }
        }
    }

    // 縦の走査
    for (int i = 0; i < w; i++) {
        int count = 0;
        for (int j = 0; j < h; j++) {
            if (a.at(j).at(i) == '.' || a.at(j).at(i) == 'x') {
                count++;
            }
        }
        if (count == h) {
            for (int k = 0; k < h; k++) {
                a.at(k).at(i) = 'x';
            }
        }
    }

    for (int i = 0; i < h; i++) {
        bool flag = false;
        for (int j = 0; j < w; j++) {
            if (a.at(i).at(j) == 'x') continue;
            else {
                cout << a.at(i).at(j);
                flag = true;
            }
        }
        if (flag) cout << endl;
        
    }
}