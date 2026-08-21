# include <iostream>


int main() {
  int s;
  std::cin >> s;
  
  if (s < 300 && s >= 200) {
    std::cout << "Success" << std::endl;
  } else {
    std::cout << "Failure" << std::endl;
  }
  
  return 0;
}
