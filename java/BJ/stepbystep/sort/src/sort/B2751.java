package sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class B2751  {
	public static void main(String[] args)throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		ArrayList<Integer> arr = new ArrayList<>();
		StringBuilder sb = new StringBuilder();
		for (int i=0;i<n;i++){
			int temp = Integer.parseInt(br.readLine());
//			System.out.println(temp);
			arr.add(temp);
		}
//		Arrays.sort(arr);
		Collections.sort(arr);
		for(int e : arr){

			sb.append(e).append('\n');
		}
		System.out.println(sb);
	}

}
