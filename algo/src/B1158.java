import java.util.*;
public class B1158 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int le = N;
        int[] arr = new int[N];
        for (int i=0; i<N;i++) {
            arr[i] = i+1;
        }


        int temp =0;
        System.out.printf("<");
        for(int i=0; i<N;i++) {
            int count = 0;
            while(count !=K) {

                if(temp==N) {
                    temp =temp-N;
                }
                if(arr[temp] != 0) {
                    count++;


                    if(count==K) {
                        if(i !=N-1) {
                            System.out.printf("%d, ", arr[temp], temp);

                        }
                        else {
                            System.out.printf("%d", arr[temp], temp);
                        }
                        arr[temp] =0;


                    }
                }
                temp++;

            }
        }
        System.out.printf(">");



    }
}
