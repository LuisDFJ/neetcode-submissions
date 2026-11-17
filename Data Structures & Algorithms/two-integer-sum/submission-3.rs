use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new();
        for (i,n) in nums.iter().enumerate() {
            let comp = target - n;
            if let Some(j) = map.get(&comp) {
                return vec![*j, i as i32];
            } else {
                map.insert(*n,i as i32);
            }
        }
        return vec![]
    }
}
