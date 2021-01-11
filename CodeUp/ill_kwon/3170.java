import java.util.HashMap;
import java.util.Scanner;
import java.util.Vector;

public class Main3170{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		HashMap<String, Integer> map = new HashMap<String, Integer>();
		int n = scan.nextInt();
		int m = scan.nextInt();
		for(int i=0;i<n;i++) {
			String s=scan.next();
			int k=scan.nextInt();
			if(map.containsKey(s))  // 중복된 값이 있을경우 기존의 값에 더해줌
				map.put(s, k+map.get(s));
			else  // 새로운 단어라면 그대로 저장
				map.put(s, k);
		}
		Vector<String> v=new Vector<String>();
		for(int i=0;i<m;i++) {
			String q=scan.next();
			v.add(q);
		}
		
		for (int i = 0; i < m; i++) { // 출력
			if (map.containsKey(v.get(i))) { // 암기하고 있는 단어인지 확인
				System.out.println(map.get(v.get(i)));
			} else { // 기존에 없는 단어라면 0 출력
				System.out.println(0);
			}
		}
		scan.close();
		
	} 
}