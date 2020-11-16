//
// Created by Johannes on 16/10/2020.
//
#include "Pawn.cpp"
#include "Rook.cpp"
#include "Knight.cpp"
#include "Bishop.cpp"
#include "Queen.cpp"
#include "King.cpp"
#include <bits/stdc++.h>
using namespace std;

vector<int> ava(int board[], const vector<int>& alive) {
    vector<int> res;
    for (int pos : alive) {
        int piece = board[pos];
        vector<int> temp;
        switch (piece % 7) {
            case 1:
                temp = Pawn::available(board, {pos, piece});
                break;
            case 2:
                temp = Rook::available(board, {pos, piece});
                break;
            case 3:
                temp = Knight::available(board, {pos, piece});
                break;
            case 4:
                temp = Bishop::available(board, {pos, piece});
                break;
            case 5:
                temp = Queen::available(board, {pos, piece});
                break;
            case 6:
                temp = King::available(board, {pos, piece});
                break;
        }
        for (int j:temp) {
            res.push_back(j);
            res.push_back(pos);
        }
    }
    return res;
}
