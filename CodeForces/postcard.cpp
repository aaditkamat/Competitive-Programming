#include<iostream>
#include <string>

using namespace std;

int count_characters(string message) {
    int count = 0;
    for (string::iterator it = message.begin(); it != message.end(); ++it) {
        if (*it != '?' && *it != '*')
            count++;
    }
    return count;
}
void decode(string message, int length) {
    string new_message = "";
    int count = count_characters(message);
    for (string::iterator it = message.begin(); it != message.end(); ++it) {
        if (*it != '?' && *it != '*') {
            new_message += *it;
        }
        else if (*it == '?') {
            if (count > length) {
                new_message.erase(new_message.end() - 1);
                count--;
            }
        } else {
            if (count < length) {
                new_message.insert(new_message.end(), length - count, *(new_message.end() - 1));
                count = length;
            } else if (count > length) {
                new_message.erase(new_message.end() - 1);
                count--;
            }
        }
    }
    if (count == length) {
        cout << new_message << endl;
    } else {
        cout << "Impossible" << endl;
    }
}

int main() {
    string message;
    getline(cin, message);
    int length;
    cin >> length;
    decode(message, length);
}