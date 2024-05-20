#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#define MAX 101
using namespace std;
int dir[4][2] = { {1, 0 }, {0, -1}, {-1, 0}, {0, 1} };


int map[MAX][MAX] = {};
int main() {
	int n;
	cin >> n;
	string str;
	cin >> str;
	int x, y;
	x = y = 50;
	map[x][y] = 1;
	int d = 0;
	vector<int> coords_x;
	vector<int> coords_y;
	for (const char& c : str) {
		if (c == 'R') {
			d += 1;
			if (d > 3) {
				d = 0;
			}
		}
		else if (c == 'L') {
			d -= 1;
			if (d < 0) {
				d = 3;
			}
		}
		else {
			x = x + dir[d][0];
			y = y + dir[d][1];
			map[x][y] = 1;
		}
	}

	int sx, sy, ex, ey;
	sx = sy = MAX;
	ex = ey = 0;

	for (int i = 0;i < MAX;i++) {
		for (int j = 0;j < MAX;j++) {
			if (map[i][j] == 1) {
				sx = min(sx, i);
				sy = min(sy, j);
				ex = max(ex, i);
				ey = max(ey, j);
			}
		}
	}
	for (int i = sx;i <= ex;i++) {
		for (int j = sy;j <= ey;j++) {
			if (map[i][j] == 1) {
				cout << ".";
			}
			else {
				cout << "#";
			}
		}
		cout << "\n";
	}
	return 0;
}
