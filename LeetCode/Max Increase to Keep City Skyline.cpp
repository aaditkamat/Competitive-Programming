// Title: Max Increase to Keep City Skyline
// Runtime: 12 ms
// Memory: 1.5 MB

class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int incr = 0;
        map<string, vector<int>> max_store;
        max_store["row"] = vector<int>();
        for (int i = 0; i < grid.size(); i++) {
            vector<int> row = grid.at(i);
            max_store["row"].push_back(*max_element(row.begin(), row.end()));
        }
        max_store["column"] = vector<int>();
        for (int i = 0; i < grid.at(0).size(); i++) {
            vector<int> column;
            for (int j = 0; j < grid.size(); j++) {
                column.push_back(grid.at(j).at(i));
            }
            max_store["column"].push_back(*max_element(column.begin(), column.end()));
        }
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.at(i).size(); j++) {
                int value = min(max_store["column"].at(i), max_store["row"].at(j));
                incr += value - grid.at(i).at(j); 
            }
        }
        return incr;
    }
};