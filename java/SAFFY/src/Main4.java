import java.util.Scanner;
import java.util.Arrays;

public class Main4 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = 0;
        n = sc.nextInt();

        int[] numbers = new int[n];
        int answer = 0;

        for (int i = 0; i < n; i++) {
            numbers[i] = sc.nextInt();
        }
//        System.out.printf(Arrays.toString(numbers));
        Arrays.sort(numbers);
//        System.out.printf(Arrays.toString(numbers));
        System.out.printf("%d", numbers[((n + 1) / 2) - 1]);
    }
}
