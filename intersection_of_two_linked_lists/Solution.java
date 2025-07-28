//  Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode p1 = headA;
        ListNode p2 = headB;
        while (p1 != p2) { // Continue until pointers meet or both are null
            p1 = (p1 == null) ? headB : p1.next;
            p2 = (p2 == null) ? headA : p2.next;
        }
        return p1;
    }
}

/** 
 * My Approach:
 * 1. Initialize two pointers, p1 and p2, to the heads of the two linked lists.
 * 2. Traverse both lists simultaneously. If a pointer reaches the end of its list, redirect it to the head of the other list.
 * 3. If the two pointers meet, return the intersection node; if they both reach the end (null), return null.
 * This ensures that both pointers traverse the same number of nodes, leading to the intersection point if it exists.
 * Time complexity: O(N + M), where N and M are the lengths of the two linked lists.
 * Space complexity: O(1)
*/