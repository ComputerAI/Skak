//
// Created by Johannes on 16/10/2020.
//
#include <bits/stdc++.h>
#include "Game.cpp"
using namespace std;
int cc=0;
Game g = Game();
/*
int alphabeta(int depth, bool p, int alpha, int beta){
    cc+=1;
    if(depth==0 || g.done()) return g.score(p, depth);
    int *poss=g.available();
    if(g.turn==p){
        int a = alpha;
        for (int i = 0; i < 9 && poss[i]!=-1; i++) {
            //if(a>=beta) break;
            g.move(poss[i]);
            int v = alphabeta(depth - 1, p, a, beta);
            a=max(v,a);
            g.pop();
        }
        delete[](poss);
        return a;
    } else{
        int b = beta;
        for (int i = 0; i < 9 && poss[i]!=-1; i++) {
            //if(b<=alpha) break;
            g.move(poss[i]);
            int v = alphabeta(depth - 1, p, alpha, b);
            b=min(v,b);
            g.pop();
        }
        delete[](poss);
        return b;
    }
}

int ab(int depth, bool p){
    int a=-1000;
    int b=-a;
    int* poss = g.available();
    int mov = poss[0];
#pragma omp parallel for num_threads(4)
    for (int i = 0; i < 9 && poss[i]!=-1; i++) {
        g.move(poss[i]);
        int v = alphabeta(depth-1,p,a,b);
        g.pop();
        if(a<v){
            a=v;
            mov=poss[i];
        }//
    }
    //cout << cc;
    cc=0;
    return mov;
}

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


int main(){
    pawn p =pawn(2,0);
    cout << p.available(*g.board)[0] << endl;
    cout << g.board[8]->team;
    cout << g.board[0]->team;
    //g.move(8,0);
    cout << g.board[8]->team;
    cout << g.board[0]->team << endl;
    vector<int> a = g.board[8*7-1]->available(*g.board);
    for (int i : a) {
        cout << i << endl;
    }//*/
    g.show();
    vector<int> n = g.available(g.get(1));
    for (int j = 0; j < n.size(); j+=2) {
        cout << n[j] << ' ';
        cout << n[j+1] << endl;
    }
    cout << g.score(1) << ' ' << g.score(2);

}


