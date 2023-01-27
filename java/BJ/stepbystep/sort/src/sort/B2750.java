package sort;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class B2750 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String a = br.readLine();
		int n = Integer.parseInt(a);
		int[] arr = new int[n];
		for(int i=0; i<n; i++) {
			arr[i]=Integer.parseInt(br.readLine());
		}
		for(int i=0; i<n;i++) {
			for(int j=i+1;j<n;j++) {
//				System.out.printf("%d %d\n",i,j );
				if(arr[i]>arr[j]) {
					int temp = arr[j];
					arr[j] = arr[i];
					arr[i] = temp;
				}
			}
		}
		for(int i :arr) {
			System.out.println(i);
		}
	}

}
