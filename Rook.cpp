//
// Created by Johannes on 15/11/2020.
//
#include <bits/stdc++.h>
using namespace std;
namespace Rook{
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
        int i = pos;
        while (i+8<8*8) {
            if ((board[i+8]+6)/7!=own) res.push_back(i+8);
            if (board[i+8]!=0) break;
            i+=8;
        }
        i=pos;
        while (i-8>=0) {
            if ((board[i-8]+6)/7!=own) res.push_back(i-8);
            if (board[i-8]!=0) break;
            i-=8;
        }
        i=pos;
        while ((i+1)%8!=0 and i+1<8*8) {
            if ((board[i+1]+6)/7!=own) res.push_back(i+1);
            if (board[i+1]!=0) break;
            i++;
        }
        i=pos;
        while ((i-1)%8!=7 and i-1>=0) {
            if ((board[i-1]+6)/7!=own) res.push_back(i-1);
            if (board[i-1]!=0) break;
            i--;
        }

        return res;
    }
}
