// You are given N cards. Each card consists of a suit and a rank. There are four suits, s (Spades), H (Hearts), D (Diamonds) and c (Clubs), and thirteen ranks, ordered (from the lowest to the highest) 2, 3, 4, 5, 6, 7, 8, 9, 18, J (Jack), Q
// (Queen), K (King) and A (Ace).
// Each card is represented by a string in the format "<<rank><suit>". For example, 10 of Spades is described as "10s", and Queen of Hearts as "QH".
// There are six ranked card sets (described in detail below). Sets are ordered by their strength from the weakest to the strongest. Your task is to detect the card sets that can be formed from the given cards. Detecting each card set is
// scored separately and is worth an equal number of points. If you detect more than one set, select the strongest one.
// Write a function:
// Results solution (vector<string> &cards);
// that, given an array of strings cards, returns a Results object representing the strongest card set that can be formed.
// Assume that the following declarations are given:
// struct Results {
// string set_name;
// vector<string> selected_cards;
// };
// • set_name is a string which should be the name of detected set (see below);
// selected_cards is a list of strings, which should be made of cards that form the detected set. Cards can be listed in any order.
// Scoring:
// • detecting each card set is scored separately and is worth an equal number of points;
// • in tests worth 50% of points only the strongest set's set_name is checked. Checking selected_cards field of the Result object is omitted in these tests.
// Card sets:
// There are six card sets ordered by their strength from the weakest (single card) to the strongest (a triple and a pair).
// Set 1: single card
// }
// • Name: "single card"
// .
// • Description: A single card of the highest rank; the suit does not matter.
// For example, for cards = ["2H", "4H", "7C", "9D", "10D", "KS"], your function should return:
// {
// "set_name" = "single card",
// "selected_cards" = ["KS"]
// Set 2: pair
// • Name: "pair"
// • Description: Two cards sharing the same rank; suits do not matter. If there are multiple pairs, return any one with the highest rank.
// For example, for cards = ["AS", "10H", "8H", "10S", "8D"], one of the correct results is:
// {
// }
// Set 3: triple
// • Name: "triple"
// • Description: Three cards sharing the same rank; suits do not matter. If there are multiple ways to choose a triple, return any with the highest rank.
// For example, for cards = ["AS", "JS", "AH", "AD", "10D", "AC"], one of the correct results is:
// {
// "set_name" = "pair",
// "selected_cards" = ["10H", "10s"]
// }
// Set 4: five in a row
// {
// • Name: "five in a row"
// • Description: Five cards of consecutive ranks starting with the highest possible rank; suits do not matter. If there are multiple ways to choose five such cards, return any.
// For example, for cards = ["6H", "7S", "8S", "9s", "10s", "JD", "JC", "KC", "AC"], one of the correct results is:
// "set_name" = "triple",
// "selected_cards" = ["AH", "AD", "AC"]
// {
// }
// Set 5: suit
// }
// "set_name" = "five in a row",
// "selected_cards" = ["7S", "8S", "9S", "10S", "JC"]
// • Name:"suit"
// • Description: Five cards sharing the same suit; the ranks do not matter. If there are multiple ways to choose five cards with the same suit, choose any set with the highest suit. The order of the suits (from the highest to
// the lowest) is S, H, D, C.
// For example, for cards = ["2D", "4D", "6D", "8D", "9D", "AC, "KC", "QC", "JC", "7c"], one of the correct results is:
// "set_name" = "suit",
// "selected_cards" = ["2D", "4D", "6D", "8D", "9D"]

// Set 6: a triple and a pair
// • Name: "a triple and a pair"
// • Description: Five cards, consisting of a triple (three cards of the same rank) and a pair (two cards of the same rank). If there are multiple ways to choose this set, choose one with the highest rank of the triple, then one
// with the highest rank of the pair. The suits do not matter.
// For example, for cards = ["100", "10H", "100", "2s", "2H", "20", "JH", "JC"], one of the correct results is:
// {
// }
// "set_name" = "a triple and a pair",
// "selected_cards" = ["10D", "10H", "10C", "JH", "JC"]
// Constraints:
// Assume that:
// • N is an integer within the range [1..10];
// • the elements of cards are all distinct;
// • each string in array cards is a correct representation of a card in <rank> <suit>" format.
// In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.


#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

struct Results {
    string set_name;
    vector<string> selected_cards;
};

Results solution(vector<string> &cards) {
    Results result;
    int n = cards.size();

    // Set 1: Single Card
    result.set_name = "single card";
    result.selected_cards = {cards[n - 1]};

    // Set 2: Pair
    if (n >= 2) {
        result.set_name = "pair";
        result.selected_cards = {cards[n - 1], cards[n - 2]};
    }

    // Set 3: Triple
    if (n >= 3 && cards[n - 1][0] == cards[n - 2][0] && cards[n - 2][0] == cards[n - 3][0]) {
        result.set_name = "triple";
        result.selected_cards = {cards[n - 1], cards[n - 2], cards[n - 3]};
    }

    // Set 4: Five in a Row
    if (n >= 5) {
        bool isFiveInARow = true;
        for (int i = 1; i < 5; i++) {
            if (cards[n - i][0] != cards[n - i - 1][0] - 1) {
                isFiveInARow = false;
                break;
            }
        }

        if (isFiveInARow) {
            result.set_name = "five in a row";
            result.selected_cards = {cards[n - 1], cards[n - 2], cards[n - 3], cards[n - 4], cards[n - 5]};
        }
    }

    // Set 5: Suit
    if (n >= 5) {
        bool isSameSuit = true;
        for (int i = 1; i < 5; i++) {
            if (cards[n - i][1] != cards[n - i - 1][1]) {
                isSameSuit = false;
                break;
            }
        }

        if (isSameSuit) {
            result.set_name = "suit";
            result.selected_cards = {cards[n - 1], cards[n - 2], cards[n - 3], cards[n - 4], cards[n - 5]};
        }
    }

    // Set 6: A Triple and a Pair
    if (n >= 5 && result.set_name != "triple" && result.set_name != "five in a row" && result.set_name != "suit") {
        for (int i = 0; i < n - 2; i++) {
            if (cards[i][0] == cards[i + 1][0] && cards[i + 1][0] == cards[i + 2][0]) {
                for (int j = i + 3; j < n - 1; j++) {
                    if (cards[j][0] == cards[j + 1][0]) {
                        result.set_name = "a triple and a pair";
                        result.selected_cards = {cards[i], cards[i + 1], cards[i + 2], cards[j], cards[j + 1]};
                        break;
                    }
                }
                if (result.set_name == "a triple and a pair") {
                    break;
                }
            }
        }
    }

    return result;
}

int main() {
    vector<string> cards = {"2H", "4H", "7C", "9D", "10D", "KS"};
    Results result = solution(cards);

    cout << "Set Name: " << result.set_name << endl;
    cout << "Selected Cards: ";
    for (const string &card : result.selected_cards) {
        cout << card << " ";
    }
    cout << endl;

    return 0;
}
