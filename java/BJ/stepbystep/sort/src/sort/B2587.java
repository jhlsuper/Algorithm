package sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class B2587 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int sum =0;
		int[] arr = new int[5];
		for(int i=0; i<5;i++) {
			int temp = Integer.parseInt(br.readLine());
			arr[i] = temp;
			sum+= temp;
			
		}
		Arrays.sort(arr);
		System.out.println(sum/5);
		System.out.println(arr[2]);
	}

}
