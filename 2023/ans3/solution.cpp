#include <iostream>
#include <vector>
#include <fstream>
#include <set>
#include <map>
#include <string>

using namespace std;

bool symNearby(vector<string> v, int k, int l)
{
  int n = v.size();
  int linesize = v[0].size();
  for (int i = k - 1; i <= k + 1; i++)
  {
    for (int j = l - 1; j <= l + 1; j++)
    {
      if (i >= 0 && i < n && j >= 0 && j < linesize)
      {
        if (v[i][j] != '.' && v[i][j] < '0' || v[i][j] > '9')
          return true;
      }
    }
  }

  return false;
}

vector<int> handleStar(map<string, int> pairs, vector<string> v, int k, int l)
{
  int n = v.size();
  int linesize = v[0].size();
  string s = "";

  for (int i = k - 1; i <= k + 1; i++)
  {
    for (int j = l - 1; j <= l + 1; j++)
    {
      if (i >= 0 && i < n && j >= 0 && j < linesize)
      {
        if (v[i][j] == '*')
        {
          s = to_string(i) + " " + to_string(j);
          if (auto search = pairs.find(s); search == pairs.end())
          {
            return {1, i, j};
          }
          else
          {
            return {2, i, j};
          }
        }
      }
    }
  }

  return {0, 0, 0};
}

int part2(vector<string> v)
{
  int n = v.size();
  int linesize = v[0].size();
  int ans = 0;

  std::map<string, int> pairs;

  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < linesize; j++)
    {
      if (v[i][j] >= '0' && v[i][j] <= '9')
      {
        string s = "";
        vector<int> flag = {0, 0, 0};
        while (j < linesize && v[i][j] >= '0' && v[i][j] <= '9')
        {
          s += v[i][j];
          if (!flag[0])
            flag = handleStar(pairs, v, i, j);
          j++;
        }

        for (auto c : flag)
          std::cout << c << " ";
        std::cout << std::endl;

        int curr = atoi(s.c_str());
        s = to_string(flag[1]) + " " + to_string(flag[2]);

        if (flag[0] == 1)
        {
          pairs.insert({s, curr});
        }
        else if (flag[0] == 2)
        {
          auto ret = pairs.find(s);
          if (ret != pairs.end())
          {
            ans += ret->second * curr;
          }
          else
            std::cout << "ERROR" << std::endl;
        }
      }
    }
  }

  return ans;
}

int part1(vector<string> v)
{
  int n = v.size();
  int linesize = v[0].size();
  int ans = 0;

  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < linesize; j++)
    {
      if (v[i][j] >= '0' && v[i][j] <= '9')
      {
        string s = "";
        bool flag = false;
        while (j < linesize && v[i][j] >= '0' && v[i][j] <= '9')
        {
          s += v[i][j];
          if (symNearby(v, i, j))
            flag = true;
          j++;
        }

        if (flag)
        {
          ans += atoi(s.c_str());
        }
      }
    }
  }

  return ans;
}

int main(int argc, char **argv)
{
  ifstream fin("input.txt");

  vector<string> v;
  string line;
  while (fin >> line)
  {
    v.push_back(line);
  }

  std::cout << part1(v) << std::endl;
  std::cout << part2(v) << std::endl;
}