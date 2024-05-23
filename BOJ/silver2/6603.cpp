#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#define num 13
using namespace std;

int arr[num];
vector<int>v;
int n;
bool visited[num] = {};

void dfs(int depth, int idx) {
	if (v.size() == 6) {
		for (const auto val : v) {
			cout << val << " ";
		}
		cout << "\n";
		return;
	}
	else {
		for (int i = idx;i < n;i++) {
			if (visited[i] == false) {
				visited[i] = true;
				v.push_back(arr[i]);
				dfs(depth + 1, i + 1);
				v.pop_back();
				visited[i] = false;
			}

		}
	}
}
int main() {
	while (1) {
		cin >> n;
		if (n == 0) {
			break;
		}

		for (int i = 0;i < n;i++) {
			cin >> arr[i];
		}

		for (int i = 0;i < num;i++) {
			visited[i] = false;
		}

		dfs(0, 0);
		cout << "\n";
	}



	return 0;
}
