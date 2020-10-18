//
// Created by Johannes on 16/10/2020.
//
#include <bits/stdc++.h>
#include "Pieces.cpp"
using namespace std;
class Game{
    public:
    Pieces** board = new Pieces*[8*8];
    bool turn = true;
    //stack <int[2]> s;
    //vector<unique_ptr<Pieces>> bb;

    //TODO add all pieces
    Game(){
        for (int i = 0; i < 8; i++) {
            board[i]=new empty();
            board[8+i]=new pawn(1,8+i);
        }
        for (int i = 0; i < 8; i++) {
            board[8*7+i]=new empty();
            board[8*6+i]=new pawn(2,8*6+i);
        }
        for (int j = 8*2; j < 8*6; j++) {
            board[j]=new empty();
        }

    }

    void move(int x, int y){
        //s.push({x,y});
        Pieces* p = board[x];
        board[x]=new empty();
        //if(board[y]->team!=0) s.push(-board[y]->team,board[y]->type);
        board[y]=p;
        p->place=y;
    }

    vector<Pieces*> get(int team){
        vector<Pieces*> res;
        for (int i = 0; i < 8*8; i++) {
            if (board[i]->team==team) res.push_back(board[i]);
        }
        return res;
    }

    vector <int> available(const vector<Pieces*>& alive){
        vector<int> s;
        for (Pieces *p : alive){
            vector<int> temp = p->available(*board);
            for (int k : temp){
                s.push_back(p->place);
                s.push_back(k);
            }
        }
        return s;
    }

    //TODO return 0 if not done, -1 if stalemate and team if won
    int done(){
        return 0;
    }

    //TODO return full score of current player
    int score(int team){
        int score=0;
        for (int i = 0; i < 8*8; i++) {
            if (board[i]->team==team) score+=board[i]->score;
            else score-=board[i]->score;
        }
        return score;
    }


    void show(){
        int n=8;
        for (int i = n-1; i >= 0; i--) {
            cout << '|';
            for (int j = 0; j < n; j++) {
                cout << board[i*n+j]->type << "(" << board[i*n+j]->team << ")|";
            }
            cout << endl;
        }

    }

};