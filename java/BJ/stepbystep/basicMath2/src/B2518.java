import java.util.Scanner;

public class B2518 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        int N = sc.nextInt();
        int sum =0;
        int min =10000;
        for(int i=M;i<=N;i++){
            if(is_prime(i)){
                if(i<min){
                    min=i;
                }
                sum+= i;
            }
        }
        if(sum==0){
            System.out.printf("%d",-1);
        }
        else{
            System.out.printf("%d\n",sum);
            System.out.printf("%d",min);
        }

    }

    public static boolean is_prime(int number){
        if(number<2){
            return false;
        }
        if(number ==2){
            return true;
        }
        for(int i=2; i<number; i++){
            if(number%i==0){
                return false;
            }

        }
        return true;
    }
}
