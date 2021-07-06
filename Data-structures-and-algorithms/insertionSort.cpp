// C++ program for insertion sort
#include <bits/stdc++.h>
#include<ctime>
using namespace std;

/* Function to sort an array using insertion sort*/
void insertionSort(int arr[], int n)
{
	int i, key, j;
	for (i = 1; i < n; i++)
	{
		key = arr[i];
		j = i - 1;

		/* Move elements of arr[0..i-1], that are
		greater than key, to one position ahead
		of their current position */
		while (j >= 0 && arr[j] > key)
		{
			arr[j + 1] = arr[j];
			j = j - 1;
		}
		arr[j + 1] = key;
	}
}

// A utility function to print an array of size n
void printArray(int arr[], int n)
{
	int i;
	for (i = 0; i < n; i++)
		cout << arr[i] << " ";
	cout << endl;
}

/* Driver code */
int main()
{
    srand(time(0));
    const unsigned int sizeOfArray = 1000;
    int arrayIntegers[sizeOfArray];

    for (int i = 0; i < sizeOfArray; i++){
        arrayIntegers[i] = rand() % 1000;
    }

    cout<<"\nNon-sorted array: \n";
    printArray(arrayIntegers, sizeOfArray);
    cout<<"\n\n";

    insertionSort(arrayIntegers, sizeOfArray);
    cout<<"Sorted array: \n\n";
    printArray(arrayIntegers, sizeOfArray);

	

	return 0;
}

// This is code is contributed by rathbhupendra
