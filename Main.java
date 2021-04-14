package com.company;

public class Main {

    static int[] reverseArray(int[] a) {
        int[] b = new int[a.length];

        for(int i = 0; i < a.length; i++){
            b[i] = a[a.length - 1- i];
        }

        return b;


    }

    static int hourglassSum(int[][] arr) {
        int sumBiggest = Integer.MIN_VALUE;
        int sum =0;
        for( int j = 0; j < 4; j++){
            for (int i = 0; i < 4; i++){
                sum = arr[j][i] + arr[j][i+1] + arr[j][i+2]
                        + arr[j+1][i+1]
                        + arr[j+2][i] + arr[j+2][i+1] + arr[j+2][i+2];
                if(sum > sumBiggest){
                    sumBiggest = sum;
                }
            }
        }

        return sumBiggest;

    }



    public static void main(String[] args) {
	// write your code here


    }
}
