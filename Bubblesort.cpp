//wrap to arrang elements of array into ascending order
//space complexity and time complexity
//how much time it takes to execute the statement is known as time complexity
//how much space it need to execute the statement is known as space comlexity
/*1.best case
2.avg case
3.wrost case
*/
#include<iostream>
using namespace std;
int main(){
    cout<<"Enter size:";
    int size;
    cin>>size;

    int arr[size];
    for(int i=0;i<size;i++){
        cout<<"Enter value of index "<<i<<":";
        cin>>arr[i];
    }
 for(int i = 0;i<size-1;i++){
    bool isSwapped = false;
    for(int j = 0;j<size-1-i;j++){
        if(arr[j]>arr[j+1]){
            int tmp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = tmp;
            isSwapped = true;
        }
    }
    if(!isSwapped) break;
}
for(int i=0;i<size;i++)
{
    cout<<arr[i]<<" ";
}
    return 0;
}