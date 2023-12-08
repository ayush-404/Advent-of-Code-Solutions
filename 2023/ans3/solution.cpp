#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

bool symNearby(vector<string> v, int i, int j) {
  
}

int main(int argc, char** argv) {
  ifstream fin("input.txt");

  vector <string> v;
  string line;
  while (fin >> line) {
    v.push_back(line);
  }

  int n = v.size();
  int linesize = v[0].size();
  int ans = 0;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < linesize; j++) {
      if (v[i][j] < '0' || v[i][j] > '9') {
        string s = "";
        int start = j;
        int end = j;
        bool flag = false;
        while (v[i][j] >= '0' || v[i][j] <= '9') {
          s += v[i][j];
          flag = symNearby(v, i, j);
          end = ++j;

          if (v[])
        }


      }
    }
  }
}