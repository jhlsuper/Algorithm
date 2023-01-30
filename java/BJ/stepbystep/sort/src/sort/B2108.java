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
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        int mid = 10000;
        int mode = 10000;

        int answer = 0;
        for (int i = 0; i < N; i++) {
            int temp = Integer.parseInt(br.readLine());
            sum += temp;
//			arr[i] =temp;
            if (max < temp) {
                max = temp;
            }
            if (min > temp) {
                min = temp;
            }
            count[4000 + temp]++;

        }
        int cnt = 0;
        int max_count = 0;
        boolean flag = false;
        for (int i = min + 4000; i <= max + 4000; i++) {
            if (count[i] > 0) {

                if (cnt < (N + 1) / 2) {
                    cnt += count[i];
                    mid = i - 4000;
                }
                if (max_count < count[i]) {
                    max_count = count[i];
                    mode = i - 4000;
                    flag = true;
                } else if (max_count == count[i] && flag) {
                    mode = i - 4000;
                    flag = false;
                }

            }
        }

        Arrays.sort(arr);
        System.out.println((int) Math.round((double) sum / N));
        System.out.println(mid);
        System.out.println(mode);
        System.out.println(max-min);
    }

}
