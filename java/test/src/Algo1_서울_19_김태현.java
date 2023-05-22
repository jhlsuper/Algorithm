import java.io.BufferedReader; //입력을 받기위한 BufferedReader
import java.io.InputStreamReader; //입력을 받기위한 InputStreamReader
import java.util.StringTokenizer; //입력받은 값을 공백을 기점으로 자르기위한 StringTokenizer

public class Algo1_서울_19_김태현 {
	
	static int[] track; //트랙의 정보를 받을 track
	static int[][] rabbit; //토끼의 정보를 받을 rabbit

	public static void main(String[] args) throws Exception{ //main 메서드
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //입력
		int t = Integer.parseInt(br.readLine()); //테스트 케이스 개수 입력
		StringBuilder sb = new StringBuilder(); //결과를 모아서 한번에 출력하기위한 StringBuilder
		for(int tc=1; tc<=t; tc++) { //테스트케이스 개수만큼 반복하기위한 for문
			sb.append('#').append(tc).append(' '); //출력 형식 입력
			track = new int[10]; //트랙 초기화
			rabbit = new int[5][2]; //토끼의 정보 초기화
			int finish = 0; //완주 한 토끼의 수를 저장할 finish
			StringTokenizer st = new StringTokenizer(br.readLine()); //입력받은 값을 자름
			for(int i=0; i<10; i++) { //트랙의 정보를 받기위한 for문
				track[i] = Integer.parseInt(st.nextToken()); //입력받은 값을 track에 저장
			}
			for(int i=0; i<5; i++) { //토끼의 정보를 받을 for문
				st = new StringTokenizer(br.readLine()); //문자열 자름
				for(int j=0; j<2; j++) { //토끼의 정보를 받을 for문
					rabbit[i][j] = Integer.parseInt(st.nextToken()); //토끼의 정보 저장
				}
			}
			
			for(int i=0; i<5; i++) { //5마리의 토끼를 조회하기위한 for문
				int up = rabbit[i][0]; //토끼의 윗 상한선
				int down = rabbit[i][1]; //토끼의 아래 하한선
				for(int j=1; j<10; j++) { //트랙을 전부 돌기위한 for문
					if(track[j-1]>track[j]) { //다음 트랙 높이가 낮을 때
						if((track[j-1]-track[j])>down) { //만약 아래 하한선보다 높다면
							break; //종료
						}
					}else if(track[j-1]<track[j]) { //다음 트랙 높이가 높을 때
						if((track[j]-track[j-1])>up) { //만약 위 상한선보다 높다면
							break; //종료
						}
					}
					if(j==9) { //트랙을 전부 완주 했다면
						finish++; // finish+1
					}
				}
			}
			sb.append(finish).append('\n'); //결과 입력
		}
		System.out.println(sb); //최종 결과 출력
	}
}
