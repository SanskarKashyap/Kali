// A group of friends is going on holiday together. They have come to a meeting point (the start of
// the journey) using N cars. There are P[K] people and S[K] seats in the K-th car for k in range [O..N-
// 1]. Some of the seats in the cars may be free, so it is possible for some of the friends to change
// the car they are in. The friends have decided that, in order to be ecological, they will leave some
// cars parked at the meeting point and travel with as few cars as possible.
// Write a function:
// int solution (vector<int> &P, vector<int> &S);
// that, given two arrays P and S, consisting of N integers each, returns the minimum number of cars
// needed to take all of the friends on holiday.
// Examples:
// 1. Given P = [1, 4, 1] and S = [1, 5, 1], the function should return 2. A person from car number 0 can
// travel in car number 1 instead. This way, car number 0 can be left parked at the meeting point.
// 2. Given P = [4, 4, 2, 4] and S = [5, 5, 2, 5], the function should return 3. One person from car number
// 2 can travel in car number 0 and the other person from car number 2 can travel in car number 3.
// 3. Given P = [2, 3, 4, 2] and S = [2, 5, 7, 2], the function should return 2. Passengers from car
// number 0 can travel in car number 1 and passengers from car number 3 can travel in car number
// 2.
// Write an efficient algorithm for the following assumptions:
// • N is an integer within the range [1..100,000];
// • each element of arrays P and S is an integer within the range [1..9];
// • every friend had a seat in the car they came in; that is, P[K] ≤ S[K] for each K within
// the range [0..N-1].



#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int solution(vector<int> &P, vector<int> &S) {
    int n = P.size();
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += P[i];
    }
    int avg = sum / n;
    int res = 0;
    for (int i = 0; i < n; i++) {
        if (P[i] > avg) {
            res += ceil((double) (P[i] - avg) / (S[i] - avg));
        }
    }
    return res;
}

int main() {
    vector<int> P = {4,4,2,4};
    vector<int> S = {5,5,2,5};
    cout << solution(P, S) << endl; // Should return 3

    return 0;
}

