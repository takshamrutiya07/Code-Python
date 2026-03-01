#include<iostream>
using namespace std;
string binary_search(int a[],int low,int high,int target){
    int mid=low+(high-low)/2;
    if(low<=high)
    {
        if(a[mid]==target)
        {
            return "Found";
        }
        else if(a[mid]<target)
        {
            binary_search(a,mid+1,high,target);
        }
        else if(a[mid]>target)
        {
            binary_search(a,low,mid-1,target);
        }
    }
        return "Not found";
}
int main()
{
     int arr[]={1,4,7,9,10};
     cout<<binary_search(arr,0,4,7);
}