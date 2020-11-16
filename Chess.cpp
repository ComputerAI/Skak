//
// Created by Johannes on 16/10/2020.
//
#include <bits/stdc++.h>
#include "Game.cpp"
using namespace std;
Game g;
int alphabeta(int depth, bool p, int alpha, int beta){
    vector<int> poss = g.available(g.get(g.turn));
    if(depth==0 || poss.empty()) return g.score(p, depth);
    if(g.turn==p){
        int a = alpha;
        for (int i = 0; i < poss.size(); i+=2) {
            //if(a>=beta) break;
            g.move(poss[i],poss[i+1]);
            int v = alphabeta(depth - 1, p, a, beta);
            a=max(v,a);
            g.pop();
        }
        return a;
    } else{
        int b = beta;
        for (int i = 0; i < poss.size(); i+=2) {
            //if(b<=alpha) break;
            g.move(poss[i],poss[i+1]);
            int v = alphabeta(depth - 1, p, alpha, b);
            b=min(v,b);
            g.pop();
        }
        return b;
    }
}

vector<int> ab(int depth, bool p){
    int a=-1000;
    int b=-a;
    vector<int> poss = g.available(g.get(p));
    int mov = poss[0];
    int pos = poss[1];
    for (int i = 0; i < poss.size(); i+=2) {
        g.move(poss[i],poss[i+1]);
        int v = alphabeta(depth-1,p,a,b);
        g.pop();
        if(a<v){
            a=v;
            mov=poss[i];
            pos=poss[i+1];
        }
    }
    return {mov,pos};
}
/*
void play(bool p){
    while (!g.done()){
        if(p==g.turn){
            int x,y;
            g.show();
            cin >> x;
            cin >> y;
            g.move(x,y);
        } else g.move(ab(2,!p));
    }
    if(g.done()==1) cout << "Player 1 won!";
    else if(g.done()==2) cout << "Player 2 won!";
    else cout << "It's a tie!";
}
//*/
void play(){
    //while (!g.done()){
    for (int i = 0; i < 2; i++) {
        vector<int> move;
        cout << g.available(g.get(g.turn)).size()/2 << endl;
        move = ab(4, g.turn);
        g.move(move[0],move[1]);
        //g.show();
        cout << g.cc << endl;
    }
}

int main(){
    g = Game();
    auto start_time = std::chrono::high_resolution_clock::now();
    play();
    auto end_time = std::chrono::high_resolution_clock::now();
    auto time = end_time - start_time;
    cout << time/std::chrono::milliseconds(1);
}


