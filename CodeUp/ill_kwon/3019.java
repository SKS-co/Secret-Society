import java.util.*;

class Schedule{
	String word;
	int date;
	public Schedule(String word, int date) {
		this.word=word;
		this.date=date;
	}
	
}

public class Main3019 {
  public static void main(String[] args) {
	  Scanner scan=new Scanner(System.in);
	  int n=scan.nextInt();
	  Schedule s1[]=new Schedule[n];
		for(int i=0;i<n;i++) {
			String name=scan.next();
			String y=scan.next();
			String m=scan.next();
			String d=scan.next();
			s1[i]=new Schedule(name,Integer.parseInt(y+m+d));
		}
	  sort(s1);  
	  print(s1);
	  scan.close();

  }

private static void print(Schedule[] arr) {
    for(int i=arr.length-1;i>=0;i--){
        System.out.println(arr[i].word);
      }	
}

private static void sort(Schedule[] arr) {
	for(int i = arr.length -1 ; i > 0 ; i--){
	      for(int j = 0; j < i; j++){
	        if(arr[j].date < arr[j+1].date){
	          Schedule schedule = arr[j];
	          arr[j] = arr[j+1];
	          arr[j+1] = schedule;
	        } 
	        else if(arr[j].date == arr[j+1].date){
	              if(arr[j].word.compareTo(arr[j+1].word) < 0){
	                Schedule schedule = arr[j];
	                arr[j] = arr[j+1];
	                arr[j+1] = schedule;
	              }
	         }
	      }
	 }
	
}

}

