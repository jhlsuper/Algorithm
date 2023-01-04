import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int i = 0; i < T; i++) {
            int biggestNumber = 0;
            int maxCount = 0;
            int a = sc.nextInt(); // test case 번호

            HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>(1000);
            for (int j = 0; j < 1000; j++) {
                int temp = sc.nextInt();
                if (hash.get(temp) == null) {
                    hash.put(temp, 1);

                } else {
                    hash.put(temp, hash.get(temp) + 1);
                    if (hash.get(temp) + 1 >= maxCount) {
                        maxCount = hash.get(temp) + 1;
                        biggestNumber = temp;
                    }
                }

            }

            System.out.printf("#%d %d\n", a, biggestNumber);
        }
    }
}