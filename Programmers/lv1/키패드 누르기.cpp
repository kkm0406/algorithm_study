#include <string>
#include <vector>
#include <deque>
#include <algorithm>
#include <map>
#include <iostream>
using namespace std;

vector<pair<int, int>> v[10];

void init(){
    v[0].push_back(make_pair(3, 1));
    v[1].push_back(make_pair(0, 0));
    v[2].push_back(make_pair(0, 1));
    v[3].push_back(make_pair(0, 2));
    v[4].push_back(make_pair(1, 0));
    v[5].push_back(make_pair(1, 1));
    v[6].push_back(make_pair(1, 2));
    v[7].push_back(make_pair(2, 0));
    v[8].push_back(make_pair(2, 1));
    v[9].push_back(make_pair(2, 2));
}


string solution(vector<int> numbers, string hand) {
    init();
    string answer = "";
    int lx = 3, ly = 0; //왼손가락 위치
    int rx = 3, ry = 2; //오른손가락 위치
    for(int num : numbers){
        if(num == 1 || num == 4 || num == 7){
            answer += "L";
            lx = v[num][0].first;
            ly = v[num][0].second;
        }else if(num == 3 || num == 6|| num == 9){
            answer += "R";
            rx = v[num][0].first;
            ry = v[num][0].second;
        }else{
            //num의 키패드 위치
            int key_x = v[num][0].first;
            int key_y = v[num][0].second;
            
            int dist_l = abs(lx-key_x) + abs(ly-key_y);
            int dist_r = abs(rx-key_x) + abs(ry-key_y);
            
            
            if(dist_l < dist_r){
                answer+= "L";
                lx = key_x;
                ly = key_y;
            }else if(dist_l > dist_r){
                answer += "R";
                rx = key_x;
                ry = key_y;
            }else{
                if(hand == "right"){
                    answer+="R";
                    rx = key_x;
                    ry = key_y;
                }else{
                    answer+="L";
                    lx = key_x;
                    ly = key_y;
                }
            }
        }
    }
    return answer;
}
