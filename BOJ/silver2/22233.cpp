#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <string>
#include <sstream>
#include <unordered_set>
#define num 200000
using namespace std;


vector<int>v;
int n, m;
unordered_set <string> memo;
int visited[num] = {};
vector<string> arr;
int main() {

	ios::sync_with_stdio(false);
	cout.tie(NULL);
	cin.tie(NULL);


	cin >> n >> m;
	for (int i = 0;i < n;i++) {
		string tmp;
		cin >> tmp;
		memo.insert(tmp);
	}
	// 블로그에 적은 글의 키워드
	for (int i = 0;i < m;i++) {
		string str, tmp;
		cin >> str;

		stringstream new_str(str);
		string token;
		while (getline(new_str, token, ',')) {
			if (memo.find(token) != memo.end()) {
				memo.erase(token);
			}
		}

		cout << memo.size() << "\n";

	}



	return 0;
}
