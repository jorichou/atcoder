# include <stdio.h>

int count_ball(int a[], int n){
  int number_of_ball[5] = {0, 0, 0, 0};
  int counter = 0;
  
  for (int i = 0; i < n; i++){
    switch(a[i]){
      case 1 : number_of_ball[0]++;
        break;
      case 2 : number_of_ball[1]++;
        break;
      case 3 : number_of_ball[2]++;
        break;
      case 4 : number_of_ball[3]++;
        break;
    }
  }
  
  for (int i = 0; i < n; i++){
    if(number_of_ball[i] >= 2 && number_of_ball[i] <= 3){
      counter++;
    }else if (number_of_ball[i] == 4){
      counter += 2;
    }
  }
  return counter;
}

int main(void){
  int A[5];
  int count;
  scanf("%d %d %d %d", &A[0], &A[1], &A[2], &A[3]);
  
  count = count_ball(A, 4);
  
  printf("%d", count);
}


