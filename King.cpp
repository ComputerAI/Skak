//
// Created by Johannes on 16/11/2020.
//
#include <bits/stdc++.h>
using namespace std;
namespace King{
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
        //Rook
        if ((board[pos+8]+6)/7!=own and pos+8<8*8) res.push_back(pos+8);
        if ((board[pos-8]+6)/7!=own and pos-8>0) res.push_back(pos-8);
        if ((board[pos+1]+6)/7!=own and (pos+1)%8!=0 and pos+1<8*8) res.push_back(pos+1);
        if ((board[pos-1]+6)/7!=own and (pos-1)%8!=7 and pos-1>=0) res.push_back(pos-1);
        //Bishop
        if (pos%8!=7){
            if ((board[pos+9]+6)/7!=own and pos+9<8*8) res.push_back(pos+9);
            if ((board[pos-7]+6)/7!=own and pos-7>0) res.push_back(pos-7);
        }
        if (pos%8!=0){
            if ((board[pos+7]+6)/7!=own and pos+7<8*8) res.push_back(pos+7);
            if ((board[pos-9]+6)/7!=own and pos-9>0) res.push_back(pos-9);
        }

        return res;
    }

    //TODO make method for finding out if king is threatened


}

