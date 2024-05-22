#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <sstream>
using namespace std;
string str;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> str;
	vector<int> v;
	int result = 0;
	
	vector<int>arr;
	for (int i = 0;i < str.size();i++) {
		if (str[i] == '(') {
			v.push_back(0);
		}
		else if (str[i] == ')') {
			int sum = 0;
			while (v.back() != 0) {
				sum += v.back();
				v.pop_back();
			}
			v.pop_back();
			v.push_back(sum);
		}
		else if(str[i] == 'H') {
			v.push_back(1);
		}
		else if (str[i] == 'C') {
			v.push_back(12);
		}
		else if (str[i] == 'O') {
			v.push_back(16);
		}
		else {
			int back = v.back();
			v.pop_back();
			v.push_back(back * (str[i] - '0'));
		}
	}

	for (const auto item : v) {
		result += item;
	}
	cout << result;
	return 0;
}
