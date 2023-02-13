import java.util.Arrays;
import java.util.Scanner;

public class Main6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n =0;
        n = sc.nextInt();

        for(int i=0; i<n; i++){
            int[] numbers = new int[10];
            int answer = 0;
            for (int j=0;j<10; j++){
                numbers[j]=sc.nextInt();
                answer += numbers[j];

            }
//            String a = String.format("%.0f", answer/10.0);

            System.out.printf("#%d %d\n",i+1,Math.round(answer/10.0));
        }


    }
}
