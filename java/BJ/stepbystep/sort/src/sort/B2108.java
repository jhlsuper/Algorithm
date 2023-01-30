package sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class B2108 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		int[] count = new int[8002];
		int sum = 0;
		int max = Integer.MAX_VALUE;
		int min = Integer.MIN_VALUE;
		int mid = 10000;
		int mode =10000;
		for (int i = 0; i < N; i++) {
			int temp = Integer.parseInt(br.readLine());
			sum+= temp;
			arr[temp+4000] ++;
			if(max<temp) {
				max = temp;
			}
			if(min>temp) {
				min = temp;
			}
			
		}
		for (int i = 0; i < 8002; i++) {
			if (count[i] > max) {
				max = count[i];
				max_count = i;

			}
		}
		for(int i=0; i<8002; i++) {
			if(count[i]==max) {
				
				counter+=1;
				answer =i;
			
			}
			if(counter ==2) {
				break;
			}
		}

		Arrays.sort(arr);
		System.out.println(sum / N);
		System.out.println(arr[(N + 1) / 2 - 1]);
		System.out.println(answer-4001);
		System.out.println(arr[arr.length - 1] - arr[0]);
	}

}
