package codeup;
import java.util.*;

public class Main3004 {

	public static void main(String[] args) {
		Vector<Integer> v=new Vector<Integer>();
		Scanner scan=new Scanner(System.in);
		Integer totalNum=scan.nextInt();
		for(int i=0;i<totalNum;i++){
			Integer data=scan.nextInt();
			v.add(data);
		}
		
		Vector<Integer> v2=new Vector<Integer>();
		for(int i=0;i<totalNum;i++){
			v2.add(v.get(i));
		}
		Collections.sort(v2);
		
		/*Map<Integer, Integer> map=new HashMap<Integer, Integer>();
		for(int i=0;i<totalNum;i++){
			Integer index=i;
			Integer data=v2.get(i);
			map.put(index, data);
		}*/
		
		for(int i=0;i<totalNum;i++) {
			for(int j=0;j<totalNum;j++) {
				if(v.get(i)==v2.get(j)) {
					System.out.print(j+" ");
				}
			}
		}
		System.out.println();
		
		scan.close();

	}

}
