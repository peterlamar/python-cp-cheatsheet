class LRUCache {
/*

["LRUCache","get","put","get","put","put","get","get"]
[[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]

put (2,1)
put (1,1)
kv: [1]=1,[2]=1
l:2,1

put (2,3)
kv:  [1]=1, [2]=3
l: 1,3
*/
public:
    int size;
    list<int> lru;
    unordered_map <int, int> kv;
    unordered_map <int, list<int>::iterator> kvitr;

    LRUCache(int capacity) {
        size = capacity;
    }
    
    int get(int key) {
        if (kv.find(key) == kv.end()){
            return -1;
        }
            
        lru.erase(kvitr[key]);
        lru.push_front(key);       
        kvitr[key] = lru.begin();

        return kv[key];
    }
    
    void put(int key, int value) {
        // check capacity
        if (kv.size() == size){
            kv.erase(lru.back());
            kvitr.erase(lru.back());
            lru.pop_back();
        }
        
        kv[key] = value;
        lru.push_front(key);
        kvitr[key] = lru.begin();
    }
};