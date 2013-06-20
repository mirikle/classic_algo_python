#include <iostream>
#include <map>
#include <algorithm>
typedef std::map<int, int> Map;
Map findOverNth(int arr[], int size, int n)
{
	Map ret_map; 
	typedef Map::value_type Elem; //pair<CONST int, int>
	int total = 0;
	std::for_each(arr, arr + size, [&, n](int val) {
			auto ret_pair = ret_map.insert(Elem(val, 0));
			++(*ret_pair.first).second; 
			++ total;
			if (ret_map.size() == n)
			for (auto iter = ret_map.begin(); iter != ret_map.end(); )
			{
			--(*iter).second; 
			-- total;
			if ((*iter).second == 0)
			ret_map.erase(iter++);
			else
			iter++;
			}
			});
	std::for_each(ret_map.begin(), ret_map.end(), [](Elem &elem) {elem.second = 0;});
	std::for_each(arr, arr + size, [&ret_map](int val) {if (ret_map.find(val) != ret_map.end()) ret_map[val] ++;});
	for (auto iter = ret_map.begin(); iter != ret_map.end(); )
	{
		if ((*iter).second <= size / n)
			ret_map.erase(iter++);
		else 
			iter++;
	}
	return ret_map;
}
using namespace std;
int main()
{
	//int arr[] = {5,6,7,8, 10, 4,4, 4, 4,1, 1,1};
	int arr[] = {5,6,7,8, 10, 10, 10,10,10,10, 4,4, 4, 4,4,1, 1,1,1};
	auto a_map = findOverNth(arr, sizeof(arr)/sizeof(int), 4);
	cout<<sizeof(arr)/sizeof(int)<<endl;
	//cout<<a_map.size()<<endl;
	for each(auto elem in a_map)
	{
		cout<<elem.first<<" "<<elem.second<<endl;
	}
}
