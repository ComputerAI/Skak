//
// Created by Johannes on 16/10/2020.
//
#include <bits/stdc++.h>
using namespace std;
class Pieces{
    public:
    int team;
    int score;
    int place;
    int origin;
    char type;

    virtual vector<int> available(Pieces board[]){
        vector<int> res;
        return res;
    };
};

class empty : public Pieces{
public:
    empty(){
        team = 0;
        score = 0;
        type='0';
    }
};

class pawn : public Pieces{
    int in[3]{0,1,-1};
    public:
    pawn(int t, int p){
    team = t;
    score = 1;
    place = p;
    origin = p;
    type = 'P';
    }
    vector<int> available(Pieces board[]) override{
        vector<int> res;
        if(place+8*in[team]>=8*8 or place+8*in[team]<0) return res;
        int enemy;
        if (team==1) {
            enemy = 2;
            if(place>8*7) res.push_back(-1);
        } else {
            enemy = 1;
            if(place<8) res.push_back(-1);
        }
        if(board[place+7*in[team]].team==enemy) res.push_back(place+7*in[team]);
        if(board[place+9*in[team]].team==enemy) res.push_back(place+9*in[team]);
        if(board[place+8*in[team]].team!=team){
            res.push_back(place+8*in[team]);
            if(origin == place and board[place+16*in[team]].team!=team) res.push_back(place+16*in[team]);
        }
        return res;
    }
};