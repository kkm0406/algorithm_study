#include <iostream>
#include <vector>
#include <deque>
#include <sstream>
#include <algorithm>
#define num 50
using namespace std;

int w, h;
int arr[num][num];
bool visited[num][num];
int dx[8] = { -1, -1, 0, 1, 1, 1, 0, -1 };
int dy[8] = { 0, 1, 1, 1, 0, -1, -1, -1 };
void init() {
	for (int i = 0;i < h;i++) {
		for (int j = 0;j < w;j++) {
			arr[i][j] = 0;
			visited[i][j] = false;
		}
	}
}
void make_map(int c, int r) {
	for (int i = 0;i < r;i++) {
		for (int j = 0;j < c;j++) {
			cin >> arr[i][j];
		}
	}

}
int bfs(int r, int c) {
	visited[r][c] = true;
	deque<pair<int, int>> q;
	q.push_back(make_pair(r, c));

	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop_front();

		for (int i = 0;i < 8;i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if ((0 <= nx && nx < h) && (0 <= ny && ny < w)) {
				if (visited[nx][ny] == false && arr[nx][ny] == 1) {
					visited[nx][ny] = true;
					q.push_back(make_pair(nx, ny));
				}
			}
		}
	}

	return 1;
}
int main() {

	while (1) {
		cin >> w >> h;
		if (w == 0 && h == 0) {
			break;
		}

		init();
		make_map(w, h);
		int cnt = 0;
		for (int i = 0;i < h;i++) {
			for (int j = 0;j < w;j++) {
				if (visited[i][j] == false && arr[i][j] == 1) {
					cnt += bfs(i, j);
				}
			}
		}

		printf("%d\n", cnt);


	}

	return 0;
}
