// Title: Largest Triangle Area
// Runtime: 448 ms
// Memory: 17.3 MB

class Solution {
public:
    double length(vector<int> first, vector<int> second) {
        return sqrt(pow(first[0] - second[0], 2) + pow(first[1] - second[1], 2));
    }
    
    double area(vector<int> first, vector<int> second, vector<int> third) {
        double first_side = length(first, second);
        double second_side = length(second, third);
        double third_side = length(third, first);
        double semi_perimeter = (first_side + second_side + third_side) / 2.0;
        return sqrt(semi_perimeter * (semi_perimeter - first_side) * (semi_perimeter - second_side) *                        (semi_perimeter - third_side));
    }
    
    double largestTriangleArea(vector<vector<int>>& points) {
        vector<double> areas;
        for (int i = 0; i < points.size(); i++) {
            for (int j = 0; j < points.size(); j++) {
                for (int k = 0; k < points.size(); k++) {
                    if (i != j && j != k) {
                        areas.push_back(area(points[i], points[j], points[k]));
                    }
                }
            }
        }
        return *max_element(areas.begin(), areas.end());
    }
};