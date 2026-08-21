# include <bits/stdc++.h>
#include <cmath>
using namespace std;

int main() {
    int s;
    cin >> s;
    int s1 = s / 100;
    int s2 = (s % 100) / 10;
    int s3 = s % 10;
    cout << s1 + s2 + s3 << endl;
}