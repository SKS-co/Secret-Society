#include <stdio.h>

int arr[51][51]; //(1 ≤ a, b ≤ 50) 이므로 0은 사용 하지 않고 50개여야 하므로 배열을 51*51로 만듬

int f(int a, int b) {
	if (a == 1 || b == 1) {         //  0행과 0열은 존재하지 않아야 하므로
		arr[a][b] = arr[b][a] = 1;  // 1행의 모든 요소와 1열의 모든 요소가 1이므로 또한 기록의 목적도 있다.
		return arr[a][b];
	}

	if (arr[a][b] != 0) {      //메모이제이션 기법 활용, 생략하고 실행해도 돌아는 가나 시간초과 발생(묻고 답하기에서 인용함) 
		return arr[a][b]; 
	}

	else {
		arr[a][b] = arr[b][a] = (f(a - 1, b) + f(a, b - 1)) % 100000000; //기록의 목적도 있다.
		return arr[a][b];
	}
}

int main() {

	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d\n", f(a, b));

	return 0;
}