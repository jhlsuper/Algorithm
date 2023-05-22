import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Algo2_서울_19_김태현 {

	static int n; //구역의 크기를 정할 n
	static char[][] area; //구역의 정보를 받을 area
	static boolean[][] visit; //방문체크를 위한 visit
	static int[][] start = new int[3][2]; //출발 좌표를 위한 start
	static int[] dr = {-1,1,0,0}; //행 방향 벡터
	static int[] dc = {0,0,-1,1}; //열 방향 벡터
	static int answer = Integer.MAX_VALUE; //정답을 저장할 answer
	static Queue<Gidung> queue = new LinkedList<>(); //bfs를 위한 queue
	
	static class Gidung{ //기둥의 상태를 가질 Gidung 클래스
		int[][] rocate = new int[3][2]; //현재 위치를 갖는 rocate
		int status; //기둥의 가로, 세로 상태를 나타내는 status(가로 : 0, 세로 : 1)
		int cost; //현재까지의 이동 비용
		
		public Gidung(int[][] rocate, int status, int cost) { //기둥의 정보를 받을 생성자
			this.rocate = rocate;
			this.status = status;
			this.cost = cost;
		}
	}

	public static void main(String[] args) throws Exception{ //main 메서드
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //입력을 받기위한 bufferedReader
		n = Integer.parseInt(br.readLine()); //구역의 크기를 n에 저장
		area = new char[n][n]; //구역 선언
		visit = new boolean[n][n]; //방문 배열 선언
		int index = 0; //첫 출발점의 좌표를 받기위한 index
		for(int i=0; i<n; i++) { //구역의 행 정보를 받기위한 for문
			char[] ch = br.readLine().toCharArray(); //공백을 기점으로 잘라서 저장
			for(int j=0; j<n; j++) { //구역의 열 정보를 받기위한 for문
				area[i][j] = ch[j]; //하나씩 area에 저장
				if(area[i][j]=='B') { //만약 B라면
					start[index][0] = i; //행 좌표 저장
					start[index][1] = j; //열 좌표 저장
					index++; //다음 좌표 저장을 위해 index +1
					visit[i][j] = true; //해당 칸 방문처리
				}
			}
		}
		int s = 0; //상태를 받을 s
		if(start[2][1]-start[1][1]==0) { //만약 상태가 세로라면
			s = 1; //1로 변경해줌
		}
		queue.offer(new Gidung(start, s, 0)); //첫 기둥의 상태를 queue에 넣음
		findRoot(); //경로 찾는 메서드 시작
		
		if(answer==Integer.MAX_VALUE) { //만약 경로를 찾지 못해 여전히 최대값이라면
			System.out.println(0); //0출력
		}else { //경로를 찾았다면
			System.out.println(answer); //값 출력
		}
		

	}
	
	static void findRoot() { //경로를 찾는 findRoot 메서드
		while(queue.size()!=0) { //queue가 빌 때까지 반복하기위한 while문
			Gidung g = queue.poll(); //queue의 가장 앞 데이터를 뽑음
			int fr = g.rocate[0][0]; //맨 위 혹은 맨 왼쪽 행 좌표
			int fc = g.rocate[0][1]; //맨 위 혹은 맨 왼쪽 열 좌표
			int lr = g.rocate[2][0]; //맨 아래 혹은 맨 오른쪽 행 좌표
			int lc = g.rocate[2][1]; //맨 아래 혹은 맨 오른쪽 열 좌표
			if(g.status==0) { // 현재 상태가 가로라면
				//만약 구역 안쪽이고 방문하지 않았고 1이 없으면
				if(fr-1>=0 && fr+1<n && (!visit[fr-1][(fc+lc)/2] || !visit[fr+1][(fc+lc)/2]) && check(fr-1,(fc+lc)/2) && check(fr+1,(fc+lc)/2)){
					if(area[fr-1][(fc+lc)/2]=='E' && area[fr+1][(fc+lc)/2]=='E') { //만약 회전한 곳이 도착지라면
						answer = Math.min(g.cost+1, answer); //답과 비교해서 낮은 수 저장
						continue; //다음 반복문 실행
					}
					visit[fr-1][(fc+lc)/2] = true; //방문 처리
					visit[fr+1][(fc+lc)/2] = true; //방문 처리
					queue.offer(new Gidung(new int[][] {{fr-1,(fc+lc)/2},{(fr+lr)/2,(fc+lc)/2},{fr+1,(fc+lc)/2}}, 1, g.cost+1)); //다음 좌표 입력
				}
			}else { // 세로 라면
				//만약 구역 안쪽이고 방문하지 않았고 1이 없으면
				if(fc-1>=0 && fc+1<n && (!visit[fc-1][(fr+lr)/2] || !visit[fc+1][(fr+lr)/2]) && check(fc-1,(fr+lr)/2) && check(fc+1,(fr+lr)/2)){
					if(area[((fr+lr)/2)-1][(fr+lr)/2]=='E' && area[((fr+lr)/2)+1][(fr+lr)/2]=='E') { //만약 회전한 곳이 도착지라면
						answer = Math.min(g.cost+1, answer); //답과 비교해서 낮은 수 저장
						continue; //다음 반복문 실행
					}
					visit[fc-1][(fr+lr)/2] = true; //방문 처리
					visit[fc+1][(fr+lr)/2] = true; //방문 처리
					queue.offer(new Gidung(new int[][] {{((fr+lr)/2)-1,(fr+lr)/2},{(fr+lr)/2,(fr+lr)/2},{((fr+lr)/2)+1,(fr+lr)/2}}, 0, g.cost+1)); //다음 좌표 입력
				}
			}
			for(int d=0; d<4; d++) { //4방향 검사
				int nfr = fr + dr[d]; //새로운 좌표들
				int nfc = fc + dc[d];
				int nlr = lr + dr[d];
				int nlc = lc + dc[d];
				if(nfr>=0 && nfc>=0 && nlr<n && nlc<n) { //만약 범위 내라면
					if(area[nfr][nfc]=='E' && area[nlr][nlc]=='E') { //도착지라면
						answer = Math.min(g.cost+1, answer); //정답과 비교해서 작은 수 저장
						continue; //다음 반복문
					}
					if((!visit[nfr][nfc] || !visit[nlr][nlc] || !visit[(nfr+nlr)/2][(nfc+nlc)/2]) && area[nfr][nfc]!='1' && area[nlr][nlc]!='1' && area[(nfr+nlr)/2][(nfc+nlc)/2]!='1') { //만약 다음 칸이 한 칸이라도 방문 하지 않은 칸이고 기둥이 없다면
						 queue.offer(new Gidung(new int[][] {{nfr,nfc},{(nfr+nlr)/2,(nfc+nlc)/2},{nlr,nlc}}, g.status, g.cost+1)); //한 칸 이동
						 visit[nfr][nfc] = true; //방문처리
						 visit[(nfr+nlr)/2][(nfc+nlc)/2] = true;
						 visit[nlr][nlc] = true;
					}
				}
			}
		}
	}
	
	static boolean check(int r, int c) { //구역 내 1이 있는지 검사하는 메서드
		int[] vr = {-1,-1,-1,0,0,1,1,1};
		int[] vc = {-1,0,1,-1,1,-1,0,1};
		for(int d=0; d<8; d++) {
			int nr = r + vr[d];
			int nc = r + vc[d];
			if(area[nr][nc]=='1') {
				return false;
			}
		}
		return true;
	}
	
}
