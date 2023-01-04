package start1;

import java.util.*;

public class Main3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int i = 0; i < T; i++) {
            int N = sc.nextInt();
            int M = sc.nextInt();

            int biggest = 0;
            int[] arrayN = new int[N];
            int[] arrayM = new int[M];
            for (int n = 0; n < N; n++) {
                arrayN[n] = sc.nextInt();
            }
            for (int m = 0; m < M; m++) {
                arrayM[m] = sc.nextInt();
            }
            int temp = 0;
            if (N == M) {
                for (int x = 0; x < N; x++) {
                    temp += arrayN[x] * arrayM[x];
                }
                if (temp > biggest) {
                    biggest = temp;
                    temp = 0;
                }
            }
            if (N > M) {

                int diff = N - M + 1;
                for (int x = 0; x < diff; x++) {
                    temp = 0;
                    for (int y = 0; y < M; y++) {

                        temp += arrayN[y + x] * arrayM[y];
                    }
                    if (temp > biggest)
                        biggest = temp;
                }

            }
            if (M > N) {

                int diff = M - N + 1;

                for (int x = 0; x < diff; x++) {
                    temp = 0;
                    for (int y = 0; y < N; y++) {

                        temp += arrayM[y + x] * arrayN[y];

                    }

                    if (temp > biggest)
                        biggest = temp;
                }

            }
            System.out.printf("#%d %d\n", i + 1, biggest);

        }

    }
}