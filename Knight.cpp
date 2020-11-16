//
// Created by Johannes on 16/11/2020.
//
#include <bits/stdc++.h>
using namespace std;
namespace Knight{
    vector<int> available(const int board[], const vector<int>& alive){
        vector<int> res;
        int pos = alive[0];
        int team = alive[1]/7+1;
        if (team==2) team=-1; //team 1 = -1, because they are on top

        // Declare non empty
        int own;
        if (team==1) own = 1;
        else own = 2;

        //Can it move
        if (pos%8!=0){
            if ((board[pos + 15] + 6)/7 != own and pos + 15 < 8 * 8) res.push_back(pos + 15);
            if ((board[pos - 17]+6)/7 != own and pos - 17 >= 0) res.push_back(pos - 17);
            if (pos%8!=1){
                if ((board[pos - 10]+6)/7 != own and pos - 10 >= 0) res.push_back(pos - 10);
                if ((board[pos + 6]+6)/7 != own and pos + 6 < 8 * 8) res.push_back(pos + 6);
            }
        }
        if (pos%8!=7){
            if ((board[pos + 17]+6)/7 != own and pos + 17 < 8 * 8) res.push_back(pos + 17);
            if ((board[pos - 15]+6)/7 != own and pos - 15 >= 0) res.push_back(pos - 15);
            if (pos%8!=6){
                if ((board[pos + 10]+6)/7 != own and pos + 10 < 8 * 8) res.push_back(pos + 10);
                if ((board[pos - 6]+6)/7 != own and pos - 6 >= 0) res.push_back(pos - 6);
            }
        }

        return res;
    }
}








