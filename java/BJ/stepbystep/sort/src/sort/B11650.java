package sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.*;

public class B11650 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[][] arr = new int[N][2];
		for (int i = 0; i < N; i++) {
			String temp = br.readLine();

			int a = Integer.parseInt(temp.split(" ")[0]);
			int b = Integer.parseInt(temp.split(" ")[1]);
//			System.out.printf("%d %d\n",a, b);
			arr[i][0] = a;
			arr[i][1] = b;
		}

		Arrays.sort(arr, new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				System.out.println("o1" + Arrays.toString(o1));
				System.out.println("o2" + Arrays.toString(o2));
				if (o1[0] == o2[0]) {

					return o1[1] - o2[1];
				} else {
					return o1[0] - o2[0];
				}
			}
		});
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < 2; j++) {
//				System.out.print(arr[i][j]+ " ");
			}
			System.out.println();
		}
	}

}
