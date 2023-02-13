import java.util.Scanner;
public class Main2 {
    public static void main(String[] args){
        Scanner sc =new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

//        System.out.printf("%d %d" ,a ,b);
        if (a==1 ){
            if(b==2){
                System.out.printf("B");
            }
            else{
                System.out.printf("A");
            }
        }
        else if(a==2){
            if(b==1){
                System.out.printf("B");
            }
            else{
                System.out.printf("A");
            }
        }
        else{
            if(b==1){
                System.out.printf("B");
            }
            else{
                System.out.printf("A");
            }
        }


    }
}
