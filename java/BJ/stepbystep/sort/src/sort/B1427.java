package sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

public class B1427 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String in = br.readLine();
		String[] st = in.split("");
		
		Arrays.sort(st,Collections.reverseOrder());
		for(String s :st) {
			System.out.print(s);
		}
	}
}
