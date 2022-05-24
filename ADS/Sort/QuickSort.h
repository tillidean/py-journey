//
// Created by JoWan on 01.12.2021.
//

#ifndef BEGINOFLIFE_QUICKSORT_H
#define BEGINOFLIFE_QUICKSORT_H


class QuickSort {
private:
    void swapp(int i, int j, int arr[]);
    void partation(int i, int j, int pt);

public:
    void sort(int arr[]);
};


#endif //BEGINOFLIFE_QUICKSORT_H
