//
// Created by Johannes on 16/10/2020.
//
#include <bits/stdc++.h>
#include "Pieces.cpp"
using namespace std;
class Game{
    public:
    int board[8*8] = {2,3,4,5,6,4,3,2,
                       1,1,1,1,1,1,1,1,
                       0,0,0,0,0,0,0,0,
                       0,0,0,0,0,0,0,0,
                       0,0,0,0,0,0,0,0,
                       0,0,0,0,0,0,0,0,
                       8,8,8,8,8,8,8,8,
                       9,10,11,12,13,11,10,9};
    bool turn = false;
    stack <vector<int>> s;
    int cc=0;
    Game()= default;

    void move(int y, int x){
        s.push({abs(y),x,board[abs(y)],board[x]});
        turn=!turn;
        int p = board[x];
        if (y<=0 and p%7==1) p+=4;
        board[x] = 0;
        board[abs(y)]=p;
    }

    void pop(){
        vector<int> move = s.top();
        s.pop();
        turn=!turn;
        board[move[0]]=move[2];
        board[move[1]]=move[3];
    }

    vector<int> available(const vector<int>& alive){
        return ava(board,alive);
    }

    //Return alive team
    vector<int> get(int team){
        vector<int> res;
        for (int i = 0; i < 8*8; i++) {
            if (board[i]==0) continue;
            if (board[i]/7==team) {
                res.push_back(i);
                //res.push_back(board[i]);
            }
        }
        return res;
    }

    void showava(int pos){
        char bb[8*8] = {};
        for (int i:available({pos})) bb[abs(i)]='B';
        bb[pos]='A';
        for (int i = 7; i >= 0; i--) {
            cout << '|';
            for (int j = 0; j < 8; j++) {
                if (bb[i*8+j]!='A' and bb[i*8+j]!='B'){
                    if (board[i*8+j]==0) cout << " " << "--" << " |";
                    else cout << board[i*8+j]%7 << "(" << board[i*8+j]/7 << ")|";
                }
                else if (board[i*8+j]==0) cout << "-" << "(" << bb[i*8+j] << ")|";
                else cout << board[i*8+j]%7 << "(" << bb[i*8+j] << ")|";

            }
            cout << endl;
        }
    }

    //TODO return full score of current player
    int score(int team, int depth){
        cc++;
        return 0+depth;
    }


    void show(){
        int n=8;
        for (int i = n-1; i >= 0; i--) {
            cout << '|';
            for (int j = 0; j < n; j++) {
                if (board[i*n+j]==0) cout << " " << "--" << " |";
                else cout << board[i*n+j]%7 << "(" << board[i*n+j]/7 << ")|";
            }
            cout << endl;
        }

    }

};