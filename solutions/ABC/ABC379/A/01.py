# include <stdio.h>

int main(void) {
  char N[4];
  scanf("%s", N);
  
  printf("%c%c%c %c%c%c", N[1], N[2], N[0], N[2], N[0], N[1]);
  
  return 0;
}