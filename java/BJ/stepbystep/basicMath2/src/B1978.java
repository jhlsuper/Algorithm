import java.util.Scanner;

public class B1978 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int answer =0;
//        int[] prime = new int[1000];
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i=0; i<n; i++) {
            arr[i] = sc.nextInt();

        }
        for(int e :arr){
//            System.out.println(is_prime(e));
            if(is_prime(e) ==true){
                answer +=1;
            }
        }
        System.out.print(answer);


    }
    public static boolean is_prime(int number){
        if(number<2){
            return false;
        }
        if(number ==2){
//            System.out.println(number);
            return true;
        }
        for(int i=2; i<number;i++){
            if(number%i ==0){
                return false;
            }
        }
        return true;
    }
}
