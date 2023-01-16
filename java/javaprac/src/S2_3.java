import java.util.*;
public class S2_3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N =sc.nextInt();
        int arr[] = new int[10];
        int count =sc.nextInt();
        for(int i=0; i<count;i++) {
            int temp = sc.nextInt();
            for(int j=1; j<N; j++) {
                if(j%temp ==0) {
                    if(arr[j-1]==0) {
                        arr[j-1]=1;
                    }
                    else if(arr[j]==1) {
                        arr[j-1]=0;
                    }
                }
            }
//            System.out.println(Arrays.toString(arr));
        }
		System.out.print(Arrays.toString(arr));
    }
}
