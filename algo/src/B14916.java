import java.util.*;

public class B14916 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //2원 5원 거스름돈
        int n = sc.nextInt();
        int answer =0;

        while(n>0){
            if(n%5==0){
                answer =n/5 +answer;
                break;
            }
            n-=2;
            answer++;
        }
        if(n<0){
            System.out.print(-1);
        }
        else{
            System.out.println(answer);
        }

    }
}
