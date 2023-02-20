import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class AAA {
    static int N = 100; // 도화지 크기

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int answer = 0;
        int[][] arr = new int[N][N];
        for (int i = 0; i < n; i++) {
            String[] temp = br.readLine().split(" ");
            int x = Integer.parseInt(temp[0]);
            int y = Integer.parseInt(temp[1]);

            for (int a = x; a < x + 10; a++) {
                for (int b = y; b < y + 10; b++) {

                    arr[a][b] = 1;


                }
                printArr(arr);
            }
        }

        for (int i = 0; i < N; i++) {

            for (int j = 0; j < N; j++) {
                answer += arr[i][j];
            }

        }
        System.out.print(answer);
    }
    public static void printArr(int[][] arr){
        for (int[] i : arr){
            System.out.println(Arrays.toString(i));
        }
    }

}
