//
// Created by Johannes on 15/11/2020.
//

#include <bits/stdc++.h>
using namespace std;
namespace Pawn{
    vector<int> available(const int board[], const vector<int>& alive){
        vector<int> res;
        int pos = alive[0];
        int team = alive[1]/7+1;
        if (team==2) team=-1; //team 1 = -1, because they are on top

        //Out of bounds
        //if(pos+8*team>=8*8 or pos+8*team<0) return res;

        // Declare non empty
        int enemy;
        if (team==1) enemy = 2;
        else enemy = 1;

        //Can it move
        if((board[pos+7*team]+6)/7==enemy and !(pos%8==7*team or (pos+1)%8==-1*team)){
            if(pos+7*team<8 or pos+7*team>=8*7) res.push_back(-(pos+7*team));
            else res.push_back(pos+7*team);
        }
        if((board[pos+9*team]+6)/7==enemy and !(pos%8==7*team or (pos+1)%8==-1*team)){
            if(pos+9*team<8 or pos+9*team>=8*7) res.push_back(-(pos+9*team));
            else res.push_back(pos+9*team);
        }
        if(board[pos+8*team]==0){
            if((pos<8*2*team or pos>=8*6*enemy) and board[pos+16*team]==0) res.push_back(pos+16*team);
            if(pos+8*team<8 or pos+8*team>=8*7) res.push_back(-(pos+8*team));
            else res.push_back(pos+8*team);
        }
        return res;
    }








}
