#include <iostream>

int main() {
  std::string s;
  int l;
  std::cin >> s;
  l = s.length();
  if (l % 5 == 0) {
    std::cout << "Yes" << std::endl;
  } else {
    std::cout << "No" << std::endl;
  }
  return 0;
}