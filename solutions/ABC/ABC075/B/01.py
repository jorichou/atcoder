#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;
#define rep_up(i, s, n) for (int i = (s); i < (int)(n); i++);
#define rep_down(i, s, n) for (int i = (s), i > (int)(n); i--);

int main() {
    int h, w;
    cin >> h >> w;
    vector<string> rows(h);

    for (int i = 0; i < h; i++) {
        cin >> rows.at(i);
    }

    for (int i = 0; i < h; i++) {
        string rowc = rows.at(i);
        for (int j = 0; j < w; j++) {
            if (rows.at(i).at(j) == '.') {
                int bn = 0;
                if (i > 0) {// 上側
                    string row = rows.at(i - 1);
                    if (j > 0) { // 左上
                        if (row.at(j - 1) == '#') {
                            bn++;
                        } 
                    }

                    if (j < w - 1) { // 右上
                        if (row.at(j + 1) == '#') {
                            bn++;
                        } 
                    }

                    if (row.at(j) == '#') { // 真上
                        bn++;
                    } 
                }
                if (i < h - 1) {// 下側
                    string row = rows.at(i + 1);
                    if (j > 0) { // 左下
                        if (row.at(j - 1) == '#') {
                            bn++;
                        } 
                    }

                    if (j < w - 1) { // 右下
                        if (row.at(j + 1) == '#') {
                            bn++;
                        } 
                    }

                    if (row.at(j) == '#') { // 真下
                        bn++;
                    } 
                }

                if (j > 0) {
                    string row = rows.at(i);
                    if (row.at(j - 1) == '#') { // 左
                        bn++;
                    }
                }

                if (j < w - 1) {
                    string row = rows.at(i);
                    if (row.at(j + 1) == '#') { // 左
                        bn++;
                    }
                }
                cout << bn;
            } else {
                cout << rowc.at(j);
                
            }
        }
        cout << endl;
    }
}