package codeup;

import java.util.*;

public class Main1805 {

	public static void main(String[] args) {
		Map<Integer, Integer> map=new HashMap<Integer, Integer>();
		Scanner scan=new Scanner(System.in);
		Integer totalNum=scan.nextInt();
		for(int i=0;i<totalNum;i++){
			Integer id=scan.nextInt();
			Integer gasNum=scan.nextInt();
			map.put(id, gasNum);
		}
		Object[] mapkey = map.keySet().toArray();
		Arrays.sort(mapkey);
		for (Integer nKey : map.keySet())
		{
			System.out.println(nKey+ " "+ map.get(nKey));
		}
		scan.close();

	}

}
