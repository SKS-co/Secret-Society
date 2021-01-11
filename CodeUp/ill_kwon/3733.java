package codeup;

import java.util.HashMap;
import java.util.Scanner;

public class Main3733 {
	static int max=0;
	static int locate=0;
	static HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int a = scan.nextInt();
		int b = scan.nextInt();
		for(int i=a;i<=b;i++) {
			int temp=recur(i);
			max=mymax(temp,max,i);
		}
		/*for(int i=a;i<=b;i++) {
			System.out.println(map.get(i));
		}*/
		
		System.out.println(locate+" "+max);
		scan.close();

	}
	//최대 길이및 최대 길이 수 구하는 함수
	static int mymax(int a, int b, int c) {
		if (a > b) {
			locate = c;
			return a;
		}
		else return b;
	}

	static int recur(int a) {
		if (a == 1) 
			return 1;
		//메모가 되어 있다면 함수 호출 말고 메모값 리턴
		if (map.containsKey(a)) 
			return map.get(a);
		//메모, 재귀 호출
		else {
			if (a % 2 == 0) {
				int temp=recur(a / 2) + 1;
				map.put(a, temp);
				return map.get(a);
			}
			else {
				int temp=recur(a * 3 + 1) + 1;
				map.put(a, temp);
				return map.get(a);
			}
		}
	}

}
