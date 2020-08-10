class LRUCache {
/*

["LRUCache","put","put","get","put","get","get"]
[[2],[2,1],[1,1],[2],[4,1],[1],[2]]

put (2,1)
put (1,1)
kv: [1]=1,[2]=1
l:2,1

get(2)
kv: [1]=1,[2]=1
l:1,2

put(4,1)
kv: [1]=1,[4]=1
l:4,2

get(1): -1
kv: [4]=1,[1]=1
l:4,2

get(2): -1
kv: [4]=1,[1]=1
l:4,2

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
            
        lru.push_front(key);        
        lru.erase(kvitr[key]);

        return kv[key];
    }
    
    void put(int key, int value) {
        kv[key] = value;
        lru.push_front(key);
        kvitr[key] = lru.begin();

        // check capacity
        if (kv.size() > size){
            kv.erase(lru.back());
            kvitr.erase(lru.back());
            lru.pop_back();
        }
    }
};