//스도쿠

import java.util.*;

public class Main4 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for (int i = 0; i < T; i++) {
            boolean answer = false;

            //////////////
            int[][] sudoku = new int[9][9];

            for (int x = 0; x < 9; x++) {

                for (int y = 0; y < 9; y++) {
                    int temp_input = sc.nextInt();
                    sudoku[x][y] = temp_input;

                }

            }
            while (answer == false) {
                for (int x = 0; x < 9; x++) {
                    HashSet<Integer> set1 = new HashSet<Integer>();
                    HashSet<Integer> set2 = new HashSet<Integer>();
                    for (int y = 0; y < 9; y++) {
                        set1.add(sudoku[x][y]);
                        set2.add(sudoku[y][x]);

                    }
                    if (set1.size() != 9 || set2.size() != 9) {
                        answer = true;
                    }
                }
                for (int x = 0; x < 9; x += 3) {
                    HashSet<Integer> set3 = new HashSet<Integer>();
                    for (int y = 0; y < 9; y += 3) {

                        for (int a = 0; a < 3; a++) {
                            for (int b = 0; b < 3; b++) {
                                set3.add(sudoku[x + a][y + b]);
                            }

                        }
                        if (set3.size() != 9) {
                            answer = true;
                        }
                    }

                }
                break;
            }

            System.out.printf("#%d %d\n", i + 1, answer == false ? 1 : 0);
            //////////////
        }
    }
}