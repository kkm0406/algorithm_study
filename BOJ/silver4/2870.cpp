#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool comp(string a, string b) {
	if (a.size() == b.size()) {
		return a < b;
	}
	return a.size() < b.size();
}
int main() {
	vector<string> v;
	int n;
	cin >> n;
	for (int i = 0;i < n;i++) {
		string str;
		cin >> str;
		string nums = "";
		for (int j = 0;j < str.length();j++) {
			if (str[j] <= 'z' && 'a' <= str[j]) {
				if (nums == "") {
					continue;
				}
				else {
					v.push_back(nums);
					nums = "";
				}
			}
			else {
				if (nums.size() == 1 && nums[0] == '0') {
					nums = str[j];

				}
				else {
					nums += str[j];
				}

			}
		}
		if (nums.size() > 0) {
			v.push_back(nums);
		}
	}

	sort(v.begin(), v.end(), comp);
	for (int i = 0;i < v.size();i++) {
		cout << v[i] <<"\n";
	}

	return 0;
}
