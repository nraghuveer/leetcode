#![allow(non_snake_case)]
struct Solution {}

impl Solution {
    pub fn min_swaps_couples(row: Vec<i32>) -> i32 {
        let N = row.len() as i32;
        let mut ans = row.clone();
        for (index, value) in row.iter().enumerate() {

            if index == value - 1 as i32 {
                continue
            }
            ans[index] = value - 1
        }
        println!("{:?}", ans);
        2
    }
}

pub fn main() {
    println!("{}", Solution::first_missing_positive(vec![2,4,5,1,3]));
}