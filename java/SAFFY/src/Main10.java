import java.util.*;

public class Main10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 10; i++) {
            int a = sc.nextInt();
            int biggestSum = 0;

            int[][] array = new int[100][100];

            for (int x = 0; x < 100; x++) {
                for (int y = 0; y < 100; y++) {
                    array[x][y] = sc.nextInt();

                }

            }

            for (int x = 0; x < 100; x++) {
                int sumA = 0;
                int sumB = 0;

                for (int y = 0; y < 100; y++) {
                    sumA += array[x][y];
                    sumB += array[y][x];

                }

                if (sumA > biggestSum)
                    biggestSum = sumA;

                if (sumB > biggestSum)
                    biggestSum = sumB;

            }
            int sumC = 0;
            int sumD = 0;
            for (int x = 0; x < 100; x++) {

                sumC += array[x][x];
                sumD += array[99 - x][x];

            }
            if (sumC > biggestSum)
                biggestSum = sumC;
            if (sumD > biggestSum)
                biggestSum = sumD;

            System.out.printf("#%d %d\n", a, biggestSum);

        }

    }
}