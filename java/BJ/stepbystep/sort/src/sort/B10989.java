package sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
//import java.util.ArrayList;
import java.util.Arrays;
//import java.util.Collections;

public class B10989 {
	//counter 정렬방법을 사용한다.
	public static void main(String[] args) throws  IOException {
		int[] arr = new int[10001];
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		int N = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		for(int i=0; i<N;i++) {
			arr[Integer.parseInt(br.readLine())]++;
		}
			
		br.close();
		for(int i=1;i<10001; i++) {
			while(arr[i]>0) {
				sb.append(i).append('\n');
				arr[i]--;
			}
		}
		System.out.println(sb);

	}
	
}
