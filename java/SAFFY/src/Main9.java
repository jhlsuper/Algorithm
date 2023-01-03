import java.util.Scanner;
import java.util.*;

public class Main9 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int i = 0; i < T; i++) {
            int a = sc.nextInt(); // test case 번호
            // int[] array = new int[1000];
            HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>(1000);
            for (int j = 0; j < 1000; j++) {
                int temp = sc.nextInt();
                if (hash.get(temp) == null) {
                    hash.put(temp, 1);

                } else {
                    hash.put(temp, hash.get(temp) + 1);
                }

            }
            System.out.println(hash);
            int max = Collections.max(hash.values());
            System.out.println(max);
            int maxKey = 0;
            for (int z = 0; z < 1000; z++) {
                if (hash.get(z) == max) {
                    maxKey = z;
                }
            }
            System.out.println(maxKey);
        }
    }
}