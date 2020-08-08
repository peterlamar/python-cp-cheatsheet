/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        
        if (!head) return head;
                
        unordered_map<Node*, Node*> m;
        Node *clonedHead = new Node(head->val);
        
        Node *newHead = clonedHead;
        Node *oldHead = head;
           
        m[oldHead]=newHead;

        while(oldHead->next){
                    
            newHead->next = new Node(oldHead->next->val);
            
            oldHead = oldHead->next;
            newHead = newHead->next;
            
            m[oldHead]=newHead;
        }
        
        oldHead = head;
        newHead = clonedHead;
        
        while (oldHead && newHead){
                    
            // If random exists
            if (oldHead->random != NULL){
                newHead->random = m[oldHead->random];           
            }
  
            oldHead = oldHead->next;
            newHead = newHead->next;
        }
        
        return clonedHead;
    }
};