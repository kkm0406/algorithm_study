#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#define num 8
using namespace std;
int n;
vector<int> v;
int result = -1e9;
int visited[num] = {};
int arr[num];
void dfs(int depth) {
	if (v.size() == n) {
		int sum = 0;
		for (int i = 1;i < v.size();i++) {
			sum += abs(v[i] - v[i - 1]);
		}
		result = max(result, sum);
	}
	for (int i = 0;i < n;i++) {
		if (visited[i] == 0) {
			visited[i] = 1;
			v.push_back(arr[i]);
			dfs(depth + 1);
			v.pop_back();
			visited[i] = 0;
		}
	}

}

int main() {
	scanf("%d", &n);

	for (int i = 0;i < n;i++) {
		cin >> arr[i];
	}

	dfs(0);
	cout << result;

	return 0;
}
