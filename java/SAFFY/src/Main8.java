import java.util.*;

public class Main8 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int i = 0; i < T; i++) {
            int N = sc.nextInt();
            int[][] array = new int[N][N];
            int[][] array90 = new int[N][N];
            int[][] array180 = new int[N][N];
            int[][] array270 = new int[N][N];
            for (int x = 0; x < N; x++) {

                for (int y = 0; y < N; y++) {
                    int temp = sc.nextInt();
                    array90[y][N - x - 1] = temp;
                    array180[N - x - 1][N - y - 1] = temp;
                    array270[N - y - 1][x] = temp;
                }
            }
            System.out.printf("#%d\n", i + 1);
            for (int x = 0; x < N; x++) {
                for (int y = 0; y < 3; y++) {

                    for (int z = 0; z < N; z++) {
                        if (y == 0) {
                            System.out.printf("%d", array90[x][z]);
                        } else if (y == 1) {
                            System.out.printf("%d", array180[x][z]);
                        } else if (y == 2) {
                            System.out.printf("%d", array270[x][z]);

                        }
                    }
                    System.out.printf(" ");

                }
                System.out.printf("\n");
            }

        }
    }

}
