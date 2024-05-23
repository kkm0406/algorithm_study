#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <sstream>
#include <string>
#define num 101
using namespace std;

int n, m;
vector <int> v[num];
bool visited[num];
int cnt = 0;
void bfs(int start) {
	deque<int> q;
	q.push_back(start);
	visited[start] = true;

	while (!q.empty()) {
		int node = q.front();
		q.pop_front();

		for (int i = 0;i < v[node].size();i++) {
			int next = v[node][i];

			if (visited[next] == false) {
				q.push_back(next);
				visited[next] = true;
				cnt++;
			}
		}
	}
}
int main() {

	ios::sync_with_stdio;
	cout.tie(nullptr);
	cin.tie(nullptr);

	cin >> n >> m;
	
	for (int i = 0;i < m;i++) {
		int a, b;
		cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
	}

	bfs(1);

	cout << cnt;
	return 0;
}
