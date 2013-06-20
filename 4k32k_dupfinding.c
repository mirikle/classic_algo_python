#include<iostream>
using namespace std;

//input has 32K
void printDup(int arr[32000]){
	//TODO arg checking
	
	//use only 4k memory
	int mem[4000];
	memset(mem, 0, sizeof(arr));
	for(int i = 0; i < sizeof(arr) / sizeof(arr[0]); ++ i){
		int num = arr[i];
		//offset left by 1
		int num_1 = num - 1;
		int byte_idx = num_1 / 8;
		int bit_idx = num_1 % 8;
		if(mem[byte_idx] & 1 << bit_idx){
			printf("%d\n", num);
		}else{
			mem[byte_idx] |= 1 << bit_idx;
		}
	}

}
