/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *result = NULL;
        ListNode **node = &result;
        
        while (l1 != NULL || l2 != NULL){
            
            if (l1 != NULL && l2 !=NULL){
                if (l1->val <= l2->val){
                    *node = new ListNode(l1->val);
                    node = &((*node)->next);
                    l1 = l1->next;
                } else if (l2->val < l1->val){
                    *node = new ListNode(l2->val);
                    node = &((*node)->next);
                    l2 = l2->next;
                }     
            } else if (l1 != NULL){
                    *node = new ListNode(l1->val);
                    node = &((*node)->next);
                    l1 = l1->next;
            }  else if (l2 != NULL){
                    *node = new ListNode(l2->val);
                    node = &((*node)->next);
                    l2 = l2->next;
            } 
            
        }
        return result;
    }
};