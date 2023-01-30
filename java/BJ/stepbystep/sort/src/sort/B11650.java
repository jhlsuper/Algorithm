package sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B11650 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			String temp = br.readLine();

			int a = Integer.parseInt(temp.split(" ")[0]);
			int b = Integer.parseInt(temp.split(" ")[1]);
			System.out.println(a, b);
		}
	}

}
