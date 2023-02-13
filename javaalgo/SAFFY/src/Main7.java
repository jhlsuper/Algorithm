import java.util.Arrays;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.*;

public class Main7 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            int N = 9;
            int[] mult = new int[3 * N];
            for (int i = 0; i < mult.length; i++)
                mult[i] = 1; // 1로 초기화 왜?

            int s = 1;
            for (int i = 0; i < N; i++) {
                s *= i + 1;
                for (int j = 0; j < N; j++) {
                    int num = sc.nextInt();
                    mult[i] *= num;
                    mult[N + j] *= num;
                    int index = (i / 3) * 3 + j / 3;
                    mult[2 * N + index] *= num;
                }
            }
            System.out.printf(Arrays.toString(mult));
            int res = 1;
            for (int i = 0; i < mult.length; i++)
                if (mult[i] != s)
                    res = 0;

            System.out.printf("#%d %d\n", test_case, res);
        }

    }

}
