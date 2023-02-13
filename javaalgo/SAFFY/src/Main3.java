import java.util.Scanner;

public class Main3 {
    public static void main(String[] args) {
        int num =0;
        int answer =0;

        Scanner sc = new Scanner(System.in);
        num = sc.nextInt();

        while(num!=0){
            answer +=num%10;
            num /=10;

        }
        System.out.printf("%d", answer);
    }
}

