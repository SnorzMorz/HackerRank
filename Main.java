package com.company;

import java.util.List;

class SinglyLinkedListNode {
    int data;
    SinglyLinkedListNode next;

}

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
	
	 public int countHi2(String str) {
        if(str.length() <= 2)
            return 0;

        if(str.substring(0, 2).equals("hi"))
            return 1 + countHi2(str.substring(2));

        if(str.substring(1, 3).equals("hi") && str.charAt(0) != 'x')
            return 1 + countHi2(str.substring(3));
        if(str.charAt(0) == 'x')
            return countHi2(str.substring(2));
        return countHi2(str.substring(1));

    }

    public String parenBit(String str) {

        if(str.charAt(0) != '(')
            return parenBit(str.substring(1));
        if(str.charAt(str.length() - 1) != ')')
            return parenBit(str.substring(0, str.length() - 1));

        return str;

    }

    public boolean nestParen(String str) {
        if(str.length)
        if(str.charAt(0) != '(' && str.charAt(str.length() - 1) != ')')
            return true;
        if(str.charAt(0) == '(' && str.charAt(str.length() - 1) == ')')
            return nestParen(str.substring(1, str.length() - 1));

        return false;
    }

    /*
     * Complete the 'dynamicArray' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. 2D_INTEGER_ARRAY queries
     */

    public static void dynamicArray(int n, List<List<Integer>> queries) {
        // Write your code here

        return;
    }

    // Complete the printLinkedList function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static void printLinkedList(SinglyLinkedListNode head) {
        boolean hasNext = true;
        SinglyLinkedListNode current = head;

        if(current.next)
        while(hasNext){

            System.out.println(current.data);

            if(current.next == null){
                hasNext = false;
            }

            current = current.next;
        }

    }

    static SinglyLinkedListNode insertNodeAtTail(SinglyLinkedListNode head, int data) {
        // This is a "method-only" submission.
        // You only need to complete this method.
        SinglyLinkedListNode n = new SinglyLinkedListNode();
        n.data = data;
        n.next = null;

        if(head == null){
            head = n;
            return head;
        }

        else
        {
            SinglyLinkedListNode c = head;
            while(c.next != null){
                c = c.next;
            }

            c.next = n;

            return head;

        }

    }



    public static void main(String[] args) {
	// write your code here


    }
}
