class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* x = new ListNode(0);
x->next = head;
ListNode* curr = x;

int dup;
while (curr->next && curr->next->next){
    if (curr->next->val == curr->next->next->val) {
        dup = curr->next->val;
        while (curr->next && curr->next->val == dup){
            curr->next = curr->next->next;
        }
    }
    else {
        curr = curr->next;
    }
}
return x->next;
        }
};
