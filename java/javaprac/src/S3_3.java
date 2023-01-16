import java.util.*;
public class S3_3 {
    public static void main(String[] args) throws Exception{
        // 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for (int i=0; i<N; i++){
            int n = sc.nextInt();
            char arr[][] = new char[n][n];

            for (int x =0; x<n; x++){
                for (int y=0; y<n; y++){
                    arr[x][y] = sc.nextLine().trim().charAt(0);
                }
            }
        }

    }
}
